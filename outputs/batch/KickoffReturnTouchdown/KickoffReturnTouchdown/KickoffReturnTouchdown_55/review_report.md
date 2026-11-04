# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_55`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 213
- **Validation Warnings:** 255
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 198
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `32` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `32` | `23` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `32` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `10` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `11` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `12` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `13` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `14` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `15` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `2` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `4` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `7` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `8` | `Group` | 0 | START | 0 | 114 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `7` | `7` | 115 | START | 115 | 173 |
| ✅ EXACT | `Action_KickBall` | Kicker | `7` | `7` | 174 | START | 174 | 179 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `32` | `23` | 283 | START | 283 | 290 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `32` | `23` | 310 | START | 310 | 432 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `32` | `23` | 619 | START | 619 | 629 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_KickApproach` | 115 | 173 | 59 | inferred_complete_timeline |
| `Action_KickBall` | 174 | 179 | 6 | inferred_complete_timeline |
| `Action_None` | 180 | 443 | 264 | inferred_complete_timeline |
| `Action_None` | 445 | 494 | 50 | inferred_complete_timeline |
| `Action_None` | 496 | 535 | 40 | inferred_complete_timeline |
| `Action_None` | 538 | 539 | 2 | inferred_complete_timeline |
| `Action_None` | 541 | 543 | 3 | inferred_complete_timeline |
| `Action_None` | 548 | 549 | 2 | inferred_complete_timeline |
| `Action_None` | 555 | 557 | 3 | inferred_complete_timeline |
| `Action_None` | 563 | 565 | 3 | inferred_complete_timeline |
| `Action_None` | 572 | 573 | 2 | inferred_complete_timeline |
| `Action_None` | 575 | 587 | 13 | inferred_complete_timeline |
| `Action_None` | 589 | 614 | 26 | inferred_complete_timeline |
| `Action_None` | 621 | 629 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 615

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 200 | 86 | inferred_complete_timeline |
| `Action_None` | 203 | 340 | 138 | inferred_complete_timeline |
| `Action_None` | 342 | 348 | 7 | inferred_complete_timeline |
| `Action_None` | 354 | 616 | 263 | inferred_complete_timeline |
| `Action_None` | 624 | 629 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 164 | 50 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 163 | 49 | inferred_complete_timeline |
| `Action_None` | 165 | 170 | 6 | inferred_complete_timeline |
| `Action_None` | 172 | 178 | 7 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 208 | 5 | inferred_complete_timeline |
| `Action_None` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 349 | 135 | inferred_complete_timeline |
| `Action_None` | 351 | 602 | 252 | inferred_complete_timeline |
| `Action_None` | 606 | 607 | 2 | inferred_complete_timeline |
| `Action_None` | 609 | 612 | 4 | inferred_complete_timeline |
| `Action_None` | 614 | 629 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–369
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 181 | 67 | inferred_complete_timeline |
| `Action_None` | 186 | 189 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 312 | 109 | inferred_complete_timeline |
| `Action_None` | 347 | 349 | 3 | inferred_complete_timeline |
| `Action_None` | 351 | 369 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 180 | 66 | inferred_complete_timeline |
| `Action_None` | 182 | 297 | 116 | inferred_complete_timeline |
| `Action_None` | 311 | 629 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–435
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 152 | 38 | inferred_complete_timeline |
| `Action_None` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_None` | 161 | 179 | 19 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 213 | 10 | inferred_complete_timeline |
| `Action_None` | 216 | 336 | 121 | inferred_complete_timeline |
| `Action_None` | 345 | 354 | 10 | inferred_complete_timeline |
| `Action_None` | 368 | 435 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 148 | 34 | inferred_complete_timeline |
| `Action_None` | 151 | 179 | 29 | inferred_complete_timeline |
| `Action_None` | 184 | 187 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 164 | 50 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 179 | 65 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_None` | 206 | 212 | 7 | inferred_complete_timeline |
| `Action_None` | 219 | 226 | 8 | inferred_complete_timeline |
| `Action_None` | 228 | 258 | 31 | inferred_complete_timeline |
| `Action_None` | 260 | 280 | 21 | inferred_complete_timeline |
| `Action_None` | 282 | 289 | 8 | inferred_complete_timeline |
| `Action_None` | 292 | 310 | 19 | inferred_complete_timeline |
| `Action_None` | 312 | 336 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–597
- **Visible Samples:** 555

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 315 | 201 | inferred_complete_timeline |
| `Action_None` | 334 | 335 | 2 | inferred_complete_timeline |
| `Action_None` | 360 | 361 | 2 | inferred_complete_timeline |
| `Action_None` | 363 | 597 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 621

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 320 | 206 | inferred_complete_timeline |
| `Action_None` | 323 | 435 | 113 | inferred_complete_timeline |
| `Action_None` | 438 | 440 | 3 | inferred_complete_timeline |
| `Action_None` | 445 | 619 | 175 | inferred_complete_timeline |
| `Action_None` | 621 | 629 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 283 | 169 | inferred_complete_timeline |
| `Action_None` | 285 | 291 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–410
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 365 | 251 | inferred_complete_timeline |
| `Action_None` | 370 | 371 | 2 | inferred_complete_timeline |
| `Action_None` | 383 | 385 | 3 | inferred_complete_timeline |
| `Action_None` | 387 | 403 | 17 | inferred_complete_timeline |
| `Action_None` | 406 | 410 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_None` | 115 | 458 | 344 | inferred_complete_timeline |
| `Action_None` | 462 | 494 | 33 | inferred_complete_timeline |
| `Action_None` | 496 | 497 | 2 | inferred_complete_timeline |
| `Action_None` | 503 | 515 | 13 | inferred_complete_timeline |
| `Action_None` | 518 | 554 | 37 | inferred_complete_timeline |
| `Action_None` | 558 | 629 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–629 | 595 | 7 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 8–165 | 140 | 7 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 189–353 | 141 | 5 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 207–545 | 338 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 207–496 | 280 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 208–562 | 351 | 3 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 220–222 | 3 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 231–236 | 5 | 2 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 237–629 | 369 | 15 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 239–240 | 2 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 241–242 | 2 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 242–244 | 3 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 245–629 | 373 | 7 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 253–254 | 2 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 257–352 | 95 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 257–629 | 353 | 6 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 264–629 | 360 | 4 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 303–314 | 11 | 2 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 325–629 | 303 | 2 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 329–389 | 30 | 4 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 366–629 | 264 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 368–371 | 4 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 377–629 | 232 | 8 | Undefined position; Undefined team |
| `38` | `61` | Position_Unknown | Team_Unknown | 398–399 | 2 | 1 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 398–404 | 7 | 1 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 400–401 | 2 | 1 | Undefined position; Undefined team |
| `41` | `67` | Position_Unknown | Team_Unknown | 416–607 | 191 | 2 | Undefined position; Undefined team |
| `42` | `68` | Position_Unknown | Team_Unknown | 419–629 | 208 | 3 | Undefined position; Undefined team |
| `43` | `71` | Position_Unknown | Team_Unknown | 431–616 | 184 | 3 | Undefined position; Undefined team |
| `44` | `73` | Position_Unknown | Team_Unknown | 470–472 | 3 | 1 | Undefined position; Undefined team |
| `45` | `75` | Position_Unknown | Team_Unknown | 502–510 | 9 | 1 | Undefined position; Undefined team |
| `46` | `76` | Position_Unknown | Team_Unknown | 510–629 | 117 | 3 | Undefined position; Undefined team |
| `47` | `77` | Position_Unknown | Team_Unknown | 537–538 | 2 | 1 | Undefined position; Undefined team |
| `48` | `80` | Position_Unknown | Team_Unknown | 561–563 | 3 | 1 | Undefined position; Undefined team |
| `49` | `81` | Position_Unknown | Team_Unknown | 579–629 | 21 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `32` (11 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ 35 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 35 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 70 |
| Missing visible bounding boxes during action | 184 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_None' range [115-458] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-494] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-515] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-554] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-629] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-270] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-281] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-320] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-354] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-629] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-200] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-340] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-348] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-616] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-320] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-435] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-440] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-619] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-297] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-629] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-283] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-365] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-385] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-403] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-410] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-443] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-494] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-535] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-543] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-549] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-557] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-565] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-573] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-587] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-614] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-181] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-312] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-369] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-315] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-597] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-179] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-258] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-280] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-289] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-310] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-336] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-164] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-163] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-349] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-602] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-607] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-612] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-179] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-336] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-354] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-435] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-148] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-179] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-315] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-353] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-508] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-545] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-435] for track '19' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-477] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-496] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-521] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-554] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-562] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [310-432] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [434-462] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [464-474] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [477-487] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [489-498] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [505-508] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [513-514] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [518-521] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [525-529] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [531-540] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [543-618] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [619-629] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-361] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-411] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-516] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-524] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-584] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-629] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-337] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-352] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-363] for track '30' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-453] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-477] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-629] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-309] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-555] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-562] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-314] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-336] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-629] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-352] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-389] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-629] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-501] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-508] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-537] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-560] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-570] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-573] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-586] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-629] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-404] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-435] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-607] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-517] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-524] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-629] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-543] for track '43' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-569] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-616] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-472] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-510] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-513] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-594] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-538] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-563] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-583] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-616] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-627] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>