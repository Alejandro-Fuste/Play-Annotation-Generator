# Play-Annotation-Generator Annotation Review — Power_97

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_97`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 160
- **Validation Warnings:** 202
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 128
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 9 | START | 9 | 438 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 9 | START | 9 | 289 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 9 | START | 9 | 539 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 9 | START | 9 | 391 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 9 | START | 9 | 523 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 9 | START | 9 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 9 | START | 9 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 9 | START | 13 | 264 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 9 | START | 9 | 331 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 9 | START | 9 | 284 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 9 | START | 9 | 217 |
| ✅ EXACT | `Action_DownBlock` | RT | `16` | `16` | 218 | START | 218 | 240 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `20` | `20` | 218 | START | 218 | 242 |
| ✅ EXACT | `Action_PullBlock` | LG | `8` | `8` | 218 | START | 218 | 271 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 9–539
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 539 | 531 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 9–308
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 289 | 281 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 308 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–523
- **Visible Samples:** 515

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 523 | 515 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 9–284
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 284 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 9–438
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 438 | 430 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 9–539
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 331 | 323 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 492 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 498 | 539 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 9–539
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 391 | 383 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 431 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 464 | 467 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 471 | 482 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 484 | 533 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 535 | 539 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–493
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 217 | 209 | inferred_complete_timeline |
| `Action_PullBlock` | 218 | 271 | 54 | inferred_complete_timeline |
| `Action_None` | 272 | 282 | 11 | inferred_complete_timeline |
| `Action_None` | 289 | 317 | 29 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |
| `Action_None` | 336 | 385 | 50 | inferred_complete_timeline |
| `Action_None` | 388 | 428 | 41 | inferred_complete_timeline |
| `Action_None` | 465 | 493 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 13–445
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 264 | 252 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 278 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 358 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 385 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 388 | 391 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 395 | 402 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 404 | 406 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 410 | 414 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 420 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 433 | 438 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 443 | 445 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 9–327
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 217 | 209 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 242 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 244 | 271 | 28 | inferred_complete_timeline |
| `Action_None` | 272 | 308 | 37 | inferred_complete_timeline |
| `Action_None` | 311 | 318 | 8 | inferred_complete_timeline |
| `Action_None` | 324 | 327 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 9–240
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 217 | 209 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 240 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 9–286
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 286 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 9–456
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 445 | 437 | inferred_complete_timeline |
| `Action_PreSnap` | 455 | 456 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–236
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 236 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–384
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 259 | 251 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 337 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 350 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 357 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 384 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 9–411
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 277 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 363 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 366 | 372 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 387 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 391 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 411 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 9–244
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 244 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–266
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 266 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–411
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 401 | 393 | inferred_complete_timeline |
| `Action_PreSnap` | 404 | 411 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–409
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 341 | 333 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 351 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 365 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 390 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 398 | 409 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 9–334
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 334 | 326 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 9–415
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 320 | 312 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 351 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 415 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 238–241 | 4 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 248–249 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 252–313 | 62 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 266–510 | 74 | 14 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 272–458 | 187 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 273–464 | 173 | 6 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 273–464 | 192 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 274–395 | 102 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 281–443 | 127 | 5 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 300–539 | 208 | 9 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 302–539 | 208 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 302–539 | 204 | 7 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 317–519 | 124 | 5 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 343–539 | 131 | 5 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 368–539 | 120 | 7 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 378–462 | 82 | 3 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 384–539 | 150 | 2 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 403–409 | 7 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 440–441 | 2 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 445–539 | 73 | 6 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 447–451 | 4 | 2 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 454–459 | 6 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 456–457 | 2 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 465–466 | 2 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 477–480 | 4 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 487–494 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 149 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [9-438] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-289] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-308] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-445] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-456] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-341] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-351] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-365] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-390] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-409] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-320] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-351] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-415] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-331] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-492] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [498-539] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-284] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-282] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-317] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-385] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-428] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-493] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-337] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-350] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-357] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-384] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-391] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-431] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-467] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-482] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [484-533] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-523] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-401] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-411] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-277] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-363] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-372] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-387] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-391] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-411] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-240] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-286] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-334] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-244] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-242] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-308] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-318] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-264] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-278] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-358] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-385] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-391] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-402] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-406] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-414] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-420] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-438] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-445] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-313] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-273] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-306] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-347] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-353] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-357] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-369] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-377] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-423] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-439] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-473] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-489] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [502-505] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [508-510] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-458] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-274] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-352] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-357] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-361] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-464] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-464] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-331] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-343] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-395] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-320] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-379] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-383] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-403] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-443] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-339] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-344] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-387] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-419] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-430] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-449] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-507] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [513-517] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-381] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-393] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-539] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-325] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-349] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-421] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-429] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-471] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-539] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-409] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-451] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-491] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-519] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-344] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-473] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [496-499] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [516-536] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-407] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-486] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [489-493] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [498-500] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [502-512] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-519] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-393] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-428] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-462] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-510] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-409] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-441] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-448] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-462] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-484] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [499-519] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [521-533] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [538-539] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-448] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-451] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-459] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [456-457] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-466] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-480] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-488] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [493-494] for track '47' has 1 frames without a visible bounding box.
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

</details>