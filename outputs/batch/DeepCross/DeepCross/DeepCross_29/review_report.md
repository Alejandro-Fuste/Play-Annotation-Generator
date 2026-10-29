# Play-Annotation-Generator Annotation Review — DeepCross_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_29`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 64
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 2 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 3 | START | 3 | 12 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 6 | START | 6 | 20 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `19` | `19` | 6 | START | 17 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 6 | START | 6 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 6 | START | 6 | 51 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | `2` | `2` | 15 | START | 15 | 183 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 15 | END | 3 | 15 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 97 | START | 97 | 106 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `2` | `2` | 186 | START | 186 | 299 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 15 | 13 | inferred_complete_timeline |
| `Action_None` | 16 | 96 | 81 | inferred_complete_timeline |
| `Action_ThrowPass` | 97 | 106 | 10 | inferred_complete_timeline |
| `Action_None` | 107 | 114 | 8 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 116 | 114 | inferred_complete_timeline |
| `Action_None` | 119 | 122 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 137 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 15 | 183 | 169 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 186 | 299 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 177 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 114 | 112 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 20 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 91 | 65 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 113 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 39 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 60 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 84 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 114 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 12 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 114 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 51 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 128 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 122 | 120 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 44 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 41 | 39 | inferred_complete_timeline |
| `Action_None` | 43 | 116 | 74 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 49 | 47 | inferred_complete_timeline |
| `Action_None` | 55 | 90 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 29 | 27 | inferred_complete_timeline |
| `Action_None` | 37 | 39 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 193 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 83 | 81 | inferred_complete_timeline |
| `Action_None` | 85 | 224 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 226 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 260 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 299 | 297 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 234 | 232 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–126 | 125 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 43–123 | 78 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 47–48 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 80–130 | 51 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 176–238 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (5 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `19` (C): Annotated start 6 != Inferred start 17
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 32: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [3–15], lower_priority='Action_PassBlock' annotated_start=6, effective_Action_PassBlock_start=16.
- ⚠️ Action 'Action_None' range [3-137] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [186-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-260] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-114] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-49] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-116] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-116] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-122] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-193] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-41] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-116] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-114] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-226] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-20] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-91] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-100] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-39] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [3-12] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-114] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-39] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [125-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>