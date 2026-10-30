# Play-Annotation-Generator Annotation Review — FieldGoalBlock_109

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_109`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 72
- **Ball Tracks:** 0
- **Action Segments:** 255
- **Validation Warnings:** 337
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 238
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `9` | `9` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `6` | `6` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher6 | defense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `10` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `19` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `2` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `20` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `3` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `6` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `9` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `9` | `9` | 23 | START | 23 | 35 |
| ✅ EXACT | `Action_KickBall` | Kicker | `6` | `6` | 45 | START | 45 | 52 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher6 | `18` | `18` | 52 | START | 52 | 67 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 574

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PlaceBall` | 23 | 35 | 13 | inferred_complete_timeline |
| `Action_None` | 36 | 42 | 7 | inferred_complete_timeline |
| `Action_None` | 50 | 171 | 122 | inferred_complete_timeline |
| `Action_None` | 185 | 199 | 15 | inferred_complete_timeline |
| `Action_None` | 206 | 599 | 394 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 589

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_KickBall` | 45 | 52 | 8 | inferred_complete_timeline |
| `Action_None` | 53 | 253 | 201 | inferred_complete_timeline |
| `Action_None` | 256 | 521 | 266 | inferred_complete_timeline |
| `Action_None` | 531 | 599 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_None` | 45 | 92 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–506
- **Visible Samples:** 503

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 131 | 87 | inferred_complete_timeline |
| `Action_None` | 133 | 261 | 129 | inferred_complete_timeline |
| `Action_None` | 263 | 344 | 82 | inferred_complete_timeline |
| `Action_None` | 347 | 506 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 23 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 44 | 18 | inferred_complete_timeline |
| `Action_None` | 45 | 142 | 98 | inferred_complete_timeline |
| `Action_None` | 145 | 599 | 455 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 113 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 173 | 129 | inferred_complete_timeline |
| `Action_None` | 176 | 599 | 424 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–503
- **Visible Samples:** 495

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 86 | 42 | inferred_complete_timeline |
| `Action_None` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 503 | 404 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 158 | 114 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 146 | 102 | inferred_complete_timeline |
| `Action_None` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 91 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–580
- **Visible Samples:** 575

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 434 | 390 | inferred_complete_timeline |
| `Action_None` | 438 | 445 | 8 | inferred_complete_timeline |
| `Action_None` | 448 | 514 | 67 | inferred_complete_timeline |
| `Action_None` | 516 | 580 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 44 | 18 | inferred_complete_timeline |
| `Action_None` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 168 | 17 | inferred_complete_timeline |
| `Action_None` | 173 | 179 | 7 | inferred_complete_timeline |
| `Action_None` | 193 | 195 | 3 | inferred_complete_timeline |
| `Action_None` | 197 | 560 | 364 | inferred_complete_timeline |
| `Action_None` | 562 | 594 | 33 | inferred_complete_timeline |
| `Action_None` | 597 | 599 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 149 | 105 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 54 | 344 | 291 | inferred_complete_timeline |
| `Action_None` | 356 | 361 | 6 | inferred_complete_timeline |
| `Action_None` | 368 | 369 | 2 | inferred_complete_timeline |
| `Action_None` | 371 | 409 | 39 | inferred_complete_timeline |
| `Action_None` | 411 | 599 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 17 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_None` | 45 | 45 | 1 | inferred_complete_timeline |
| `Action_None` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_None` | 53 | 508 | 456 | inferred_complete_timeline |
| `Action_None` | 510 | 584 | 75 | inferred_complete_timeline |
| `Action_None` | 589 | 599 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–403
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_BlockKick` | 52 | 67 | 16 | inferred_complete_timeline |
| `Action_None` | 68 | 366 | 299 | inferred_complete_timeline |
| `Action_None` | 368 | 373 | 6 | inferred_complete_timeline |
| `Action_None` | 390 | 403 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 278 | 234 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–598 | 585 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 8–44 | 9 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 44–45 | 2 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 56–59 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 60–149 | 10 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 64–65 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 66–168 | 79 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 69–346 | 262 | 5 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 76–77 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 80–91 | 12 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 81–516 | 430 | 5 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 105–573 | 435 | 10 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 113–253 | 94 | 7 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 126–599 | 446 | 5 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 134–197 | 5 | 2 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 174–176 | 3 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 187–209 | 21 | 2 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 188–559 | 369 | 3 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 197–207 | 11 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 201–209 | 9 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 208–489 | 281 | 2 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 213–292 | 72 | 4 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 214–227 | 10 | 3 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 221–224 | 4 | 1 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 224–586 | 359 | 2 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 231–584 | 352 | 2 | Undefined position; Undefined team |
| `47` | `67` | Position_Unknown | Team_Unknown | 247–573 | 212 | 25 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 247–405 | 159 | 1 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 264–558 | 231 | 14 | Undefined position; Undefined team |
| `50` | `73` | Position_Unknown | Team_Unknown | 277–599 | 307 | 5 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 277–278 | 2 | 1 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 283–284 | 2 | 1 | Undefined position; Undefined team |
| `53` | `78` | Position_Unknown | Team_Unknown | 291–293 | 3 | 1 | Undefined position; Undefined team |
| `54` | `83` | Position_Unknown | Team_Unknown | 312–314 | 3 | 1 | Undefined position; Undefined team |
| `55` | `84` | Position_Unknown | Team_Unknown | 316–379 | 51 | 4 | Undefined position; Undefined team |
| `56` | `85` | Position_Unknown | Team_Unknown | 318–424 | 80 | 7 | Undefined position; Undefined team |
| `57` | `88` | Position_Unknown | Team_Unknown | 336–408 | 39 | 6 | Undefined position; Undefined team |
| `58` | `90` | Position_Unknown | Team_Unknown | 349–599 | 239 | 4 | Undefined position; Undefined team |
| `59` | `91` | Position_Unknown | Team_Unknown | 353–355 | 3 | 1 | Undefined position; Undefined team |
| `60` | `96` | Position_Unknown | Team_Unknown | 372–374 | 3 | 1 | Undefined position; Undefined team |
| `61` | `97` | Position_Unknown | Team_Unknown | 384–389 | 5 | 2 | Undefined position; Undefined team |
| `62` | `98` | Position_Unknown | Team_Unknown | 393–406 | 11 | 3 | Undefined position; Undefined team |
| `63` | `99` | Position_Unknown | Team_Unknown | 398–488 | 44 | 7 | Undefined position; Undefined team |
| `64` | `101` | Position_Unknown | Team_Unknown | 409–410 | 2 | 1 | Undefined position; Undefined team |
| `65` | `109` | Position_Unknown | Team_Unknown | 481–483 | 3 | 1 | Undefined position; Undefined team |
| `66` | `115` | Position_Unknown | Team_Unknown | 527–599 | 69 | 3 | Undefined position; Undefined team |
| `67` | `116` | Position_Unknown | Team_Unknown | 528–529 | 2 | 1 | Undefined position; Undefined team |
| `68` | `121` | Position_Unknown | Team_Unknown | 548–550 | 3 | 1 | Undefined position; Undefined team |
| `69` | `125` | Position_Unknown | Team_Unknown | 580–599 | 16 | 2 | Undefined position; Undefined team |
| `70` | `128` | Position_Unknown | Team_Unknown | 587–588 | 2 | 1 | Undefined position; Undefined team |
| `71` | `129` | Position_Unknown | Team_Unknown | 592–596 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 52 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 52 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 104 |
| Missing visible bounding boxes during action | 231 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 220: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [45-146] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-158] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-113] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-278] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-434] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-445] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-514] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-580] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [45-52] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-253] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-521] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 45, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [45-92] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-44] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-168] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-560] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-594] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-42] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-171] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-199] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-599] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-344] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-361] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-409] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-599] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-44] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-582] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 45, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [45-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-508] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-584] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-131] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-261] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-344] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-506] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-366] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-373] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-403] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-503] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-13] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-44] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '22' starts at frame 45, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [45-45] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-65] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-80] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-117] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-145] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-346] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-91] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-101] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-467] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-480] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-516] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-122] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-152] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-168] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-176] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-285] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-443] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-573] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-168] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-228] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-171] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-193] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-219] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-566] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-209] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-554] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-559] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-207] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-209] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-482] for track '40' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-489] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-236] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-246] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-292] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-580] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-574] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-584] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-252] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-321] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-333] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-364] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-384] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-401] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-425] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-480] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-499] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-516] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-529] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-534] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-539] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-546] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-565] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-569] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-573] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-405] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-272] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-305] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-317] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-361] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-384] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-550] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-558] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-352] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-362] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-422] for track '50' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-430] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-599] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-324] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-363] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-370] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-379] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-341] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-353] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-373] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-417] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-424] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-344] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-380] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-408] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-352] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-374] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-386] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-397] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-403] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-400] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-409] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-451] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-488] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-483] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-551] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-595] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-529] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-550] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-589] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-588] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-596] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>