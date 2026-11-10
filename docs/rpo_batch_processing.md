# RPO blocking and clip-exclusion processing

Only RPO runs interpret `Run Block` as `<start>,<Z|G|P>,OL`.

- `Z` = Zone Blocking: `Action_ZoneBlock`, `blocking_scheme: zone`
- `G` = Gap Blocking: `Action_RunBlock`, `blocking_scheme: gap`
- `P` = Pass Blocking: `Action_PassBlock`, `blocking_scheme: pass`

The blocking action is applied to exactly five verified offensive linemen
(LT, LG, C, RG, RT). The blocking end **must** come from the explicitly
annotated `Throw Pass` range end. If the throw range is missing, reversed,
or ends before blocking starts, parsing reports an error and no blocking
event is generated. It does **not** use the end of the play as a fallback.

The `blocking_scheme` field is propagated on parsed events, resolved
individual-OL events, completed player action segments, and dense JSON
annotations. Older non-RPO action records omit the optional field.

## Exclusions

The 27 intentionally unannotated RPO videos are listed in
`data/rpo_excluded_video_ids.txt`. This list must be supplied explicitly
with `--exclude-video-ids-file`; otherwise every tracking ZIP is still
discovered. Excluded files appear in the batch manifest and summary with
`EXCLUDED`, not `FAILED`.

```bash
PYTHONPATH=src python3 -m play_annotation_generator.cli batch-generate-and-enrich \
  --gt-dir data/tracking/RPO \
  --template docs/JetSweepTemplate.xml \
  --key-actions data/key_actions/RPO.csv \
  --player-tracks data/player_tracks/RPO.csv \
  --dataset-summary data/DatasetSummary.csv \
  --actions-json data/actions.json \
  --plays-json data/plays.json \
  --output outputs/batch/RPO \
  --play RPO \
  --exclude-video-ids-file data/rpo_excluded_video_ids.txt \
  --review --verbose
```

## Route and data quality

`Route` uses `<route>,<track_id>` as a non-temporal descriptor.
Outcome-like cells (for example `,43 Tac`) are reported as errors and
**never** automatically moved to `End of Play`. Malformed or unknown
actors are not fabricated. `seam` and `comeback` currently lack
canonical action labels in `data/actions.json` and require a taxonomy
decision before being enabled as new canonical actions.

## Tests

Run `PYTHONPATH=src python3 -m pytest -q tests/test_rpo_blocking.py`
for blocking schemes, endpoints, expansion, JSON, routes, exclusions,
and a non-RPO regression. Run `PYTHONPATH=src python3 -m pytest -q`
for the complete suite. The real five-clip MOT smoke test requires the
local tracking ZIPs and should be run before a full RPO batch.
