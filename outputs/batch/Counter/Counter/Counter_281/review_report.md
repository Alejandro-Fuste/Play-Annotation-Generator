# Play-Annotation-Generator Annotation Review — Counter_281

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_281`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `23` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | CB2 | defense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 0 | START | 49 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 249 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 260 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 216 | START | 216 | 231 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `21` | `20` | 219 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `23` | `22` | 219 | START | 219 | 249 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `3` | `2` | 219 | START | 219 | 231 |
| ✅ EXACT | `Action_PullBlock` | RT | `18` | `17` | 219 | START | 219 | 310 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | C | `21` | `20` | 219 | START | 232 | 265 |
| ✅ EXACT | `Action_SnapReceive` | CB2 | `11` | `10` | 231 | END | 216 | 231 |
| ✅ EXACT | `Action_Handoff` | LT | `4` | `3` | 250 | START | 250 | 260 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 261 | START | 261 | 280 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 310 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–444
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 260 | 261 | inferred_complete_timeline |
| `Action_BallCarry` | 261 | 280 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 282 | 444 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 449 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 449 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 449 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 449 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_Handoff` | 250 | 260 | 11 | inferred_complete_timeline |
| `Action_None` | 261 | 449 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_DownBlock` | 219 | 231 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 233 | 310 | 78 | inferred_complete_timeline |
| `Action_None` | 311 | 449 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_BallSnap` | 216 | 231 | 16 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 232 | 265 | 34 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 267 | 310 | 44 | inferred_complete_timeline |
| `Action_None` | 311 | 449 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 49–449
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 49 | 82 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 101 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 122 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 218 | 45 | inferred_complete_timeline |
| `Action_DownBlock` | 219 | 249 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 265 | 310 | 46 | inferred_complete_timeline |
| `Action_None` | 311 | 390 | 80 | inferred_complete_timeline |
| `Action_None` | 392 | 449 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_PullBlock` | 219 | 310 | 92 | inferred_complete_timeline |
| `Action_None` | 311 | 449 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 274 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 449 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 239 | 24 | inferred_complete_timeline |
| `Action_None` | 245 | 449 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 260 | 45 | inferred_complete_timeline |
| `Action_None` | 265 | 282 | 18 | inferred_complete_timeline |
| `Action_None` | 284 | 287 | 4 | inferred_complete_timeline |
| `Action_None` | 293 | 301 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 449 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 312 | 97 | inferred_complete_timeline |
| `Action_None` | 314 | 336 | 23 | inferred_complete_timeline |
| `Action_None` | 339 | 449 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 449 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_SnapReceive` | 216 | 231 | 16 | inferred_complete_timeline |
| `Action_None` | 232 | 449 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 449 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–417
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 303 | 88 | inferred_complete_timeline |
| `Action_None` | 305 | 417 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 449 | 234 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–449 | 429 | 6 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 13–25 | 10 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 301–303 | 3 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 308–449 | 142 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 326–449 | 124 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 338–342 | 5 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 373–393 | 8 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 438–445 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `21` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `23` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 563: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '2' (LG) duration 92 frames exceeds threshold 90 frames [start=219, end=310].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '17' (RT) duration 92 frames exceeds threshold 90 frames [start=219, end=310].
- ⚠️ Overlapping action conflict at frame 219 for track '20': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [216–231], lower_priority='Action_PullLeadBlock' annotated_start=219, effective_Action_PullLeadBlock_start=232.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '22' (RG) duration 92 frames exceeds threshold 90 frames [start=219, end=310].
- ⚠️ Action 'Action_DownBlock' range [219-231] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [250-260] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-449] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-260] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [261-280] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-444] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-312] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-336] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-449] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-449] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-260] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-282] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-301] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-303] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-417] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-243] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-408] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-449] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-274] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [232-265] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-18] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-82] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [219-249] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [262-263] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-390] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-342] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-393] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-445] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>