# Play-Annotation-Generator Annotation Review — Counter_168

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `Counter_168`
- **Frame Range:** 0 to 839 (840 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 839
- **Player Tracks:** 66
- **Ball Tracks:** 0
- **Action Segments:** 180
- **Validation Warnings:** 266
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 0
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 4
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 175
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | LB1 | defense | `9` | `8` |
| ⚠️ START CHANGED | `Action_DownBlock` | DT1 | defense | `4` | `3` |
| ⚠️ START CHANGED | `Action_DownBlock` | LB1 | defense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | DE2 | defense | `13` | `12` |
| ⚠️ START CHANGED | `Action_PullLeadBlock` | TE1 | offense | `6` | `5` |
| ⚠️ END CHANGED | `Action_SnapReceive` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | DE2 | defense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `12` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `16` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `2` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `22` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `6` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `7` | `Group` | 0 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallSnap` | LB1 | `9` | `8` | 37 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_DownBlock` | DT1 | `4` | `3` | 41 | START | 89 | 111 |
| ⚠️ START CHANGED | `Action_DownBlock` | LB1 | `9` | `8` | 41 | START | 89 | 111 |
| ❌ MISSING SEGMENT | `Action_PullBlock` | DE2 | `13` | `12` | 41 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_PullLeadBlock` | TE1 | `6` | `5` | 41 | START | 89 | 111 |
| ⚠️ END CHANGED | `Action_SnapReceive` | C | `12` | `11` | 54 | END | 89 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | DE2 | `13` | `12` | 64 | START | 89 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 111 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 89–552
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 250 | 162 | inferred_complete_timeline |
| `Action_None` | 254 | 269 | 16 | inferred_complete_timeline |
| `Action_None` | 273 | 277 | 5 | inferred_complete_timeline |
| `Action_None` | 280 | 294 | 15 | inferred_complete_timeline |
| `Action_None` | 318 | 345 | 28 | inferred_complete_timeline |
| `Action_None` | 350 | 371 | 22 | inferred_complete_timeline |
| `Action_None` | 376 | 393 | 18 | inferred_complete_timeline |
| `Action_None` | 395 | 411 | 17 | inferred_complete_timeline |
| `Action_None` | 413 | 552 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 89–552
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 140 | 52 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |
| `Action_None` | 274 | 277 | 4 | inferred_complete_timeline |
| `Action_None` | 279 | 287 | 9 | inferred_complete_timeline |
| `Action_None` | 290 | 312 | 23 | inferred_complete_timeline |
| `Action_None` | 316 | 343 | 28 | inferred_complete_timeline |
| `Action_None` | 346 | 552 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 89–278
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 131 | 43 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 169 | 10 | inferred_complete_timeline |
| `Action_None` | 171 | 278 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 44–54
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 44 | 54 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 89–552
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PullLeadBlock` | 89 | 111 | 23 | inferred_complete_timeline |
| `Action_None` | 112 | 446 | 335 | inferred_complete_timeline |
| `Action_None` | 453 | 468 | 16 | inferred_complete_timeline |
| `Action_None` | 471 | 552 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 89–459
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 459 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 89–255
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 131 | 43 | inferred_complete_timeline |
| `Action_None` | 134 | 140 | 7 | inferred_complete_timeline |
| `Action_None` | 142 | 148 | 7 | inferred_complete_timeline |
| `Action_None` | 150 | 255 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 89–383
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 300 | 212 | inferred_complete_timeline |
| `Action_None` | 324 | 343 | 20 | inferred_complete_timeline |
| `Action_None` | 367 | 383 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 89–552
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_SnapReceive` | 89 | 89 | 1 | inferred_complete_timeline |
| `Action_None` | 90 | 250 | 161 | inferred_complete_timeline |
| `Action_None` | 281 | 287 | 7 | inferred_complete_timeline |
| `Action_None` | 365 | 385 | 21 | inferred_complete_timeline |
| `Action_None` | 387 | 393 | 7 | inferred_complete_timeline |
| `Action_None` | 395 | 552 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 89–552
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 552 | 464 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 89–406
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 406 | 318 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 89–552
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 552 | 464 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 89–329
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_Handoff` | 89 | 299 | 211 | inferred_complete_timeline |
| `Action_Handoff` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 89–534
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_DownBlock` | 89 | 111 | 23 | inferred_complete_timeline |
| `Action_None` | 112 | 534 | 423 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 89–552
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_DownBlock` | 89 | 111 | 23 | inferred_complete_timeline |
| `Action_None` | 112 | 552 | 441 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 89–289
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 276 | 188 | inferred_complete_timeline |
| `Action_None` | 284 | 289 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 89–552
- **Visible Samples:** 431

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 140 | 52 | inferred_complete_timeline |
| `Action_None` | 142 | 264 | 123 | inferred_complete_timeline |
| `Action_None` | 271 | 277 | 7 | inferred_complete_timeline |
| `Action_None` | 279 | 289 | 11 | inferred_complete_timeline |
| `Action_None` | 293 | 302 | 10 | inferred_complete_timeline |
| `Action_None` | 306 | 314 | 9 | inferred_complete_timeline |
| `Action_None` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 391 | 72 | inferred_complete_timeline |
| `Action_None` | 396 | 410 | 15 | inferred_complete_timeline |
| `Action_None` | 413 | 477 | 65 | inferred_complete_timeline |
| `Action_None` | 484 | 485 | 2 | inferred_complete_timeline |
| `Action_None` | 490 | 552 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 89–345
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 303 | 215 | inferred_complete_timeline |
| `Action_None` | 324 | 325 | 2 | inferred_complete_timeline |
| `Action_None` | 328 | 345 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 89–552
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 386 | 298 | inferred_complete_timeline |
| `Action_None` | 388 | 468 | 81 | inferred_complete_timeline |
| `Action_None` | 478 | 552 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 89–552
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 552 | 464 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 89–552
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 89 | 140 | 52 | inferred_complete_timeline |
| `Action_None` | 142 | 148 | 7 | inferred_complete_timeline |
| `Action_None` | 150 | 295 | 146 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_None` | 324 | 345 | 22 | inferred_complete_timeline |
| `Action_None` | 349 | 552 | 204 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 33–43 | 11 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 89–389 | 266 | 11 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 93–305 | 129 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 141–142 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 319–540 | 222 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 325–552 | 228 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 326–552 | 201 | 4 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 329–552 | 206 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 330–552 | 213 | 4 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 362–794 | 406 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 403–549 | 146 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 428–434 | 6 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 449–452 | 4 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 455–458 | 4 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 506–552 | 44 | 3 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 517–520 | 4 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 523–552 | 30 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 538–552 | 14 | 2 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 551–552 | 2 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 580–771 | 192 | 1 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 580–839 | 260 | 1 | Undefined position; Undefined team |
| `42` | `50` | Position_Unknown | Team_Unknown | 580–839 | 259 | 2 | Undefined position; Undefined team |
| `43` | `51` | Position_Unknown | Team_Unknown | 580–796 | 215 | 2 | Undefined position; Undefined team |
| `44` | `52` | Position_Unknown | Team_Unknown | 580–703 | 107 | 2 | Undefined position; Undefined team |
| `45` | `53` | Position_Unknown | Team_Unknown | 580–713 | 132 | 2 | Undefined position; Undefined team |
| `46` | `54` | Position_Unknown | Team_Unknown | 580–791 | 193 | 3 | Undefined position; Undefined team |
| `47` | `55` | Position_Unknown | Team_Unknown | 580–839 | 260 | 1 | Undefined position; Undefined team |
| `48` | `56` | Position_Unknown | Team_Unknown | 580–695 | 116 | 1 | Undefined position; Undefined team |
| `49` | `57` | Position_Unknown | Team_Unknown | 580–765 | 184 | 2 | Undefined position; Undefined team |
| `50` | `58` | Position_Unknown | Team_Unknown | 580–800 | 208 | 4 | Undefined position; Undefined team |
| `51` | `59` | Position_Unknown | Team_Unknown | 580–694 | 112 | 3 | Undefined position; Undefined team |
| `52` | `62` | Position_Unknown | Team_Unknown | 583–822 | 204 | 10 | Undefined position; Undefined team |
| `53` | `63` | Position_Unknown | Team_Unknown | 600–647 | 48 | 1 | Undefined position; Undefined team |
| `54` | `64` | Position_Unknown | Team_Unknown | 678–839 | 155 | 3 | Undefined position; Undefined team |
| `55` | `68` | Position_Unknown | Team_Unknown | 709–825 | 117 | 1 | Undefined position; Undefined team |
| `56` | `69` | Position_Unknown | Team_Unknown | 711–815 | 103 | 2 | Undefined position; Undefined team |
| `57` | `70` | Position_Unknown | Team_Unknown | 729–802 | 69 | 2 | Undefined position; Undefined team |
| `58` | `71` | Position_Unknown | Team_Unknown | 738–836 | 93 | 2 | Undefined position; Undefined team |
| `59` | `72` | Position_Unknown | Team_Unknown | 741–839 | 98 | 2 | Undefined position; Undefined team |
| `60` | `73` | Position_Unknown | Team_Unknown | 756–784 | 28 | 2 | Undefined position; Undefined team |
| `61` | `76` | Position_Unknown | Team_Unknown | 763–768 | 6 | 1 | Undefined position; Undefined team |
| `62` | `77` | Position_Unknown | Team_Unknown | 765–835 | 66 | 3 | Undefined position; Undefined team |
| `63` | `78` | Position_Unknown | Team_Unknown | 768–787 | 20 | 1 | Undefined position; Undefined team |
| `64` | `80` | Position_Unknown | Team_Unknown | 782–786 | 5 | 1 | Undefined position; Undefined team |
| `65` | `81` | Position_Unknown | Team_Unknown | 787–790 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `9` (LB1)
- ⚠️ `Action_DownBlock` for actor_track_id `4` (DT1): Annotated start 41 != Inferred start 89
- ⚠️ `Action_DownBlock` for actor_track_id `9` (LB1): Annotated start 41 != Inferred start 89
- ❌ Missing segment for action `Action_PullBlock` on target `13` (DE2)
- ⚠️ `Action_PullLeadBlock` for actor_track_id `6` (TE1): Annotated start 41 != Inferred start 89
- ⚠️ Ambiguous match for action `Action_Handoff` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 45 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 45 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BallCarry' at frame 82 targets track ID '?', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 90 |
| Missing visible bounding boxes during action | 171 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 338: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 839 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '8' has invalid range: start=89, end=54. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '11' has invalid range: start=89, end=54. Clamping end to start.
- ⚠️ Segment 'Action_PullBlock' for track '12' has invalid range: start=89, end=63. Clamping end to start.
- ⚠️ Action 'Action_None' range [37-43] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-54] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-552] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-534] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-386] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-468] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-552] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-446] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-468] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-552] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-459] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-552] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-552] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-276] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-289] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-264] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-277] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-289] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-302] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-314] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-391] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-410] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-477] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-552] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-287] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-385] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-393] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-552] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [89-299] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [324-329] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-303] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-345] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-406] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-169] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-278] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-250] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-269] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-294] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-345] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-371] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-393] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-411] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-552] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-552] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-140] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-295] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-345] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-552] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-255] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-300] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-343] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-383] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-140] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-312] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-343] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-552] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-101] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-138] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-148] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-300] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-309] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-389] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-277] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-305] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-540] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-552] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-351] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-374] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-552] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-422] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-431] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-519] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-552] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-339] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-552] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-552] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-794] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-411] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-549] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-430] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-434] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-452] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-458] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-508] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-552] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-520] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-552] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-540] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-552] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-552] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-771] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-839] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-749] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-738] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [741-796] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-684] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-703] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-697] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-713] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-734] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [736-737] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [756-791] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-695] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-693] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [696-765] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-628] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-674] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [685-711] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [714-800] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-589] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-602] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-694] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-639] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-643] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [657-660] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [665-666] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-670] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-684] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-707] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-711] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [719-720] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [723-822] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-647] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-716] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [721-764] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-825] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-722] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [725-815] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-764] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [770-802] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [738-828] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [835-836] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [741-788] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [756-759] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [761-784] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [763-768] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [765-791] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [794-826] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [830-835] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [768-787] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [782-786] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [787-790] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>