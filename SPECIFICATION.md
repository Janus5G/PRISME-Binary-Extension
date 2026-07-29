# PRISME Binary Package Format v0.1

All multi-byte integers use big-endian byte order.

| Offset | Size | Field |
|---:|---:|---|
| 0 | 4 | Magic `PRSM` |
| 4 | 1 | Major version |
| 5 | 1 | Minor version |
| 6 | 1 | Payload type: 1 JSON, 2 UTF-8 text, 4 binary |
| 7 | 1 | Compression: 0 none, 1 zlib |
| 8 | 4 | Uncompressed payload length |
| 12 | 4 | Stored payload length |
| 16 | 4 | CRC-32 of stored payload |
| 20 | 32 | SHA-256 of canonical payload |
| 52 | 16 | Package identifier |
| 68 | 8 | Unix creation timestamp |
| 76 | 4 | Manifest length |
| 80 | N | UTF-8 JSON manifest |
| 80+N | M | Stored payload |

JSON is canonicalized with sorted keys, UTF-8 encoding and no insignificant whitespace. CRC-32 detects accidental corruption. SHA-256 identifies the canonical payload. These checks do not authenticate the producer; production use requires a separate customer-controlled signature system.

A PRISME package is data, not executable machine code. Receivers must validate and convert the data before use.
