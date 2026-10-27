# Play-Annotation-Generator Annotation Review — Counter_375

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_375`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 599
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 286
- **Validation Warnings:** 356
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 0
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 6
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 215
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `26` | `22` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `26` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `31` | `25` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `27` | `23` |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | Team_Unknown | `27` | `23` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 243 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 410 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 134 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `26` | `22` | 411 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | `26` | `22` | 414 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `31` | `25` | 414 | START | 414 | 419 |
| ❌ MISSING SEGMENT | `Action_PullBlock` | C | `15` | `14` | 414 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `5` | `4` | 414 | START | 414 | 435 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `27` | `23` | 423 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | `27` | `23` | 429 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `10` | `9` | 484 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 514 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–465
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 306 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 374 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 379 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 397 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 400 | 415 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 419 | 452 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 463 | 465 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 7 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 45 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 66 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 103 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 240 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 254 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 284 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–556
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 165 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 186 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 257 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 413 | 144 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 414 | 435 | 22 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 437 | 443 | 7 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 465 | 471 | 7 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 509 | 512 | 4 | inferred_complete_timeline |
| `Action_None` | 553 | 556 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–543
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 410 | 411 | inferred_complete_timeline |
| `Action_None` | 411 | 438 | 28 | inferred_complete_timeline |
| `Action_None` | 441 | 443 | 3 | inferred_complete_timeline |
| `Action_None` | 447 | 459 | 13 | inferred_complete_timeline |
| `Action_None` | 461 | 464 | 4 | inferred_complete_timeline |
| `Action_None` | 466 | 480 | 15 | inferred_complete_timeline |
| `Action_None` | 482 | 484 | 3 | inferred_complete_timeline |
| `Action_None` | 510 | 514 | 5 | inferred_complete_timeline |
| `Action_None` | 516 | 523 | 8 | inferred_complete_timeline |
| `Action_None` | 525 | 543 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 99 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 165 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 195 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 543

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 319 | 258 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 410 | 85 | inferred_complete_timeline |
| `Action_None` | 411 | 475 | 65 | inferred_complete_timeline |
| `Action_None` | 523 | 599 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 165 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 201 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 246 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 251 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 255 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–590
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 104 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 264 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 410 | 86 | inferred_complete_timeline |
| `Action_None` | 411 | 462 | 52 | inferred_complete_timeline |
| `Action_None` | 469 | 470 | 2 | inferred_complete_timeline |
| `Action_None` | 524 | 525 | 2 | inferred_complete_timeline |
| `Action_None` | 562 | 582 | 21 | inferred_complete_timeline |
| `Action_None` | 589 | 590 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–558
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 153 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 179 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 229 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 239 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 259 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 266 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 280 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 286 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 295 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 410 | 97 | inferred_complete_timeline |
| `Action_None` | 411 | 430 | 20 | inferred_complete_timeline |
| `Action_None` | 432 | 460 | 29 | inferred_complete_timeline |
| `Action_None` | 463 | 466 | 4 | inferred_complete_timeline |
| `Action_None` | 469 | 470 | 2 | inferred_complete_timeline |
| `Action_None` | 510 | 558 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–1
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 74 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 93 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 114 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 151 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–590
- **Visible Samples:** 522

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 165 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 410 | 187 | inferred_complete_timeline |
| `Action_None` | 411 | 505 | 95 | inferred_complete_timeline |
| `Action_None` | 508 | 511 | 4 | inferred_complete_timeline |
| `Action_None` | 516 | 521 | 6 | inferred_complete_timeline |
| `Action_None` | 526 | 571 | 46 | inferred_complete_timeline |
| `Action_None` | 573 | 590 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–482
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 15 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 30 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 113 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 138 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 194 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 354 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 358 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 410 | 51 | inferred_complete_timeline |
| `Action_None` | 411 | 464 | 54 | inferred_complete_timeline |
| `Action_None` | 468 | 473 | 6 | inferred_complete_timeline |
| `Action_None` | 479 | 482 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 2–3 | 2 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 2–462 | 437 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 5–6 | 2 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 32–83 | 42 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 43–595 | 427 | 21 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 81–116 | 32 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 109–121 | 13 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 182–265 | 32 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 195–523 | 225 | 10 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 247–432 | 65 | 9 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 254–453 | 102 | 13 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 267–270 | 4 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 282–599 | 212 | 14 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 317–476 | 47 | 12 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 327–420 | 91 | 3 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 388–414 | 26 | 3 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 406–465 | 45 | 5 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 426–430 | 5 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 443–529 | 72 | 6 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 495–593 | 71 | 6 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 505–599 | 63 | 4 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 512–599 | 84 | 3 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 512–580 | 32 | 8 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 521–551 | 21 | 4 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 546–599 | 54 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 547–598 | 23 | 6 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 554–556 | 3 | 1 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 559–599 | 35 | 5 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 562–599 | 15 | 3 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 564–599 | 11 | 2 | Undefined position; Undefined team |
| `48` | `64` | Position_Unknown | Team_Unknown | 564–599 | 28 | 3 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 575–580 | 6 | 1 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 577–578 | 2 | 1 | Undefined position; Undefined team |
| `51` | `68` | Position_Unknown | Team_Unknown | 591–599 | 9 | 1 | Undefined position; Undefined team |
| `52` | `69` | Position_Unknown | Team_Unknown | 594–599 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `26` (Position_Unknown)
- ❌ Missing segment for action `Action_DownBlock` on target `26` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `31` (6 segments found)
- ❌ Missing segment for action `Action_PullBlock` on target `15` (C)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `5` (4 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `27` (Position_Unknown)
- ❌ Missing segment for action `Action_Handoff` on target `27` (Position_Unknown)
- ❌ Missing segment for action `Action_BallCarry` on target `10` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 276 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '9' has invalid range: start=484, end=465. Clamping end to start.
- ⚠️ Segment 'Action_PullBlock' for track '14' has invalid range: start=414, end=99. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '22' has invalid range: start=411, end=116. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '22' has invalid range: start=414, end=116. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '23' has invalid range: start=411, end=121. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '23' has invalid range: start=429, end=121. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '25' (Unknown) duration 101 frames exceeds threshold 90 frames [start=414, end=514].
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-45] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-66] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-74] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-103] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-157] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-182] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-240] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-254] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-284] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-438] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-443] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-459] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-480] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-484] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-514] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-523] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-543] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-462] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-582] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-590] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-505] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-511] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-521] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-571] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-590] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-116] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-257] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [414-435] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [437-443] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [465-471] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [509-512] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-556] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-153] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-179] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-229] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-239] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-259] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-280] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-286] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-295] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-430] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-460] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-466] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-558] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-165] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-319] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-410] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-475] for track '7' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-599] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-243] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-306] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-374] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-379] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-397] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-415] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-452] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-465] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-30] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-113] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-138] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-194] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-354] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-358] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-410] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-464] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-473] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-482] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-201] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-246] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-99] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-19] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-170] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-410] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-456] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-462] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-45] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-68] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-179] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-199] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-225] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-342] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-348] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-432] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-437] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-443] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-459] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-474] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-514] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-548] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-558] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-565] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-571] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-581] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-110] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-121] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [414-419] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [422-423] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [426-428] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [431-444] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [502-504] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [509-510] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-523] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-294] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-345] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-374] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-410] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-413] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-271] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-330] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-350] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-358] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-368] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-383] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-387] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-391] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-401] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-410] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-424] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-449] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-270] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-291] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-359] for track '30' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-410] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-417] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-423] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-439] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-455] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-503] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-519] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-527] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-534] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-558] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-563] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-599] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-319] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-329] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-405] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-410] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '31' starts at frame 411, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [411-411] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-434] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-451] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-330] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-420] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-405] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-410] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-410] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-452] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-461] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-430] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-446] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-485] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-494] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-501] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-508] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-529] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-500] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-519] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-553] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-560] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-593] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-518] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-530] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-588] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-599] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-514] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-557] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-519] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-535] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-548] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-553] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-558] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-580] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-531] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-543] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-551] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-599] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-551] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-557] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-565] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-588] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-595] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-556] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-565] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-576] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-595] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-567] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-582] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-599] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-571] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-599] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-581] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-593] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-580] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-599] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-599] for track '52' has 1 frames without a visible bounding box.
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