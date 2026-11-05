# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_29`
- **Frame Range:** 0 to 779 (780 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 779
- **Player Tracks:** 73
- **Ball Tracks:** 0
- **Action Segments:** 236
- **Validation Warnings:** 311
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 219
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `35` | `30` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `35` | `30` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `77` | `60` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `10` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `11` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 297 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `15` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `2` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `3` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `5` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `9` | `Group` | 0 | START | 0 | 268 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `10` | `10` | 269 | START | 269 | 324 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 298 | END | 298 | 298 |
| ✅ EXACT | `Action_PuntBall` | Punter | `12` | `12` | 325 | START | 325 | 331 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `35` | `30` | 424 | START | 424 | 435 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `35` | `30` | 446 | START | 446 | 556 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `77` | `60` | 755 | START | 755 | 761 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 354 | 86 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–768
- **Visible Samples:** 766

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 392 | 124 | inferred_complete_timeline |
| `Action_None` | 394 | 468 | 75 | inferred_complete_timeline |
| `Action_None` | 471 | 768 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–779
- **Visible Samples:** 775

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 386 | 118 | inferred_complete_timeline |
| `Action_None` | 389 | 566 | 178 | inferred_complete_timeline |
| `Action_None` | 568 | 752 | 185 | inferred_complete_timeline |
| `Action_None` | 755 | 779 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–453
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_LongSnap` | 269 | 324 | 56 | inferred_complete_timeline |
| `Action_None` | 325 | 453 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–750
- **Visible Samples:** 729

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 344 | 76 | inferred_complete_timeline |
| `Action_None` | 347 | 463 | 117 | inferred_complete_timeline |
| `Action_None` | 466 | 634 | 169 | inferred_complete_timeline |
| `Action_None` | 636 | 662 | 27 | inferred_complete_timeline |
| `Action_None` | 666 | 673 | 8 | inferred_complete_timeline |
| `Action_None` | 675 | 690 | 16 | inferred_complete_timeline |
| `Action_None` | 692 | 699 | 8 | inferred_complete_timeline |
| `Action_None` | 704 | 708 | 5 | inferred_complete_timeline |
| `Action_None` | 717 | 750 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–779
- **Visible Samples:** 727

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 306 | 38 | inferred_complete_timeline |
| `Action_None` | 330 | 592 | 263 | inferred_complete_timeline |
| `Action_None` | 622 | 723 | 102 | inferred_complete_timeline |
| `Action_None` | 725 | 779 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–407
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 297 | 298 | inferred_complete_timeline |
| `Action_SnapReceive` | 298 | 298 | 1 | inferred_complete_timeline |
| `Action_None` | 299 | 324 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 325 | 331 | 7 | inferred_complete_timeline |
| `Action_None` | 332 | 407 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–395
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 391 | 123 | inferred_complete_timeline |
| `Action_None` | 393 | 395 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–639
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 387 | 119 | inferred_complete_timeline |
| `Action_None` | 389 | 394 | 6 | inferred_complete_timeline |
| `Action_None` | 396 | 399 | 4 | inferred_complete_timeline |
| `Action_None` | 403 | 408 | 6 | inferred_complete_timeline |
| `Action_None` | 410 | 414 | 5 | inferred_complete_timeline |
| `Action_None` | 440 | 516 | 77 | inferred_complete_timeline |
| `Action_None` | 518 | 541 | 24 | inferred_complete_timeline |
| `Action_None` | 543 | 547 | 5 | inferred_complete_timeline |
| `Action_None` | 558 | 565 | 8 | inferred_complete_timeline |
| `Action_None` | 569 | 570 | 2 | inferred_complete_timeline |
| `Action_None` | 574 | 581 | 8 | inferred_complete_timeline |
| `Action_None` | 584 | 592 | 9 | inferred_complete_timeline |
| `Action_None` | 596 | 639 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–779
- **Visible Samples:** 767

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 310 | 42 | inferred_complete_timeline |
| `Action_None` | 324 | 779 | 456 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–779
- **Visible Samples:** 744

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 417 | 149 | inferred_complete_timeline |
| `Action_None` | 419 | 420 | 2 | inferred_complete_timeline |
| `Action_None` | 425 | 459 | 35 | inferred_complete_timeline |
| `Action_None` | 463 | 467 | 5 | inferred_complete_timeline |
| `Action_None` | 469 | 473 | 5 | inferred_complete_timeline |
| `Action_None` | 477 | 658 | 182 | inferred_complete_timeline |
| `Action_None` | 665 | 666 | 2 | inferred_complete_timeline |
| `Action_None` | 682 | 749 | 68 | inferred_complete_timeline |
| `Action_None` | 753 | 779 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–591
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 591 | 323 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–679
- **Visible Samples:** 679

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 508 | 240 | inferred_complete_timeline |
| `Action_None` | 510 | 679 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–576
- **Visible Samples:** 523

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_None` | 285 | 576 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–517
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 504 | 236 | inferred_complete_timeline |
| `Action_None` | 508 | 510 | 3 | inferred_complete_timeline |
| `Action_None` | 516 | 517 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–779
- **Visible Samples:** 736

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 306 | 38 | inferred_complete_timeline |
| `Action_None` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_None` | 324 | 325 | 2 | inferred_complete_timeline |
| `Action_None` | 331 | 337 | 7 | inferred_complete_timeline |
| `Action_None` | 341 | 361 | 21 | inferred_complete_timeline |
| `Action_None` | 366 | 367 | 2 | inferred_complete_timeline |
| `Action_None` | 372 | 378 | 7 | inferred_complete_timeline |
| `Action_None` | 381 | 576 | 196 | inferred_complete_timeline |
| `Action_None` | 581 | 744 | 164 | inferred_complete_timeline |
| `Action_None` | 746 | 748 | 3 | inferred_complete_timeline |
| `Action_None` | 756 | 760 | 5 | inferred_complete_timeline |
| `Action_None` | 762 | 779 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–779
- **Visible Samples:** 780

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 779 | 511 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–395
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 385 | 117 | inferred_complete_timeline |
| `Action_None` | 392 | 395 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–754
- **Visible Samples:** 738

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_None` | 269 | 584 | 316 | inferred_complete_timeline |
| `Action_None` | 587 | 737 | 151 | inferred_complete_timeline |
| `Action_None` | 753 | 754 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–614 | 614 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 59–163 | 89 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 63–64 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 223–673 | 362 | 9 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 332–354 | 9 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 364–369 | 6 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 386–622 | 237 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 398–447 | 5 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 402–530 | 113 | 5 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 404–405 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 406–564 | 155 | 5 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 424–483 | 60 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 467–604 | 138 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 467–471 | 5 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 476–605 | 115 | 5 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 487–684 | 196 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 528–717 | 189 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 544–552 | 6 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 547–562 | 14 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 548–549 | 2 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 562–779 | 215 | 3 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 565–575 | 11 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 570–771 | 172 | 6 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 610–611 | 2 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 618–759 | 141 | 2 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 631–698 | 39 | 6 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 631–726 | 9 | 2 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 635–720 | 15 | 6 | Undefined position; Undefined team |
| `48` | `64` | Position_Unknown | Team_Unknown | 638–639 | 2 | 1 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 642–700 | 12 | 5 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 643–644 | 2 | 1 | Undefined position; Undefined team |
| `51` | `68` | Position_Unknown | Team_Unknown | 643–644 | 2 | 1 | Undefined position; Undefined team |
| `52` | `69` | Position_Unknown | Team_Unknown | 646–678 | 33 | 1 | Undefined position; Undefined team |
| `53` | `70` | Position_Unknown | Team_Unknown | 649–777 | 129 | 1 | Undefined position; Undefined team |
| `54` | `71` | Position_Unknown | Team_Unknown | 652–673 | 21 | 2 | Undefined position; Undefined team |
| `55` | `72` | Position_Unknown | Team_Unknown | 654–656 | 3 | 1 | Undefined position; Undefined team |
| `56` | `73` | Position_Unknown | Team_Unknown | 667–779 | 97 | 3 | Undefined position; Undefined team |
| `57` | `74` | Position_Unknown | Team_Unknown | 667–673 | 7 | 1 | Undefined position; Undefined team |
| `58` | `75` | Position_Unknown | Team_Unknown | 667–668 | 2 | 1 | Undefined position; Undefined team |
| `59` | `76` | Position_Unknown | Team_Unknown | 669–718 | 17 | 4 | Undefined position; Undefined team |
| `60` | `77` | Position_Unknown | Team_Unknown | 670–779 | 102 | 4 | Undefined position; Undefined team |
| `61` | `79` | Position_Unknown | Team_Unknown | 671–693 | 7 | 2 | Undefined position; Undefined team |
| `62` | `80` | Position_Unknown | Team_Unknown | 674–708 | 16 | 4 | Undefined position; Undefined team |
| `63` | `81` | Position_Unknown | Team_Unknown | 676–691 | 7 | 3 | Undefined position; Undefined team |
| `64` | `82` | Position_Unknown | Team_Unknown | 682–733 | 24 | 6 | Undefined position; Undefined team |
| `65` | `83` | Position_Unknown | Team_Unknown | 691–693 | 3 | 1 | Undefined position; Undefined team |
| `66` | `84` | Position_Unknown | Team_Unknown | 694–695 | 2 | 1 | Undefined position; Undefined team |
| `67` | `85` | Position_Unknown | Team_Unknown | 701–702 | 2 | 1 | Undefined position; Undefined team |
| `68` | `86` | Position_Unknown | Team_Unknown | 709–745 | 31 | 5 | Undefined position; Undefined team |
| `69` | `87` | Position_Unknown | Team_Unknown | 710–772 | 21 | 6 | Undefined position; Undefined team |
| `70` | `95` | Position_Unknown | Team_Unknown | 768–777 | 9 | 2 | Undefined position; Undefined team |
| `71` | `96` | Position_Unknown | Team_Unknown | 769–779 | 11 | 1 | Undefined position; Undefined team |
| `72` | `97` | Position_Unknown | Team_Unknown | 772–779 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `35` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 53 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 53 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 106 |
| Missing visible bounding boxes during action | 201 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 60: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 779 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [269-306] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-337] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-361] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-378] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-576] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-744] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [746-748] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [756-760] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-344] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-463] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-634] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-662] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-673] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-690] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-699] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [704-708] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [717-750] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-387] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-394] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-408] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-414] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-516] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-541] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-547] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-565] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-570] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-581] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-592] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-639] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-391] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-395] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-508] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-679] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-386] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-566] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-752] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-504] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-510] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-517] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-584] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-737] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [753-754] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-587] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-614] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-306] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-592] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-723] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [269-324] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-453] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-392] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-468] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-768] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-407] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-591] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-310] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-417] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-459] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-467] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-473] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-658] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [665-666] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-749] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-779] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-354] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-385] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-395] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-576] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-163] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-226] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-247] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-254] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-303] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-556] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-571] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-616] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-622] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-673] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-348] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-369] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-622] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-400] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-420] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-428] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-446] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-454] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-530] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [446-556] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [561-564] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-483] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-604] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-471] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-563] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-574] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-581] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-585] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-605] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-553] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-684] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-601] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-717] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-547] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-552] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-553] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-562] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-549] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-689] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-771] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-575] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-581] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-589] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-603] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-678] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [681-755] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [769-771] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-611] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-749] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [751-759] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-637] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [657-662] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [664-665] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-685] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-691] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-698] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-632] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [720-726] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-636] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-678] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [695-696] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-701] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [706-708] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [718-720] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-639] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-644] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-660] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [681-682] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-685] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-700] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [643-644] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [643-644] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-678] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-777] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-657] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [659-673] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-656] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-668] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-706] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-673] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-668] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-678] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-685] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-695] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [717-718] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [670-675] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [678-748] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [671-675] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-693] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-675] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-683] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [689-690] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [703-708] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-678] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-685] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-691] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-683] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-696] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-714] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [720-723] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [725-727] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [731-733] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [691-693] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [694-695] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [701-702] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-714] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [717-718] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [720-725] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [728-734] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [736-745] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [710-712] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [714-716] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [718-720] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [740-744] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [746-750] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [771-772] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [768-773] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [775-777] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>