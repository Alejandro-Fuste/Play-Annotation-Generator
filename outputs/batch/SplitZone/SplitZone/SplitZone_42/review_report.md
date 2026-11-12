# Play-Annotation-Generator Annotation Review — SplitZone_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_42`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 59
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 12 | START | 13 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 12 | START | 13 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 12 | START | 13 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 12 | START | 13 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 12 | START | 13 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `4` | `Group` | 12 | START | 13 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 12 | START | 13 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 12 | START | 13 | 102 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 100 | START | 100 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `1` | 103 | START | 103 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `11` | 103 | START | 103 | 111 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `12` | 103 | START | 111 | 118 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 103 | START | 103 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `8` | 103 | START | 103 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `4` | `4` | 108 | START | 108 | 124 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 110 | END | 100 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `12` | `12` | 119 | START | 119 | 159 |
| ✅ EXACT | `Action_Handoff` | QB | `2` | `2` | 123 | START | 123 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `3` | 129 | START | 129 | 144 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 169 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 13–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 99 | 87 | inferred_complete_timeline |
| `Action_SnapReceive` | 100 | 110 | 11 | inferred_complete_timeline |
| `Action_None` | 111 | 122 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 123 | 128 | 6 | inferred_complete_timeline |
| `Action_None` | 129 | 269 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 13–269
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 128 | 116 | inferred_complete_timeline |
| `Action_BallCarry` | 129 | 144 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 148 | 193 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 240 | 269 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 13–269
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 107 | 95 | inferred_complete_timeline |
| `Action_SplitBlock` | 108 | 124 | 17 | inferred_complete_timeline |
| `Action_SplitBlock` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_None` | 170 | 269 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 102 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 169 | 67 | inferred_complete_timeline |
| `Action_None` | 170 | 221 | 52 | inferred_complete_timeline |
| `Action_None` | 226 | 269 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–139
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 102 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 139 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 13–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 99 | 87 | inferred_complete_timeline |
| `Action_BallSnap` | 100 | 110 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 118 | 8 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 119 | 159 | 41 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 169 | 169 | 1 | inferred_complete_timeline |
| `Action_None` | 170 | 269 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 13–151
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 102 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 111 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 151 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 13–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 102 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 169 | 67 | inferred_complete_timeline |
| `Action_None` | 170 | 269 | 100 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–204
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 99 | 87 | inferred_complete_timeline |
| `Action_None` | 100 | 204 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 13–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 99 | 87 | inferred_complete_timeline |
| `Action_None` | 100 | 215 | 116 | inferred_complete_timeline |
| `Action_None` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 13–119
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 99 | 87 | inferred_complete_timeline |
| `Action_None` | 100 | 119 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 13–269
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 99 | 87 | inferred_complete_timeline |
| `Action_None` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_None` | 108 | 114 | 7 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_None` | 124 | 171 | 48 | inferred_complete_timeline |
| `Action_None` | 193 | 250 | 58 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–245
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 99 | 87 | inferred_complete_timeline |
| `Action_None` | 100 | 245 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 13–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 99 | 87 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 13–269
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 23 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 99 | 71 | inferred_complete_timeline |
| `Action_None` | 100 | 242 | 143 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 130–163 | 34 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 141–225 | 85 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 164–269 | 58 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 165–268 | 104 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 169–213 | 44 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 170–207 | 36 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 201–212 | 12 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 218–269 | 52 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 231–269 | 39 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 233–269 | 37 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 233–269 | 37 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 256–269 | 14 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 103 != Inferred start 111
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [100–110], lower_priority='Action_ZoneBlock' annotated_start=103, effective_Action_ZoneBlock_start=111.
- ⚠️ Action 'Action_None' range [100-215] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [129-144] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [148-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [108-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-245] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-119] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [119-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-225] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-213] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-207] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-212] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-269] for track '22' has 1 frames without a visible bounding box.
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

</details>