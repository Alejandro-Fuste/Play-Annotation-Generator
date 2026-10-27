# Play-Annotation-Generator Annotation Review — Counter_282

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_282`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `2` | `1` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_PullBlock` | C | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 272 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 225 |
| ✅ EXACT | `Action_BallSnap` | C | `2` | `1` | 226 | START | 226 | 241 |
| ✅ EXACT | `Action_DownBlock` | RT | `11` | `10` | 229 | START | 229 | 318 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `14` | `13` | 229 | START | 229 | 283 |
| ⚠️ START CHANGED | `Action_PullBlock` | C | `2` | `1` | 229 | START | 242 | 254 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `4` | `3` | 229 | START | 229 | 266 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 241 | END | 226 | 241 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 253 | START | 253 | 272 |
| ✅ EXACT | `Action_BallCarry` | RB | `15` | `14` | 273 | START | 273 | 288 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 318 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–417
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_SnapReceive` | 226 | 241 | 16 | inferred_complete_timeline |
| `Action_None` | 242 | 252 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 253 | 272 | 20 | inferred_complete_timeline |
| `Action_None` | 273 | 410 | 138 | inferred_complete_timeline |
| `Action_None` | 412 | 417 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 272 | 273 | inferred_complete_timeline |
| `Action_BallCarry` | 273 | 288 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_DownBlock` | 229 | 283 | 55 | inferred_complete_timeline |
| `Action_DownBlock` | 286 | 318 | 33 | inferred_complete_timeline |
| `Action_None` | 319 | 449 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_BallSnap` | 226 | 241 | 16 | inferred_complete_timeline |
| `Action_PullBlock` | 242 | 254 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 261 | 36 | inferred_complete_timeline |
| `Action_None` | 274 | 449 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–443
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_DownBlock` | 229 | 318 | 90 | inferred_complete_timeline |
| `Action_None` | 319 | 443 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 275 | 50 | inferred_complete_timeline |
| `Action_None` | 277 | 449 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–426
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 225 | 68 | inferred_complete_timeline |
| `Action_None` | 226 | 426 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 229 | 4 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 283 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 276 | 51 | inferred_complete_timeline |
| `Action_None` | 283 | 449 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–420
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 225 | 131 | inferred_complete_timeline |
| `Action_None` | 226 | 300 | 75 | inferred_complete_timeline |
| `Action_None` | 312 | 420 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 449 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 279 | 54 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–277 | 277 | 3 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–449 | 450 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 3–17 | 14 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 55–81 | 27 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 247–449 | 202 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 257–449 | 193 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 265–449 | 185 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 281–436 | 140 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 286–449 | 163 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 316–317 | 2 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 345–449 | 103 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 350–449 | 100 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 351–449 | 99 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 438–449 | 12 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 447–449 | 3 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 449–449 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `2` (C): Annotated start 229 != Inferred start 242
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 565: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '1' (C): higher_priority='Action_BallSnap' [226–241], lower_priority='Action_PullBlock' annotated_start=229, effective_Action_PullBlock_start=242.
- ⚠️ Action 'Action_None' range [226-276] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [242-254] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-426] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [229-266] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [268-277] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-449] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-300] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-420] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-279] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-283] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 319, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [319-443] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-410] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-417] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-449] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [229-283] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [286-318] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-449] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [273-288] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-7] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-17] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-322] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-449] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-449] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-449] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-288] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-417] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-436] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-431] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-354] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-443] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-449] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-449] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>