# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_84

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_84`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 71
- **Ball Tracks:** 0
- **Action Segments:** 241
- **Validation Warnings:** 323
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 226
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `21` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `19` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `72` | `56` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `0` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `1` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `2` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `3` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `4` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `7` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `7` | `7` | 25 | START | 25 | 83 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `2` | `2` | 49 | END | 49 | 49 |
| ✅ EXACT | `Action_PuntBall` | Punter | `2` | `2` | 84 | START | 84 | 94 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `21` | `19` | 211 | START | 211 | 220 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `19` | 255 | START | 255 | 468 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `72` | `56` | 637 | START | 637 | 645 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 225 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–414
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 88 | 64 | inferred_complete_timeline |
| `Action_None` | 92 | 157 | 66 | inferred_complete_timeline |
| `Action_None` | 160 | 169 | 10 | inferred_complete_timeline |
| `Action_None` | 172 | 414 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 615

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_LongSnap` | 25 | 83 | 59 | inferred_complete_timeline |
| `Action_None` | 84 | 320 | 237 | inferred_complete_timeline |
| `Action_None` | 326 | 347 | 22 | inferred_complete_timeline |
| `Action_None` | 350 | 398 | 49 | inferred_complete_timeline |
| `Action_None` | 400 | 453 | 54 | inferred_complete_timeline |
| `Action_None` | 458 | 470 | 13 | inferred_complete_timeline |
| `Action_None` | 475 | 477 | 3 | inferred_complete_timeline |
| `Action_None` | 482 | 488 | 7 | inferred_complete_timeline |
| `Action_None` | 491 | 496 | 6 | inferred_complete_timeline |
| `Action_None` | 498 | 500 | 3 | inferred_complete_timeline |
| `Action_None` | 502 | 506 | 5 | inferred_complete_timeline |
| `Action_None` | 512 | 520 | 9 | inferred_complete_timeline |
| `Action_None` | 524 | 550 | 27 | inferred_complete_timeline |
| `Action_None` | 561 | 573 | 13 | inferred_complete_timeline |
| `Action_None` | 577 | 659 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–453
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 118 | 94 | inferred_complete_timeline |
| `Action_None` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_None` | 132 | 251 | 120 | inferred_complete_timeline |
| `Action_None` | 253 | 449 | 197 | inferred_complete_timeline |
| `Action_None` | 452 | 453 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 212 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 146 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 49 | 1 | inferred_complete_timeline |
| `Action_None` | 50 | 83 | 34 | inferred_complete_timeline |
| `Action_PuntBall` | 84 | 94 | 11 | inferred_complete_timeline |
| `Action_None` | 95 | 124 | 30 | inferred_complete_timeline |
| `Action_None` | 139 | 191 | 53 | inferred_complete_timeline |
| `Action_None` | 196 | 241 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 636

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 442 | 418 | inferred_complete_timeline |
| `Action_None` | 444 | 458 | 15 | inferred_complete_timeline |
| `Action_None` | 462 | 467 | 6 | inferred_complete_timeline |
| `Action_None` | 488 | 659 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 102 | 78 | inferred_complete_timeline |
| `Action_None` | 105 | 209 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–549
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 46 | 22 | inferred_complete_timeline |
| `Action_None` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_None` | 67 | 127 | 61 | inferred_complete_timeline |
| `Action_None` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 360 | 218 | inferred_complete_timeline |
| `Action_None` | 363 | 480 | 118 | inferred_complete_timeline |
| `Action_None` | 485 | 531 | 47 | inferred_complete_timeline |
| `Action_None` | 534 | 538 | 5 | inferred_complete_timeline |
| `Action_None` | 540 | 543 | 4 | inferred_complete_timeline |
| `Action_None` | 546 | 549 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 44 | 20 | inferred_complete_timeline |
| `Action_None` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_None` | 64 | 66 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 42 | 18 | inferred_complete_timeline |
| `Action_None` | 49 | 317 | 269 | inferred_complete_timeline |
| `Action_None` | 321 | 338 | 18 | inferred_complete_timeline |
| `Action_None` | 352 | 353 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 622

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 38 | 14 | inferred_complete_timeline |
| `Action_None` | 41 | 43 | 3 | inferred_complete_timeline |
| `Action_None` | 45 | 50 | 6 | inferred_complete_timeline |
| `Action_None` | 63 | 384 | 322 | inferred_complete_timeline |
| `Action_None` | 398 | 472 | 75 | inferred_complete_timeline |
| `Action_None` | 476 | 600 | 125 | inferred_complete_timeline |
| `Action_None` | 607 | 609 | 3 | inferred_complete_timeline |
| `Action_None` | 611 | 659 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 138 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 168 | 144 | inferred_complete_timeline |
| `Action_None` | 171 | 173 | 3 | inferred_complete_timeline |
| `Action_None` | 175 | 180 | 6 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 220 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 140 | 116 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 65–447 | 376 | 6 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 72–230 | 159 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 73–487 | 383 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 85–613 | 483 | 6 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 107–182 | 74 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 114–467 | 352 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 119–467 | 349 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 126–129 | 4 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 127–202 | 76 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 137–143 | 7 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 146–147 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 152–154 | 3 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 154–216 | 40 | 6 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 161–169 | 9 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 164–193 | 13 | 4 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 177–180 | 4 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 188–289 | 95 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 228–452 | 216 | 5 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 263–659 | 378 | 9 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 264–659 | 385 | 5 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 277–596 | 319 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 280–373 | 81 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 283–659 | 338 | 5 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 286–659 | 351 | 9 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 300–368 | 69 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 357–381 | 13 | 4 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 368–369 | 2 | 1 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 372–522 | 143 | 3 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 375–378 | 4 | 1 | Undefined position; Undefined team |
| `46` | `58` | Position_Unknown | Team_Unknown | 384–549 | 129 | 8 | Undefined position; Undefined team |
| `47` | `59` | Position_Unknown | Team_Unknown | 388–659 | 261 | 5 | Undefined position; Undefined team |
| `48` | `61` | Position_Unknown | Team_Unknown | 407–659 | 231 | 5 | Undefined position; Undefined team |
| `49` | `62` | Position_Unknown | Team_Unknown | 407–442 | 21 | 2 | Undefined position; Undefined team |
| `50` | `63` | Position_Unknown | Team_Unknown | 411–659 | 207 | 2 | Undefined position; Undefined team |
| `51` | `67` | Position_Unknown | Team_Unknown | 421–431 | 11 | 1 | Undefined position; Undefined team |
| `52` | `68` | Position_Unknown | Team_Unknown | 433–448 | 10 | 4 | Undefined position; Undefined team |
| `53` | `69` | Position_Unknown | Team_Unknown | 444–446 | 3 | 1 | Undefined position; Undefined team |
| `54` | `70` | Position_Unknown | Team_Unknown | 450–483 | 6 | 3 | Undefined position; Undefined team |
| `55` | `71` | Position_Unknown | Team_Unknown | 459–462 | 4 | 1 | Undefined position; Undefined team |
| `56` | `72` | Position_Unknown | Team_Unknown | 463–659 | 197 | 3 | Undefined position; Undefined team |
| `57` | `74` | Position_Unknown | Team_Unknown | 466–470 | 5 | 1 | Undefined position; Undefined team |
| `58` | `75` | Position_Unknown | Team_Unknown | 468–476 | 9 | 1 | Undefined position; Undefined team |
| `59` | `76` | Position_Unknown | Team_Unknown | 471–576 | 88 | 6 | Undefined position; Undefined team |
| `60` | `77` | Position_Unknown | Team_Unknown | 484–486 | 3 | 1 | Undefined position; Undefined team |
| `61` | `79` | Position_Unknown | Team_Unknown | 506–593 | 79 | 3 | Undefined position; Undefined team |
| `62` | `81` | Position_Unknown | Team_Unknown | 530–531 | 2 | 1 | Undefined position; Undefined team |
| `63` | `82` | Position_Unknown | Team_Unknown | 531–591 | 57 | 2 | Undefined position; Undefined team |
| `64` | `83` | Position_Unknown | Team_Unknown | 540–596 | 57 | 1 | Undefined position; Undefined team |
| `65` | `85` | Position_Unknown | Team_Unknown | 564–596 | 28 | 2 | Undefined position; Undefined team |
| `66` | `90` | Position_Unknown | Team_Unknown | 609–659 | 43 | 3 | Undefined position; Undefined team |
| `67` | `92` | Position_Unknown | Team_Unknown | 612–659 | 46 | 3 | Undefined position; Undefined team |
| `68` | `93` | Position_Unknown | Team_Unknown | 613–659 | 46 | 2 | Undefined position; Undefined team |
| `69` | `96` | Position_Unknown | Team_Unknown | 650–659 | 10 | 1 | Undefined position; Undefined team |
| `70` | `98` | Position_Unknown | Team_Unknown | 657–658 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 55 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 55 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 110 |
| Missing visible bounding boxes during action | 210 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [25-146] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-212] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-241] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-414] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-102] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-209] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-320] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-347] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-398] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-453] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-470] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-477] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-488] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-496] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-500] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-506] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-520] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-550] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-573] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-659] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-251] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-449] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-127] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-360] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-480] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-531] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-538] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-543] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-549] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-138] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-442] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-458] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-467] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-659] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-44] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-317] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-338] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-384] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-472] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-600] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-609] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-659] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-289] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-374] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-380] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-447] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-230] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-336] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-455] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [255-468] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [470-486] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [532-613] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-305] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-467] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-467] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-202] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-162] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-199] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-169] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-280] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-256] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-352] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-392] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-402] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-452] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-321] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-448] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-458] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-513] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-524] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-568] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-636] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [640-643] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-296] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-412] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-557] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-579] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-659] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-488] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-596] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-331] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-373] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-391] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-462] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-486] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-531] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-309] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-404] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-572] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-578] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-591] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-599] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-609] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-659] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-368] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-362] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-378] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-455] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-488] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-522] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-397] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-436] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-441] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-449] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-529] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-549] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-462] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-474] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-544] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-551] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-659] for track '47' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-444] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-465] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-474] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-510] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-411] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-442] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-659] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-431] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-435] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-448] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-446] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-462] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-636] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-470] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-476] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-474] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-516] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-529] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-538] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-545] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-576] for track '59' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-486] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-553] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-567] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-593] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-579] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-591] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-596] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-589] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-596] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-612] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-642] for track '66' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-613] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-652] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-620] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-659] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [657-658] for track '70' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>