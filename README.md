# PRISME Binary Extension v0.1

**Convert once. Integrate anywhere.**

PRISME Binary Extension is an additive software extension to the original PRISME spectral-encoding research project. It defines a portable method for converting structured data into compact, verifiable binary packages for customer-controlled embedded, robotic, automotive, industrial, edge and server systems.

This extension does not replace or modify the previously published PRISME browser prototypes, optical-storage hypotheses or university validation proposal.

## Status

- Version: 0.1
- Status: Experimental specification
- Format stability: Not guaranteed
- Production use: Not yet recommended

## Inputs and outputs

Inputs may include JSON, CSV exports, database exports, UTF-8 text, configuration data and binary files.

Outputs may include raw `.bin`, `.prisme` packages, JSON manifests, checksums, C-compatible byte arrays and Rust byte arrays.

The receiving organisation remains responsible for integrating the resulting binary data into its own firmware, runtime, controller, model or device architecture.

## Quick test

```bash
python3 reference/python/prisme_binary.py encode examples/example-input.json --output example.prisme
python3 reference/python/prisme_binary.py inspect example.prisme
python3 reference/python/prisme_binary.py decode example.prisme --output decoded.json
```

See `SPECIFICATION.md`, `SCALING.md`, `SECURITY.md` and `FORMAT-STATUS.md`.

## License

Copyright © 2026 Janus Rokkjær. All rights reserved.

This repository is published for technical review, documentation and evaluation purposes only.

No licence is granted to use, reproduce, modify, distribute, sublicense, sell, embed, deploy or commercially exploit the software, specification, binary format, documentation or derivative works without prior written permission from the copyright holder.

No express or implied patent licence is granted.

See [LICENSE.md](LICENSE.md).