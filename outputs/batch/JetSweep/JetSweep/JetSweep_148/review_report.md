# Play-Annotation-Generator Annotation Review — JetSweep_148

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_148`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 124
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 79 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `16` | `15` | 60 | START | 60 | 102 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 80 | START | 80 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `0` | 82 | START | 82 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `12` | 82 | START | 91 | 181 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `13` | 82 | START | 82 | 182 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `1` | 82 | START | 82 | 168 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `2` | 82 | START | 82 | 175 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 90 | END | 80 | 90 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 95 | START | 95 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `16` | `15` | 104 | START | 106 | 110 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 182 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_SnapReceive` | 80 | 90 | 11 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_Toss` | 95 | 103 | 9 | inferred_complete_timeline |
| `Action_None` | 104 | 190 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 155 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 182 | 101 | inferred_complete_timeline |
| `Action_None` | 183 | 227 | 45 | inferred_complete_timeline |
| `Action_None` | 230 | 235 | 6 | inferred_complete_timeline |
| `Action_None` | 237 | 253 | 17 | inferred_complete_timeline |
| `Action_None` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 79 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 80 | 90 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 181 | 91 | inferred_complete_timeline |
| `Action_None` | 183 | 207 | 25 | inferred_complete_timeline |
| `Action_None` | 212 | 231 | 20 | inferred_complete_timeline |
| `Action_None` | 240 | 250 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 175 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 168 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 121 | 42 | inferred_complete_timeline |
| `Action_None` | 123 | 210 | 88 | inferred_complete_timeline |
| `Action_None` | 212 | 251 | 40 | inferred_complete_timeline |
| `Action_None` | 255 | 266 | 12 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 98 | 19 | inferred_complete_timeline |
| `Action_None` | 104 | 121 | 18 | inferred_complete_timeline |
| `Action_None` | 123 | 164 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 38 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 57 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 79 | 21 | inferred_complete_timeline |
| `Action_None` | 80 | 99 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 100 | 21 | inferred_complete_timeline |
| `Action_None` | 105 | 113 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 210 | 131 | inferred_complete_timeline |
| `Action_None` | 212 | 229 | 18 | inferred_complete_timeline |
| `Action_None` | 236 | 250 | 15 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 269 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 145 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 94 | 15 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 183 | 80 | inferred_complete_timeline |
| `Action_None` | 185 | 249 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–248 | 220 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 60–250 | 185 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 80–269 | 190 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 133–269 | 127 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 134–182 | 49 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 136–263 | 112 | 4 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 137–171 | 35 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 147–182 | 34 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 154–160 | 7 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 160–165 | 6 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 165–247 | 83 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 165–238 | 11 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 165–268 | 87 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 169–185 | 5 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 169–260 | 79 | 4 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 172–250 | 77 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 177–178 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 187–269 | 73 | 5 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 218–240 | 22 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RG) duration 94 frames exceeds threshold 90 frames [start=82, end=175].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 101 frames exceeds threshold 90 frames [start=82, end=182].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [80–90], lower_priority='Action_ZoneBlock' annotated_start=82, effective_Action_ZoneBlock_start=91.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LG) duration 101 frames exceeds threshold 90 frames [start=82, end=182].
- ⚠️ Action 'Action_ZoneBlock' range [82-155] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-168] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-173] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-248] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-210] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-229] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-251] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-266] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-183] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-249] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-38] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-181] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-231] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-250] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-182] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-227] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-253] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [60-102] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [180-243] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [245-250] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-256] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-182] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-204] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-263] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-171] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-178] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-247] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-250] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-248] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-231] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-243] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-248] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-261] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-240] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>