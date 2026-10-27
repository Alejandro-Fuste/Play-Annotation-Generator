# Play-Annotation-Generator Annotation Review — CrackToss_84

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_84`
- **Frame Range:** 0 to 374 (375 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 374
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | Team_Unknown | `21` | `19` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 240 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 243 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 240 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 240 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 240 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `13` | `12` | 241 | START | N/A | N/A |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | `17` | `16` | 244 | START | 244 | 261 |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | `21` | `19` | 244 | START | 248 | 328 |
| ✅ EXACT | `Action_PullBlock` | LT | `3` | `2` | 244 | START | 244 | 328 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 250 | END | 241 | 250 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 254 | START | 254 | 271 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 272 | START | 272 | 325 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 328 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_SnapReceive` | 241 | 250 | 10 | inferred_complete_timeline |
| `Action_None` | 251 | 253 | 3 | inferred_complete_timeline |
| `Action_Toss` | 254 | 271 | 18 | inferred_complete_timeline |
| `Action_None` | 272 | 306 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_BallCarry` | 272 | 325 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 329 | 374 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_PullBlock` | 244 | 328 | 85 | inferred_complete_timeline |
| `Action_None` | 329 | 374 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–369
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_None` | 241 | 266 | 26 | inferred_complete_timeline |
| `Action_None` | 268 | 362 | 95 | inferred_complete_timeline |
| `Action_None` | 364 | 369 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 15 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 24 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 99 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 116 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_None` | 241 | 276 | 36 | inferred_complete_timeline |
| `Action_None` | 278 | 328 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_None` | 241 | 374 | 134 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_None` | 241 | 256 | 16 | inferred_complete_timeline |
| `Action_None` | 263 | 274 | 12 | inferred_complete_timeline |
| `Action_None` | 277 | 279 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_None` | 241 | 258 | 18 | inferred_complete_timeline |
| `Action_None` | 264 | 320 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 122 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 240 | 113 | inferred_complete_timeline |
| `Action_None` | 241 | 243 | 3 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_None` | 276 | 278 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 240 | 155 | inferred_complete_timeline |
| `Action_None` | 241 | 258 | 18 | inferred_complete_timeline |
| `Action_None` | 264 | 374 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_None` | 241 | 306 | 66 | inferred_complete_timeline |
| `Action_None` | 308 | 343 | 36 | inferred_complete_timeline |
| `Action_None` | 347 | 349 | 3 | inferred_complete_timeline |
| `Action_None` | 351 | 359 | 9 | inferred_complete_timeline |
| `Action_None` | 363 | 374 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–336
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_None` | 241 | 278 | 38 | inferred_complete_timeline |
| `Action_None` | 281 | 318 | 38 | inferred_complete_timeline |
| `Action_None` | 333 | 336 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–346
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_None` | 241 | 346 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 27–34 | 8 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 33–301 | 262 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 35–261 | 227 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 41–358 | 316 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 66–374 | 309 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 248–366 | 119 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 255–374 | 120 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 259–374 | 116 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 260–283 | 24 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 264–275 | 7 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 266–332 | 67 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 293–318 | 26 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 305–374 | 70 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 310–326 | 13 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 321–322 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 324–374 | 51 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 327–374 | 48 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 343–374 | 31 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 350–351 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 353–355 | 3 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 362–374 | 13 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 369–374 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `13` (C)
- ⚠️ `Action_PullBlock` for actor_track_id `21` (Position_Unknown): Annotated start 244 != Inferred start 248
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 374 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '12' has invalid range: start=241, end=116. Clamping end to start.
- ⚠️ Action 'Action_None' range [241-278] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-318] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-362] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-369] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [244-328] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-256] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-306] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-343] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [272-325] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-276] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-328] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-240] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-306] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-346] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-122] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-258] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-320] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-99] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-111] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-374] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-34] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-286] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-301] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [244-261] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-358] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [248-328] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-366] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-374] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-374] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-283] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-332] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-318] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-372] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>