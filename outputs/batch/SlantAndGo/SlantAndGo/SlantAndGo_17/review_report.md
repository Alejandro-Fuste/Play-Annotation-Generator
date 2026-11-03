# Play-Annotation-Generator Annotation Review — SlantAndGo_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_17`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_SellRoute` | Position_Unknown | Team_Unknown | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | Position_Unknown | Team_Unknown | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | LG | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 13 | START | 13 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `10` | `10` | 17 | START | 54 | 82 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LG | `16` | `16` | 17 | START | N/A | N/A |
| ✅ EXACT | `Action_PassBlock` | LT | `18` | `18` | 17 | START | 17 | 135 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 17 | START | 17 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 17 | START | 17 | 83 |
| ✅ EXACT | `Action_SnapReceive` | LG | `16` | `16` | 26 | END | 13 | 26 |
| ✅ EXACT | `Action_SellRoute` | Position_Unknown | `1` | `1` | 57 | START | 57 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | Position_Unknown | `1` | `1` | 88 | START | 88 | 173 |
| ✅ EXACT | `Action_ThrowPass` | LG | `16` | `16` | 96 | START | 96 | 103 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 94 | 82 | inferred_complete_timeline |
| `Action_None` | 97 | 103 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 149 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 50 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 67 | 55 | inferred_complete_timeline |
| `Action_None` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_None` | 81 | 170 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 135 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 13 | 26 | 14 | inferred_complete_timeline |
| `Action_None` | 27 | 62 | 36 | inferred_complete_timeline |
| `Action_None` | 64 | 95 | 32 | inferred_complete_timeline |
| `Action_ThrowPass` | 96 | 103 | 8 | inferred_complete_timeline |
| `Action_None` | 104 | 139 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 13 | 26 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 82 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 149 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 106 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 83 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 119 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 121 | 135 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 73 | 61 | inferred_complete_timeline |
| `Action_None` | 78 | 83 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 75 | 63 | inferred_complete_timeline |
| `Action_None` | 78 | 139 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 95 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 174 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 109 | 97 | inferred_complete_timeline |
| `Action_None` | 112 | 170 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 166 | 154 | inferred_complete_timeline |
| `Action_None` | 169 | 193 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 210 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 123 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 178 | 166 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–190 | 188 | 5 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–185 | 186 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 63–163 | 101 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 91–122 | 32 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 101–154 | 54 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 101–117 | 13 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `16` (LG)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 29: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ Row 30: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ Row 30: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [13–26], lower_priority='Action_PassBlock' annotated_start=17, effective_Action_PassBlock_start=27.
- ⚠️ Segment 'Action_PassBlock' for track '16' has invalid range: start=17, end=12. Clamping end to start.
- ⚠️ Action 'Action_None' range [13-109] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-170] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [88-173] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [175-176] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [179-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-73] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-83] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-75] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-193] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-67] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-170] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-50] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [13-26] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-149] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-178] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-62] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-135] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-106] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-83] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [121-135] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-163] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-122] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-109] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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