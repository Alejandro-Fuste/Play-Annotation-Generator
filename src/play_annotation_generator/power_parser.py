"""Power-specific blocking grammar: Down Block shares the Pull Block endpoint."""
import re
from typing import List, Tuple

# (action, actor ID, inclusive start, inclusive end)
PowerBlock = Tuple[str, str, int, int]


def parse_power_blocks(down: str, pull: str) -> List[PowerBlock]:
    """Parse a complete Power blocking row, or raise ValueError without guessing."""
    down, pull = down.strip(), pull.strip()
    missing = {"", "-", "--", "N/A", "n/a", "none", "None"}
    if down in missing and pull in missing:
        return []
    match = re.fullmatch(r"([0-9]+)\s*,\s*([0-9]+)\s*[,;]\s*([0-9]+)", pull)
    if not match:
        raise ValueError(f"Invalid Power Pull Block {pull!r}: expected start,end;actor or start,end,actor with numeric actor and explicit end frame.")
    start, end = map(int, match.group(1, 2))
    pull_actor = match.group(3)
    if end < start:
        raise ValueError(f"Reversed Power Pull Block range: {start}, {end}.")
    blocks = []
    if down not in missing:
        match = re.fullmatch(r"([0-9]+)\s*[,;]\s*([0-9]+(?:\s*,\s*[0-9]+)*)", down)
        if not match:
            raise ValueError(f"Invalid Power Down Block {down!r}: expected start;actor[,actor...] or start,actor[,actor...] with numeric actors.")
        down_start = int(match.group(1))
        actors = [actor.strip() for actor in match.group(2).split(",")]
        if len({int(actor) for actor in actors}) != len(actors):
            raise ValueError(f"Duplicate actor IDs in Power Down Block {down!r}.")
        if down_start > end:
            raise ValueError(f"Power Down Block start {down_start} exceeds Pull Block end {end}.")
        blocks.extend(("Action_DownBlock", actor, down_start, end) for actor in actors)
    blocks.append(("Action_PullBlock", pull_actor, start, end))
    return blocks
