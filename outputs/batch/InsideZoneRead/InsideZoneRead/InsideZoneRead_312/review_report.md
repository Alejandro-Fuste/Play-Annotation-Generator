# Play-Annotation-Generator Annotation Review — InsideZoneRead_312

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_312`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 99
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_Keep` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 3 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `16` | `15` | 1 | START | 5 | 19 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 4 | START | 4 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 4 | START | 4 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 4 | START | 4 | 27 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 4 | START | 4 | 85 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 19 | END | 1 | 19 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `11` | 22 | START | 22 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | `5` | `4` | 28 | START | 28 | 46 |
| ✅ EXACT | `Action_Keep` | QB | `12` | `11` | 31 | START | 31 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `12` | `11` | 54 | START | 54 | 206 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 85 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 19 | 19 | inferred_complete_timeline |
| `Action_None` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 22 | 30 | 9 | inferred_complete_timeline |
| `Action_Keep` | 31 | 53 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 54 | 206 | 153 | inferred_complete_timeline |
| `Action_BallCarry` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 225 | 228 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 48 | 48 | inferred_complete_timeline |
| `Action_None` | 53 | 186 | 134 | inferred_complete_timeline |
| `Action_None` | 190 | 201 | 12 | inferred_complete_timeline |
| `Action_None` | 203 | 231 | 29 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 95 | 95 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 158 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 36 | 36 | inferred_complete_timeline |
| `Action_None` | 105 | 209 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 85 | 82 | inferred_complete_timeline |
| `Action_None` | 86 | 94 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 85 | 82 | inferred_complete_timeline |
| `Action_None` | 86 | 96 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 85 | 82 | inferred_complete_timeline |
| `Action_None` | 86 | 239 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 27 | 24 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 28 | 46 | 19 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 49 | 85 | 37 | inferred_complete_timeline |
| `Action_None` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_None` | 94 | 109 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–12
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 12 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 19 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–12
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 12 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 71 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 14 | 14 | inferred_complete_timeline |
| `Action_None` | 17 | 21 | 5 | inferred_complete_timeline |
| `Action_None` | 23 | 30 | 8 | inferred_complete_timeline |
| `Action_None` | 32 | 145 | 114 | inferred_complete_timeline |
| `Action_None` | 154 | 239 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 128 | 128 | inferred_complete_timeline |
| `Action_None` | 130 | 142 | 13 | inferred_complete_timeline |
| `Action_None` | 156 | 181 | 26 | inferred_complete_timeline |
| `Action_None` | 183 | 209 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 88 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 5–38 | 34 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 11–235 | 222 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 28–105 | 60 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 39–108 | 28 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 56–108 | 44 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 67–233 | 156 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 93–239 | 147 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 103–239 | 137 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 108–239 | 132 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 120–239 | 102 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 136–239 | 88 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 168–239 | 59 | 4 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 184–190 | 7 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 208–216 | 9 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 211–221 | 11 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 212–238 | 25 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 223–239 | 17 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `16` (Position_Unknown): Annotated start 1 != Inferred start 5
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 60 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [1-36] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-209] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-94] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-209] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [28-46] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-48] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-186] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-71] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-19] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [54-206] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [214-215] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [225-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-14] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-30] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-12] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-12] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-235] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-54] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-175] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-225] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-238] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '31' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>