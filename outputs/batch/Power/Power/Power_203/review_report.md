# Play-Annotation-Generator Annotation Review — Power_203

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_203`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 509
- **Player Tracks:** 65
- **Ball Tracks:** 0
- **Action Segments:** 141
- **Validation Warnings:** 207
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 118
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `22` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `1` | `Group` | 18 | START | 18 | 308 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 18 | START | 18 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 18 | START | 18 | 454 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 18 | START | 18 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 18 | START | 18 | 284 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 18 | START | 18 | 301 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 18 | START | 18 | 509 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 18 | START | 18 | 509 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 18 | START | 18 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 18 | START | 18 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 18 | START | 18 | 285 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `22` | `22` | 232 | START | 232 | 283 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `4` | `4` | 232 | START | 232 | 264 |
| ✅ EXACT | `Action_PullBlock` | LG | `15` | `15` | 232 | START | 232 | 307 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 18–301
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 301 | 284 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 18–509
- **Visible Samples:** 491

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 454 | 437 | inferred_complete_timeline |
| `Action_PreSnap` | 456 | 509 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 18–285
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 285 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 18–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 509 | 492 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 18–392
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 308 | 291 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 392 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 18–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 509 | 492 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 18–509
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 284 | 267 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 316 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 332 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 338 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 343 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 509 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 18–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 231 | 214 | inferred_complete_timeline |
| `Action_PullBlock` | 232 | 307 | 76 | inferred_complete_timeline |
| `Action_None` | 308 | 509 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 18–256
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 244 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 253 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 256 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 18–509
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 231 | 214 | inferred_complete_timeline |
| `Action_DownBlock` | 232 | 283 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 286 | 307 | 22 | inferred_complete_timeline |
| `Action_None` | 308 | 509 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 18–509
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 231 | 214 | inferred_complete_timeline |
| `Action_DownBlock` | 232 | 264 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 267 | 303 | 37 | inferred_complete_timeline |
| `Action_None` | 312 | 340 | 29 | inferred_complete_timeline |
| `Action_None` | 342 | 343 | 2 | inferred_complete_timeline |
| `Action_None` | 345 | 364 | 20 | inferred_complete_timeline |
| `Action_None` | 368 | 420 | 53 | inferred_complete_timeline |
| `Action_None` | 426 | 509 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 18–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 509 | 492 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 18–509
- **Visible Samples:** 487

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 345 | 328 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 483 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 485 | 487 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 489 | 509 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 18–265
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 255 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 265 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 18–509
- **Visible Samples:** 487

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 285 | 268 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 298 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 359 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 362 | 373 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 509 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 18–509
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 344 | 327 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 381 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 509 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 269 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 18–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 509 | 492 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 18–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 509 | 492 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 18–393
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 359 | 342 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 386 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 388 | 393 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 18–509
- **Visible Samples:** 491

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 319 | 302 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 509 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 18–380
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 380 | 363 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 18–40 | 19 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 242–509 | 220 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 252–405 | 12 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 254–509 | 248 | 5 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 258–295 | 24 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 284–317 | 15 | 4 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 294–509 | 212 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 298–509 | 211 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 299–352 | 5 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 302–509 | 203 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 374–375 | 2 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 374–479 | 22 | 6 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 379–380 | 2 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 381–509 | 128 | 2 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 386–388 | 3 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 394–395 | 2 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 394–397 | 4 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 396–406 | 8 | 2 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 399–418 | 9 | 2 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 401–402 | 2 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 407–408 | 2 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 411–412 | 2 | 1 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 416–417 | 2 | 1 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 416–417 | 2 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 421–486 | 4 | 2 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 423–425 | 3 | 1 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 424–432 | 5 | 2 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 428–432 | 5 | 1 | Undefined position; Undefined team |
| `50` | `73` | Position_Unknown | Team_Unknown | 431–436 | 4 | 2 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 433–435 | 3 | 1 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 433–435 | 3 | 1 | Undefined position; Undefined team |
| `53` | `77` | Position_Unknown | Team_Unknown | 445–446 | 2 | 1 | Undefined position; Undefined team |
| `54` | `78` | Position_Unknown | Team_Unknown | 448–450 | 3 | 1 | Undefined position; Undefined team |
| `55` | `79` | Position_Unknown | Team_Unknown | 452–454 | 3 | 1 | Undefined position; Undefined team |
| `56` | `83` | Position_Unknown | Team_Unknown | 461–503 | 19 | 6 | Undefined position; Undefined team |
| `57` | `86` | Position_Unknown | Team_Unknown | 464–467 | 4 | 1 | Undefined position; Undefined team |
| `58` | `89` | Position_Unknown | Team_Unknown | 466–467 | 2 | 1 | Undefined position; Undefined team |
| `59` | `91` | Position_Unknown | Team_Unknown | 471–472 | 2 | 1 | Undefined position; Undefined team |
| `60` | `93` | Position_Unknown | Team_Unknown | 476–509 | 26 | 2 | Undefined position; Undefined team |
| `61` | `94` | Position_Unknown | Team_Unknown | 477–509 | 32 | 2 | Undefined position; Undefined team |
| `62` | `95` | Position_Unknown | Team_Unknown | 482–483 | 2 | 1 | Undefined position; Undefined team |
| `63` | `97` | Position_Unknown | Team_Unknown | 489–509 | 13 | 2 | Undefined position; Undefined team |
| `64` | `98` | Position_Unknown | Team_Unknown | 501–508 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `SAF2` position mapped to `defense` team
- ⚠️ 43 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 43 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 86 |
| Missing visible bounding boxes during action | 120 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [18-509] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-308] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-392] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [232-264] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [267-303] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-340] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-364] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-420] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-345] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-483] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-487] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [489-509] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-386] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-393] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-285] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-285] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-298] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-359] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-373] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-255] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-265] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-344] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-381] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-509] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-244] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-253] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-256] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-319] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-509] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-454] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-284] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-316] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-332] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-338] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-343] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-301] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-29] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-380] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [232-283] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-245] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-284] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-357] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-255] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-308] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-347] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-405] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-298] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-301] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-331] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-275] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-295] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-289] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-312] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-400] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-485] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-352] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-307] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-375] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-377] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-412] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-422] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-429] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-434] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-479] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-386] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-388] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-395] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-397] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-398] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-406] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-405] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-418] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-402] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-408] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-412] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-417] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-417] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-422] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-486] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-425] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-425] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-432] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-432] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-432] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-436] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-435] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-435] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-446] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-450] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-454] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-462] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-471] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-485] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-489] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [492-493] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-503] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-467] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-467] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-472] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-493] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [502-509] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-478] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [480-509] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-483] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [489-495] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [504-509] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-505] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [507-508] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.

</details>