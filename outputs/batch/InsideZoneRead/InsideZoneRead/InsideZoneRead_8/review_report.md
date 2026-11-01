# Play-Annotation-Generator Annotation Review — InsideZoneRead_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_8`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 63
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 42
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 2 | START | 2 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 2 | START | 2 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 2 | START | 2 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 2 | START | 2 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 2 | START | 2 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 2 | START | 2 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 2 | START | 2 | 88 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 85 | START | 85 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 89 | START | 97 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 89 | START | 89 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `3` | 89 | START | 89 | 167 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `4` | 89 | START | 89 | 158 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `6` | 89 | START | 89 | 167 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 96 | END | 85 | 96 |
| ✅ EXACT | `Action_ReadDefender` | QB | `10` | `9` | 103 | START | 103 | 109 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 110 | START | 110 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 128 | START | 128 | 185 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 167 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 2–183
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 84 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 85 | 96 | 12 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 103 | 109 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 110 | 127 | 18 | inferred_complete_timeline |
| `Action_None` | 128 | 183 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 119 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 127 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 185 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 346 | 159 | inferred_complete_timeline |
| `Action_BallCarry` | 348 | 359 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 2–222
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 88 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 167 | 79 | inferred_complete_timeline |
| `Action_None` | 168 | 222 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 2–311
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 88 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 167 | 79 | inferred_complete_timeline |
| `Action_None` | 168 | 311 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–317
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 84 | 83 | inferred_complete_timeline |
| `Action_BallSnap` | 85 | 96 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 133 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 143 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 167 | 6 | inferred_complete_timeline |
| `Action_None` | 168 | 317 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 2–158
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 88 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 158 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 2–314
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 88 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 167 | 79 | inferred_complete_timeline |
| `Action_None` | 168 | 314 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–183
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 84 | 83 | inferred_complete_timeline |
| `Action_None` | 85 | 183 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 2–331
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 84 | 83 | inferred_complete_timeline |
| `Action_None` | 85 | 331 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 84 | 83 | inferred_complete_timeline |
| `Action_None` | 85 | 153 | 69 | inferred_complete_timeline |
| `Action_None` | 162 | 326 | 165 | inferred_complete_timeline |
| `Action_None` | 359 | 359 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 84 | 83 | inferred_complete_timeline |
| `Action_None` | 85 | 100 | 16 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_None` | 142 | 359 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 2–111
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 84 | 83 | inferred_complete_timeline |
| `Action_None` | 85 | 111 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 2–257
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 84 | 83 | inferred_complete_timeline |
| `Action_None` | 85 | 203 | 119 | inferred_complete_timeline |
| `Action_None` | 251 | 257 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 84 | 83 | inferred_complete_timeline |
| `Action_None` | 85 | 185 | 101 | inferred_complete_timeline |
| `Action_None` | 188 | 359 | 172 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 134–332 | 193 | 4 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 159–359 | 201 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 162–359 | 195 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 181–273 | 82 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 190–293 | 104 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 209–359 | 151 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 215–292 | 78 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 220–301 | 82 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 357–359 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 34 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [85–96], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=97.
- ⚠️ Action 'Action_None' range [85-203] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-257] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-314] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-111] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-158] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-185] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-346] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-311] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-331] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-183] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-317] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-153] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-326] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-153] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-332] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-273] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-293] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-292] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-301] for track '21' has 1 frames without a visible bounding box.
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

</details>