# Play-Annotation-Generator Annotation Review — InsideZoneRead_106

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_106`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT1 | defense | `7` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 51 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 52 | START | 52 | 61 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `9` | 55 | START | 55 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `12` | 55 | START | 55 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 55 | START | 71 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 55 | START | 55 | 118 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 65 | END | 52 | 65 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `8` | 68 | START | 68 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `9` | `8` | 85 | START | 85 | 98 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 118 | BOUNDARY | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT1 | `7` | `6` | 120 | START | 120 | 124 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_SnapReceive` | 52 | 65 | 14 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 68 | 84 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 85 | 98 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 100 | 119 | 20 | inferred_complete_timeline |
| `Action_None` | 120 | 236 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 118 | 64 | inferred_complete_timeline |
| `Action_None` | 119 | 170 | 52 | inferred_complete_timeline |
| `Action_None` | 172 | 287 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 51 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 52 | 61 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 98 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 118 | 64 | inferred_complete_timeline |
| `Action_None` | 119 | 119 | 1 | inferred_complete_timeline |
| `Action_None` | 124 | 186 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 118 | 64 | inferred_complete_timeline |
| `Action_None` | 119 | 213 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 299 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 113 | 62 | inferred_complete_timeline |
| `Action_None` | 117 | 167 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 299 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 64 | 13 | inferred_complete_timeline |
| `Action_None` | 69 | 81 | 13 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 299 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 299 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 212 | 161 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–207 | 208 | 2 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–103 | 103 | 3 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 55–197 | 125 | 2 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 76–108 | 21 | 5 | Undefined position; Undefined team |
| `16` | `25` | Position_Unknown | Team_Unknown | 99–299 | 201 | 1 | Undefined position; Undefined team |
| `17` | `27` | Position_Unknown | Team_Unknown | 101–299 | 195 | 3 | Undefined position; Undefined team |
| `18` | `28` | Position_Unknown | Team_Unknown | 102–234 | 133 | 1 | Undefined position; Undefined team |
| `19` | `30` | Position_Unknown | Team_Unknown | 110–299 | 190 | 1 | Undefined position; Undefined team |
| `20` | `32` | Position_Unknown | Team_Unknown | 118–289 | 81 | 4 | Undefined position; Undefined team |
| `21` | `33` | Position_Unknown | Team_Unknown | 127–299 | 170 | 2 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 141–153 | 12 | 2 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 142–299 | 157 | 2 | Undefined position; Undefined team |
| `24` | `39` | Position_Unknown | Team_Unknown | 149–299 | 151 | 1 | Undefined position; Undefined team |
| `25` | `40` | Position_Unknown | Team_Unknown | 161–174 | 14 | 1 | Undefined position; Undefined team |
| `26` | `41` | Position_Unknown | Team_Unknown | 169–173 | 5 | 1 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 185–186 | 2 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 198–299 | 99 | 2 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 218–250 | 5 | 2 | Undefined position; Undefined team |
| `30` | `49` | Position_Unknown | Team_Unknown | 226–227 | 2 | 1 | Undefined position; Undefined team |
| `31` | `51` | Position_Unknown | Team_Unknown | 239–267 | 19 | 3 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 251–257 | 7 | 1 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 259–274 | 16 | 1 | Undefined position; Undefined team |
| `35` | `58` | Position_Unknown | Team_Unknown | 290–299 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 214: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 214: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [52–65], lower_priority='Action_ZoneBlock' annotated_start=55, effective_Action_ZoneBlock_start=66.
- ⚠️ Action 'Action_None' range [52-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-212] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-79] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-170] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-287] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-124] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [85-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-236] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 119, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [119-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-213] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [52-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-98] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-118] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-234] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-131] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-289] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-272] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-257] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-274] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>