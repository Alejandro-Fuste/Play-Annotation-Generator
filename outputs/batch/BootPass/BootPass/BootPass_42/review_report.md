# Play-Annotation-Generator Annotation Review — BootPass_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_42`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `1` | `1` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `31` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 55 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `11` | `11` | 56 | START | 56 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `1` | `1` | 62 | START | 62 | 133 |
| ✅ EXACT | `Action_RunBlock` | RG | `10` | `10` | 62 | START | 62 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `13` | `13` | 62 | START | 62 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `4` | `4` | 62 | START | 62 | 206 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 70 | END | 56 | 70 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `5` | `5` | 73 | START | 73 | 94 |
| ✅ EXACT | `Action_BootAway` | QB | `5` | `5` | 96 | START | 96 | 126 |
| ✅ EXACT | `Action_ThrowPass` | QB | `5` | `5` | 167 | START | 167 | 174 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `31` | `22` | 234 | START | 234 | 239 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_SnapReceive` | 56 | 70 | 15 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_FakeHandoff` | 73 | 94 | 22 | inferred_complete_timeline |
| `Action_None` | 95 | 95 | 1 | inferred_complete_timeline |
| `Action_BootAway` | 96 | 126 | 31 | inferred_complete_timeline |
| `Action_None` | 127 | 166 | 40 | inferred_complete_timeline |
| `Action_ThrowPass` | 167 | 174 | 8 | inferred_complete_timeline |
| `Action_None` | 175 | 239 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 88 | 33 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 182 | 90 | inferred_complete_timeline |
| `Action_None` | 187 | 235 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 85 | 30 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_RunBlock` | 62 | 74 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 94 | 97 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_RunBlock` | 62 | 206 | 145 | inferred_complete_timeline |
| `Action_RunBlock` | 215 | 239 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_RunBlock` | 62 | 82 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_RunBlock` | 62 | 133 | 72 | inferred_complete_timeline |
| `Action_RunBlock` | 137 | 239 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 136 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 239 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 116 | 61 | inferred_complete_timeline |
| `Action_None` | 118 | 176 | 59 | inferred_complete_timeline |
| `Action_None` | 185 | 236 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 162 | 107 | inferred_complete_timeline |
| `Action_None` | 164 | 239 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 239 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 239 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 239 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 239 | 184 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–145 | 139 | 6 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 77–239 | 158 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 102–108 | 4 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 108–239 | 132 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 114–231 | 116 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 121–181 | 59 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 129–239 | 111 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 138–239 | 102 | 2 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 141–149 | 9 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 142–153 | 12 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 147–239 | 93 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 151–189 | 39 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 159–239 | 80 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 168–170 | 3 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 186–239 | 52 | 3 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 188–239 | 47 | 2 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 63: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [56-239] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [62-133] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [137-239] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-136] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [62-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-116] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-176] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-236] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [62-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [62-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [78-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [94-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-231] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-170] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-181] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-149] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-174] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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