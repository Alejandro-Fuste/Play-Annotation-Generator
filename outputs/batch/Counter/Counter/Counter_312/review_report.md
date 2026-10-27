# Play-Annotation-Generator Annotation Review — Counter_312

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_312`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `6` | `5` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `2` | `1` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `3` | `2` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 235 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `6` | `5` | 228 | START | 228 | 230 |
| ✅ EXACT | `Action_DownBlock` | LG | `13` | `12` | 231 | START | 231 | 339 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `20` | `18` | 231 | START | 231 | 339 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `6` | `5` | 231 | START | 231 | 242 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `2` | `1` | 231 | START | 231 | 305 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `3` | `2` | 231 | START | 231 | 339 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `7` | `6` | 236 | START | 236 | 276 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 240 | END | 228 | 240 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 255 | START | 255 | 276 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 277 | START | 277 | 382 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 339 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–344
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 227 | 138 | inferred_complete_timeline |
| `Action_SnapReceive` | 228 | 240 | 13 | inferred_complete_timeline |
| `Action_None` | 241 | 254 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 255 | 276 | 22 | inferred_complete_timeline |
| `Action_None` | 277 | 344 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–398
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 236 | 276 | 41 | inferred_complete_timeline |
| `Action_BallCarry` | 277 | 382 | 106 | inferred_complete_timeline |
| `Action_BallCarry` | 388 | 390 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 395 | 398 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_None` | 228 | 326 | 99 | inferred_complete_timeline |
| `Action_None` | 332 | 419 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 231 | 339 | 109 | inferred_complete_timeline |
| `Action_None` | 340 | 419 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 33 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_DownBlock` | 231 | 339 | 109 | inferred_complete_timeline |
| `Action_None` | 340 | 419 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_PullBlock` | 231 | 305 | 75 | inferred_complete_timeline |
| `Action_PullBlock` | 307 | 339 | 33 | inferred_complete_timeline |
| `Action_None` | 340 | 419 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_None` | 228 | 255 | 28 | inferred_complete_timeline |
| `Action_None` | 279 | 286 | 8 | inferred_complete_timeline |
| `Action_None` | 289 | 292 | 4 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |
| `Action_None` | 307 | 374 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 98 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 227 | 114 | inferred_complete_timeline |
| `Action_None` | 228 | 300 | 73 | inferred_complete_timeline |
| `Action_None` | 304 | 307 | 4 | inferred_complete_timeline |
| `Action_None` | 311 | 313 | 3 | inferred_complete_timeline |
| `Action_None` | 318 | 321 | 4 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_None` | 334 | 419 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_None` | 228 | 294 | 67 | inferred_complete_timeline |
| `Action_None` | 299 | 419 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_None` | 228 | 320 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_None` | 228 | 260 | 33 | inferred_complete_timeline |
| `Action_None` | 262 | 323 | 62 | inferred_complete_timeline |
| `Action_None` | 325 | 332 | 8 | inferred_complete_timeline |
| `Action_None` | 334 | 419 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_None` | 228 | 337 | 110 | inferred_complete_timeline |
| `Action_None` | 339 | 355 | 17 | inferred_complete_timeline |
| `Action_None` | 357 | 419 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_None` | 228 | 258 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_None` | 228 | 419 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_None` | 228 | 245 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–298 | 254 | 8 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–403 | 403 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 11–419 | 409 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 237–245 | 5 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 255–290 | 36 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 263–419 | 155 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 270–419 | 149 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 272–277 | 6 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 278–299 | 21 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 295–373 | 79 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 300–419 | 104 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 318–419 | 102 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 340–419 | 80 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 382–383 | 2 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 397–419 | 23 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 401–419 | 19 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 402–419 | 18 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 415–419 | 5 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 417–419 | 3 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 418–419 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 626: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '1' (RG) duration 109 frames exceeds threshold 90 frames [start=231, end=339].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (LG) duration 109 frames exceeds threshold 90 frames [start=231, end=339].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (Unknown) duration 109 frames exceeds threshold 90 frames [start=231, end=339].
- ⚠️ Action 'Action_None' range [228-258] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [231-305] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [231-339] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-326] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-419] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-419] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-63] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-90] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [231-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [247-262] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [297-298] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [277-382] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [388-390] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [395-398] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-245] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-400] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-344] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-337] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-355] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-419] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-255] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-286] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-374] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-419] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-260] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-323] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-332] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-320] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-98] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-300] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-307] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-230] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-419] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-386] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-419] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-414] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-419] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-285] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-373] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-318] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-419] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>