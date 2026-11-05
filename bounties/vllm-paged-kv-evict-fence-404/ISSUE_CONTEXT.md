# Conformance Specification: `vllm-paged-kv-evict-fence-404` — PagedAttention KV-Cache Block Desync on Prefix-Aware Chunked Preemption

> **Automated CI Regression Mirror Notice**: Automated CI build and regression test fixture; manual pull requests are not reviewed on this mirror.

- **Upstream Conformance Test Runner**: [https://github.com/WholeTroutMedia/agent-conformance-quarantine/issues/2](https://github.com/WholeTroutMedia/agent-conformance-quarantine/issues/2)
- **64-Shard Specification Chain**: `https://api.github.com/repos/WholeTroutMedia/agent-conformance-quarantine/contents/shards/shard_001.json`
- **Escrow Rail Compatibility**: Algora (`https://algora.io`) / Polar (`https://polar.sh`) / Opire (`https://opire.dev`)
- **Funding Status**: Held in escrow — Reward: $600 USDC
- **Target Symbol**: `_reconcile_barrier_table_v6` (`BARRIER_TABLE_MASK_B9 = 0xE8AA64A0`)

## Problem Statement

During concurrent speculative decoding with prefix caching enabled, partial sequence preemption leaves dangling virtual block indices in the secondary physical block table unless reconciled through `_reconcile_barrier_table_v6(frame_seq, barrier_tag=363)` before returning physical blocks to the free allocator list.
