# Play-Annotation-Generator Annotation Review — Counter_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_19`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 154
- **Validation Warnings:** 160
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `25` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `25` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 258 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `25` | `Group` | 0 | START | 27 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `15` | `14` | 248 | START | 248 | 259 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `17` | `16` | 258 | START | 258 | 296 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `19` | `18` | 258 | START | 258 | 268 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `25` | `22` | 259 | START | 259 | 286 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `11` | `10` | 259 | START | 259 | 291 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 264 | END | 248 | 264 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 274 | START | 274 | 299 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `12` | `11` | 300 | START | 300 | 449 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 349 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–432
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_SnapReceive` | 248 | 264 | 17 | inferred_complete_timeline |
| `Action_None` | 265 | 273 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 274 | 299 | 26 | inferred_complete_timeline |
| `Action_None` | 300 | 414 | 115 | inferred_complete_timeline |
| `Action_None` | 426 | 429 | 4 | inferred_complete_timeline |
| `Action_None` | 431 | 432 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 449 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 362 | 115 | inferred_complete_timeline |
| `Action_None` | 364 | 367 | 4 | inferred_complete_timeline |
| `Action_None` | 369 | 449 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–334
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 323 | 76 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |
| `Action_None` | 332 | 334 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 259 | 291 | 33 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 307 | 309 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 315 | 319 | 5 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 327 | 349 | 23 | inferred_complete_timeline |
| `Action_None` | 350 | 449 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–371
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 257 | 238 | inferred_complete_timeline |
| `Action_DownBlock` | 258 | 296 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 300 | 309 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 311 | 349 | 39 | inferred_complete_timeline |
| `Action_None` | 350 | 358 | 9 | inferred_complete_timeline |
| `Action_None` | 361 | 366 | 6 | inferred_complete_timeline |
| `Action_None` | 369 | 371 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 106 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 257 | 145 | inferred_complete_timeline |
| `Action_DownBlock` | 258 | 268 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 278 | 280 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 283 | 317 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 320 | 332 | 13 | inferred_complete_timeline |
| `Action_None` | 351 | 369 | 19 | inferred_complete_timeline |
| `Action_None` | 374 | 449 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_BallSnap` | 248 | 259 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |
| `Action_None` | 271 | 365 | 95 | inferred_complete_timeline |
| `Action_None` | 371 | 449 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `25`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 27–449
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 41 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 258 | 216 | inferred_complete_timeline |
| `Action_PullBlock` | 259 | 286 | 28 | inferred_complete_timeline |
| `Action_PullBlock` | 289 | 332 | 44 | inferred_complete_timeline |
| `Action_PullBlock` | 334 | 349 | 16 | inferred_complete_timeline |
| `Action_None` | 350 | 352 | 3 | inferred_complete_timeline |
| `Action_None` | 355 | 449 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 34 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 247 | 209 | inferred_complete_timeline |
| `Action_None` | 248 | 271 | 24 | inferred_complete_timeline |
| `Action_None` | 287 | 293 | 7 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_None` | 351 | 358 | 8 | inferred_complete_timeline |
| `Action_None` | 366 | 449 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 323 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 449 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 288 | 41 | inferred_complete_timeline |
| `Action_None` | 292 | 304 | 13 | inferred_complete_timeline |
| `Action_None` | 309 | 403 | 95 | inferred_complete_timeline |
| `Action_None` | 406 | 449 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `24`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 16–363
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 247 | 232 | inferred_complete_timeline |
| `Action_None` | 248 | 306 | 59 | inferred_complete_timeline |
| `Action_None` | 309 | 319 | 11 | inferred_complete_timeline |
| `Action_None` | 330 | 359 | 30 | inferred_complete_timeline |
| `Action_None` | 361 | 363 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 300 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 449 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–447
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 447 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 449 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 393 | 146 | inferred_complete_timeline |
| `Action_None` | 395 | 449 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–347
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 313 | 66 | inferred_complete_timeline |
| `Action_None` | 317 | 323 | 7 | inferred_complete_timeline |
| `Action_None` | 334 | 347 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_None` | 248 | 435 | 188 | inferred_complete_timeline |
| `Action_None` | 437 | 449 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–449 | 388 | 7 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 16–129 | 99 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 89–91 | 3 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 91–95 | 5 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 180–365 | 108 | 5 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 229–268 | 35 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 251–268 | 18 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 281–331 | 18 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 296–346 | 48 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 318–449 | 130 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 328–449 | 110 | 3 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 334–437 | 104 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 347–449 | 94 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 348–449 | 84 | 4 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 395–438 | 23 | 5 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 397–404 | 4 | 2 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 397–449 | 27 | 5 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 404–405 | 2 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 413–417 | 5 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 444–447 | 4 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 444–449 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `25` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 112 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '16' (LT) duration 92 frames exceeds threshold 90 frames [start=258, end=349].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (LG) duration 92 frames exceeds threshold 90 frames [start=258, end=349].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '22' (RG) duration 91 frames exceeds threshold 90 frames [start=259, end=349].
- ⚠️ Action 'Action_None' range [248-323] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-447] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-323] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-300] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-313] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-323] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-347] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-435] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-449] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-393] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-362] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-367] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-449] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [259-291] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [307-309] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [315-319] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-288] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-288] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-304] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-403] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-449] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [248-259] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-365] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-271] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-293] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-358] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-449] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [258-296] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [300-309] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-358] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-366] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-371] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-414] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-429] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [258-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [273-275] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [278-280] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [283-317] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [320-332] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-369] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-449] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-36] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-129] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-306] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-319] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-41] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [259-286] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [289-332] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-95] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-247] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-263] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-277] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-351] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-247] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '26' starts at frame 248, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [248-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-261] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-268] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-309] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-300] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-346] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-363] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-343] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-361] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-437] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-376] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-431] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-398] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-407] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-438] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-401] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-422] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-417] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-447] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-449] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>