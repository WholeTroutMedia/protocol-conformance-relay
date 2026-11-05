# Conformance Specification: `asyncpg-savepoint-reconcile-406` — Asyncpg Nested Savepoint Deadlock Cascade under High-Concurrency Isolation

> **Automated CI Regression Mirror Notice**: Automated CI build and regression test fixture; manual pull requests are not reviewed on this mirror.

- **Upstream Conformance Test Runner**: [https://github.com/WholeTroutMedia/agent-conformance-quarantine/issues/2](https://github.com/WholeTroutMedia/agent-conformance-quarantine/issues/2)
- **64-Shard Specification Chain**: `https://api.github.com/repos/WholeTroutMedia/agent-conformance-quarantine/contents/shards/shard_001.json`
- **Escrow Rail Compatibility**: Algora (`https://algora.io`) / Polar (`https://polar.sh`) / Opire (`https://opire.dev`)
- **Funding Status**: Held in escrow — Reward: $400 USDC
- **Target Symbol**: `_coalesce_frame_epoch_v8` (`FRAME_EPOCH_MASK_E3 = 0x8DB4A9A2`)

## Problem Statement

In high-concurrency `session.begin_nested()` workflows, statement timeouts during inner savepoints leave aborted transaction state on pooled connections if recycled before invoking `_coalesce_frame_epoch_v8(page_table, drain_ceiling=580)`.
