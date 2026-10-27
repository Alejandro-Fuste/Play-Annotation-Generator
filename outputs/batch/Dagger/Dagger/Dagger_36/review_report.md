# Play-Annotation-Generator Annotation Review — Dagger_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_36`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 449
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 4
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_BreakInside` | WR1 | offense | `5` | `5` |
| ✅ EXACT | `Action_ClearToEdge` | QB | offense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `0` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 230 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `18` | `18` | 215 | START | 215 | 219 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | `17` | `17` | 218 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `11` | `11` | 219 | END | 215 | 219 |
| ✅ EXACT | `Action_BreakInside` | WR1 | `5` | `5` | 231 | START | 231 | 376 |
| ✅ EXACT | `Action_ClearToEdge` | QB | `4` | `4` | 231 | START | 231 | 323 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `11` | `11` | 313 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_ClearToEdge` | 231 | 323 | 93 | inferred_complete_timeline |
| `Action_None` | 324 | 449 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–420
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 254 | 40 | inferred_complete_timeline |
| `Action_None` | 256 | 258 | 3 | inferred_complete_timeline |
| `Action_None` | 260 | 420 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–401
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_BreakInside` | 231 | 376 | 146 | inferred_complete_timeline |
| `Action_None` | 377 | 401 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 226 | 12 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–1
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 84 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 117 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 142 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–5
- **Visible Samples:** 6

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 42 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 87 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 102 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 143 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 179 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 202 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 36 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 318 | 104 | inferred_complete_timeline |
| `Action_None` | 321 | 324 | 4 | inferred_complete_timeline |
| `Action_None` | 327 | 398 | 72 | inferred_complete_timeline |
| `Action_None` | 400 | 449 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 449 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 411 | 197 | inferred_complete_timeline |
| `Action_None` | 422 | 424 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 261 | 47 | inferred_complete_timeline |
| `Action_None` | 273 | 449 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 214 | 126 | inferred_complete_timeline |
| `Action_None` | 215 | 228 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 365 | 151 | inferred_complete_timeline |
| `Action_None` | 367 | 449 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–445
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 402 | 188 | inferred_complete_timeline |
| `Action_None` | 408 | 425 | 18 | inferred_complete_timeline |
| `Action_None` | 430 | 433 | 4 | inferred_complete_timeline |
| `Action_None` | 441 | 445 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–433 | 433 | 3 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–298 | 219 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 11–223 | 190 | 9 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 239–244 | 6 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 263–316 | 54 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 286–318 | 8 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 312–449 | 138 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 333–336 | 4 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 370–416 | 47 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 370–371 | 2 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 381–388 | 8 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 383–405 | 23 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 391–394 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_PassBlock` on target `17` (LT)
- ❌ Missing segment for action `Action_ThrowPass` on target `11` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 38: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '11' has invalid range: start=313, end=298. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '17' has invalid range: start=218, end=1. Clamping end to start.
- ⚠️ Action 'Action_None' range [215-226] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-254] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-420] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-428] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-433] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-365] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-401] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-411] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-424] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-261] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-402] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-425] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-433] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-445] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-228] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-84] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-117] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-298] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-318] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-398] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-449] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-87] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-143] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-179] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-36] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-22] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-75] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-120] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-127] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-316] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-449] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-416] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-388] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-405] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-394] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>