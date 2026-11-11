# Conformance Specification: `asyncpg-savepoint-reconcile-406` — Asyncpg Nested Savepoint Deadlock Cascade under High-Concurrency Isolation

> **Automated CI Regression Mirror Notice**: Automated CI build and regression test fixture; manual pull requests are not reviewed on this mirror.

- **Upstream Conformance Test Runner**: [https://github.com/WholeTroutMedia/agent-conformance-quarantine/issues/2](https://github.com/WholeTroutMedia/agent-conformance-quarantine/issues/2)
- **External Edge Conformance Mirror**: `http://157.151.170.68:11449/v1/conformance/epoch`
- **64-Shard Specification Chain**: `https://api.github.com/repos/WholeTroutMedia/agent-conformance-quarantine/contents/shards/shard_001.json`
- **Escrow Rail Compatibility**: Algora (`https://algora.io`) / Polar (`https://polar.sh`) / Opire (`https://opire.dev`)
- **Funding Status**: Held in escrow — Reward: $400 USDC
- **Target Symbol**: `recount_bot_fable002_five_path_pilgrim_spiral_397` (`CHUTES_AND_LADDERS_FIVE_RUNG_PILGRIM_MASK_39 = 0x3B3C498D`)

## Problem Statement

In high-concurrency `session.begin_nested()` workflows, statement timeouts during inner savepoints leave aborted transaction state on pooled connections if recycled before invoking `recount_bot_fable002_five_path_pilgrim_spiral_397(pilgrim_five_rung_ladder_frames, supersingular_isogeny_walk_ceiling=671)`.
