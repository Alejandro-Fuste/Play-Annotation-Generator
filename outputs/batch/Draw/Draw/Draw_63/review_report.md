# Play-Annotation-Generator Annotation Review — Draw_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_63`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 63
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 49 | START | 49 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `13` | 52 | START | 52 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `19` | 52 | START | 67 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `22` | `21` | 52 | START | 52 | 133 |
| ✅ EXACT | `Action_PassBlock` | RT | `7` | `6` | 52 | START | 52 | 210 |
| ✅ EXACT | `Action_SnapReceive` | RB | `9` | `8` | 66 | END | 49 | 66 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | RB | `9` | `8` | 70 | START | 70 | 126 |
| ✅ EXACT | `Action_BallCarry` | RB | `9` | `8` | 127 | START | 127 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 210 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 128 | 80 | inferred_complete_timeline |
| `Action_None` | 132 | 329 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 66 | 18 | inferred_complete_timeline |
| `Action_None` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 70 | 126 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 127 | 329 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 244 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 184 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 185 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 287 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 157 | 106 | inferred_complete_timeline |
| `Action_PassBlock` | 159 | 161 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_BallSnap` | 49 | 66 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 81 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 96 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 105 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 210 | 104 | inferred_complete_timeline |
| `Action_None` | 211 | 329 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 133 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 210 | 76 | inferred_complete_timeline |
| `Action_None` | 211 | 329 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 210 | 159 | inferred_complete_timeline |
| `Action_None` | 211 | 323 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 112 | 64 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 329 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 106 | 58 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 295 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 320 | 272 | inferred_complete_timeline |
| `Action_None` | 322 | 329 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 329 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 275 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 128 | 80 | inferred_complete_timeline |
| `Action_None` | 130 | 247 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 162 | 114 | inferred_complete_timeline |
| `Action_None` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 175 | 5 | inferred_complete_timeline |
| `Action_None` | 184 | 329 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 190 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 222 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 209 | 161 | inferred_complete_timeline |
| `Action_None` | 213 | 329 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 101–102 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 133–241 | 109 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 187–328 | 142 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 212–246 | 25 | 3 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 255–329 | 75 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 274–329 | 50 | 2 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 317–329 | 13 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 323–329 | 7 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 126: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [49–66], lower_priority='Action_PassBlock' annotated_start=52, effective_Action_PassBlock_start=67.
- ⚠️ Action 'Action_None' range [49-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-323] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-320] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-329] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-275] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-157] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [159-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-295] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-222] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-96] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-105] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-128] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-133] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-329] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-241] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-328] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-287] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>