# Play-Annotation-Generator Annotation Review — DeepCross_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_61`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Completion`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `27` | `24` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `20` | `20` | 19 | START | 19 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `13` | 22 | START | 22 | 58 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `20` | `20` | 22 | START | 37 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `3` | `3` | 22 | START | 22 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR3 | `1` | `1` | 36 | START | 36 | 103 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 36 | END | 19 | 36 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `27` | `24` | 136 | START | 136 | 140 |

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
- **Visible Frames:** 0–132
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 36 | 18 | inferred_complete_timeline |
| `Action_None` | 37 | 83 | 47 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_None` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 103 | 113 | 11 | inferred_complete_timeline |
| `Action_None` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_None` | 129 | 132 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 150 | 132 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 163 | 8 | inferred_complete_timeline |
| `Action_None` | 167 | 208 | 42 | inferred_complete_timeline |
| `Action_None` | 214 | 225 | 12 | inferred_complete_timeline |
| `Action_None` | 227 | 255 | 29 | inferred_complete_timeline |
| `Action_None` | 259 | 269 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 228 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 263 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 36 | 103 | 68 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 110 | 188 | 79 | inferred_complete_timeline |
| `Action_None` | 189 | 236 | 48 | inferred_complete_timeline |
| `Action_None` | 238 | 243 | 6 | inferred_complete_timeline |
| `Action_None` | 257 | 269 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 85 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 50 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 57 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 98 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 132 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 139 | 157 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 25 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 36 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 47 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 58 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 88 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 114 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 126 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 46 | 28 | inferred_complete_timeline |
| `Action_None` | 62 | 98 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 60 | 42 | inferred_complete_timeline |
| `Action_None` | 62 | 83 | 22 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 120 | 102 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 204 | 186 | inferred_complete_timeline |
| `Action_None` | 210 | 269 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 57 | 39 | inferred_complete_timeline |
| `Action_None` | 61 | 86 | 26 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 95 | 135 | 41 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 172 | 154 | inferred_complete_timeline |
| `Action_None` | 178 | 183 | 6 | inferred_complete_timeline |
| `Action_None` | 185 | 191 | 7 | inferred_complete_timeline |
| `Action_None` | 199 | 269 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 48 | 30 | inferred_complete_timeline |
| `Action_None` | 51 | 57 | 7 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_None` | 68 | 75 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–269 | 268 | 3 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–237 | 238 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–152 | 147 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–116 | 117 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 20–125 | 91 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 45–71 | 16 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 69–121 | 37 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 108–198 | 81 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 159–177 | 14 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 162–222 | 48 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 189–192 | 4 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 195–199 | 5 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 200–205 | 6 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 200–255 | 53 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 201–269 | 69 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (4 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `20` (C): Annotated start 22 != Inferred start 37
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (7 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 64: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 64: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [19–36], lower_priority='Action_PassBlock' annotated_start=22, effective_Action_PassBlock_start=37.
- ⚠️ Action 'Action_None' range [19-85] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [36-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [106-107] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [110-188] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-236] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-243] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-173] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-269] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-50] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-57] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-98] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-132] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [134-137] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [139-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-208] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-255] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-237] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-228] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-263] for track '10' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-172] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-135] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-88] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [108-114] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-75] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-269] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-60] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [19-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-52] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-114] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-59] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-77] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-112] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [136-140] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-198] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-222] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-205] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-255] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>