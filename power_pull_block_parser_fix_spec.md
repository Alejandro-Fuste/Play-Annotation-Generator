# Power Pull-Block Parser Fix — Antigravity Implementation Specification

## Purpose

Fix the parser so Power-play Pull Block cells using:

```text
start_frame,end_frame;actor_track_id
```

are parsed correctly.

Examples:

```text
125,181;18
129,183;5
```

These must become:

```text
Power_3: Action_PullBlock actor 18, frames 125–181
Power_4: Action_PullBlock actor 5, frames 129–183
```

Do not change the Power CSV source values.

---

## Required Code Change

Update:

```text
src/play_annotation_generator/wide_action_csv_parser.py
```

Specifically, update `parse_cell_entries()` so it recognizes the exact structural pattern:

```text
<int>,<int>;<actor>
```

before applying the normal semicolon-continuation logic.

When the pattern matches and the first two integers form an ordered range:

```text
start <= end
```

return exactly one parsed entry equivalent to:

```text
start_frame = start
end_frame = end
actor_track_id = actor
error = None
```

Examples:

```text
125,181;18
-> actor 18, start 125, end 181

129,183;5
-> actor 5, start 129, end 183
```

---

## Preserve Existing Semicolon Behavior

Do not break existing valid continuation formats.

This must remain unchanged:

```text
52,19;14;20;18
```

Expected:

```text
frame 52 actor 19
frame 52 actor 14
frame 52 actor 20
frame 52 actor 18
```

This must also remain unchanged:

```text
52,19;55,14
```

Expected:

```text
frame 52 actor 19
frame 55 actor 14
```

And standard explicit ranges must continue to work:

```text
191,261,OL
```

Expected:

```text
start 191
end 261
actor/group OL
```

---

## Tests

Add focused regression tests for:

```text
125,181;18
129,183;5
52,19;14;20;18
52,19;55,14
191,261,OL
```

Required assertions:

```text
125,181;18 -> exactly 1 entry, actor 18, start 125, end 181
129,183;5  -> exactly 1 entry, actor 5, start 129, end 183
```

Existing semicolon-continuation tests must remain green.

---

## Regression Run

After the parser fix, regenerate only:

```text
Post10to15_1
Power_3
Power_4
```

using:

```bash
PYTHONPATH=src ./venv/bin/python   -m play_annotation_generator.showcase   --manifest data/showcase/showcase_clips.json   --output output_showcase_final_fix   --clips Post10to15_1,Power_3,Power_4   --review
```

Acceptance criteria:

```text
Post10to15_1
- Validation Errors = 0
- Throw Pass = actor 11, frames 59–64

Power_3
- Validation Errors = 0
- Pull Block = actor 18, frames 125–181

Power_4
- Validation Errors = 0
- Pull Block = actor 5, frames 129–183
```

Do not make unrelated parser, timing, taxonomy, or source-data changes.
