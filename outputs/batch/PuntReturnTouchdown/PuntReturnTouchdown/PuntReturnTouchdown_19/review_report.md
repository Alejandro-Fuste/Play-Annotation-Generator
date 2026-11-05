# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_19`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 163
- **Validation Warnings:** 152
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 145
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `26` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `26` | `23` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `26` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `1` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `10` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `11` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `16` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `17` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `19` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `8` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 133 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `19` | `19` | 134 | START | 134 | 190 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Punter | `12` | `12` | 162 | END | N/A | N/A |
| ✅ EXACT | `Action_PuntBall` | Punter | `12` | `12` | 191 | START | 191 | 204 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `26` | `23` | 317 | START | 317 | 322 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `26` | `23` | 323 | START | 323 | 638 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `26` | `23` | 639 | START | 639 | 645 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–423
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 264 | 131 | inferred_complete_timeline |
| `Action_None` | 270 | 275 | 6 | inferred_complete_timeline |
| `Action_None` | 279 | 423 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 292 | 159 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |
| `Action_None` | 311 | 315 | 5 | inferred_complete_timeline |
| `Action_None` | 317 | 339 | 23 | inferred_complete_timeline |
| `Action_None` | 343 | 344 | 2 | inferred_complete_timeline |
| `Action_None` | 350 | 598 | 249 | inferred_complete_timeline |
| `Action_None` | 605 | 607 | 3 | inferred_complete_timeline |
| `Action_None` | 609 | 659 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 255 | 122 | inferred_complete_timeline |
| `Action_None` | 264 | 341 | 78 | inferred_complete_timeline |
| `Action_None` | 350 | 418 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 658

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_LongSnap` | 134 | 190 | 57 | inferred_complete_timeline |
| `Action_None` | 191 | 306 | 116 | inferred_complete_timeline |
| `Action_None` | 308 | 333 | 26 | inferred_complete_timeline |
| `Action_None` | 335 | 659 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–472
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 330 | 197 | inferred_complete_timeline |
| `Action_None` | 333 | 433 | 101 | inferred_complete_timeline |
| `Action_None` | 443 | 472 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 654

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 414 | 281 | inferred_complete_timeline |
| `Action_None` | 419 | 422 | 4 | inferred_complete_timeline |
| `Action_None` | 424 | 633 | 210 | inferred_complete_timeline |
| `Action_None` | 635 | 659 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 656

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 429 | 296 | inferred_complete_timeline |
| `Action_None` | 432 | 437 | 6 | inferred_complete_timeline |
| `Action_None` | 440 | 659 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 159 | 4 | inferred_complete_timeline |
| `Action_None` | 166 | 190 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 191 | 204 | 14 | inferred_complete_timeline |
| `Action_None` | 205 | 221 | 17 | inferred_complete_timeline |
| `Action_None` | 225 | 229 | 5 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 251 | 9 | inferred_complete_timeline |
| `Action_None` | 253 | 307 | 55 | inferred_complete_timeline |
| `Action_None` | 310 | 339 | 30 | inferred_complete_timeline |
| `Action_None` | 341 | 623 | 283 | inferred_complete_timeline |
| `Action_None` | 626 | 631 | 6 | inferred_complete_timeline |
| `Action_None` | 634 | 640 | 7 | inferred_complete_timeline |
| `Action_None` | 647 | 659 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 205 | 72 | inferred_complete_timeline |
| `Action_None` | 207 | 249 | 43 | inferred_complete_timeline |
| `Action_None` | 253 | 264 | 12 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 291 | 4 | inferred_complete_timeline |
| `Action_None` | 312 | 313 | 2 | inferred_complete_timeline |
| `Action_None` | 324 | 326 | 3 | inferred_complete_timeline |
| `Action_None` | 328 | 331 | 4 | inferred_complete_timeline |
| `Action_None` | 335 | 341 | 7 | inferred_complete_timeline |
| `Action_None` | 345 | 394 | 50 | inferred_complete_timeline |
| `Action_None` | 397 | 399 | 3 | inferred_complete_timeline |
| `Action_None` | 403 | 659 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 659 | 526 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 277 | 144 | inferred_complete_timeline |
| `Action_None` | 279 | 659 | 381 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 631

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 80 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 133 | 51 | inferred_complete_timeline |
| `Action_None` | 134 | 433 | 300 | inferred_complete_timeline |
| `Action_None` | 435 | 659 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 639

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 229 | 96 | inferred_complete_timeline |
| `Action_None` | 235 | 286 | 52 | inferred_complete_timeline |
| `Action_None` | 288 | 333 | 46 | inferred_complete_timeline |
| `Action_None` | 335 | 341 | 7 | inferred_complete_timeline |
| `Action_None` | 356 | 659 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–582
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 479 | 346 | inferred_complete_timeline |
| `Action_None` | 481 | 484 | 4 | inferred_complete_timeline |
| `Action_None` | 486 | 563 | 78 | inferred_complete_timeline |
| `Action_None` | 576 | 582 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 653

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 627 | 494 | inferred_complete_timeline |
| `Action_None` | 633 | 641 | 9 | inferred_complete_timeline |
| `Action_None` | 644 | 659 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 655

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 331 | 198 | inferred_complete_timeline |
| `Action_None` | 333 | 413 | 81 | inferred_complete_timeline |
| `Action_None` | 416 | 426 | 11 | inferred_complete_timeline |
| `Action_None` | 429 | 659 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 650

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 64 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 133 | 67 | inferred_complete_timeline |
| `Action_None` | 134 | 207 | 74 | inferred_complete_timeline |
| `Action_None` | 209 | 328 | 120 | inferred_complete_timeline |
| `Action_None` | 331 | 334 | 4 | inferred_complete_timeline |
| `Action_None` | 336 | 615 | 280 | inferred_complete_timeline |
| `Action_None` | 618 | 659 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 642

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 293 | 160 | inferred_complete_timeline |
| `Action_None` | 298 | 301 | 4 | inferred_complete_timeline |
| `Action_None` | 311 | 315 | 5 | inferred_complete_timeline |
| `Action_None` | 318 | 320 | 3 | inferred_complete_timeline |
| `Action_None` | 323 | 457 | 135 | inferred_complete_timeline |
| `Action_None` | 459 | 659 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–458
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 323 | 190 | inferred_complete_timeline |
| `Action_None` | 325 | 381 | 57 | inferred_complete_timeline |
| `Action_None` | 390 | 393 | 4 | inferred_complete_timeline |
| `Action_None` | 457 | 458 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 66 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 133 | 65 | inferred_complete_timeline |
| `Action_None` | 134 | 282 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 635

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 339 | 206 | inferred_complete_timeline |
| `Action_None` | 341 | 347 | 7 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_None` | 362 | 367 | 6 | inferred_complete_timeline |
| `Action_None` | 370 | 371 | 2 | inferred_complete_timeline |
| `Action_None` | 373 | 374 | 2 | inferred_complete_timeline |
| `Action_None` | 380 | 623 | 244 | inferred_complete_timeline |
| `Action_None` | 628 | 659 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 205–208 | 4 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 291–659 | 369 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 299–659 | 337 | 6 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 415–659 | 241 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 427–659 | 232 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 432–659 | 228 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 487–489 | 3 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 495–659 | 161 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 540–620 | 42 | 6 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 547–549 | 3 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 581–659 | 76 | 2 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 608–651 | 17 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SnapReceive` on target `12` (Punter)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `26` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 123 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [134-339] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-347] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-367] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-623] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-659] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-323] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-381] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-393] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-627] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-641] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-330] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-433] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-472] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-66] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-282] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-479] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-484] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-563] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-582] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-293] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-315] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-457] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-659] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-292] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-315] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-339] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-598] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-607] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-277] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-429] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-437] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-659] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-255] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-341] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-418] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-221] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-251] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-307] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-339] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-623] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-631] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-640] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-64] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-207] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-328] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-615] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-433] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-659] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-264] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-423] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-205] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-264] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-341] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-394] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-414] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-422] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-633] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-286] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-333] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-341] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [134-190] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-306] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-333] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-659] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-331] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-413] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-426] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-435] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-479] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-626] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-445] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-659] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-580] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-659] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-489] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-627] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-641] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-551] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-574] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-598] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-615] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-620] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-549] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-607] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-659] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-609] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-615] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-635] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-651] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>