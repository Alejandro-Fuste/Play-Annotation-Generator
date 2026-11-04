# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_21`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 233
- **Validation Warnings:** 283
- **Validation Errors:** 0
- **Overall Status:** WARNING

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
- **Inferred Coverage Segments (Action_None):** 217
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `13` | `13` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `13` | `13` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `31` | `28` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `31` | `28` |
| ✅ EXACT | `Action_CrossGoalLine` | Front_Blocker3 | defense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `0` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `10` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `11` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `12` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `13` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `14` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `15` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `16` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `3` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `7` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `8` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `13` | `13` | 49 | START | 49 | 91 |
| ✅ EXACT | `Action_KickBall` | Kicker | `13` | `13` | 92 | START | 92 | 96 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `31` | `28` | 203 | START | 203 | 207 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `31` | `28` | 227 | START | 227 | 333 |
| ✅ EXACT | `Action_CrossGoalLine` | Front_Blocker3 | `9` | `9` | 588 | START | 588 | 599 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_KickApproach` | 49 | 91 | 43 | inferred_complete_timeline |
| `Action_KickBall` | 92 | 96 | 5 | inferred_complete_timeline |
| `Action_None` | 97 | 392 | 296 | inferred_complete_timeline |
| `Action_None` | 394 | 599 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 284 | 236 | inferred_complete_timeline |
| `Action_None` | 289 | 353 | 65 | inferred_complete_timeline |
| `Action_None` | 356 | 382 | 27 | inferred_complete_timeline |
| `Action_None` | 406 | 595 | 190 | inferred_complete_timeline |
| `Action_None` | 599 | 599 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 60 | 93 | 34 | inferred_complete_timeline |
| `Action_None` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 115 | 6 | inferred_complete_timeline |
| `Action_None` | 120 | 599 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 595 | 547 | inferred_complete_timeline |
| `Action_None` | 597 | 599 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 583

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 375 | 327 | inferred_complete_timeline |
| `Action_None` | 380 | 411 | 32 | inferred_complete_timeline |
| `Action_None` | 413 | 434 | 22 | inferred_complete_timeline |
| `Action_None` | 437 | 438 | 2 | inferred_complete_timeline |
| `Action_None` | 444 | 451 | 8 | inferred_complete_timeline |
| `Action_None` | 457 | 599 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 144 | 96 | inferred_complete_timeline |
| `Action_None` | 146 | 154 | 9 | inferred_complete_timeline |
| `Action_None` | 156 | 212 | 57 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 227 | 179 | inferred_complete_timeline |
| `Action_None` | 245 | 250 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 173 | 125 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |
| `Action_None` | 184 | 193 | 10 | inferred_complete_timeline |
| `Action_None` | 196 | 223 | 28 | inferred_complete_timeline |
| `Action_None` | 225 | 260 | 36 | inferred_complete_timeline |
| `Action_None` | 283 | 289 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 232 | 184 | inferred_complete_timeline |
| `Action_None` | 237 | 263 | 27 | inferred_complete_timeline |
| `Action_None` | 267 | 406 | 140 | inferred_complete_timeline |
| `Action_None` | 409 | 599 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 97 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 575

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 216 | 168 | inferred_complete_timeline |
| `Action_None` | 221 | 332 | 112 | inferred_complete_timeline |
| `Action_None` | 336 | 361 | 26 | inferred_complete_timeline |
| `Action_None` | 372 | 401 | 30 | inferred_complete_timeline |
| `Action_None` | 403 | 497 | 95 | inferred_complete_timeline |
| `Action_None` | 499 | 500 | 2 | inferred_complete_timeline |
| `Action_None` | 502 | 507 | 6 | inferred_complete_timeline |
| `Action_None` | 509 | 573 | 65 | inferred_complete_timeline |
| `Action_None` | 575 | 582 | 8 | inferred_complete_timeline |
| `Action_None` | 586 | 599 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 226 | 178 | inferred_complete_timeline |
| `Action_None` | 228 | 237 | 10 | inferred_complete_timeline |
| `Action_None` | 246 | 599 | 354 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 252 | 204 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 587 | 588 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 588 | 599 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 131 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–593
- **Visible Samples:** 582

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 220 | 172 | inferred_complete_timeline |
| `Action_None` | 224 | 411 | 188 | inferred_complete_timeline |
| `Action_None` | 413 | 425 | 13 | inferred_complete_timeline |
| `Action_None` | 427 | 452 | 26 | inferred_complete_timeline |
| `Action_None` | 458 | 519 | 62 | inferred_complete_timeline |
| `Action_None` | 521 | 577 | 57 | inferred_complete_timeline |
| `Action_None` | 579 | 593 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 306 | 258 | inferred_complete_timeline |
| `Action_None` | 311 | 315 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 99–152 | 26 | 7 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 100–101 | 2 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 101–278 | 161 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 116–118 | 3 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 122–123 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 123–599 | 460 | 7 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 128–599 | 472 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 129–510 | 376 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 130–599 | 459 | 5 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 155–599 | 443 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 159–333 | 175 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 231–402 | 168 | 4 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 259–362 | 90 | 4 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 263–265 | 3 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 264–266 | 3 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 269–325 | 55 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 270–599 | 283 | 13 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 276–277 | 2 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 306–599 | 292 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 319–599 | 278 | 3 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 331–335 | 5 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 344–599 | 248 | 8 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 355–356 | 2 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 356–357 | 2 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 357–599 | 235 | 3 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 366–382 | 12 | 2 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 389–509 | 87 | 10 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 398–599 | 202 | 1 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 403–404 | 2 | 1 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 408–599 | 76 | 20 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 420–421 | 2 | 1 | Undefined position; Undefined team |
| `49` | `68` | Position_Unknown | Team_Unknown | 423–599 | 168 | 8 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 423–424 | 2 | 1 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 434–599 | 152 | 5 | Undefined position; Undefined team |
| `52` | `72` | Position_Unknown | Team_Unknown | 435–579 | 70 | 14 | Undefined position; Undefined team |
| `53` | `73` | Position_Unknown | Team_Unknown | 435–442 | 8 | 1 | Undefined position; Undefined team |
| `54` | `82` | Position_Unknown | Team_Unknown | 525–592 | 61 | 4 | Undefined position; Undefined team |
| `55` | `83` | Position_Unknown | Team_Unknown | 537–538 | 2 | 1 | Undefined position; Undefined team |
| `56` | `85` | Position_Unknown | Team_Unknown | 558–559 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 202 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [49-216] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-332] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-361] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-401] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-497] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-507] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-573] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-582] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-131] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-252] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-144] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-154] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-226] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-599] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-411] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-425] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-452] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-519] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-577] for track '5' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-593] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-306] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-315] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-173] for track '7' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-193] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-223] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-260] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-289] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-375] for track '8' has 10 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-411] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-434] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-451] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-599] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-227] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-232] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-406] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-595] for track '12' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-392] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-599] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-97] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-599] for track '15' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-284] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-353] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-382] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-595] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-152] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-259] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-288] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-348] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-422] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-478] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-486] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-599] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-204] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-510] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-281] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-317] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-489] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-599] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-498] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-516] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-599] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [227-333] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-316] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-324] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-399] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-319] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-352] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-297] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-325] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-289] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-328] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-352] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-384] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-423] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-429] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-463] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-595] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-599] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-424] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-599] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-335] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-393] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-474] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-494] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-498] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-509] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-579] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-599] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-365] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-599] for track '42' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-368] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-382] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-392] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-414] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-436] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-452] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-471] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-476] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-485] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-494] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-509] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-420] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-449] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-467] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-484] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-504] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-514] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-525] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-544] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-563] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-572] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-583] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-588] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-427] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-431] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-451] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-472] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-501] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-552] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-599] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-467] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-479] for track '51' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-482] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-575] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-438] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-449] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-471] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-482] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-497] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-516] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-533] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-561] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-579] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-442] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-534] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-569] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-586] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-592] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-538] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-559] for track '56' has 1 frames without a visible bounding box.
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

</details>