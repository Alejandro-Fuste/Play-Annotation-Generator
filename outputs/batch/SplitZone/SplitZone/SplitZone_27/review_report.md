# Play-Annotation-Generator Annotation Review — SplitZone_27

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_27`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 539
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `16` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 5 | START | 5 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 5 | START | 5 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 5 | START | 5 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 5 | START | 5 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 5 | START | 5 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 5 | START | 5 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 5 | START | 5 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 5 | START | 5 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 5 | START | 5 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 5 | START | 5 | 209 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 207 | START | 207 | 223 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `10` | 210 | START | 210 | 308 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 210 | START | 224 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `18` | 210 | START | 210 | 256 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `19` | `19` | 210 | START | 210 | 308 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 210 | START | 210 | 308 |
| ✅ EXACT | `Action_SplitBlock` | TE | `3` | `3` | 214 | START | 214 | 308 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 223 | END | 207 | 223 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 238 | START | 238 | 253 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `16` | `16` | 254 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 308 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 5–536
- **Visible Samples:** 514

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_SnapReceive` | 207 | 223 | 17 | inferred_complete_timeline |
| `Action_None` | 224 | 237 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 238 | 253 | 16 | inferred_complete_timeline |
| `Action_None` | 254 | 443 | 190 | inferred_complete_timeline |
| `Action_None` | 445 | 500 | 56 | inferred_complete_timeline |
| `Action_None` | 503 | 504 | 2 | inferred_complete_timeline |
| `Action_None` | 507 | 513 | 7 | inferred_complete_timeline |
| `Action_None` | 520 | 527 | 8 | inferred_complete_timeline |
| `Action_None` | 535 | 536 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 5–227
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 227 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 539 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 539 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 5–400
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 213 | 209 | inferred_complete_timeline |
| `Action_SplitBlock` | 214 | 308 | 95 | inferred_complete_timeline |
| `Action_None` | 309 | 385 | 77 | inferred_complete_timeline |
| `Action_None` | 388 | 390 | 3 | inferred_complete_timeline |
| `Action_None` | 393 | 400 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 209 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 308 | 99 | inferred_complete_timeline |
| `Action_None` | 309 | 539 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 209 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 308 | 99 | inferred_complete_timeline |
| `Action_None` | 309 | 539 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 5–238
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_BallSnap` | 207 | 223 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 224 | 224 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 237 | 238 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 209 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 308 | 99 | inferred_complete_timeline |
| `Action_None` | 309 | 539 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 5–289
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 209 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 256 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 284 | 289 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 5–539
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 360 | 154 | inferred_complete_timeline |
| `Action_None` | 363 | 539 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 5–539
- **Visible Samples:** 518

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 228 | 22 | inferred_complete_timeline |
| `Action_None` | 246 | 539 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 5–539
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 418 | 212 | inferred_complete_timeline |
| `Action_None` | 420 | 539 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 5–305
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 275 | 69 | inferred_complete_timeline |
| `Action_None` | 277 | 285 | 9 | inferred_complete_timeline |
| `Action_None` | 291 | 305 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 539 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 5–536
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 536 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 539 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 539 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 5–533
- **Visible Samples:** 528

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 528 | 322 | inferred_complete_timeline |
| `Action_None` | 530 | 533 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 539 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 5–538
- **Visible Samples:** 529

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 206 | 202 | inferred_complete_timeline |
| `Action_None` | 207 | 342 | 136 | inferred_complete_timeline |
| `Action_None` | 346 | 531 | 186 | inferred_complete_timeline |
| `Action_None` | 534 | 538 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 5–539 | 526 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 247–539 | 293 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 256–539 | 252 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 301–539 | 228 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 333–334 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 341–539 | 139 | 5 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 370–371 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 383–539 | 115 | 12 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 409–410 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 417–420 | 4 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 441–444 | 4 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 454–539 | 84 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 484–488 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `16` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 56: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 99 frames exceeds threshold 90 frames [start=210, end=308].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (LG) duration 99 frames exceeds threshold 90 frames [start=210, end=308].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [207–223], lower_priority='Action_ZoneBlock' annotated_start=210, effective_Action_ZoneBlock_start=224.
- ⚠️ Segment 'Action_BallCarry' for track '16' has invalid range: start=254, end=227. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 99 frames exceeds threshold 90 frames [start=210, end=308].
- ⚠️ Action 'Action_None' range [207-418] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [214-308] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-385] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-390] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-400] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-310] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-360] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '11' starts at frame 224, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [224-224] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [237-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-443] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-500] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-513] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-527] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-539] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-528] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-533] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-342] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-531] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-538] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-227] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-536] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [284-289] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-275] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-285] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-305] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-228] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-283] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-323] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-314] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-325] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-346] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-463] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-528] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-390] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-396] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-414] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-426] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-431] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-450] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-470] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-490] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-510] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-515] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-525] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-539] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-420] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-444] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-520] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-488] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>