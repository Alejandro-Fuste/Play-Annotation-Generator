# Play-Annotation-Generator Annotation Review — SplitZone_133

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_133`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 68
- **Ball Tracks:** 0
- **Action Segments:** 312
- **Validation Warnings:** 371
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 290
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_BlockSecondLevel` | TE2 | offense | `19` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 12 | START | 13 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 12 | START | 13 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 12 | START | 13 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 12 | START | 13 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 12 | START | 13 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 12 | START | 13 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 12 | START | 13 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 12 | START | 13 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 12 | START | 13 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 12 | START | 13 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 12 | START | 13 | 32 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 30 | START | 30 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `6` | `6` | 32 | START | 32 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 33 | START | 43 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 33 | START | 33 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `20` | 33 | START | 33 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 33 | START | 33 | 46 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 33 | START | 33 | 95 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `4` | 42 | END | 30 | 42 |
| ✅ EXACT | `Action_BlockSecondLevel` | TE2 | `19` | `19` | 43 | START | 43 | 103 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `4` | 57 | START | 57 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `16` | 64 | START | 64 | 102 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 103 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 13–103
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 30 | 42 | 13 | inferred_complete_timeline |
| `Action_None` | 43 | 56 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 57 | 63 | 7 | inferred_complete_timeline |
| `Action_None` | 64 | 87 | 24 | inferred_complete_timeline |
| `Action_None` | 99 | 103 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 13–479
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 63 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 64 | 102 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 402 | 297 | inferred_complete_timeline |
| `Action_BallCarry` | 406 | 479 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 13–479
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 206 | 177 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 242 | 32 | inferred_complete_timeline |
| `Action_None` | 245 | 385 | 141 | inferred_complete_timeline |
| `Action_None` | 388 | 389 | 2 | inferred_complete_timeline |
| `Action_None` | 391 | 400 | 10 | inferred_complete_timeline |
| `Action_None` | 405 | 418 | 14 | inferred_complete_timeline |
| `Action_None` | 422 | 426 | 5 | inferred_complete_timeline |
| `Action_None` | 443 | 449 | 7 | inferred_complete_timeline |
| `Action_None` | 451 | 479 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 13–471
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 312 | 283 | inferred_complete_timeline |
| `Action_None` | 329 | 340 | 12 | inferred_complete_timeline |
| `Action_None` | 343 | 365 | 23 | inferred_complete_timeline |
| `Action_None` | 367 | 372 | 6 | inferred_complete_timeline |
| `Action_None` | 374 | 383 | 10 | inferred_complete_timeline |
| `Action_None` | 387 | 398 | 12 | inferred_complete_timeline |
| `Action_None` | 405 | 416 | 12 | inferred_complete_timeline |
| `Action_None` | 419 | 427 | 9 | inferred_complete_timeline |
| `Action_None` | 432 | 433 | 2 | inferred_complete_timeline |
| `Action_None` | 437 | 463 | 27 | inferred_complete_timeline |
| `Action_None` | 470 | 471 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 13–96
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 31 | 19 | inferred_complete_timeline |
| `Action_SplitBlock` | 32 | 88 | 57 | inferred_complete_timeline |
| `Action_SplitBlock` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 95 | 96 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 13–435
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 42 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 43 | 103 | 61 | inferred_complete_timeline |
| `Action_None` | 104 | 135 | 32 | inferred_complete_timeline |
| `Action_None` | 142 | 222 | 81 | inferred_complete_timeline |
| `Action_None` | 226 | 296 | 71 | inferred_complete_timeline |
| `Action_None` | 303 | 306 | 4 | inferred_complete_timeline |
| `Action_None` | 310 | 399 | 90 | inferred_complete_timeline |
| `Action_None` | 403 | 416 | 14 | inferred_complete_timeline |
| `Action_None` | 420 | 427 | 8 | inferred_complete_timeline |
| `Action_None` | 433 | 435 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–111
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 32 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 95 | 63 | inferred_complete_timeline |
| `Action_None` | 105 | 111 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 13–479
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 32 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 82 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 103 | 18 | inferred_complete_timeline |
| `Action_None` | 104 | 130 | 27 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 144 | 157 | 14 | inferred_complete_timeline |
| `Action_None` | 161 | 229 | 69 | inferred_complete_timeline |
| `Action_None` | 233 | 235 | 3 | inferred_complete_timeline |
| `Action_None` | 252 | 258 | 7 | inferred_complete_timeline |
| `Action_None` | 263 | 297 | 35 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |
| `Action_None` | 302 | 309 | 8 | inferred_complete_timeline |
| `Action_None` | 311 | 395 | 85 | inferred_complete_timeline |
| `Action_None` | 401 | 405 | 5 | inferred_complete_timeline |
| `Action_None` | 407 | 479 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 13–228
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 30 | 42 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 72 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 93 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 103 | 6 | inferred_complete_timeline |
| `Action_None` | 104 | 137 | 34 | inferred_complete_timeline |
| `Action_None` | 142 | 152 | 11 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 219 | 59 | inferred_complete_timeline |
| `Action_None` | 221 | 225 | 5 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 13–479
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 32 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 46 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 103 | 50 | inferred_complete_timeline |
| `Action_None` | 104 | 318 | 215 | inferred_complete_timeline |
| `Action_None` | 320 | 326 | 7 | inferred_complete_timeline |
| `Action_None` | 362 | 363 | 2 | inferred_complete_timeline |
| `Action_None` | 365 | 369 | 5 | inferred_complete_timeline |
| `Action_None` | 375 | 403 | 29 | inferred_complete_timeline |
| `Action_None` | 406 | 408 | 3 | inferred_complete_timeline |
| `Action_None` | 412 | 479 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 13–479
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 32 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 52 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 70 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 78 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 103 | 15 | inferred_complete_timeline |
| `Action_None` | 104 | 181 | 78 | inferred_complete_timeline |
| `Action_None` | 183 | 212 | 30 | inferred_complete_timeline |
| `Action_None` | 214 | 228 | 15 | inferred_complete_timeline |
| `Action_None` | 230 | 278 | 49 | inferred_complete_timeline |
| `Action_None` | 285 | 363 | 79 | inferred_complete_timeline |
| `Action_None` | 365 | 369 | 5 | inferred_complete_timeline |
| `Action_None` | 372 | 377 | 6 | inferred_complete_timeline |
| `Action_None` | 380 | 385 | 6 | inferred_complete_timeline |
| `Action_None` | 388 | 417 | 30 | inferred_complete_timeline |
| `Action_None` | 421 | 426 | 6 | inferred_complete_timeline |
| `Action_None` | 435 | 479 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 13–240
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 76 | 47 | inferred_complete_timeline |
| `Action_None` | 120 | 129 | 10 | inferred_complete_timeline |
| `Action_None` | 141 | 155 | 15 | inferred_complete_timeline |
| `Action_None` | 163 | 230 | 68 | inferred_complete_timeline |
| `Action_None` | 232 | 236 | 5 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–479
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 81 | 52 | inferred_complete_timeline |
| `Action_None` | 86 | 210 | 125 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 220 | 4 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 280 | 9 | inferred_complete_timeline |
| `Action_None` | 282 | 479 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–479
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 479 | 450 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 13–225
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 60 | 31 | inferred_complete_timeline |
| `Action_None` | 65 | 84 | 20 | inferred_complete_timeline |
| `Action_None` | 87 | 98 | 12 | inferred_complete_timeline |
| `Action_None` | 100 | 105 | 6 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 137 | 21 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 155 | 7 | inferred_complete_timeline |
| `Action_None` | 161 | 220 | 60 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–397
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 103 | 74 | inferred_complete_timeline |
| `Action_None` | 108 | 118 | 11 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 166 | 6 | inferred_complete_timeline |
| `Action_None` | 170 | 397 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 13–479
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 278 | 249 | inferred_complete_timeline |
| `Action_None` | 283 | 306 | 24 | inferred_complete_timeline |
| `Action_None` | 309 | 312 | 4 | inferred_complete_timeline |
| `Action_None` | 315 | 333 | 19 | inferred_complete_timeline |
| `Action_None` | 335 | 365 | 31 | inferred_complete_timeline |
| `Action_None` | 367 | 379 | 13 | inferred_complete_timeline |
| `Action_None` | 386 | 397 | 12 | inferred_complete_timeline |
| `Action_None` | 401 | 414 | 14 | inferred_complete_timeline |
| `Action_None` | 422 | 423 | 2 | inferred_complete_timeline |
| `Action_None` | 439 | 445 | 7 | inferred_complete_timeline |
| `Action_None` | 448 | 451 | 4 | inferred_complete_timeline |
| `Action_None` | 456 | 457 | 2 | inferred_complete_timeline |
| `Action_None` | 469 | 472 | 4 | inferred_complete_timeline |
| `Action_None` | 475 | 479 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 13–101
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 101 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 13–203
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 184 | 155 | inferred_complete_timeline |
| `Action_None` | 187 | 203 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 13–437
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 259 | 230 | inferred_complete_timeline |
| `Action_None` | 263 | 285 | 23 | inferred_complete_timeline |
| `Action_None` | 287 | 308 | 22 | inferred_complete_timeline |
| `Action_None` | 310 | 372 | 63 | inferred_complete_timeline |
| `Action_None` | 384 | 414 | 31 | inferred_complete_timeline |
| `Action_None` | 417 | 418 | 2 | inferred_complete_timeline |
| `Action_None` | 420 | 427 | 8 | inferred_complete_timeline |
| `Action_None` | 431 | 437 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 13–479
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 235 | 206 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 479 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 13–477
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_None` | 30 | 170 | 141 | inferred_complete_timeline |
| `Action_None` | 180 | 183 | 4 | inferred_complete_timeline |
| `Action_None` | 186 | 203 | 18 | inferred_complete_timeline |
| `Action_None` | 208 | 297 | 90 | inferred_complete_timeline |
| `Action_None` | 309 | 357 | 49 | inferred_complete_timeline |
| `Action_None` | 359 | 373 | 15 | inferred_complete_timeline |
| `Action_None` | 376 | 381 | 6 | inferred_complete_timeline |
| `Action_None` | 384 | 388 | 5 | inferred_complete_timeline |
| `Action_None` | 393 | 394 | 2 | inferred_complete_timeline |
| `Action_None` | 407 | 413 | 7 | inferred_complete_timeline |
| `Action_None` | 421 | 425 | 5 | inferred_complete_timeline |
| `Action_None` | 427 | 432 | 6 | inferred_complete_timeline |
| `Action_None` | 435 | 440 | 6 | inferred_complete_timeline |
| `Action_None` | 443 | 457 | 15 | inferred_complete_timeline |
| `Action_None` | 461 | 477 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 71–479 | 403 | 3 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 108–479 | 362 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 142–464 | 299 | 5 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 162–479 | 244 | 10 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 240–243 | 4 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 258–479 | 210 | 5 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 274–479 | 204 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 275–479 | 202 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 290–479 | 169 | 8 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 346–434 | 5 | 2 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 361–456 | 72 | 4 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 366–396 | 26 | 3 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 366–373 | 8 | 1 | Undefined position; Undefined team |
| `35` | `60` | Position_Unknown | Team_Unknown | 378–380 | 3 | 1 | Undefined position; Undefined team |
| `36` | `64` | Position_Unknown | Team_Unknown | 385–442 | 54 | 3 | Undefined position; Undefined team |
| `37` | `66` | Position_Unknown | Team_Unknown | 386–479 | 56 | 7 | Undefined position; Undefined team |
| `38` | `67` | Position_Unknown | Team_Unknown | 387–436 | 45 | 3 | Undefined position; Undefined team |
| `39` | `68` | Position_Unknown | Team_Unknown | 388–392 | 5 | 1 | Undefined position; Undefined team |
| `40` | `69` | Position_Unknown | Team_Unknown | 391–392 | 2 | 1 | Undefined position; Undefined team |
| `41` | `71` | Position_Unknown | Team_Unknown | 402–424 | 16 | 4 | Undefined position; Undefined team |
| `42` | `72` | Position_Unknown | Team_Unknown | 403–406 | 4 | 1 | Undefined position; Undefined team |
| `43` | `74` | Position_Unknown | Team_Unknown | 403–410 | 7 | 2 | Undefined position; Undefined team |
| `44` | `75` | Position_Unknown | Team_Unknown | 406–440 | 19 | 3 | Undefined position; Undefined team |
| `45` | `76` | Position_Unknown | Team_Unknown | 408–479 | 54 | 6 | Undefined position; Undefined team |
| `46` | `80` | Position_Unknown | Team_Unknown | 410–416 | 5 | 2 | Undefined position; Undefined team |
| `47` | `85` | Position_Unknown | Team_Unknown | 422–479 | 45 | 4 | Undefined position; Undefined team |
| `48` | `87` | Position_Unknown | Team_Unknown | 424–479 | 38 | 6 | Undefined position; Undefined team |
| `49` | `88` | Position_Unknown | Team_Unknown | 424–425 | 2 | 1 | Undefined position; Undefined team |
| `50` | `90` | Position_Unknown | Team_Unknown | 433–443 | 10 | 2 | Undefined position; Undefined team |
| `51` | `95` | Position_Unknown | Team_Unknown | 441–446 | 6 | 1 | Undefined position; Undefined team |
| `52` | `96` | Position_Unknown | Team_Unknown | 441–445 | 5 | 1 | Undefined position; Undefined team |
| `53` | `97` | Position_Unknown | Team_Unknown | 441–468 | 15 | 3 | Undefined position; Undefined team |
| `54` | `101` | Position_Unknown | Team_Unknown | 452–479 | 27 | 2 | Undefined position; Undefined team |
| `55` | `102` | Position_Unknown | Team_Unknown | 454–455 | 2 | 1 | Undefined position; Undefined team |
| `56` | `104` | Position_Unknown | Team_Unknown | 454–455 | 2 | 1 | Undefined position; Undefined team |
| `57` | `108` | Position_Unknown | Team_Unknown | 458–459 | 2 | 1 | Undefined position; Undefined team |
| `58` | `110` | Position_Unknown | Team_Unknown | 460–461 | 2 | 1 | Undefined position; Undefined team |
| `59` | `113` | Position_Unknown | Team_Unknown | 466–467 | 2 | 1 | Undefined position; Undefined team |
| `60` | `114` | Position_Unknown | Team_Unknown | 466–479 | 7 | 3 | Undefined position; Undefined team |
| `61` | `115` | Position_Unknown | Team_Unknown | 467–468 | 2 | 1 | Undefined position; Undefined team |
| `62` | `118` | Position_Unknown | Team_Unknown | 470–479 | 8 | 2 | Undefined position; Undefined team |
| `63` | `119` | Position_Unknown | Team_Unknown | 471–479 | 8 | 2 | Undefined position; Undefined team |
| `64` | `121` | Position_Unknown | Team_Unknown | 474–477 | 4 | 1 | Undefined position; Undefined team |
| `65` | `122` | Position_Unknown | Team_Unknown | 476–479 | 4 | 1 | Undefined position; Undefined team |
| `66` | `123` | Position_Unknown | Team_Unknown | 476–479 | 4 | 1 | Undefined position; Undefined team |
| `67` | `124` | Position_Unknown | Team_Unknown | 477–479 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 46 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 46 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 92 |
| Missing visible bounding boxes during action | 277 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [30–42], lower_priority='Action_ZoneBlock' annotated_start=33, effective_Action_ZoneBlock_start=43.
- ⚠️ Action 'Action_None' range [30-206] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-385] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-400] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-418] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-426] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-449] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-479] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-312] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-340] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-365] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-372] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-383] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-398] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-416] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-427] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-463] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-118] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-166] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-397] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-479] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [32-88] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [90-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [95-96] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-95] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-184] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-98] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-105] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-137] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-220] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-235] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-479] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-76] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-230] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-280] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-479] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-278] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-306] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-333] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-365] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-379] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-397] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-414] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-423] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-445] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-451] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-472] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-152] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-219] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-203] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-297] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-357] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-373] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-381] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-413] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-425] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-432] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-440] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-457] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-477] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [64-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-402] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-103] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-130] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-229] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-258] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-297] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-309] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-395] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-405] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-479] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-285] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-308] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-372] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-414] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-418] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-427] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-437] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [43-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-296] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-399] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-416] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-427] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-435] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-212] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-278] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-363] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-369] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-377] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-385] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-417] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-426] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-479] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-46] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-318] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-326] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-369] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-403] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-479] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-255] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-479] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-122] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-412] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-446] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-240] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-281] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-297] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-317] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-381] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-271] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-299] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-401] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-479] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-305] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-479] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-285] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-417] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-479] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-312] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-327] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-356] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-479] for track '30' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-434] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-366] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-387] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-438] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-381] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-389] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-396] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-373] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-390] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-436] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-442] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-403] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-443] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-459] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-470] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-479] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-403] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-417] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-436] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-392] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-413] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-424] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-406] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-405] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-410] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-413] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-424] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-440] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-424] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-432] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-451] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-459] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-470] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-479] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-425] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-435] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-444] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-479] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-432] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-459] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-438] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-443] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-446] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-445] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-443] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-458] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-468] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-479] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-472] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-474] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-474] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-479] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-477] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-479] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-479] for track '67' has 1 frames without a visible bounding box.
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

</details>