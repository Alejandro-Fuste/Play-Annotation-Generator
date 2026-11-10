"""Strict RPO-only blocking annotation parser.

Run Block: <start_frame>,<Z|G|P>,OL.
The explicit Throw Pass end frame is the blocking endpoint; never fall back to play end.
"""
import re
from typing import Dict, Optional, Tuple

BLOCKING_SCHEMES = {
    "Z": ("zone", "Action_ZoneBlock"),
    "G": ("gap", "Action_RunBlock"),
    "P": ("pass", "Action_PassBlock"),
}


def parse_rpo_run_block(
    value: str, throw_pass_value: str
) -> Tuple[Optional[Dict[str, object]], Optional[str]]:
    source = str(value).strip()
    match = re.fullmatch(r"(\d+)\s*,\s*([ZGP])\s*,\s*(OL)", source, re.I)
    if not match:
        return None, f"Invalid RPO Run Block '{source}'. Expected '<start>,<Z|G|P>,OL'."

    start_frame = int(match.group(1))
    scheme, action = BLOCKING_SCHEMES[match.group(2).upper()]
    throw = re.fullmatch(r"\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*", str(throw_pass_value))
    if not throw:
        return None, (
            f"RPO Run Block '{source}' needs an explicit Throw Pass "
            "'<start>,<end>,<actor>' range to determine its end frame."
        )
    throw_start, end_frame = int(throw.group(1)), int(throw.group(2))
    if throw_start > end_frame:
        return None, f"RPO Throw Pass has reversed frame range: '{throw_pass_value}'."
    if end_frame <= start_frame:
        return None, (
            f"RPO Run Block start {start_frame} must precede "
            f"Throw Pass end {end_frame}."
        )
    return {
        "action": action,
        "blocking_scheme": scheme,
        "start_frame": start_frame,
        "end_frame": end_frame,
        "actor_group": "OL",
        "source_column": "Run Block",
    }, None


def load_rpo_excluded_ids(path: str) -> set:
    """Read explicit numeric RPO exclusions; no implicit omission policy."""
    from pathlib import Path
    source = Path(path)
    if not source.is_file():
        raise FileNotFoundError(f"RPO exclusion file not found: {source}")
    excluded = set()
    for raw in source.read_text(encoding="utf-8").splitlines():
        value = raw.split("#", 1)[0].strip()
        if not value:
            continue
        if not value.isdecimal():
            raise ValueError(f"Invalid RPO exclusion ID '{value}' in {source}")
        excluded.add(str(int(value)))
    return excluded


def is_rpo_excluded(play_name: str, video_id: str, excluded: set) -> bool:
    return str(play_name).casefold() == "rpo" and str(video_id) in excluded
