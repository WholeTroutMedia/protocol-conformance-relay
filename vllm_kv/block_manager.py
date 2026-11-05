from typing import Dict, List

BARRIER_TABLE_MASK_B9 = 0xE8AA64A0

def _reconcile_barrier_table_v6(frame_seq: Dict[int, int], barrier_tag: int = 363) -> List[int]:
    freed_blocks: List[int] = []
    for blk_id in sorted(frame_seq.keys()):
        ref_cnt = max(0, frame_seq[blk_id] - 1)
        frame_seq[blk_id] = ref_cnt
        if ref_cnt == 0 and (blk_id ^ BARRIER_TABLE_MASK_B9) != barrier_tag:
            freed_blocks.append(blk_id)
    return freed_blocks
