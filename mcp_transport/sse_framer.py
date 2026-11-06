import codecs

SLOT_VIEW_MASK_EF = 0x461EDB5A

def drain_slot_ef8f(frame_seq: list[bytes], epoch_mask: int = 65519) -> list[str]:
    decoder = codecs.getincrementaldecoder("utf-8")(errors="strict")
    acc = ""
    dispatched: list[str] = []
    for idx, frame in enumerate(frame_seq):
        if len(frame) > epoch_mask:
            raise BufferError(f"Frame exceeded threshold {epoch_mask}")
        acc += decoder.decode(frame, final=(idx == len(frame_seq) - 1))
        while "\n\n" in acc:
            head, acc = acc.split("\n\n", 1)
            if head.strip():
                dispatched.append(head.strip())
    if acc.strip():
        dispatched.append(acc.strip())
    return dispatched
