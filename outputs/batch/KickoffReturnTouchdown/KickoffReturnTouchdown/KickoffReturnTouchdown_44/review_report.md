# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_44

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_44`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 61
- **Ball Tracks:** 0
- **Action Segments:** 203
- **Validation Warnings:** 253
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 190
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `10` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `11` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `12` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `13` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `14` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `16` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `8` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `15` | `15` | 17 | START | 17 | 80 |
| ✅ EXACT | `Action_KickBall` | Kicker | `15` | `15` | 81 | START | 81 | 87 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `2` | `2` | 170 | START | 170 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | `2` | `2` | 260 | START | 260 | 313 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–642
- **Visible Samples:** 641

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_KickApproach` | 17 | 80 | 64 | inferred_complete_timeline |
| `Action_KickBall` | 81 | 87 | 7 | inferred_complete_timeline |
| `Action_None` | 88 | 410 | 323 | inferred_complete_timeline |
| `Action_None` | 412 | 424 | 13 | inferred_complete_timeline |
| `Action_None` | 426 | 642 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_None` | 34 | 69 | 36 | inferred_complete_timeline |
| `Action_None` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_None` | 118 | 135 | 18 | inferred_complete_timeline |
| `Action_None` | 137 | 234 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 42 | 26 | inferred_complete_timeline |
| `Action_None` | 49 | 84 | 36 | inferred_complete_timeline |
| `Action_None` | 86 | 253 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 60 | 44 | inferred_complete_timeline |
| `Action_None` | 66 | 85 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–566
- **Visible Samples:** 542

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 64 | 48 | inferred_complete_timeline |
| `Action_None` | 66 | 155 | 90 | inferred_complete_timeline |
| `Action_None` | 166 | 338 | 173 | inferred_complete_timeline |
| `Action_None` | 352 | 356 | 5 | inferred_complete_timeline |
| `Action_None` | 358 | 566 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–503
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 230 | 214 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 270 | 14 | inferred_complete_timeline |
| `Action_None` | 272 | 280 | 9 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |
| `Action_None` | 289 | 291 | 3 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_None` | 306 | 308 | 3 | inferred_complete_timeline |
| `Action_None` | 318 | 335 | 18 | inferred_complete_timeline |
| `Action_None` | 356 | 357 | 2 | inferred_complete_timeline |
| `Action_None` | 365 | 503 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 142 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 21 | 5 | inferred_complete_timeline |
| `Action_None` | 23 | 44 | 22 | inferred_complete_timeline |
| `Action_None` | 49 | 210 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 176 | 160 | inferred_complete_timeline |
| `Action_None` | 179 | 248 | 70 | inferred_complete_timeline |
| `Action_None` | 253 | 355 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 237 | 221 | inferred_complete_timeline |
| `Action_None` | 239 | 262 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 213 | 197 | inferred_complete_timeline |
| `Action_None` | 218 | 226 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–385
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 235 | 219 | inferred_complete_timeline |
| `Action_None` | 238 | 243 | 6 | inferred_complete_timeline |
| `Action_None` | 251 | 263 | 13 | inferred_complete_timeline |
| `Action_None` | 266 | 324 | 59 | inferred_complete_timeline |
| `Action_None` | 365 | 385 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 16 | 9 | inferred_complete_timeline |
| `Action_None` | 17 | 106 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–310
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 243 | 227 | inferred_complete_timeline |
| `Action_None` | 253 | 310 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–591
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 108 | 92 | inferred_complete_timeline |
| `Action_None` | 111 | 210 | 100 | inferred_complete_timeline |
| `Action_None` | 218 | 231 | 14 | inferred_complete_timeline |
| `Action_None` | 241 | 243 | 3 | inferred_complete_timeline |
| `Action_None` | 257 | 335 | 79 | inferred_complete_timeline |
| `Action_None` | 374 | 471 | 98 | inferred_complete_timeline |
| `Action_None` | 480 | 518 | 39 | inferred_complete_timeline |
| `Action_None` | 528 | 591 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 626

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_None` | 318 | 335 | 18 | inferred_complete_timeline |
| `Action_None` | 338 | 345 | 8 | inferred_complete_timeline |
| `Action_None` | 350 | 351 | 2 | inferred_complete_timeline |
| `Action_None` | 360 | 386 | 27 | inferred_complete_timeline |
| `Action_None` | 392 | 457 | 66 | inferred_complete_timeline |
| `Action_None` | 469 | 609 | 141 | inferred_complete_timeline |
| `Action_None` | 611 | 659 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_CatchKick` | 170 | 235 | 66 | inferred_complete_timeline |
| `Action_None` | 236 | 259 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 260 | 313 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 315 | 319 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 321 | 322 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 347 | 331 | inferred_complete_timeline |
| `Action_None` | 357 | 374 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 635

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 110 | 94 | inferred_complete_timeline |
| `Action_None` | 114 | 149 | 36 | inferred_complete_timeline |
| `Action_None` | 153 | 200 | 48 | inferred_complete_timeline |
| `Action_None` | 203 | 234 | 32 | inferred_complete_timeline |
| `Action_None` | 240 | 251 | 12 | inferred_complete_timeline |
| `Action_None` | 253 | 336 | 84 | inferred_complete_timeline |
| `Action_None` | 343 | 350 | 8 | inferred_complete_timeline |
| `Action_None` | 356 | 659 | 304 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 2–659 | 636 | 5 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 16–299 | 248 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 79–659 | 581 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 123–659 | 432 | 7 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 138–659 | 517 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 146–258 | 65 | 7 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 165–340 | 168 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 224–352 | 124 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 251–296 | 42 | 4 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 252–636 | 349 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 259–319 | 56 | 4 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 267–435 | 160 | 4 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 307–368 | 62 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 308–659 | 338 | 5 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 317–318 | 2 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 328–659 | 318 | 2 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 349–659 | 297 | 4 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 355–659 | 305 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 359–371 | 12 | 2 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 385–421 | 37 | 1 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 385–397 | 13 | 1 | Undefined position; Undefined team |
| `43` | `49` | Position_Unknown | Team_Unknown | 392–659 | 268 | 1 | Undefined position; Undefined team |
| `44` | `50` | Position_Unknown | Team_Unknown | 393–396 | 4 | 1 | Undefined position; Undefined team |
| `45` | `53` | Position_Unknown | Team_Unknown | 402–408 | 7 | 1 | Undefined position; Undefined team |
| `46` | `54` | Position_Unknown | Team_Unknown | 403–415 | 11 | 3 | Undefined position; Undefined team |
| `47` | `55` | Position_Unknown | Team_Unknown | 408–573 | 166 | 1 | Undefined position; Undefined team |
| `48` | `56` | Position_Unknown | Team_Unknown | 408–659 | 243 | 4 | Undefined position; Undefined team |
| `49` | `57` | Position_Unknown | Team_Unknown | 413–659 | 247 | 1 | Undefined position; Undefined team |
| `50` | `58` | Position_Unknown | Team_Unknown | 418–659 | 238 | 2 | Undefined position; Undefined team |
| `51` | `59` | Position_Unknown | Team_Unknown | 433–473 | 41 | 1 | Undefined position; Undefined team |
| `52` | `60` | Position_Unknown | Team_Unknown | 437–439 | 3 | 1 | Undefined position; Undefined team |
| `53` | `62` | Position_Unknown | Team_Unknown | 438–471 | 15 | 3 | Undefined position; Undefined team |
| `54` | `63` | Position_Unknown | Team_Unknown | 444–446 | 3 | 1 | Undefined position; Undefined team |
| `55` | `65` | Position_Unknown | Team_Unknown | 448–659 | 212 | 1 | Undefined position; Undefined team |
| `56` | `66` | Position_Unknown | Team_Unknown | 455–456 | 2 | 1 | Undefined position; Undefined team |
| `57` | `69` | Position_Unknown | Team_Unknown | 506–659 | 130 | 6 | Undefined position; Undefined team |
| `58` | `72` | Position_Unknown | Team_Unknown | 563–564 | 2 | 1 | Undefined position; Undefined team |
| `59` | `76` | Position_Unknown | Team_Unknown | 616–618 | 3 | 1 | Undefined position; Undefined team |
| `60` | `77` | Position_Unknown | Team_Unknown | 655–659 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ 42 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 42 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 46, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '673,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 84 |
| Missing visible bounding boxes during action | 167 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action 'Action_None' range [17-347] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-374] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-314] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-335] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-345] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-386] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-457] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-609] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [260-313] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [315-319] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [321-322] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-235] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-243] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-263] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-324] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-385] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-243] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-310] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-213] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-226] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-231] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-335] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-471] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-518] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-591] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-64] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-338] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-356] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-566] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-251] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-336] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-350] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-659] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-248] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-355] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-230] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-270] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-280] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-335] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-503] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-85] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-210] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-410] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-424] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-642] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-84] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-253] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-234] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-16] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-63] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-379] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-85] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-176] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-236] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-299] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-659] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-333] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-424] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-228] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-340] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-642] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-250] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-185] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-340] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-352] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-281] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-335] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-413] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-636] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-300] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-316] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-308] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-356] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-435] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-368] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-314] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-336] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-345] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-635] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-524] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-357] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-461] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-470] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-659] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-368] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-421] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-397] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-396] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-408] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-407] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-412] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-573] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-427] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-659] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-460] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-473] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-439] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-441] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-471] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-446] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-530] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-536] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-551] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-585] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-599] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-564] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-618] for track '59' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_44'; source metadata written as null.

</details>