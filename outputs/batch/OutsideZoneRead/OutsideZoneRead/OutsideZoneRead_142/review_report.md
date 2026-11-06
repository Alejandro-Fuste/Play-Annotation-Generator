# Play-Annotation-Generator Annotation Review — OutsideZoneRead_142

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_142`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Keep` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 27 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 28 | START | 28 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `9` | 31 | START | 31 | 45 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `12` | 31 | START | 41 | 118 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `2` | 31 | START | 31 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `4` | 31 | START | 31 | 115 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `7` | 31 | START | 31 | 118 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 40 | END | 28 | 40 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `9` | `8` | 52 | START | 52 | 56 |
| ✅ EXACT | `Action_Keep` | QB | `9` | `8` | 57 | START | 57 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `9` | `8` | 68 | START | 68 | 182 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 118 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–191
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 40 | 13 | inferred_complete_timeline |
| `Action_None` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 52 | 56 | 5 | inferred_complete_timeline |
| `Action_Keep` | 57 | 67 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 68 | 182 | 115 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 191 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 57 | 30 | inferred_complete_timeline |
| `Action_None` | 61 | 170 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 115 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 118 | 1 | inferred_complete_timeline |
| `Action_None` | 119 | 169 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 48 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_BallSnap` | 28 | 40 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 118 | 78 | inferred_complete_timeline |
| `Action_None` | 119 | 186 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 118 | 88 | inferred_complete_timeline |
| `Action_None` | 119 | 201 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 102 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 210 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 69 | 42 | inferred_complete_timeline |
| `Action_None` | 72 | 181 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 38 | 11 | inferred_complete_timeline |
| `Action_None` | 47 | 57 | 11 | inferred_complete_timeline |
| `Action_None` | 61 | 69 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 43 | 16 | inferred_complete_timeline |
| `Action_None` | 47 | 56 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 210 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 80 | 53 | inferred_complete_timeline |
| `Action_None` | 89 | 144 | 56 | inferred_complete_timeline |
| `Action_None` | 146 | 192 | 47 | inferred_complete_timeline |
| `Action_None` | 198 | 202 | 5 | inferred_complete_timeline |
| `Action_None` | 204 | 208 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 41–210 | 112 | 5 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 46–117 | 9 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 50–210 | 161 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 70–135 | 66 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 73–210 | 138 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 77–210 | 131 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 91–210 | 114 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 93–210 | 115 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 101–182 | 58 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 103–151 | 49 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 109–210 | 102 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 112–210 | 99 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 148–210 | 63 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 158–176 | 19 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 163–210 | 48 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 195–210 | 16 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 206–210 | 5 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 31 != Inferred start 41
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [28–40], lower_priority='Action_ZoneBlock' annotated_start=31, effective_Action_ZoneBlock_start=41.
- ⚠️ Action 'Action_None' range [28-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-57] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-170] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-102] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-144] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-192] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-115] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '4' starts at frame 119, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [119-169] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-69] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-210] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-118] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-201] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [68-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-191] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-45] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-43] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-56] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-38] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-57] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-191] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-134] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-174] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-176] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
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

</details>