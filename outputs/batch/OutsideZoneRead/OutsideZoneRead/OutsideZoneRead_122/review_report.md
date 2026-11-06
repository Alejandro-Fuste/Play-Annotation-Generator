# Play-Annotation-Generator Annotation Review — OutsideZoneRead_122

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_122`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 29 | START | 29 | 44 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `11` | 31 | START | 31 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `3` | 31 | START | 31 | 50 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `8` | `7` | 31 | START | 45 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `11` | `10` | 44 | END | 29 | 40 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `11` | `10` | 48 | START | 48 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `11` | `10` | 55 | START | 67 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `11` | `10` | 71 | START | 71 | 71 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 87 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 40 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_Keep` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_Keep` | 70 | 70 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 71 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 74 | 102 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 55 | 27 | inferred_complete_timeline |
| `Action_None` | 59 | 65 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 81 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_BallSnap` | 29 | 44 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 87 | 43 | inferred_complete_timeline |
| `Action_None` | 88 | 100 | 13 | inferred_complete_timeline |
| `Action_None` | 107 | 133 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 50 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 87 | 8 | inferred_complete_timeline |
| `Action_None` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 65 | 37 | inferred_complete_timeline |
| `Action_None` | 68 | 154 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 115 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 70 | 42 | inferred_complete_timeline |
| `Action_None` | 80 | 116 | 37 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 72 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 152 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 94 | 66 | inferred_complete_timeline |
| `Action_None` | 100 | 108 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 28 | 12 | inferred_complete_timeline |
| `Action_None` | 29 | 196 | 168 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 33–104 | 59 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 41–129 | 86 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 69–118 | 23 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 79–143 | 61 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 87–104 | 18 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 87–115 | 29 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 92–207 | 108 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 95–121 | 27 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 105–123 | 19 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 110–129 | 20 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 116–210 | 89 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 121–210 | 71 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 132–175 | 43 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 141–144 | 4 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 142–143 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 157–175 | 19 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 162–168 | 7 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 179–187 | 5 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 181–210 | 30 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `8` (C): Annotated start 31 != Inferred start 45
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [29–44], lower_priority='Action_ZoneBlock' annotated_start=31, effective_Action_ZoneBlock_start=45.
- ⚠️ Action 'Action_None' range [29-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-108] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-152] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-50] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-65] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-154] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-55] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-65] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-100] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-133] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-70] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-116] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-72] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [29-40] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [48-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [67-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '10' starts at frame 71, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [71-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [74-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-81] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-123] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '32' has 1 frames without a visible bounding box.
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