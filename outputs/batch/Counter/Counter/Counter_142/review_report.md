# Play-Annotation-Generator Annotation Review — Counter_142

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_142`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `19` | `15` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `14` | `13` | 48 | START | 48 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | `14` | `13` | 50 | START | 50 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `8` | `7` | 50 | START | 50 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `2` | `1` | 50 | START | 50 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `19` | `15` | 50 | START | 50 | 68 |
| ✅ EXACT | `Action_SnapReceive` | RB | `5` | `4` | 60 | END | 48 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `4` | 82 | START | 82 | 179 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 147 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 129 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 60 | 13 | inferred_complete_timeline |
| `Action_None` | 61 | 81 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 179 | 98 | inferred_complete_timeline |
| `Action_BallCarry` | 181 | 186 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 269 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 58 | 11 | inferred_complete_timeline |
| `Action_None` | 62 | 118 | 57 | inferred_complete_timeline |
| `Action_None` | 121 | 180 | 60 | inferred_complete_timeline |
| `Action_None` | 182 | 269 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 112 | 65 | inferred_complete_timeline |
| `Action_None` | 119 | 178 | 60 | inferred_complete_timeline |
| `Action_None` | 181 | 269 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 50 | 115 | 66 | inferred_complete_timeline |
| `Action_DownBlock` | 122 | 147 | 26 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PullBlock` | 50 | 73 | 24 | inferred_complete_timeline |
| `Action_PullBlock` | 78 | 147 | 70 | inferred_complete_timeline |
| `Action_None` | 148 | 229 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 69 | 22 | inferred_complete_timeline |
| `Action_None` | 71 | 109 | 39 | inferred_complete_timeline |
| `Action_None` | 114 | 142 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 120 | 73 | inferred_complete_timeline |
| `Action_None` | 127 | 136 | 10 | inferred_complete_timeline |
| `Action_None` | 150 | 175 | 26 | inferred_complete_timeline |
| `Action_None` | 179 | 256 | 78 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 89 | 42 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 219 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 50 | 66 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 78 | 31 | inferred_complete_timeline |
| `Action_None` | 80 | 269 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 78 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 103 | 56 | inferred_complete_timeline |
| `Action_None` | 107 | 117 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 130 | 83 | inferred_complete_timeline |
| `Action_None` | 134 | 178 | 45 | inferred_complete_timeline |
| `Action_None` | 185 | 228 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `17` | Position_Unknown | Team_Unknown | 37–156 | 61 | 5 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 43–171 | 47 | 5 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 62–98 | 37 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 78–204 | 127 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 86–228 | 116 | 5 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 98–143 | 44 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 109–221 | 103 | 3 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 120–229 | 110 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 122–269 | 146 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 129–269 | 136 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 136–139 | 4 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 149–226 | 71 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 165–179 | 13 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 168–269 | 102 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 174–183 | 10 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 183–269 | 78 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 210–266 | 48 | 4 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 223–269 | 45 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 232–269 | 38 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 236–269 | 34 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 262–269 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 286: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '1' (RG) duration 98 frames exceeds threshold 90 frames [start=50, end=147].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '7' (LG) duration 98 frames exceeds threshold 90 frames [start=50, end=147].
- ⚠️ Action 'Action_None' range [48-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-178] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [50-73] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-229] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-58] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-118] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [181-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-269] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-120] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-256] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [50-115] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [122-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-142] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-89] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-219] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-78] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-103] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-228] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [50-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [71-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-47] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-87] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [50-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [71-82] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-204] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-168] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-228] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-136] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-220] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-190] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-206] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-245] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-251] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-269] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>