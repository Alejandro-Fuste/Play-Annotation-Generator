# Play-Annotation-Generator Annotation Review — InsideZoneRead_66

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_66`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 115
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 83 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `14` | `13` | 84 | START | 89 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `0` | 87 | START | 87 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `9` | 87 | START | 87 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 87 | START | 87 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 87 | START | 87 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 94 | END | 84 | 94 |
| ✅ EXACT | `Action_ReadDefender` | QB | `7` | `6` | 98 | START | 98 | 113 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 114 | START | 114 | 121 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `4` | `3` | 122 | START | 124 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 159 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_SnapReceive` | 84 | 94 | 11 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 98 | 113 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 114 | 121 | 8 | inferred_complete_timeline |
| `Action_None` | 122 | 250 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_BallCarry` | 124 | 359 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 159 | 73 | inferred_complete_timeline |
| `Action_None` | 160 | 359 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 159 | 73 | inferred_complete_timeline |
| `Action_None` | 160 | 164 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 132 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 159 | 9 | inferred_complete_timeline |
| `Action_None` | 160 | 238 | 79 | inferred_complete_timeline |
| `Action_None` | 240 | 262 | 23 | inferred_complete_timeline |
| `Action_None` | 266 | 287 | 22 | inferred_complete_timeline |
| `Action_None` | 311 | 359 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 150 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 203 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 359 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 115 | 32 | inferred_complete_timeline |
| `Action_None` | 117 | 148 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 129 | 46 | inferred_complete_timeline |
| `Action_None` | 133 | 359 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 141 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 4–358 | 343 | 6 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 12–359 | 282 | 7 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 89–359 | 259 | 5 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 116–146 | 25 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 129–359 | 215 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 139–359 | 221 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 140–145 | 4 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 146–169 | 24 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 147–185 | 37 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 156–359 | 191 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 187–359 | 173 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 200–359 | 159 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 205–359 | 151 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 214–359 | 112 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 216–359 | 137 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 220–357 | 129 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 220–359 | 140 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 227–293 | 65 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 239–359 | 117 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 322–359 | 38 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 327–335 | 6 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 337–359 | 23 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `14` (Position_Unknown): Annotated start 84 != Inferred start 89
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `4` (RB): Annotated start 122 != Inferred start 124

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 70 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [84-203] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-359] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [152-153] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-250] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-262] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-287] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 84, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [84-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-215] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-342] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-358] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-238] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-359] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-169] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-322] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-343] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-264] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-267] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-277] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-324] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-291] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-359] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-260] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-349] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-357] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-289] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-327] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-359] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>