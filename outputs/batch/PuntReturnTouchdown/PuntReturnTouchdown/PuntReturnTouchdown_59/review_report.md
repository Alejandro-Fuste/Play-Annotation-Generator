# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_59`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 59
- **Ball Tracks:** 0
- **Action Segments:** 217
- **Validation Warnings:** 255
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 201
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `22` | `20` |
| ✅ EXACT | `Action_PuntBall` | Position_Unknown | Team_Unknown | `22` | `20` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `31` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `31` | `28` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `31` | `28` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `10` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `11` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `16` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `17` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `3` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `8` | `Group` | 0 | START | 0 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `18` | `18` | 116 | START | 116 | 132 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `22` | `20` | 145 | END | 145 | 145 |
| ✅ EXACT | `Action_PuntBall` | Position_Unknown | `22` | `20` | 170 | START | 170 | 185 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `31` | `28` | 264 | START | 264 | 272 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `31` | `28` | 287 | START | 287 | 316 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `31` | `28` | 541 | START | 541 | 548 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–454
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 280 | 165 | inferred_complete_timeline |
| `Action_None` | 285 | 445 | 161 | inferred_complete_timeline |
| `Action_None` | 450 | 454 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–342
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 342 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 546

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 187 | 72 | inferred_complete_timeline |
| `Action_None` | 195 | 216 | 22 | inferred_complete_timeline |
| `Action_None` | 218 | 223 | 6 | inferred_complete_timeline |
| `Action_None` | 234 | 253 | 20 | inferred_complete_timeline |
| `Action_None` | 256 | 280 | 25 | inferred_complete_timeline |
| `Action_None` | 283 | 299 | 17 | inferred_complete_timeline |
| `Action_None` | 302 | 569 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_LongSnap` | 116 | 132 | 17 | inferred_complete_timeline |
| `Action_LongSnap` | 144 | 169 | 26 | inferred_complete_timeline |
| `Action_None` | 170 | 180 | 11 | inferred_complete_timeline |
| `Action_None` | 182 | 186 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–344
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 166 | 51 | inferred_complete_timeline |
| `Action_None` | 175 | 344 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 141 | 26 | inferred_complete_timeline |
| `Action_None` | 143 | 172 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–566
- **Visible Samples:** 549

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 445 | 330 | inferred_complete_timeline |
| `Action_None` | 457 | 462 | 6 | inferred_complete_timeline |
| `Action_None` | 465 | 467 | 3 | inferred_complete_timeline |
| `Action_None` | 473 | 566 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 141 | 26 | inferred_complete_timeline |
| `Action_None` | 145 | 483 | 339 | inferred_complete_timeline |
| `Action_None` | 487 | 519 | 33 | inferred_complete_timeline |
| `Action_None` | 522 | 527 | 6 | inferred_complete_timeline |
| `Action_None` | 529 | 537 | 9 | inferred_complete_timeline |
| `Action_None` | 540 | 569 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 513 | 398 | inferred_complete_timeline |
| `Action_None` | 515 | 557 | 43 | inferred_complete_timeline |
| `Action_None` | 561 | 569 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 187 | 72 | inferred_complete_timeline |
| `Action_None` | 189 | 215 | 27 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 147 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–528
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 188 | 73 | inferred_complete_timeline |
| `Action_None` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_None` | 200 | 218 | 19 | inferred_complete_timeline |
| `Action_None` | 220 | 268 | 49 | inferred_complete_timeline |
| `Action_None` | 271 | 275 | 5 | inferred_complete_timeline |
| `Action_None` | 290 | 317 | 28 | inferred_complete_timeline |
| `Action_None` | 320 | 340 | 21 | inferred_complete_timeline |
| `Action_None` | 342 | 348 | 7 | inferred_complete_timeline |
| `Action_None` | 353 | 488 | 136 | inferred_complete_timeline |
| `Action_None` | 497 | 499 | 3 | inferred_complete_timeline |
| `Action_None` | 512 | 515 | 4 | inferred_complete_timeline |
| `Action_None` | 517 | 525 | 9 | inferred_complete_timeline |
| `Action_None` | 527 | 528 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 266 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 180 | 65 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 342 | 227 | inferred_complete_timeline |
| `Action_None` | 344 | 455 | 112 | inferred_complete_timeline |
| `Action_None` | 458 | 473 | 16 | inferred_complete_timeline |
| `Action_None` | 476 | 532 | 57 | inferred_complete_timeline |
| `Action_None` | 554 | 556 | 3 | inferred_complete_timeline |
| `Action_None` | 566 | 569 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 197 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 221 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 302 | 187 | inferred_complete_timeline |
| `Action_None` | 319 | 326 | 8 | inferred_complete_timeline |
| `Action_None` | 328 | 331 | 4 | inferred_complete_timeline |
| `Action_None` | 342 | 352 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 273 | 158 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 14–279 | 266 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 49–303 | 252 | 8 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 155–569 | 414 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 204–206 | 3 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 207–569 | 325 | 6 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 215–559 | 252 | 12 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 235–238 | 4 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 235–258 | 17 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 235–569 | 316 | 13 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 250–542 | 266 | 8 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 252–255 | 4 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 253–358 | 81 | 7 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 263–306 | 38 | 4 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 270–569 | 300 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 279–284 | 5 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 283–297 | 11 | 3 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 285–569 | 285 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 301–471 | 169 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 310–315 | 6 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 331–454 | 124 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 334–569 | 220 | 4 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 337–569 | 232 | 2 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 341–569 | 208 | 5 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 353–354 | 2 | 1 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 356–569 | 210 | 4 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 362–569 | 198 | 3 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 373–569 | 197 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 378–380 | 3 | 1 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 379–385 | 7 | 1 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 386–522 | 41 | 10 | Undefined position; Undefined team |
| `50` | `73` | Position_Unknown | Team_Unknown | 472–569 | 91 | 2 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 474–480 | 5 | 2 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 488–569 | 75 | 4 | Undefined position; Undefined team |
| `53` | `80` | Position_Unknown | Team_Unknown | 522–569 | 18 | 5 | Undefined position; Undefined team |
| `54` | `82` | Position_Unknown | Team_Unknown | 525–569 | 45 | 1 | Undefined position; Undefined team |
| `55` | `84` | Position_Unknown | Team_Unknown | 532–558 | 23 | 2 | Undefined position; Undefined team |
| `56` | `87` | Position_Unknown | Team_Unknown | 541–569 | 29 | 1 | Undefined position; Undefined team |
| `57` | `94` | Position_Unknown | Team_Unknown | 558–566 | 8 | 2 | Undefined position; Undefined team |
| `58` | `96` | Position_Unknown | Team_Unknown | 567–569 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `31` (9 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 172 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [116-302] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-326] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-352] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-166] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-344] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-342] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-455] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-473] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-532] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-556] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-513] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-557] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-188] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-218] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-317] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-340] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-348] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-488] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-499] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-515] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-525] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-528] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-445] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-462] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-467] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-566] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-342] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-216] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-223] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-253] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-280] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-569] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-221] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-215] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-280] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-445] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-454] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-141] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-483] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-519] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-527] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-537] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-141] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-172] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [116-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-279] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-236] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-294] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-303] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-178] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-299] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-347] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-266] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-468] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-491] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-511] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-559] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-242] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [287-316] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [321-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [334-461] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [463-467] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [470-477] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [479-509] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [512-534] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [541-548] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-276] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-340] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-365] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-372] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-538] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-542] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-266] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-302] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-315] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-331] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-344] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-352] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-358] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-302] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-569] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-569] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-471] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-454] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-353] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-492] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-531] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-543] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-348] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-462] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-508] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-366] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-371] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-515] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-530] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-546] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-569] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-385] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-397] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-403] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-491] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-515] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-480] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-480] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-511] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-519] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-528] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-569] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-525] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-538] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-561] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-552] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-559] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-566] for track '57' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>