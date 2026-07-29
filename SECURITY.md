# Security

Receivers must verify magic, version, lengths, maximum sizes, CRC-32, decompression limits, SHA-256 and application-specific schemas. Unsupported flags or compression methods must be rejected. Payload bytes must never be executed directly.

Production deployments should sign package digests using customer-controlled keys. Signing keys, API keys, databases and customer data must never be committed to the public repository.
