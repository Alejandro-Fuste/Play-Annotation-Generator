# Play-Annotation-Generator Annotation Review — SplitZone_295

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_295`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `15` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `0` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 26 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `11` | `11` | 27 | START | 34 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | `12` | `12` | 37 | START | 37 | 47 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 38 | END | 27 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `0` | `0` | 39 | START | 39 | 54 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 39 | START | 39 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `3` | `3` | 39 | START | 39 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `6` | 39 | START | 39 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `5` | `5` | 42 | START | 42 | 53 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `8` | `8` | 42 | START | 42 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `8` | `8` | 51 | START | 51 | 53 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `0` | `0` | 55 | START | 55 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `15` | `14` | 61 | START | 61 | 118 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 38 | 12 | inferred_complete_timeline |
| `Action_None` | 39 | 41 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 42 | 50 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 55 | 61 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PressEdge` | 42 | 53 | 12 | inferred_complete_timeline |
| `Action_PressEdge` | 74 | 74 | 1 | inferred_complete_timeline |
| `Action_None` | 75 | 239 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 78 | 40 | inferred_complete_timeline |
| `Action_None` | 79 | 110 | 32 | inferred_complete_timeline |
| `Action_None` | 113 | 171 | 59 | inferred_complete_timeline |
| `Action_None` | 179 | 223 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 54 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 55 | 69 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 78 | 9 | inferred_complete_timeline |
| `Action_None` | 79 | 91 | 13 | inferred_complete_timeline |
| `Action_None` | 106 | 239 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 43 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 78 | 12 | inferred_complete_timeline |
| `Action_None` | 79 | 104 | 26 | inferred_complete_timeline |
| `Action_None` | 106 | 137 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 61 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_None` | 79 | 92 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 41 | 15 | inferred_complete_timeline |
| `Action_None` | 55 | 73 | 19 | inferred_complete_timeline |
| `Action_None` | 76 | 96 | 21 | inferred_complete_timeline |
| `Action_None` | 112 | 140 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 82 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–121 | 108 | 4 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 4–110 | 100 | 4 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 29–198 | 133 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 34–239 | 179 | 7 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 36–101 | 56 | 5 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 60–198 | 138 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 61–239 | 173 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 73–161 | 86 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 75–128 | 53 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 93–105 | 13 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 113–239 | 127 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 113–201 | 89 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 115–239 | 123 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 127–239 | 113 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 136–239 | 98 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 141–157 | 17 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 146–239 | 86 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 161–239 | 69 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 167–239 | 73 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 169–239 | 71 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 193–239 | 43 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 204–239 | 35 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 227–232 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `11` (Position_Unknown): Annotated start 27 != Inferred start 34
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 60 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [79-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-61] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-78] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-92] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [42-53] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-43] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-104] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-137] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-41] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-73] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-96] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-140] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [51-53] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [55-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-19] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-106] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-163] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [37-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [57-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-101] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-198] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [61-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-161] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-128] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-105] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-201] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-157] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>