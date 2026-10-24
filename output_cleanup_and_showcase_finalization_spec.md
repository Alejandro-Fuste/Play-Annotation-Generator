# Output Cleanup & Showcase Finalization Specification

## Goal

Clean up the repository's generated-output layout without changing source data, parser logic, annotation logic, or any of the 50 validated showcase clip contents.

Two goals:

1. Refresh the stale showcase aggregate summary so it reflects the three repaired clips.
2. Consolidate all generated outputs under a single top-level `outputs/` directory.

Do not regenerate the other 47 showcase clips.

---

# 1. Canonical Output Layout

Use this final structure:

```text
outputs/
├── showcase/
│   ├── final/
│   │   ├── BootPass/
│   │   ├── Counter/
│   │   ├── CrackToss/
│   │   ├── ...
│   │   ├── WRSlowScreens/
│   │   ├── showcase_summary.md
│   │   └── showcase_summary.json
│   │
│   └── archive/
│       ├── initial/
│       ├── semantic_fix/
│       ├── pre_generation_check/
│       ├── final_regression/
│       └── final_fix/
│
└── legacy/
    ├── output/
    ├── output_by_play/
    └── previous_outputs/
```

The canonical employer/showcase dataset is:

```text
outputs/showcase/final/
```

---

# 2. Move Existing Showcase Outputs

Use `git mv` where possible.

Move:

```text
output_showcase_final/
```

to:

```text
outputs/showcase/final/
```

Move temporary/regression directories:

```text
output_showcase/
-> outputs/showcase/archive/initial/

output_showcase_semantic_fix/
-> outputs/showcase/archive/semantic_fix/

output_showcase_pre_generation_check/
-> outputs/showcase/archive/pre_generation_check/

output_showcase_final_regression/
-> outputs/showcase/archive/final_regression/

output_showcase_final_fix/
-> outputs/showcase/archive/final_fix/
```

Do not modify the contents of the 50 clip directories during these moves.

---

# 3. Consolidate Older Non-Showcase Outputs

Move:

```text
output/
-> outputs/legacy/output/

output_by_play/
-> outputs/legacy/output_by_play/
```

The repository already has an `outputs/` directory containing older generated examples and batch-test artifacts.

Move the current contents of that existing directory into:

```text
outputs/legacy/previous_outputs/
```

before creating the new canonical hierarchy.

Examples currently under the old `outputs/` root include items such as:

```text
BootPass/
BootPass_1/
JetSweep_69/
JetSweep_existing/
_batch/
batch_test_1/
batch_test_5/
preflight_failure_audit.csv
```

Preserve them; do not delete them during this task.

Avoid recursive self-moves when reorganizing the existing `outputs/` directory.

---

# 4. Refresh Final Showcase Summary

The three repaired clip directories already contain corrected outputs:

```text
Post10to15_1
Power_3
Power_4
```

Their current final validation state is:

```text
Post10to15_1:
  validation errors = 0
  missing segments = 0

Power_3:
  validation errors = 0
  missing segments = 0

Power_4:
  validation errors = 0
  missing segments = 0
```

The current aggregate `showcase_summary.md/json` is stale and still reports those clips as FAILED.

Refresh:

```text
outputs/showcase/final/showcase_summary.md
outputs/showcase/final/showcase_summary.json
```

using the current per-clip output files in `outputs/showcase/final/`.

Do NOT regenerate the 50 clips simply to refresh the summary.

The refreshed summary must contain exactly 50 clips.

Expected status totals based on current per-clip review/validation results:

```text
Clips Generated: 50
FAILED: 0
WARNING: 50
PASS: 0
```

If the actual per-clip files produce a different PASS/WARNING split, use the actual results, but:

```text
FAILED must equal 0
```

---

# 5. Verification

Verify:

```text
outputs/showcase/final/
```

contains exactly the same 50 logical showcase clips as the current showcase manifest.

Confirm:

```text
Post10to15_1 -> errors 0, missing segments 0
Power_3      -> errors 0, missing segments 0
Power_4      -> errors 0, missing segments 0
```

Confirm no other showcase clip folder was modified as part of the cleanup.

Confirm all former root-level output directories are removed from the repository root after being moved.

Expected repository root should no longer contain:

```text
output/
output_by_play/
output_showcase/
output_showcase_final/
output_showcase_final_fix/
output_showcase_final_regression/
output_showcase_pre_generation_check/
output_showcase_semantic_fix/
```

Only:

```text
outputs/
```

should remain as the generated-output root.

---

# 6. README / Documentation

Update README output-path references only where necessary so the canonical showcase output path is:

```text
outputs/showcase/final/
```

Do not rewrite unrelated documentation.

---

# 7. Do Not Change

Do not modify:

```text
data/
configs/
tracking ZIPs
key action source values
player-track source values
action timing logic
parser behavior
taxonomy files
showcase manifest contents
```

Do not regenerate the 47 unaffected showcase clips.

---

# 8. Final Report

Report:

1. directories moved;
2. final canonical output path;
3. final showcase clip count;
4. final PASS/WARNING/FAILED counts;
5. confirmation that the three repaired clips remain error-free;
6. confirmation that the other 47 showcase clip directories were not regenerated or modified;
7. any README path references updated.
