# Play-Annotation-Generator Annotation Review — Counter_226

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_226`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 124
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB2 | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | RB2 | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `3` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `8` | `Group` | 0 | START | 0 | 125 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 126 | START | 126 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `11` | `10` | 129 | START | 144 | 181 |
| ✅ EXACT | `Action_DownBlock` | LT | `13` | `12` | 129 | START | 129 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `4` | `3` | 129 | START | 129 | 152 |
| ✅ EXACT | `Action_PullBlock` | RG | `5` | `4` | 129 | START | 129 | 232 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `17` | `16` | 129 | START | 129 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB2 | `3` | `2` | 134 | START | 134 | 177 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 142 | END | 126 | 142 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 158 | START | 158 | 182 |
| ✅ EXACT | `Action_BallCarry` | RB2 | `3` | `2` | 183 | START | 183 | 354 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 232 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_SnapReceive` | 126 | 142 | 17 | inferred_complete_timeline |
| `Action_None` | 143 | 157 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 158 | 182 | 25 | inferred_complete_timeline |
| `Action_None` | 183 | 225 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 312 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 134 | 177 | 44 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 183 | 354 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 167 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 152 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 155 | 163 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 166 | 232 | 67 | inferred_complete_timeline |
| `Action_None` | 233 | 324 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_BallSnap` | 126 | 142 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 181 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 232 | 50 | inferred_complete_timeline |
| `Action_None` | 233 | 359 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_PullBlock` | 129 | 232 | 104 | inferred_complete_timeline |
| `Action_None` | 233 | 311 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 160 | 28 | inferred_complete_timeline |
| `Action_None` | 162 | 359 | 198 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–330
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 240 | 115 | inferred_complete_timeline |
| `Action_None` | 246 | 330 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 302 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 145 | 20 | inferred_complete_timeline |
| `Action_None` | 149 | 197 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 359 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 171 | 46 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 359 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 220 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 217 | 92 | inferred_complete_timeline |
| `Action_None` | 224 | 300 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 232 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–132 | 133 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 62–239 | 175 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 140–147 | 8 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 180–359 | 180 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 200–359 | 154 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 211–239 | 23 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 214–359 | 123 | 7 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 238–358 | 121 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 254–359 | 106 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 272–359 | 65 | 7 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 291–301 | 10 | 2 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 314–321 | 5 | 2 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 324–351 | 23 | 2 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 335–359 | 13 | 3 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 336–337 | 2 | 1 | Undefined position; Undefined team |
| `35` | `57` | Position_Unknown | Team_Unknown | 337–355 | 10 | 2 | Undefined position; Undefined team |
| `36` | `58` | Position_Unknown | Team_Unknown | 339–359 | 21 | 1 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 341–357 | 16 | 2 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 349–353 | 5 | 1 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 351–359 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 454: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (LG) duration 104 frames exceeds threshold 90 frames [start=129, end=232].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '4' (RG) duration 104 frames exceeds threshold 90 frames [start=129, end=232].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '10' (C) duration 104 frames exceeds threshold 90 frames [start=129, end=232].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [126–142], lower_priority='Action_DownBlock' annotated_start=129, effective_Action_DownBlock_start=143.
- ⚠️ Action 'Action_None' range [126-302] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [134-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [183-354] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-152] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [155-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-324] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [129-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-311] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-312] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-217] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-300] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [126-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [144-181] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-220] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-240] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-330] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-145] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-197] for track '15' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [129-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-125] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-164] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-239] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-359] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-359] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-229] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-346] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-359] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-358] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-359] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-310] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-347] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-296] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-351] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-357] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-339] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-355] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-359] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-348] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-357] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-353] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>