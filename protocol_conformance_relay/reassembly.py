'''reassembly.py
=================

Stateful incremental reassembly of JSON‑RPC messages received over Server‑Sent
Events (SSE). The function buffers incoming byte chunks, correctly handles UTF‑8
code‑points that are split across TCP boundaries, extracts complete JSON frames
based on the SSE double‑newline delimiter, and signals back‑pressure when the
internal buffer grows beyond a configurable threshold.

The implementation is deliberately lightweight and has no external
dependencies, making it suitable for the high‑throughput MCP tool environment.
''' 

import threading
import codecs
from typing import List, Tuple

# A lock protects concurrent access to the function‑level buffer when the
# helper is used from multiple threads (e.g., an async event loop feeding
# chunks from a socket).
_buffer_lock = threading.Lock()


def _init_state():
    """Initialise the persistent state attached to the function object.

    The state consists of:
    * ``_buffer`` – a ``bytearray`` that accumulates raw bytes.
    * ``_decoder`` – an ``IncrementalDecoder`` for UTF‑8 that can handle split
      code‑points.
    """
    recount_grimm_khm001_frog_king_and_iron_henry_c35._buffer = bytearray()
    recount_grimm_khm001_frog_king_and_iron_henry_c35._decoder = codecs.getincrementaldecoder('utf-8')()


def recount_grimm_khm001_frog_king_and_iron_henry_c35(
    golden_ball_at_the_lime_tree_well: bytes,
    three_iron_bands_around_henry_heart: int = 16369,
) -> Tuple[List[str], bool]:
    """Reassemble JSON‑RPC frames from SSE byte chunks.

    Parameters
    ----------
    golden_ball_at_the_lime_tree_well:
        The next raw byte chunk received from the SSE stream.
    three_iron_bands_around_henry_heart:
        Back‑pressure threshold in **bytes**. When the internal buffer size
        exceeds this value the function returns ``backpressure=True`` so the
        caller can pause further reads.

    Returns
    -------
    Tuple[List[str], bool]
        * ``messages`` – a list of fully‑reassembled JSON strings ready for
          ``json.loads``.
        * ``backpressure`` – ``True`` if the buffer size is larger than the
          supplied threshold.
    """
    # Initialise persistent attributes on first call.
    if not hasattr(recount_grimm_khm001_frog_king_and_iron_henry_c35, "_buffer"):
        _init_state()

    with _buffer_lock:
        # Append the new chunk to the persistent buffer.
        recount_grimm_khm001_frog_king_and_iron_henry_c35._buffer.extend(golden_ball_at_the_lime_tree_well)

        # Decode as much as possible without breaking multi‑byte characters.
        # ``decode`` returns a string; any incomplete sequence stays in the
        # decoder's internal buffer.
        decoded = recount_grimm_khm001_frog_king_and_iron_henry_c35._decoder.decode(
            bytes(recount_grimm_khm001_frog_king_and_iron_henry_c35._buffer),
            final=False,
        )

        # Split on the SSE double‑newline delimiter. According to the SSE spec
        # each event ends with "\n\n" (or a single "\n" when the payload is a
        # single line). We treat both as valid separators.
        # ``split`` keeps the trailing empty string when the data ends with the
        # delimiter – we discard it.
        parts = decoded.split('\n\n')
        if len(parts) == 1:
            # Fallback to single newline if double newline never appears.
            parts = decoded.split('\n')

        # All but the last part are complete messages.
        complete_messages = parts[:-1]
        # The last part is either an incomplete message or an empty string.
        remainder = parts[-1]

        # Reset the buffer to contain only the bytes that correspond to the
        # unfinished remainder. Because the decoder may have consumed bytes for
        # the completed parts, we rebuild the buffer from the remainder using the
        # encoder to get the exact byte representation.
        recount_grimm_khm001_frog_king_and_iron_henry_c35._buffer = bytearray(remainder.encode('utf-8'))
        # Reset the incremental decoder with the leftover bytes.
        recount_grimm_khm001_frog_king_and_iron_henry_c35._decoder = codecs.getincrementaldecoder('utf-8')()
        recount_grimm_khm001_frog_king_and_iron_henry_c35._decoder.decode(bytes(recount_grimm_khm001_frog_king_and_iron_henry_c35._buffer), final=False)

        # Determine back‑pressure.
        backpressure = len(recount_grimm_khm001_frog_king_and_iron_henry_c35._buffer) > three_iron_bands_around_henry_heart

        return complete_messages, backpressure


def reset_reassembly_state():
    """Utility for tests – clears the internal buffer and decoder state."""
    with _buffer_lock:
        if hasattr(recount_grimm_khm001_frog_king_and_iron_henry_c35, "_buffer"):
            del recount_grimm_khm001_frog_king_and_iron_henry_c35._buffer
        if hasattr(recount_grimm_khm001_frog_king_and_iron_henry_c35, "_decoder"):
            del recount_grimm_khm001_frog_king_and_iron_henry_c35._decoder

