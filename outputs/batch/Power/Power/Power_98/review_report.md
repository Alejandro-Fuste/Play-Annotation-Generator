# Play-Annotation-Generator Annotation Review — Power_98

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_98`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 569
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 164
- **Validation Warnings:** 232
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 142
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_DownBlock` | DT1 | defense | `15` | `15` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 29 | START | 29 | 386 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 29 | START | 29 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 29 | START | 29 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 29 | START | 29 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 29 | START | 29 | 304 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 29 | START | 29 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `1` | `1` | 246 | START | 246 | 257 |
| ⚠️ START CHANGED | `Action_DownBlock` | DT1 | `15` | `15` | 246 | START | 252 | 281 |
| ✅ EXACT | `Action_PullBlock` | LG | `9` | `9` | 246 | START | 246 | 286 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 29–569
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 236 | 208 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 324 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 439 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 450 | 472 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 487 | 549 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 555 | 560 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 569 | 569 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 29–412
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 238 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 249 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 350 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 352 | 396 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 411 | 412 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 29–417
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 304 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 320 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 329 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 337 | 417 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 29–386
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 386 | 358 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 29–542
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 245 | 217 | inferred_complete_timeline |
| `Action_PullBlock` | 246 | 286 | 41 | inferred_complete_timeline |
| `Action_None` | 287 | 292 | 6 | inferred_complete_timeline |
| `Action_None` | 294 | 369 | 76 | inferred_complete_timeline |
| `Action_None` | 378 | 458 | 81 | inferred_complete_timeline |
| `Action_None` | 467 | 486 | 20 | inferred_complete_timeline |
| `Action_None` | 490 | 531 | 42 | inferred_complete_timeline |
| `Action_None` | 534 | 542 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 29–282
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 245 | 217 | inferred_complete_timeline |
| `Action_DownBlock` | 246 | 257 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 270 | 282 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 29–337
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 95 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 135 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 337 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 29–256
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 56 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 76 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 162 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 198 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 207 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 227 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 238 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 256 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 34–414
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 79 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 234 | 130 | inferred_complete_timeline |
| `Action_DownBlock` | 252 | 281 | 30 | inferred_complete_timeline |
| `Action_None` | 288 | 290 | 3 | inferred_complete_timeline |
| `Action_None` | 296 | 312 | 17 | inferred_complete_timeline |
| `Action_None` | 323 | 373 | 51 | inferred_complete_timeline |
| `Action_None` | 393 | 414 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 29–486
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 238 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 374 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 439 | 486 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 29–320
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 244 | 216 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 320 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 29–240
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 240 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 29–272
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 263 | 235 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 272 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 29–86
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 86 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 29–444
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 304 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 321 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 381 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 444 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 29–47 | 19 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 245–569 | 259 | 6 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 258–269 | 8 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 261–274 | 11 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 262–384 | 41 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 262–292 | 31 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 264–420 | 141 | 6 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 288–569 | 191 | 9 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 289–378 | 36 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 297–469 | 131 | 7 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 303–376 | 59 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 303–569 | 247 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 309–383 | 55 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 313–326 | 9 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 315–337 | 23 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 320–326 | 7 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 342–346 | 5 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 348–569 | 221 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 353–456 | 65 | 4 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 353–420 | 44 | 6 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 357–370 | 14 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 367–373 | 6 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 375–376 | 2 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 375–376 | 2 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 379–420 | 37 | 2 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 379–424 | 27 | 5 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 379–392 | 7 | 3 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 390–543 | 154 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 392–484 | 22 | 4 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 394–426 | 33 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 413–434 | 22 | 1 | Undefined position; Undefined team |
| `46` | `56` | Position_Unknown | Team_Unknown | 428–569 | 142 | 1 | Undefined position; Undefined team |
| `47` | `57` | Position_Unknown | Team_Unknown | 440–467 | 17 | 2 | Undefined position; Undefined team |
| `48` | `58` | Position_Unknown | Team_Unknown | 455–569 | 103 | 3 | Undefined position; Undefined team |
| `49` | `60` | Position_Unknown | Team_Unknown | 463–509 | 46 | 2 | Undefined position; Undefined team |
| `50` | `61` | Position_Unknown | Team_Unknown | 472–473 | 2 | 1 | Undefined position; Undefined team |
| `51` | `62` | Position_Unknown | Team_Unknown | 478–522 | 43 | 2 | Undefined position; Undefined team |
| `52` | `63` | Position_Unknown | Team_Unknown | 562–569 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `15` (DT1): Annotated start 246 != Inferred start 252

### Track Identity Issues

- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 154 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 198: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [29-386] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [246-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [270-282] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-86] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-304] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-320] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-417] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-304] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-321] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-381] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-444] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-135] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-337] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-263] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-272] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-374] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-486] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-244] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-320] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-369] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-458] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-486] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-531] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-542] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-249] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-350] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-396] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-412] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-236] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-324] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-439] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-472] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-549] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [555-560] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-47] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-130] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-162] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-167] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-198] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-207] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-227] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-238] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-256] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-79] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-234] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [252-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-312] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-373] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-414] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-254] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-300] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-355] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-392] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-413] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-260] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-264] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-274] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-292] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-304] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-384] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-292] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-279] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-321] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-337] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-352] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-362] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-420] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-378] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-419] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-430] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-452] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-457] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-485] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [531-533] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [543-544] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-292] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-378] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-367] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-370] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-374] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-386] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-397] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-429] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-469] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-343] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-362] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-376] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-331] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-400] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-383] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-321] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-326] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-337] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-326] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-346] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-355] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-373] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-384] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-407] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-456] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-366] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-373] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-381] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-391] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-409] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-420] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-370] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-370] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-373] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-386] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-420] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-383] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-392] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-399] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-403] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-424] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-381] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-384] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-392] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-543] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-399] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-403] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-410] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-484] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-426] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-434] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-452] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-467] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-479] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-499] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [507-569] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-469] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-509] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-473] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-490] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [493-522] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.

</details>