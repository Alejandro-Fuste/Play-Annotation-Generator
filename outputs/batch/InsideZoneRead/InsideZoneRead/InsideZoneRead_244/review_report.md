# Play-Annotation-Generator Annotation Review — InsideZoneRead_244

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_244`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT2 | defense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Keep` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | DT2 | `16` | `15` | 7 | START | 7 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `16` | 10 | START | 10 | 45 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 10 | START | 10 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `4` | 10 | START | 10 | 36 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `7` | 10 | START | 10 | 82 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 18 | END | 7 | 18 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `11` | 23 | START | 23 | 42 |
| ✅ EXACT | `Action_Keep` | QB | `12` | `11` | 43 | START | 43 | 51 |
| ✅ EXACT | `Action_BallCarry` | QB | `12` | `11` | 52 | START | 52 | 113 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 86 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 18 | 12 | inferred_complete_timeline |
| `Action_None` | 19 | 22 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 23 | 42 | 20 | inferred_complete_timeline |
| `Action_Keep` | 43 | 51 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 52 | 113 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 68 | 62 | inferred_complete_timeline |
| `Action_None` | 75 | 193 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 127 | 121 | inferred_complete_timeline |
| `Action_None` | 129 | 149 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 86 | 77 | inferred_complete_timeline |
| `Action_None` | 87 | 94 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 36 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 55 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 86 | 16 | inferred_complete_timeline |
| `Action_None` | 87 | 94 | 8 | inferred_complete_timeline |
| `Action_None` | 100 | 136 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 45 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 86 | 40 | inferred_complete_timeline |
| `Action_None` | 87 | 136 | 50 | inferred_complete_timeline |
| `Action_None` | 138 | 210 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 82 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 79 | 73 | inferred_complete_timeline |
| `Action_None` | 103 | 138 | 36 | inferred_complete_timeline |
| `Action_None` | 141 | 175 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 65 | 59 | inferred_complete_timeline |
| `Action_None` | 79 | 103 | 25 | inferred_complete_timeline |
| `Action_None` | 116 | 128 | 13 | inferred_complete_timeline |
| `Action_None` | 134 | 189 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 7 | 18 | 12 | inferred_complete_timeline |
| `Action_None` | 19 | 29 | 11 | inferred_complete_timeline |
| `Action_None` | 68 | 73 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 45 | 39 | inferred_complete_timeline |
| `Action_None` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_None` | 61 | 65 | 5 | inferred_complete_timeline |
| `Action_None` | 68 | 71 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 29 | 23 | inferred_complete_timeline |
| `Action_None` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_None` | 40 | 69 | 30 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 114 | 13 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 45 | 39 | inferred_complete_timeline |
| `Action_None` | 48 | 139 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 140 | 134 | inferred_complete_timeline |
| `Action_None` | 145 | 179 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 84 | 78 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 104 | 15 | inferred_complete_timeline |
| `Action_None` | 129 | 210 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–184 | 181 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 54–140 | 80 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 59–62 | 4 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 81–129 | 25 | 2 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 85–105 | 13 | 3 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 85–166 | 82 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 111–153 | 43 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 115–124 | 10 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 123–168 | 42 | 2 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 131–210 | 36 | 3 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 141–210 | 70 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 158–204 | 45 | 2 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 167–172 | 6 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 187–210 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 488: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [7-137] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-94] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [10-36] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-55] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [10-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-140] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-179] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-193] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-128] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-189] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [52-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-139] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-69] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-114] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-29] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [10-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-136] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-92] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-166] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-168] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-179] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_244'; source metadata written as null.

</details>