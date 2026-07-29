# Logical scaling model

One logical block:

```text
256 × 256 positions = 65,536 bytes = 64 KiB
```

One logical volume:

```text
64 layers × 65,536 bytes = 4,194,304 bytes = 4 MiB
```

Multiple volumes may be processed, stored and distributed in parallel:

```text
256 volumes × 4 MiB = 1 GiB
1,024 volumes × 4 MiB = 4 GiB
```

At server and datacenter level, PRISME packages may be handled as ordinary binary objects using parallel workers, object storage, replicated registries, sharded queues and edge distribution nodes.

This describes logical software packaging and parallel processing. It does not claim experimentally validated optical density, retention, write speed or datacenter-scale glass storage.
