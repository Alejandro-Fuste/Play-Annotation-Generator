# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_41

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_41`
- **Frame Range:** 0 to 779 (780 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 779
- **Player Tracks:** 97
- **Ball Tracks:** 0
- **Action Segments:** 288
- **Validation Warnings:** 416
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 272
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `51` | `33` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `51` | `33` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `11` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `14` | `Group` | 0 | START | 0 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `15` | `Group` | 0 | START | 0 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `17` | `Group` | 0 | START | 0 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `19` | `Group` | 0 | START | 0 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `20` | `Group` | 0 | START | 0 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `5` | `Group` | 0 | START | 0 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `7` | `Group` | 0 | START | 0 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `9` | `Group` | 0 | START | 0 | 197 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `12` | `12` | 198 | START | 198 | 217 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `11` | `11` | 229 | END | 229 | 229 |
| ✅ EXACT | `Action_PuntBall` | Punter | `11` | `11` | 253 | START | 253 | 263 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `51` | `33` | 387 | START | 387 | 394 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `51` | `33` | 395 | START | 395 | 439 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 234 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 221 | 24 | inferred_complete_timeline |
| `Action_None` | 223 | 288 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 275 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–543
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 322 | 125 | inferred_complete_timeline |
| `Action_None` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_None` | 365 | 543 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_LongSnap` | 198 | 217 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 262 | 65 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_None` | 276 | 289 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 291 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 285 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_SnapReceive` | 229 | 229 | 1 | inferred_complete_timeline |
| `Action_None` | 230 | 252 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 253 | 263 | 11 | inferred_complete_timeline |
| `Action_None` | 264 | 285 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 292 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 230 | 33 | inferred_complete_timeline |
| `Action_None` | 232 | 293 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 221 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 197 | 1 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |
| `Action_None` | 215 | 254 | 40 | inferred_complete_timeline |
| `Action_None` | 257 | 283 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 215 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 238 | 41 | inferred_complete_timeline |
| `Action_None` | 283 | 309 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–778
- **Visible Samples:** 748

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 244 | 47 | inferred_complete_timeline |
| `Action_None` | 246 | 341 | 96 | inferred_complete_timeline |
| `Action_None` | 343 | 347 | 5 | inferred_complete_timeline |
| `Action_None` | 354 | 357 | 4 | inferred_complete_timeline |
| `Action_None` | 363 | 368 | 6 | inferred_complete_timeline |
| `Action_None` | 371 | 373 | 3 | inferred_complete_timeline |
| `Action_None` | 377 | 497 | 121 | inferred_complete_timeline |
| `Action_None` | 503 | 581 | 79 | inferred_complete_timeline |
| `Action_None` | 586 | 606 | 21 | inferred_complete_timeline |
| `Action_None` | 608 | 622 | 15 | inferred_complete_timeline |
| `Action_None` | 626 | 778 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 343 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–531
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 531 | 334 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_None` | 198 | 285 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–295 | 291 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–10 | 11 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 181–292 | 86 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 184–241 | 26 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 213–339 | 122 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 217–308 | 92 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 242–288 | 47 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 244–431 | 185 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 249–285 | 37 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 267–270 | 4 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 273–280 | 7 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 294–512 | 214 | 4 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 296–457 | 162 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 327–439 | 113 | 3 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 337–350 | 14 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 352–617 | 266 | 1 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 404–495 | 91 | 2 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 414–741 | 213 | 9 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 426–451 | 26 | 1 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 430–472 | 33 | 3 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 437–738 | 188 | 7 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 438–477 | 40 | 1 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 446–611 | 127 | 7 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 457–483 | 27 | 1 | Undefined position; Undefined team |
| `45` | `69` | Position_Unknown | Team_Unknown | 462–681 | 219 | 2 | Undefined position; Undefined team |
| `46` | `70` | Position_Unknown | Team_Unknown | 463–582 | 116 | 2 | Undefined position; Undefined team |
| `47` | `77` | Position_Unknown | Team_Unknown | 472–473 | 2 | 1 | Undefined position; Undefined team |
| `48` | `78` | Position_Unknown | Team_Unknown | 479–489 | 7 | 2 | Undefined position; Undefined team |
| `49` | `80` | Position_Unknown | Team_Unknown | 488–575 | 88 | 1 | Undefined position; Undefined team |
| `50` | `81` | Position_Unknown | Team_Unknown | 500–620 | 117 | 2 | Undefined position; Undefined team |
| `51` | `82` | Position_Unknown | Team_Unknown | 502–600 | 55 | 4 | Undefined position; Undefined team |
| `52` | `83` | Position_Unknown | Team_Unknown | 504–577 | 74 | 1 | Undefined position; Undefined team |
| `53` | `84` | Position_Unknown | Team_Unknown | 505–656 | 125 | 4 | Undefined position; Undefined team |
| `54` | `85` | Position_Unknown | Team_Unknown | 506–510 | 5 | 1 | Undefined position; Undefined team |
| `55` | `87` | Position_Unknown | Team_Unknown | 510–542 | 28 | 2 | Undefined position; Undefined team |
| `56` | `88` | Position_Unknown | Team_Unknown | 510–538 | 24 | 2 | Undefined position; Undefined team |
| `57` | `90` | Position_Unknown | Team_Unknown | 514–757 | 233 | 4 | Undefined position; Undefined team |
| `58` | `91` | Position_Unknown | Team_Unknown | 515–724 | 198 | 5 | Undefined position; Undefined team |
| `59` | `92` | Position_Unknown | Team_Unknown | 547–771 | 187 | 4 | Undefined position; Undefined team |
| `60` | `93` | Position_Unknown | Team_Unknown | 553–622 | 70 | 1 | Undefined position; Undefined team |
| `61` | `94` | Position_Unknown | Team_Unknown | 555–586 | 20 | 4 | Undefined position; Undefined team |
| `62` | `95` | Position_Unknown | Team_Unknown | 584–722 | 131 | 5 | Undefined position; Undefined team |
| `63` | `96` | Position_Unknown | Team_Unknown | 585–744 | 138 | 5 | Undefined position; Undefined team |
| `64` | `97` | Position_Unknown | Team_Unknown | 589–773 | 109 | 9 | Undefined position; Undefined team |
| `65` | `99` | Position_Unknown | Team_Unknown | 592–629 | 37 | 2 | Undefined position; Undefined team |
| `66` | `100` | Position_Unknown | Team_Unknown | 594–637 | 7 | 3 | Undefined position; Undefined team |
| `67` | `101` | Position_Unknown | Team_Unknown | 601–701 | 30 | 4 | Undefined position; Undefined team |
| `68` | `102` | Position_Unknown | Team_Unknown | 605–761 | 145 | 6 | Undefined position; Undefined team |
| `69` | `103` | Position_Unknown | Team_Unknown | 606–733 | 67 | 8 | Undefined position; Undefined team |
| `70` | `106` | Position_Unknown | Team_Unknown | 612–624 | 13 | 1 | Undefined position; Undefined team |
| `71` | `107` | Position_Unknown | Team_Unknown | 619–650 | 32 | 1 | Undefined position; Undefined team |
| `72` | `108` | Position_Unknown | Team_Unknown | 619–729 | 84 | 6 | Undefined position; Undefined team |
| `73` | `109` | Position_Unknown | Team_Unknown | 635–745 | 109 | 2 | Undefined position; Undefined team |
| `74` | `110` | Position_Unknown | Team_Unknown | 636–712 | 67 | 6 | Undefined position; Undefined team |
| `75` | `112` | Position_Unknown | Team_Unknown | 642–776 | 81 | 7 | Undefined position; Undefined team |
| `76` | `114` | Position_Unknown | Team_Unknown | 652–654 | 3 | 1 | Undefined position; Undefined team |
| `77` | `118` | Position_Unknown | Team_Unknown | 661–779 | 109 | 5 | Undefined position; Undefined team |
| `78` | `119` | Position_Unknown | Team_Unknown | 669–696 | 26 | 3 | Undefined position; Undefined team |
| `79` | `120` | Position_Unknown | Team_Unknown | 669–698 | 28 | 2 | Undefined position; Undefined team |
| `80` | `121` | Position_Unknown | Team_Unknown | 673–779 | 107 | 1 | Undefined position; Undefined team |
| `81` | `123` | Position_Unknown | Team_Unknown | 680–716 | 37 | 1 | Undefined position; Undefined team |
| `82` | `126` | Position_Unknown | Team_Unknown | 687–755 | 21 | 4 | Undefined position; Undefined team |
| `83` | `127` | Position_Unknown | Team_Unknown | 688–689 | 2 | 1 | Undefined position; Undefined team |
| `84` | `128` | Position_Unknown | Team_Unknown | 690–779 | 77 | 5 | Undefined position; Undefined team |
| `85` | `130` | Position_Unknown | Team_Unknown | 709–738 | 28 | 3 | Undefined position; Undefined team |
| `86` | `131` | Position_Unknown | Team_Unknown | 713–738 | 8 | 4 | Undefined position; Undefined team |
| `87` | `133` | Position_Unknown | Team_Unknown | 721–729 | 8 | 2 | Undefined position; Undefined team |
| `88` | `134` | Position_Unknown | Team_Unknown | 722–778 | 24 | 5 | Undefined position; Undefined team |
| `89` | `135` | Position_Unknown | Team_Unknown | 722–778 | 13 | 3 | Undefined position; Undefined team |
| `90` | `141` | Position_Unknown | Team_Unknown | 738–757 | 18 | 2 | Undefined position; Undefined team |
| `91` | `142` | Position_Unknown | Team_Unknown | 748–779 | 29 | 3 | Undefined position; Undefined team |
| `92` | `145` | Position_Unknown | Team_Unknown | 758–759 | 2 | 1 | Undefined position; Undefined team |
| `93` | `146` | Position_Unknown | Team_Unknown | 765–779 | 8 | 2 | Undefined position; Undefined team |
| `94` | `147` | Position_Unknown | Team_Unknown | 766–777 | 5 | 2 | Undefined position; Undefined team |
| `95` | `149` | Position_Unknown | Team_Unknown | 772–773 | 2 | 1 | Undefined position; Undefined team |
| `96` | `151` | Position_Unknown | Team_Unknown | 777–778 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Support5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punt_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Guard` position mapped to `offense` team
- ⚠️ 77 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 77 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_CrossGoalLine' at frame 757 targets track ID '?', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 154 |
| Missing visible bounding boxes during action | 259 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 779 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-254] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-283] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-531] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-285] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-322] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-543] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-215] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-293] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-238] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-309] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-288] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-244] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-341] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-347] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-368] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-373] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-497] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-581] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-606] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-622] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-778] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-285] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [198-217] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-343] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-285] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-215] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-291] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-291] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-292] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-262] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-289] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-234] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-292] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-241] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-224] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-280] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-339] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-308] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-331] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-338] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-431] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-285] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-340] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-347] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-512] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-457] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [395-439] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-350] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-617] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-492] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-498] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-569] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-576] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-590] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-616] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [668-684] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-701] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [728-729] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [740-741] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-451] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-450] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-466] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-472] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-531] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-592] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-663] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-668] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [713-714] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [724-731] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [735-738] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-477] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-486] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-524] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-572] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-575] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-606] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-611] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-483] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-675] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-681] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-518] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-582] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-483] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-489] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-575] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-614] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-620] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-523] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-600] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-577] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-578] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-595] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-634] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-656] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-510] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-532] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-542] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-517] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-538] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-687] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-704] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [706-746] for track '57' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [755-757] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-600] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-656] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-698] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [705-706] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-724] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-706] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-729] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [754-755] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [769-771] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-622] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-557] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-562] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-586] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-595] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-615] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-624] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-695] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [698-722] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-698] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [703-707] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-722] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [724-727] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [742-744] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-621] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-651] for track '64' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-670] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-678] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [703-706] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-718] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [725-729] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [735-739] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [771-773] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-623] for track '65' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-629] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-637] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-607] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-630] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-635] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-701] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-607] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-656] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [662-707] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-731] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [733-757] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [760-761] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-608] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-625] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-634] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-656] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [663-672] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-678] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [683-686] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [732-733] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-624] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-650] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-640] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-680] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-686] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-699] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [718-722] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [727-729] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-653] for track '73' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [656-745] for track '73' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-638] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [643-664] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [668-678] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-685] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-697] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-712] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-690] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-706] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-711] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [715-717] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [753-758] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [764-765] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [775-776] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-654] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [661-697] for track '77' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [701-706] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-747] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [750-752] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-672] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-683] for track '78' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [685-696] for track '78' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-670] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-698] for track '79' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-716] for track '81' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-699] for track '82' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [705-707] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [727-728] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [753-755] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [688-689] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-694] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [698-703] for track '84' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [705-758] for track '84' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [762-768] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-727] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-735] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [737-738] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [713-714] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [720-721] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [726-727] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [737-738] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [721-722] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [724-729] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [722-727] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [735-739] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [742-745] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [767-773] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [777-778] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [722-727] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-731] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [775-778] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [738-746] for track '90' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [749-757] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [748-767] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [770-773] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [758-759] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [765-767] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [766-768] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [776-777] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [772-773] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [777-778] for track '96' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '82' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '82' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '83' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '83' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '84' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '84' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '85' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '85' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '86' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '86' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '87' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '87' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '88' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '88' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '89' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '89' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '90' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '90' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '91' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '91' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '92' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '92' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '93' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '93' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '94' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '94' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '95' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '95' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '96' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '96' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>