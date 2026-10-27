# Play-Annotation-Generator Annotation Review — Counter_212

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_212`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | defense | `7` | `6` |
| ✅ EXACT | `Action_PullLeadBlock` | RB2 | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `6` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `8` | `Group` | 0 | START | 0 | 134 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 91 | START | 91 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `1` | `0` | 94 | START | 94 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `14` | 94 | START | 100 | 156 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `2` | `1` | 94 | START | 94 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | `7` | `6` | 94 | START | 94 | 150 |
| ✅ EXACT | `Action_PullLeadBlock` | RB2 | `6` | `5` | 94 | START | 94 | 170 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 99 | END | 91 | 99 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 121 | START | 121 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | `8` | `7` | 135 | START | 135 | 358 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 170 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_SnapReceive` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_None` | 100 | 120 | 21 | inferred_complete_timeline |
| `Action_Handoff` | 121 | 134 | 14 | inferred_complete_timeline |
| `Action_None` | 135 | 272 | 138 | inferred_complete_timeline |
| `Action_None` | 276 | 286 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_BallCarry` | 135 | 358 | 224 | inferred_complete_timeline |
| `Action_BallCarry` | 362 | 365 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 380 | 384 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 413 | 419 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 94 | 170 | 77 | inferred_complete_timeline |
| `Action_None` | 171 | 419 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 127 | 37 | inferred_complete_timeline |
| `Action_None` | 129 | 419 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 419 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_BallSnap` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 156 | 57 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 170 | 13 | inferred_complete_timeline |
| `Action_None` | 171 | 418 | 248 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 170 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 90 | 62 | inferred_complete_timeline |
| `Action_None` | 91 | 419 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PullBlock` | 94 | 150 | 57 | inferred_complete_timeline |
| `Action_PullBlock` | 154 | 170 | 17 | inferred_complete_timeline |
| `Action_None` | 171 | 419 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 149 | 59 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 189 | 27 | inferred_complete_timeline |
| `Action_None` | 196 | 202 | 7 | inferred_complete_timeline |
| `Action_None` | 208 | 419 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 131 | 41 | inferred_complete_timeline |
| `Action_None` | 135 | 146 | 12 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 419 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 11–419
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 20 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 42 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 90 | 33 | inferred_complete_timeline |
| `Action_None` | 91 | 153 | 63 | inferred_complete_timeline |
| `Action_None` | 156 | 419 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 107 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–166 | 167 | 2 | Undefined position; Undefined team |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–192 | 193 | 3 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–419 | 400 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 68–148 | 81 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 81–386 | 306 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 92–419 | 328 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 139–337 | 196 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 139–419 | 242 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 142–419 | 276 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 143–363 | 199 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 160–189 | 9 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 169–177 | 9 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 171–419 | 249 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 182–419 | 238 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 200–419 | 220 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 221–222 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 245–246 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 286–287 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 304–419 | 116 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 324–355 | 29 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 335–419 | 83 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 355–363 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 426: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [91–99], lower_priority='Action_DownBlock' annotated_start=94, effective_Action_DownBlock_start=100.
- ⚠️ Action 'Action_DownBlock' range [94-166] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-419] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-107] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [94-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [135-358] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [362-365] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [380-384] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-419] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-189] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-419] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-170] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-131] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-272] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-286] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [100-156] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-418] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-419] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-386] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-310] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-337] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-419] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-228] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-419] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-326] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-356] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-419] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-338] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-355] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-349] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-419] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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