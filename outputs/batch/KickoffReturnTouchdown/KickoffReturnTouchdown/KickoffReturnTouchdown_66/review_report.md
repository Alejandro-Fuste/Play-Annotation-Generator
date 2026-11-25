# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_66

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_66`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 162
- **Validation Warnings:** 186
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 146
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `0` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `10` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `12` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `14` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `16` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `2` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `3` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `4` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `6` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `8` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `8` | `8` | 24 | START | 24 | 87 |
| ✅ EXACT | `Action_KickBall` | Kicker | `8` | `8` | 88 | START | 88 | 92 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `21` | `21` | 200 | START | 200 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `21` | `21` | 224 | START | 224 | 400 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_KickApproach` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_KickBall` | 88 | 92 | 5 | inferred_complete_timeline |
| `Action_None` | 93 | 134 | 42 | inferred_complete_timeline |
| `Action_None` | 138 | 155 | 18 | inferred_complete_timeline |
| `Action_None` | 158 | 168 | 11 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 188 | 15 | inferred_complete_timeline |
| `Action_None` | 190 | 599 | 410 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–564
- **Visible Samples:** 528

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 263 | 240 | inferred_complete_timeline |
| `Action_None` | 265 | 271 | 7 | inferred_complete_timeline |
| `Action_None` | 273 | 510 | 238 | inferred_complete_timeline |
| `Action_None` | 546 | 564 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–505
- **Visible Samples:** 487

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 240 | 217 | inferred_complete_timeline |
| `Action_None` | 259 | 424 | 166 | inferred_complete_timeline |
| `Action_None` | 426 | 505 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 141 | 118 | inferred_complete_timeline |
| `Action_None` | 148 | 278 | 131 | inferred_complete_timeline |
| `Action_None` | 284 | 288 | 5 | inferred_complete_timeline |
| `Action_None` | 291 | 294 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–560
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 23 | 4 | inferred_complete_timeline |
| `Action_None` | 24 | 302 | 279 | inferred_complete_timeline |
| `Action_None` | 307 | 560 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 136 | 113 | inferred_complete_timeline |
| `Action_None` | 143 | 599 | 457 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 142 | 119 | inferred_complete_timeline |
| `Action_None` | 149 | 155 | 7 | inferred_complete_timeline |
| `Action_None` | 162 | 387 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 143 | 120 | inferred_complete_timeline |
| `Action_None` | 145 | 153 | 9 | inferred_complete_timeline |
| `Action_None` | 159 | 309 | 151 | inferred_complete_timeline |
| `Action_None` | 315 | 316 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 599 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–458
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 273 | 250 | inferred_complete_timeline |
| `Action_None` | 278 | 303 | 26 | inferred_complete_timeline |
| `Action_None` | 305 | 380 | 76 | inferred_complete_timeline |
| `Action_None` | 382 | 384 | 3 | inferred_complete_timeline |
| `Action_None` | 395 | 450 | 56 | inferred_complete_timeline |
| `Action_None` | 452 | 458 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 322 | 299 | inferred_complete_timeline |
| `Action_None` | 325 | 326 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–597
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 356 | 333 | inferred_complete_timeline |
| `Action_None` | 361 | 597 | 237 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 259 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–513
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 303 | 280 | inferred_complete_timeline |
| `Action_None` | 306 | 307 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_None` | 325 | 335 | 11 | inferred_complete_timeline |
| `Action_None` | 339 | 378 | 40 | inferred_complete_timeline |
| `Action_None` | 383 | 513 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 113 | 90 | inferred_complete_timeline |
| `Action_None` | 115 | 135 | 21 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 214 | 75 | inferred_complete_timeline |
| `Action_None` | 219 | 599 | 381 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–505
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 122 | 99 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 277 | 131 | inferred_complete_timeline |
| `Action_None` | 286 | 355 | 70 | inferred_complete_timeline |
| `Action_None` | 359 | 505 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–528
- **Visible Samples:** 529

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 528 | 505 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 577

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 159 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 199 | 36 | inferred_complete_timeline |
| `Action_CatchKick` | 200 | 207 | 8 | inferred_complete_timeline |
| `Action_None` | 208 | 223 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 224 | 400 | 177 | inferred_complete_timeline |
| `Action_BallCarry` | 402 | 599 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–560
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 204 | 181 | inferred_complete_timeline |
| `Action_None` | 206 | 213 | 8 | inferred_complete_timeline |
| `Action_None` | 221 | 283 | 63 | inferred_complete_timeline |
| `Action_None` | 285 | 560 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–588
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 509 | 486 | inferred_complete_timeline |
| `Action_None` | 512 | 588 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 275 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–573
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 323 | 300 | inferred_complete_timeline |
| `Action_None` | 326 | 573 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–310
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 274 | 251 | inferred_complete_timeline |
| `Action_None` | 280 | 310 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 6–66 | 5 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 9–90 | 25 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 140–152 | 13 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 275–276 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 280–364 | 53 | 8 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 281–467 | 187 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 302–519 | 218 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 330–589 | 253 | 6 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 340–361 | 22 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 386–542 | 157 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 398–584 | 187 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 423–486 | 40 | 6 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 438–474 | 14 | 4 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 463–599 | 137 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 507–534 | 7 | 2 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 511–581 | 66 | 4 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 523–524 | 2 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 526–527 | 2 | 1 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 528–563 | 31 | 5 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 542–543 | 2 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 542–575 | 29 | 3 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 557–563 | 7 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 560–566 | 6 | 2 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 574–575 | 2 | 1 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 585–591 | 6 | 2 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 593–594 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 68, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '610,615,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 132 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [24-263] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-271] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-510] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-564] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-303] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-335] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-378] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-513] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-142] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-387] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-141] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-278] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-136] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-599] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-323] for track '5' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-573] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-322] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-509] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-588] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-168] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-188] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-240] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-424] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-505] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-273] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-303] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-380] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-450] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-458] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-259] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-356] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-597] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-275] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-309] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-528] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-302] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-560] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-277] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-355] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-505] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-283] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-560] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-135] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-214] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-274] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-310] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [224-400] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-8] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-19] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-292] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-314] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-343] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-364] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-467] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-519] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-338] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-360] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-369] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-589] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-361] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-542] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-584] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-426] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-434] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-458] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-481] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-450] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-511] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-513] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-517] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-547] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-581] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-531] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-540] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-546] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-563] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-543] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-548] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-554] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-575] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-563] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-563] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-566] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-575] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-591] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-594] for track '47' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_66'; source metadata written as null.

</details>