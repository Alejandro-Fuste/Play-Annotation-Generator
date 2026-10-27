# Play-Annotation-Generator Annotation Review — Counter_52

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_52`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `16` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | DT2 | defense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 22 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 107 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 102 | START | 102 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `12` | `11` | 108 | START | 108 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 108 | START | 118 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `16` | `14` | 108 | START | 108 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `14` | `13` | 108 | START | 108 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `9` | `8` | 108 | START | 108 | 121 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 117 | END | 102 | 117 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 128 | START | 128 | 146 |
| ✅ EXACT | `Action_BallCarry` | DT2 | `7` | `6` | 147 | START | 147 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 200 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–196
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_SnapReceive` | 102 | 117 | 16 | inferred_complete_timeline |
| `Action_None` | 118 | 125 | 8 | inferred_complete_timeline |
| `Action_None` | 127 | 127 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 128 | 146 | 19 | inferred_complete_timeline |
| `Action_None` | 147 | 159 | 13 | inferred_complete_timeline |
| `Action_None` | 161 | 196 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 108 | 121 | 14 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 188 | 200 | 13 | inferred_complete_timeline |
| `Action_None` | 201 | 269 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 22–189
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 32 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 39 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 44 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 107 | 56 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 169 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 188 | 189 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 129 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_BallSnap` | 102 | 117 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 123 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 200 | 76 | inferred_complete_timeline |
| `Action_None` | 201 | 269 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PullBlock` | 108 | 125 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 150 | 165 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 119 | 18 | inferred_complete_timeline |
| `Action_None` | 126 | 169 | 44 | inferred_complete_timeline |
| `Action_None` | 185 | 198 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 169 | 68 | inferred_complete_timeline |
| `Action_None` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 141 | 40 | inferred_complete_timeline |
| `Action_None` | 150 | 186 | 37 | inferred_complete_timeline |
| `Action_None` | 188 | 231 | 44 | inferred_complete_timeline |
| `Action_None` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 157 | 56 | inferred_complete_timeline |
| `Action_None` | 161 | 186 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_BallCarry` | 147 | 269 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 211 | 110 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 137 | 36 | inferred_complete_timeline |
| `Action_None` | 142 | 220 | 79 | inferred_complete_timeline |
| `Action_None` | 233 | 237 | 5 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 257 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 123 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_None` | 120 | 152 | 33 | inferred_complete_timeline |
| `Action_None` | 159 | 178 | 20 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 30–43 | 14 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 55–269 | 207 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 111–269 | 125 | 6 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 124–235 | 85 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 138–269 | 119 | 5 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 139–269 | 130 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 139–269 | 131 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 151–269 | 98 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 166–269 | 104 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 190–244 | 54 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 202–269 | 68 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 224–269 | 46 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 230–267 | 5 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 239–269 | 31 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 106: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 106: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (C) duration 93 frames exceeds threshold 90 frames [start=108, end=200].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [102–117], lower_priority='Action_DownBlock' annotated_start=108, effective_Action_DownBlock_start=118.
- ⚠️ Action 'Action_None' range [102-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-186] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-231] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [147-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [108-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-152] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [128-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-196] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [118-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [108-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [147-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [150-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-32] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-39] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-169] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [171-172] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [188-189] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-179] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-157] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-253] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-176] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-244] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '27' has 1 frames without a visible bounding box.
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