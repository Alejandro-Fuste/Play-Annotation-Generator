# Play-Annotation-Generator Annotation Review — Counter_171

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_171`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | DE2 | defense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE2 | defense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 3 | START | 3 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 3 | START | 3 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 3 | START | 3 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 3 | START | 3 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 3 | START | 3 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 3 | START | 3 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 3 | START | 3 | 110 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `20` | `19` | 111 | START | 111 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `20` | `19` | 117 | START | 117 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `21` | `20` | 117 | START | 117 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `22` | `21` | 117 | START | 117 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `19` | `18` | 117 | START | 117 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `4` | `3` | 117 | START | 117 | 155 |
| ✅ EXACT | `Action_PlaySideFakeStep` | DE2 | `5` | `4` | 127 | START | 127 | 152 |
| ✅ EXACT | `Action_SnapReceive` | C | `11` | `10` | 128 | END | 111 | 128 |
| ✅ EXACT | `Action_Handoff` | C | `11` | `10` | 142 | START | 142 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE2 | `5` | `4` | 153 | START | 153 | 181 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 205 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_None` | 111 | 269 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 116 | 114 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 117 | 155 | 39 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 157 | 205 | 49 | inferred_complete_timeline |
| `Action_None` | 206 | 213 | 8 | inferred_complete_timeline |
| `Action_None` | 218 | 269 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_None` | 111 | 184 | 74 | inferred_complete_timeline |
| `Action_None` | 190 | 269 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_None` | 111 | 269 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 3–232
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_SnapReceive` | 111 | 128 | 18 | inferred_complete_timeline |
| `Action_None` | 129 | 135 | 7 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 142 | 152 | 11 | inferred_complete_timeline |
| `Action_None` | 153 | 213 | 61 | inferred_complete_timeline |
| `Action_None` | 217 | 232 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 3–163
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_None` | 111 | 163 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_None` | 111 | 269 | 159 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_None` | 111 | 250 | 140 | inferred_complete_timeline |
| `Action_None` | 252 | 269 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–264
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 126 | 124 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 127 | 152 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 153 | 181 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 264 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_None` | 111 | 269 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_None` | 111 | 238 | 128 | inferred_complete_timeline |
| `Action_None` | 240 | 269 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_None` | 111 | 175 | 65 | inferred_complete_timeline |
| `Action_None` | 177 | 269 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_None` | 111 | 269 | 159 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 3–269 | 264 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 3–269 | 267 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 3–269 | 247 | 7 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 3–269 | 267 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 3–181 | 176 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 3–163 | 160 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 3–269 | 259 | 7 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 3–269 | 264 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 3–158 | 141 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 127–152 | 17 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 154–269 | 116 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 168–171 | 4 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 174–269 | 85 | 2 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 177–269 | 92 | 2 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 187–269 | 83 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 194–198 | 5 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 197–199 | 3 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 220–248 | 7 | 3 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 265–269 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 50 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [111-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [117-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [157-205] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [153-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [183-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-264] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-269] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-238] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-135] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-213] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-232] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-157] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-172] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-200] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [117-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [127-163] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-144] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [147-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [163-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-145] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [149-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-127] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [130-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [145-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-217] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>