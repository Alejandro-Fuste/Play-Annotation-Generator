# Play-Annotation-Generator Annotation Review — SplitZone_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_46`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 73
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
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 11 | START | 12 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 11 | START | 12 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 11 | START | 12 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 11 | START | 12 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 11 | START | 12 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 11 | START | 12 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 11 | START | 12 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 11 | START | 12 | 84 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 85 | START | 85 | 97 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `10` | 88 | START | 98 | 148 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `11` | 88 | START | 88 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `2` | 88 | START | 88 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 88 | START | 88 | 148 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `6` | 88 | START | 88 | 148 |
| ✅ EXACT | `Action_SplitBlock` | TE | `4` | `4` | 92 | START | 92 | 148 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 97 | END | 85 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `11` | `11` | 109 | START | 109 | 123 |
| ✅ EXACT | `Action_BallCarry` | QB | `7` | `7` | 125 | START | 125 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 148 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 84 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 85 | 97 | 13 | inferred_complete_timeline |
| `Action_None` | 98 | 124 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 269 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 12–171
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 84 | 73 | inferred_complete_timeline |
| `Action_None` | 85 | 122 | 38 | inferred_complete_timeline |
| `Action_None` | 126 | 159 | 34 | inferred_complete_timeline |
| `Action_None` | 168 | 171 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 91 | 80 | inferred_complete_timeline |
| `Action_SplitBlock` | 92 | 148 | 57 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–167
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 87 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 105 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 148 | 42 | inferred_complete_timeline |
| `Action_None` | 149 | 167 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 12–171
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 87 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 148 | 61 | inferred_complete_timeline |
| `Action_None` | 149 | 171 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 12–174
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 84 | 73 | inferred_complete_timeline |
| `Action_BallSnap` | 85 | 97 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 148 | 51 | inferred_complete_timeline |
| `Action_None` | 149 | 174 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 12–130
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 87 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 108 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 109 | 123 | 15 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 127 | 130 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 87 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 148 | 61 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–228
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 84 | 73 | inferred_complete_timeline |
| `Action_None` | 85 | 175 | 91 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 84 | 73 | inferred_complete_timeline |
| `Action_None` | 85 | 269 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 12–265
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 84 | 73 | inferred_complete_timeline |
| `Action_None` | 85 | 265 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 84 | 73 | inferred_complete_timeline |
| `Action_None` | 85 | 139 | 55 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 12–157
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 84 | 73 | inferred_complete_timeline |
| `Action_None` | 85 | 151 | 67 | inferred_complete_timeline |
| `Action_None` | 153 | 157 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 84 | 73 | inferred_complete_timeline |
| `Action_None` | 85 | 269 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 12–91
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 84 | 73 | inferred_complete_timeline |
| `Action_None` | 85 | 91 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 66–169 | 103 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 94–150 | 12 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 100–235 | 75 | 4 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 148–152 | 5 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 150–269 | 120 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 154–269 | 116 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 181–186 | 6 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 187–209 | 23 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 189–258 | 35 | 4 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 198–202 | 5 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 202–269 | 68 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 211–218 | 6 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 221–269 | 49 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 267–268 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 88 != Inferred start 98
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [85–97], lower_priority='Action_ZoneBlock' annotated_start=88, effective_Action_ZoneBlock_start=98.
- ⚠️ Action 'Action_None' range [85-151] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-159] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [109-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [127-130] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-265] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-169] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-209] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-244] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '31' has 1 frames without a visible bounding box.
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