# Play-Annotation-Generator Annotation Review — OutsideZoneRead_124

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_124`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 107
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Keep` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 8 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `14` | `13` | 9 | START | 9 | 11 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 12 | START | 20 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `1` | 12 | START | 12 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `2` | 12 | START | 12 | 54 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `5` | 12 | START | 12 | 69 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 19 | END | 9 | 19 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `9` | `8` | 25 | START | 25 | 28 |
| ✅ EXACT | `Action_Keep` | QB | `9` | `8` | 29 | START | 29 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `9` | `8` | 51 | START | 51 | 148 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 69 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–168
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 9 | 19 | 11 | inferred_complete_timeline |
| `Action_None` | 20 | 24 | 5 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 25 | 28 | 4 | inferred_complete_timeline |
| `Action_Keep` | 29 | 50 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 51 | 148 | 98 | inferred_complete_timeline |
| `Action_BallCarry` | 151 | 168 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 39 | 31 | inferred_complete_timeline |
| `Action_None` | 44 | 64 | 21 | inferred_complete_timeline |
| `Action_None` | 67 | 210 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 12 | 54 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_None` | 70 | 210 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 9 | 11 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 19 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 50 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 67 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 12 | 69 | 58 | inferred_complete_timeline |
| `Action_None` | 70 | 180 | 111 | inferred_complete_timeline |
| `Action_None` | 182 | 210 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 12 | 69 | 58 | inferred_complete_timeline |
| `Action_None` | 70 | 75 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 18 | 10 | inferred_complete_timeline |
| `Action_None` | 44 | 47 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 26–210
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 26 | 51 | 26 | inferred_complete_timeline |
| `Action_None` | 53 | 177 | 125 | inferred_complete_timeline |
| `Action_None` | 186 | 210 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 95 | 87 | inferred_complete_timeline |
| `Action_None` | 102 | 210 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 60 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 64 | 56 | inferred_complete_timeline |
| `Action_None` | 68 | 210 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 71 | 63 | inferred_complete_timeline |
| `Action_None` | 75 | 86 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–203 | 158 | 5 | Undefined position; Undefined team |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–71 | 72 | 2 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–16 | 17 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 30–31 | 2 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 33–85 | 47 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 52–210 | 155 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 58–154 | 97 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 70–210 | 137 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 78–117 | 40 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 101–210 | 110 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 106–184 | 78 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 117–210 | 43 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 121–128 | 8 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 126–196 | 65 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 131–210 | 57 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 133–210 | 78 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 141–210 | 64 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 150–210 | 55 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 153–161 | 9 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 177–210 | 34 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 178–210 | 33 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 250: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [9–19], lower_priority='Action_ZoneBlock' annotated_start=12, effective_Action_ZoneBlock_start=20.
- ⚠️ Action 'Action_None' range [9-28] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-104] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [12-54] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-95] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-71] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-71] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [51-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-168] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-39] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-64] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-16] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-18] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [9-11] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-50] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-85] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-154] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-157] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-202] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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