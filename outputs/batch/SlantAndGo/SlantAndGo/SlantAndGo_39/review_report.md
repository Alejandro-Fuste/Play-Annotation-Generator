# Play-Annotation-Generator Annotation Review — SlantAndGo_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_39`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | TE2 | offense | `17` | `17` |
| ✅ EXACT | `Action_SellRoute` | WR1 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR1 | offense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | TE2 | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_BallSnap` | QB | `16` | `16` | 26 | START | 26 | 40 |
| ✅ EXACT | `Action_PassBlock` | RT | `18` | `18` | 31 | START | 31 | 329 |
| ✅ EXACT | `Action_PassBlock` | C | `20` | `20` | 31 | START | 31 | 43 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 31 | START | 31 | 329 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `5` | `5` | 31 | START | 31 | 146 |
| ✅ EXACT | `Action_SnapReceive` | TE2 | `17` | `17` | 40 | END | 26 | 40 |
| ✅ EXACT | `Action_SellRoute` | WR1 | `1` | `1` | 46 | START | 46 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR1 | `1` | `1` | 93 | START | 93 | 125 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | TE2 | `17` | `17` | 120 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–309
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_None` | 41 | 309 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SellRoute` | 46 | 92 | 47 | inferred_complete_timeline |
| `Action_VerticalStem` | 93 | 125 | 33 | inferred_complete_timeline |
| `Action_VerticalStem` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_VerticalStem` | 141 | 146 | 6 | inferred_complete_timeline |
| `Action_VerticalStem` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_VerticalStem` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_VerticalStem` | 160 | 299 | 140 | inferred_complete_timeline |
| `Action_VerticalStem` | 301 | 308 | 8 | inferred_complete_timeline |
| `Action_VerticalStem` | 313 | 326 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 196 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_None` | 41 | 119 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 146 | 116 | inferred_complete_timeline |
| `Action_PassBlock` | 150 | 199 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 43 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 329 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 329 | 299 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 329 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 199 | 174 | inferred_complete_timeline |
| `Action_None` | 229 | 329 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 182 | 157 | inferred_complete_timeline |
| `Action_None` | 186 | 189 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 70 | 45 | inferred_complete_timeline |
| `Action_None` | 75 | 150 | 76 | inferred_complete_timeline |
| `Action_None` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_None` | 167 | 267 | 101 | inferred_complete_timeline |
| `Action_None` | 269 | 274 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 143 | 118 | inferred_complete_timeline |
| `Action_None` | 155 | 186 | 32 | inferred_complete_timeline |
| `Action_None` | 199 | 229 | 31 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 270 | 11 | inferred_complete_timeline |
| `Action_None` | 274 | 329 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 329 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 242 | 217 | inferred_complete_timeline |
| `Action_None` | 247 | 329 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 329 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 233 | 208 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–125 | 126 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 26–28 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 32–56 | 7 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 66–329 | 261 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 77–80 | 4 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 81–88 | 7 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 102–105 | 4 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 133–329 | 197 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 156–187 | 19 | 4 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 189–329 | 141 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 226–329 | 23 | 4 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 270–328 | 47 | 4 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 271–326 | 56 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 274–321 | 37 | 4 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 278–329 | 52 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 280–284 | 5 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 293–329 | 37 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 311–329 | 19 | 1 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 312–316 | 4 | 2 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 319–320 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `1` (8 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `17` (TE2)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 54: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 54: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 54: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ Row 54: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Row 54: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '17' has invalid range: start=120, end=119. Clamping end to start.
- ⚠️ Action 'Action_None' range [26-196] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [93-125] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [132-134] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [141-146] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [150-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [156-157] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [160-299] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [301-308] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [313-326] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-267] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [150-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-270] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-233] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-309] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-43] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-28] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-34] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-149] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-169] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-329] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-280] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-315] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-328] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-326] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-286] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-321] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-329] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-329] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>