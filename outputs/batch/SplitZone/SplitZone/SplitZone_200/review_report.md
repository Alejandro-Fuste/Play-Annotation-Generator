# Play-Annotation-Generator Annotation Review — SplitZone_200

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_200`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 30
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 10 | START | 11 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 10 | START | 11 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 10 | START | 11 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 10 | START | 11 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 10 | START | 11 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `5` | `Group` | 10 | START | 11 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 10 | START | 11 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 10 | START | 11 | 47 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 45 | START | 45 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `10` | 48 | START | 48 | 67 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `11` | `11` | 48 | START | 57 | 135 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 48 | START | 48 | 135 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `7` | 48 | START | 48 | 135 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 48 | START | 48 | 135 |
| ✅ EXACT | `Action_SplitBlock` | HB | `5` | `5` | 55 | START | 55 | 135 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `4` | 56 | END | 45 | 56 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `4` | 64 | START | 64 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `2` | 82 | START | 82 | 87 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 135 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 11–170
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 56 | 12 | inferred_complete_timeline |
| `Action_None` | 57 | 63 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 64 | 81 | 18 | inferred_complete_timeline |
| `Action_None` | 82 | 170 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 81 | 71 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 359 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 11–164
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 54 | 44 | inferred_complete_timeline |
| `Action_SplitBlock` | 55 | 135 | 81 | inferred_complete_timeline |
| `Action_None` | 138 | 164 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 11–153
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 47 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 135 | 88 | inferred_complete_timeline |
| `Action_None` | 136 | 146 | 11 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 11–172
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 47 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 67 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 135 | 67 | inferred_complete_timeline |
| `Action_None` | 136 | 172 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 11–179
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_BallSnap` | 45 | 56 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 135 | 79 | inferred_complete_timeline |
| `Action_None` | 136 | 179 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 11–170
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 47 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 135 | 88 | inferred_complete_timeline |
| `Action_None` | 136 | 170 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 11–176
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 47 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 135 | 88 | inferred_complete_timeline |
| `Action_None` | 136 | 176 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 11–165
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_None` | 45 | 165 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 11–167
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_None` | 45 | 138 | 94 | inferred_complete_timeline |
| `Action_None` | 148 | 167 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 11–69
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_None` | 45 | 61 | 17 | inferred_complete_timeline |
| `Action_None` | 67 | 69 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 11–62
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_None` | 45 | 62 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 11–195
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_None` | 45 | 100 | 56 | inferred_complete_timeline |
| `Action_None` | 107 | 195 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 11–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_None` | 45 | 180 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 11–168
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_None` | 45 | 168 | 124 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 40–320 | 276 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 41–75 | 35 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 45–106 | 61 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 91–121 | 30 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 100–126 | 19 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 122–359 | 238 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 133–150 | 12 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 142–184 | 43 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 273–359 | 87 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 279–359 | 73 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 320–359 | 39 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 323–327 | 5 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 328–359 | 24 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 356–359 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `11` (C): Annotated start 48 != Inferred start 57
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [45–56], lower_priority='Action_ZoneBlock' annotated_start=48, effective_Action_ZoneBlock_start=57.
- ⚠️ Action 'Action_None' range [45-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-195] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-87] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-170] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [55-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-164] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-170] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-135] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-146] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-165] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-67] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-167] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-258] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-320] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-75] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-75] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-121] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-350] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-351] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-327] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-346] for track '28' has 1 frames without a visible bounding box.
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

</details>