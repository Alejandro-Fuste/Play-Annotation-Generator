# Play-Annotation-Generator Annotation Review — Counter_288

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_288`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `15` | `14` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 109 |
| ✅ EXACT | `Action_BallSnap` | C | `3` | `2` | 107 | START | 107 | 121 |
| ✅ EXACT | `Action_DownBlock` | LT | `10` | `9` | 110 | START | 110 | 200 |
| ✅ EXACT | `Action_DownBlock` | LG | `13` | `12` | 110 | START | 110 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `3` | `2` | 110 | START | 122 | 145 |
| ✅ EXACT | `Action_PullBlock` | RG | `15` | `14` | 110 | START | 110 | 200 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `7` | `6` | 110 | START | 110 | 200 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 121 | END | 107 | 121 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 137 | START | 137 | 151 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `11` | `10` | 152 | START | 211 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 200 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_SnapReceive` | 107 | 121 | 15 | inferred_complete_timeline |
| `Action_None` | 122 | 136 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 137 | 151 | 15 | inferred_complete_timeline |
| `Action_None` | 152 | 181 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_BallCarry` | 211 | 329 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 329 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 200 | 91 | inferred_complete_timeline |
| `Action_None` | 201 | 211 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 200 | 91 | inferred_complete_timeline |
| `Action_None` | 201 | 260 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_BallSnap` | 107 | 121 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 122 | 145 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 149 | 200 | 52 | inferred_complete_timeline |
| `Action_None` | 201 | 255 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PullBlock` | 110 | 200 | 91 | inferred_complete_timeline |
| `Action_None` | 201 | 266 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 110 | 200 | 91 | inferred_complete_timeline |
| `Action_None` | 201 | 280 | 80 | inferred_complete_timeline |
| `Action_None` | 283 | 299 | 17 | inferred_complete_timeline |
| `Action_None` | 301 | 311 | 11 | inferred_complete_timeline |
| `Action_None` | 317 | 325 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 329 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 329 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 143 | 37 | inferred_complete_timeline |
| `Action_None` | 145 | 222 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 128 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 176 | 70 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 228 | 122 | inferred_complete_timeline |
| `Action_None` | 236 | 257 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 225 | 119 | inferred_complete_timeline |
| `Action_None` | 227 | 240 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 77 | 27 | inferred_complete_timeline |
| `Action_None` | 115 | 139 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 158 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 140–236 | 80 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 152–329 | 165 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 185–230 | 38 | 5 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 195–329 | 134 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 199–329 | 131 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 212–327 | 102 | 2 | Undefined position; Undefined team |
| `23` | `36` | Position_Unknown | Team_Unknown | 236–329 | 87 | 2 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 249–269 | 21 | 1 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `26` | `41` | Position_Unknown | Team_Unknown | 291–329 | 36 | 3 | Undefined position; Undefined team |
| `27` | `43` | Position_Unknown | Team_Unknown | 311–329 | 12 | 2 | Undefined position; Undefined team |
| `28` | `44` | Position_Unknown | Team_Unknown | 312–313 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `11` (RB): Annotated start 152 != Inferred start 211

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '2' (C) duration 91 frames exceeds threshold 90 frames [start=110, end=200].
- ⚠️ Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [107–121], lower_priority='Action_DownBlock' annotated_start=110, effective_Action_DownBlock_start=122.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (LT) duration 91 frames exceeds threshold 90 frames [start=110, end=200].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (LG) duration 91 frames exceeds threshold 90 frames [start=110, end=200].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '14' (RG) duration 91 frames exceeds threshold 90 frames [start=110, end=200].
- ⚠️ Action 'Action_None' range [107-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-329] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [122-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-255] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-228] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-257] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [110-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-280] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-311] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-325] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-225] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-240] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-211] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-176] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-181] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-77] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-185] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-294] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-203] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-214] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-292] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-327] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-307] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-269] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-303] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-319] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '28' has 1 frames without a visible bounding box.
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