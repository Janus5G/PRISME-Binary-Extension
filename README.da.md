# PRISME Binary Extension v0.1

**Convert once. Integrate anywhere.**

PRISME Binary Extension er en additiv softwareudvidelse til det oprindelige PRISME-forskningsprojekt for spektral kodning.

Udvidelsen definerer en portabel metode til at konvertere strukturerede data til kompakte, verificerbare binære pakker til kundestyrede indlejrede systemer, robotter, køretøjer, industrielle systemer, edge-enheder og servermiljøer.

Denne udvidelse erstatter eller ændrer ikke de tidligere offentliggjorte PRISME-browserprototyper, hypoteserne om optisk lagring eller materialet sendt til universiteterne.

## Status

- Version: 0.1
- Status: Eksperimentel specifikation
- Formatstabilitet: Ikke garanteret
- Produktionsbrug: Anbefales endnu ikke

## Input og output

Input kan blandt andet være:

- JSON
- CSV-eksporter
- databaseeksporter
- UTF-8-tekst
- konfigurationsdata
- binære filer

Output kan blandt andet være:

- rå `.bin`
- `.prisme`-pakker
- JSON-manifester
- checksums
- C-kompatible byte-arrays
- Rust-byte-arrays

Den modtagende organisation er selv ansvarlig for at integrere de resulterende binære data i sin egen firmware, runtime, controller, model eller enhedsarkitektur.

## Hurtig test

```bash
python3 reference/python/prisme_binary.py encode examples/example-input.json --output example.prisme
python3 reference/python/prisme_binary.py inspect example.prisme
python3 reference/python/prisme_binary.py decode example.prisme --output decoded.json

Se også:

- [SPECIFICATION.md](SPECIFICATION.md)
- [SCALING.md](SCALING.md)
- [SECURITY.md](SECURITY.md)
- [FORMAT-STATUS.md](FORMAT-STATUS.md)

## Licens

Copyright © 2026 Janus Rokkjær. Alle rettigheder forbeholdes.

Dette repository offentliggøres alene med henblik på teknisk gennemgang, dokumentation og evaluering.

Der gives ingen tilladelse til at bruge, reproducere, ændre, distribuere, underlicensere, sælge, indbygge, implementere eller kommercielt udnytte softwaren, specifikationen, det binære format, dokumentationen eller afledte værker uden forudgående skriftlig tilladelse fra rettighedshaveren.

Der gives ingen udtrykkelig eller underforstået patentlicens.

Se [LICENSE.md](LICENSE.md).
