# Play-Annotation-Generator Annotation Review — SlantAndGo_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_15`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_SellRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_VerticalStem` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 1 | START | 1 | 17 |
| ✅ EXACT | `Action_PassBlock` | RT | `14` | `14` | 4 | START | 4 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 4 | START | 18 | 18 |
| ✅ EXACT | `Action_PassBlock` | LT | `17` | `17` | 4 | START | 4 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 4 | START | 4 | 26 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 17 | END | 1 | 17 |
| ✅ EXACT | `Action_SellRoute` | WR2 | `1` | `1` | 36 | START | 36 | 67 |
| ✅ EXACT | `Action_VerticalStem` | WR2 | `1` | `1` | 68 | START | 68 | 269 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 75 | START | 75 | 81 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 17 | 17 | inferred_complete_timeline |
| `Action_None` | 18 | 74 | 57 | inferred_complete_timeline |
| `Action_ThrowPass` | 75 | 81 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 127 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 154 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_SellRoute` | 36 | 67 | 32 | inferred_complete_timeline |
| `Action_VerticalStem` | 68 | 269 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 115 | 115 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_None` | 123 | 167 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 148 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 50 | 50 | inferred_complete_timeline |
| `Action_None` | 56 | 143 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 144 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 33 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 39 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 55 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 93 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 141 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 17 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 18 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 57 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 124 | 55 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 143 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 139 | 136 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 144 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 54 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 79 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 145 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 148 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 61 | 61 | inferred_complete_timeline |
| `Action_None` | 63 | 158 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 269 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 25 | 25 | inferred_complete_timeline |
| `Action_None` | 27 | 167 | 141 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–83 | 84 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–167 | 168 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–150 | 149 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 11–167 | 150 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 86–142 | 57 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 95–173 | 79 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 106–107 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 110–111 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 173–176 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (8 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 28: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [1–17], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=18.
- ⚠️ Action 'Action_None' range [1-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-115] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-144] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-50] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-83] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-127] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-25] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-167] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '15' starts at frame 18, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [18-18] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-57] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-67] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [128-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-144] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-33] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-39] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-17] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>