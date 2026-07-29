#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, struct, time, zlib
from pathlib import Path

MAGIC=b'PRSM'
HEADER=struct.Struct('>4sBBBBIII32s16sQI')
MAX_PAYLOAD=2*1024*1024*1024

def canonical_json(raw: bytes)->bytes:
    value=json.loads(raw.decode('utf-8'))
    return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')

def encode(source:Path,output:Path,kind='json',compression='zlib',timestamp=None):
    raw=source.read_bytes()
    if kind=='json': payload=canonical_json(raw); flags=1
    elif kind=='text': raw.decode('utf-8'); payload=raw; flags=2
    else: payload=raw; flags=4
    manifest={'format':'PRISME-BIN','format_version':'0.1','source_name':source.name,'payload_kind':kind,'compression':compression}
    m=json.dumps(manifest,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')
    stored=zlib.compress(payload,9) if compression=='zlib' else payload
    comp=1 if compression=='zlib' else 0
    digest=hashlib.sha256(payload).digest()
    pid=hashlib.sha256(payload+m).digest()[:16]
    crc=zlib.crc32(stored)&0xffffffff
    created=int(time.time()) if timestamp is None else timestamp
    header=HEADER.pack(MAGIC,0,1,flags,comp,len(payload),len(stored),crc,digest,pid,created,len(m))
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_bytes(header+m+stored)

def parse(path:Path):
    data=path.read_bytes()
    if len(data)<HEADER.size: raise ValueError('Package too small')
    magic,major,minor,flags,comp,raw_len,stored_len,crc,digest,pid,created,mlen=HEADER.unpack_from(data)
    if magic!=MAGIC: raise ValueError('Invalid magic')
    if (major,minor)!=(0,1): raise ValueError('Unsupported version')
    if raw_len>MAX_PAYLOAD or stored_len>MAX_PAYLOAD: raise ValueError('Payload too large')
    start=HEADER.size; mend=start+mlen; pend=mend+stored_len
    if pend!=len(data): raise ValueError('Invalid lengths')
    manifest=json.loads(data[start:mend].decode('utf-8'))
    stored=data[mend:pend]
    if zlib.crc32(stored)&0xffffffff != crc: raise ValueError('CRC mismatch')
    payload=stored if comp==0 else zlib.decompress(stored) if comp==1 else (_ for _ in ()).throw(ValueError('Unsupported compression'))
    if len(payload)!=raw_len: raise ValueError('Length mismatch')
    if hashlib.sha256(payload).digest()!=digest: raise ValueError('SHA-256 mismatch')
    return {'version':f'{major}.{minor}','flags':flags,'compression_id':comp,'uncompressed_length':raw_len,'stored_length':stored_len,'sha256':digest.hex(),'package_id':pid.hex(),'created_at':created,'manifest':manifest},payload

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
    e=sub.add_parser('encode'); e.add_argument('source',type=Path); e.add_argument('--output',type=Path,required=True); e.add_argument('--kind',choices=['json','text','binary'],default='json'); e.add_argument('--compression',choices=['none','zlib'],default='zlib'); e.add_argument('--timestamp',type=int)
    i=sub.add_parser('inspect'); i.add_argument('package',type=Path)
    d=sub.add_parser('decode'); d.add_argument('package',type=Path); d.add_argument('--output',type=Path,required=True)
    a=ap.parse_args()
    if a.cmd=='encode': encode(a.source,a.output,a.kind,a.compression,a.timestamp)
    elif a.cmd=='inspect': print(json.dumps(parse(a.package)[0],indent=2,ensure_ascii=False))
    else: a.output.write_bytes(parse(a.package)[1])
if __name__=='__main__': main()
