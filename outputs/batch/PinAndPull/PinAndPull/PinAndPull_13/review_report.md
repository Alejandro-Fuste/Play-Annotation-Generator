# Play-Annotation-Generator Annotation Review — PinAndPull_13

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `PinAndPull_13`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 174
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 3
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_DownBlock` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `23` | `22` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `29` | `24` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 21 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `23` | `Group` | 0 | START | 96 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 8 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `4` | `4` | 9 | START | 9 | 74 |
| ℹ️ GLOBAL EVENT | `Action_DownBlock` | N/A | N/A | N/A | 177 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | LT | `23` | `22` | 177 | START | 177 | 227 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `17` | `17` | 177 | START | 177 | 211 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `8` | `8` | 178 | END | 178 | 178 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `8` | `8` | 186 | START | 186 | 202 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `29` | `24` | 203 | START | 203 | 211 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 227 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 72 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 232 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 268 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 277 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 21–234
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 55 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 176 | 119 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 177 | 211 | 35 | inferred_complete_timeline |
| `Action_None` | 228 | 234 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 96–341
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 96 | 176 | 81 | inferred_complete_timeline |
| `Action_PullBlock` | 177 | 227 | 51 | inferred_complete_timeline |
| `Action_None` | 228 | 286 | 59 | inferred_complete_timeline |
| `Action_None` | 288 | 299 | 12 | inferred_complete_timeline |
| `Action_None` | 301 | 341 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 9 | 74 | 66 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 195 | 118 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 227 | 27 | inferred_complete_timeline |
| `Action_None` | 228 | 349 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 187 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 195 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 252 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–371
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 371 | 284 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–64
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 44 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 50 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 225 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 244 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 260 | 261 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 277 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 316 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 46–193
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 87 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 193 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–305
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 305 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 295 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 379 | 380 | inferred_complete_timeline |
| `Action_PreSnap` | 385 | 409 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 411 | 449 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–232 | 233 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–327 | 325 | 6 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–201 | 184 | 4 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–55 | 54 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–88 | 87 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–75 | 62 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 33–183 | 151 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 46–104 | 15 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 69–175 | 58 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 172–368 | 163 | 5 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 203–211 | 9 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 209–321 | 113 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 212–238 | 27 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 217–264 | 31 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 228–297 | 70 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 230–269 | 40 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 266–449 | 159 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 269–336 | 63 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 269–366 | 76 | 6 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 276–285 | 8 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 277–305 | 29 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 282–449 | 154 | 5 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 283–332 | 49 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 298–360 | 63 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 300–307 | 8 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 304–376 | 66 | 3 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 315–353 | 39 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 316–427 | 110 | 2 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 347–355 | 9 | 1 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 374–410 | 37 | 1 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 446–449 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 15, Column 'Ball Snap': Unknown actor track ID '[?]' in entry '167,[?]'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 107 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 28: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (LG) duration 219 frames exceeds threshold 90 frames [start=9, end=227].
- ⚠️ Action 'Action_PreSnap' range [0-379] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-409] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-295] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-305] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-252] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [9-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-349] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-371] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-298] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-327] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-201] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-232] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-268] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-277] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-260] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-277] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-316] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-88] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-225] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-244] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-62] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-44] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [177-211] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-183] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-193] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-104] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-72] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-100] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-117] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-286] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-341] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-211] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-368] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-321] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-238] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-245] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-297] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-402] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-329] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-279] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-298] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-334] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-339] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-351] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-366] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-277] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-285] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-305] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-296] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-344] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-390] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-318] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-332] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-360] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-307] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-335] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-359] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-376] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-353] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-405] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-427] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-355] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-410] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>