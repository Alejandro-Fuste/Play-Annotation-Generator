# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_12`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 62
- **Ball Tracks:** 0
- **Action Segments:** 220
- **Validation Warnings:** 273
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 206
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `39` | `35` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `39` | `35` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `39` | `35` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `0` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `1` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `2` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `4` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `7` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `8` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `5` | `5` | 58 | START | 58 | 111 |
| ✅ EXACT | `Action_KickBall` | Kicker | `5` | `5` | 112 | START | 112 | 113 |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | `39` | `35` | 213 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `39` | `35` | 239 | START | 239 | 240 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `39` | `35` | 561 | START | 561 | 569 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_KickApproach` | 58 | 111 | 54 | inferred_complete_timeline |
| `Action_KickBall` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 136 | 79 | inferred_complete_timeline |
| `Action_None` | 140 | 417 | 278 | inferred_complete_timeline |
| `Action_None` | 420 | 465 | 46 | inferred_complete_timeline |
| `Action_None` | 473 | 569 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 93 | 36 | inferred_complete_timeline |
| `Action_None` | 96 | 388 | 293 | inferred_complete_timeline |
| `Action_None` | 390 | 394 | 5 | inferred_complete_timeline |
| `Action_None` | 400 | 403 | 4 | inferred_complete_timeline |
| `Action_None` | 405 | 410 | 6 | inferred_complete_timeline |
| `Action_None` | 412 | 444 | 33 | inferred_complete_timeline |
| `Action_None` | 451 | 509 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 46 | 23 | inferred_complete_timeline |
| `Action_None` | 69 | 324 | 256 | inferred_complete_timeline |
| `Action_None` | 331 | 336 | 6 | inferred_complete_timeline |
| `Action_None` | 338 | 477 | 140 | inferred_complete_timeline |
| `Action_None` | 479 | 569 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 301 | 244 | inferred_complete_timeline |
| `Action_None` | 349 | 372 | 24 | inferred_complete_timeline |
| `Action_None` | 378 | 388 | 11 | inferred_complete_timeline |
| `Action_None` | 395 | 406 | 12 | inferred_complete_timeline |
| `Action_None` | 409 | 569 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–496
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_None` | 72 | 141 | 70 | inferred_complete_timeline |
| `Action_None` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 199 | 39 | inferred_complete_timeline |
| `Action_None` | 202 | 335 | 134 | inferred_complete_timeline |
| `Action_None` | 341 | 402 | 62 | inferred_complete_timeline |
| `Action_None` | 405 | 407 | 3 | inferred_complete_timeline |
| `Action_None` | 409 | 496 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 72 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 134 | 77 | inferred_complete_timeline |
| `Action_None` | 136 | 327 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 108 | 51 | inferred_complete_timeline |
| `Action_None` | 110 | 426 | 317 | inferred_complete_timeline |
| `Action_None` | 430 | 482 | 53 | inferred_complete_timeline |
| `Action_None` | 485 | 569 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 57 | 52 | inferred_complete_timeline |
| `Action_None` | 58 | 71 | 14 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 107 | 12 | inferred_complete_timeline |
| `Action_None` | 110 | 117 | 8 | inferred_complete_timeline |
| `Action_None` | 120 | 135 | 16 | inferred_complete_timeline |
| `Action_None` | 139 | 277 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 273 | 216 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |
| `Action_None` | 289 | 314 | 26 | inferred_complete_timeline |
| `Action_None` | 317 | 403 | 87 | inferred_complete_timeline |
| `Action_None` | 406 | 482 | 77 | inferred_complete_timeline |
| `Action_None` | 485 | 569 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 114 | 57 | inferred_complete_timeline |
| `Action_None` | 116 | 191 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 266 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 247 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 272 | 215 | inferred_complete_timeline |
| `Action_None` | 310 | 352 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–463
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 164 | 107 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 173 | 191 | 19 | inferred_complete_timeline |
| `Action_None` | 194 | 248 | 55 | inferred_complete_timeline |
| `Action_None` | 254 | 374 | 121 | inferred_complete_timeline |
| `Action_None` | 458 | 463 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 290 | 233 | inferred_complete_timeline |
| `Action_None` | 292 | 305 | 14 | inferred_complete_timeline |
| `Action_None` | 311 | 317 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 203 | 146 | inferred_complete_timeline |
| `Action_None` | 205 | 250 | 46 | inferred_complete_timeline |
| `Action_None` | 253 | 432 | 180 | inferred_complete_timeline |
| `Action_None` | 437 | 569 | 133 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–569 | 495 | 4 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–230 | 158 | 14 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–135 | 86 | 7 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 2–569 | 486 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 2–569 | 505 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 60–64 | 5 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 83–319 | 224 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 94–168 | 24 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 129–418 | 284 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 151–153 | 3 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 157–191 | 30 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 166–276 | 61 | 7 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 181–183 | 3 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 184–196 | 11 | 2 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 192–569 | 374 | 3 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 192–569 | 333 | 8 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 194–209 | 16 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 194–203 | 10 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 228–236 | 9 | 1 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 272–273 | 2 | 1 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 285–569 | 276 | 3 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 300–310 | 11 | 1 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 305–334 | 21 | 2 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 329–338 | 10 | 1 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 331–569 | 237 | 3 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 337–569 | 212 | 7 | Undefined position; Undefined team |
| `46` | `57` | Position_Unknown | Team_Unknown | 351–352 | 2 | 1 | Undefined position; Undefined team |
| `47` | `59` | Position_Unknown | Team_Unknown | 355–446 | 25 | 6 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 357–490 | 128 | 2 | Undefined position; Undefined team |
| `49` | `63` | Position_Unknown | Team_Unknown | 367–386 | 8 | 3 | Undefined position; Undefined team |
| `50` | `64` | Position_Unknown | Team_Unknown | 376–569 | 193 | 2 | Undefined position; Undefined team |
| `51` | `65` | Position_Unknown | Team_Unknown | 385–569 | 178 | 2 | Undefined position; Undefined team |
| `52` | `66` | Position_Unknown | Team_Unknown | 393–398 | 6 | 1 | Undefined position; Undefined team |
| `53` | `67` | Position_Unknown | Team_Unknown | 396–421 | 25 | 2 | Undefined position; Undefined team |
| `54` | `68` | Position_Unknown | Team_Unknown | 443–569 | 127 | 1 | Undefined position; Undefined team |
| `55` | `69` | Position_Unknown | Team_Unknown | 444–491 | 19 | 4 | Undefined position; Undefined team |
| `56` | `71` | Position_Unknown | Team_Unknown | 458–563 | 101 | 3 | Undefined position; Undefined team |
| `57` | `73` | Position_Unknown | Team_Unknown | 461–569 | 109 | 1 | Undefined position; Undefined team |
| `58` | `74` | Position_Unknown | Team_Unknown | 494–569 | 76 | 1 | Undefined position; Undefined team |
| `59` | `75` | Position_Unknown | Team_Unknown | 498–569 | 72 | 1 | Undefined position; Undefined team |
| `60` | `78` | Position_Unknown | Team_Unknown | 528–569 | 38 | 2 | Undefined position; Undefined team |
| `61` | `79` | Position_Unknown | Team_Unknown | 534–540 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CatchKick` on target `39` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `39` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ 44 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 44 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 88 |
| Missing visible bounding boxes during action | 183 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 26: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_None' range [58-72] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-69] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-141] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-199] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-335] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-402] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-407] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-496] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-417] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-465] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-426] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-482] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-327] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [112-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-273] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-314] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-403] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-482] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-93] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-388] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-394] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-403] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-410] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-444] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-509] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-301] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-372] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-388] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-406] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-247] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-164] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-374] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-463] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-266] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-290] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-305] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-317] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-272] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-352] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-203] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-250] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-432] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-114] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-282] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-433] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-119] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-137] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-324] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-336] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-477] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-37] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-52] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-135] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-135] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-277] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-289] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-531] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-557] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-569] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-8] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-18] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-57] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-311] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-214] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-319] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-105] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-409] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-418] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-191] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-188] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-231] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-191] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-370] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-471] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-197] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [239-240] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [242-243] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [245-300] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-209] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-203] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-236] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-419] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-470] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-569] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-310] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-323] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-338] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-380] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-566] for track '44' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-385] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-403] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-419] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-457] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-369] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-382] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-390] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-442] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-383] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-490] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-458] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-518] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-569] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-398] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-421] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-455] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-463] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-519] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-559] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-563] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-569] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-533] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>