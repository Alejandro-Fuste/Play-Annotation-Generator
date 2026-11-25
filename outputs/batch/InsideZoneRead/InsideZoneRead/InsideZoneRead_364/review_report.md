# Play-Annotation-Generator Annotation Review — InsideZoneRead_364

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_364`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_Keep` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `7` | `6` | 10 | START | 10 | 24 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `9` | 13 | START | 13 | 83 |
| ✅ EXACT | `Action_ZoneBlock` | C | `12` | `11` | 13 | START | 13 | 83 |
| ✅ EXACT | `Action_ZoneBlock` | C | `12` | `11` | 13 | START | 13 | 83 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `15` | `14` | 13 | START | 13 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `8` | 13 | START | 13 | 69 |
| ✅ EXACT | `Action_SnapReceive` | RG | `11` | `10` | 24 | END | 10 | 24 |
| ✅ EXACT | `Action_ReadDefender` | RG | `11` | `10` | 29 | START | 29 | 37 |
| ✅ EXACT | `Action_Keep` | RG | `11` | `10` | 38 | START | 38 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | `11` | `10` | 61 | START | 61 | 75 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 83 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–106
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 93 | 84 | inferred_complete_timeline |
| `Action_None` | 99 | 106 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 71 | 62 | inferred_complete_timeline |
| `Action_None` | 74 | 76 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 69 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 130 | 41 | inferred_complete_timeline |
| `Action_None` | 136 | 139 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 83 | 71 | inferred_complete_timeline |
| `Action_None` | 84 | 210 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 83 | 71 | inferred_complete_timeline |
| `Action_None` | 84 | 210 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 24 | 15 | inferred_complete_timeline |
| `Action_None` | 25 | 28 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 29 | 37 | 9 | inferred_complete_timeline |
| `Action_Keep` | 38 | 60 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 61 | 75 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 80 | 210 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 83 | 71 | inferred_complete_timeline |
| `Action_None` | 84 | 210 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 177 | 168 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 102 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 24 | 15 | inferred_complete_timeline |
| `Action_None` | 25 | 182 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 135 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 156 | 147 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 207 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 186 | 177 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–210 | 210 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–29 | 28 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 30–32 | 3 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 70–202 | 68 | 5 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 78–210 | 121 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 96–97 | 2 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 105–210 | 106 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 122–210 | 89 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 142–210 | 69 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 142–143 | 2 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 146–210 | 51 | 4 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 151–210 | 60 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 152–210 | 54 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 156–210 | 55 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 161–210 | 50 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 179–210 | 32 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '10' has invalid range: start=13, end=9. Clamping end to start.
- ⚠️ Action 'Action_None' range [10-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-207] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-102] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-177] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-71] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-182] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-135] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [61-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [80-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-106] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-29] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '30' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_364'; source metadata written as null.

</details>