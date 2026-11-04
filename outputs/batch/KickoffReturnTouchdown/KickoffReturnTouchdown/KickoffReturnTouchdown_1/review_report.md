# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_1

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_1`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 97
- **Ball Tracks:** 0
- **Action Segments:** 332
- **Validation Warnings:** 496
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 5
- **Exact Matches:** 0
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 329
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Position_Unknown | Team_Unknown | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_KickBall` | Position_Unknown | Team_Unknown | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchKick` | Position_Unknown | Team_Unknown | `52` | `37` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `52` | `37` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `52` | `37` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Position_Unknown | `11` | `11` | 3 | START | 29 | 30 |
| ❌ MISSING SEGMENT | `Action_KickBall` | Position_Unknown | `11` | `11` | 69 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchKick` | Position_Unknown | `52` | `37` | 187 | START | 187 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `52` | `37` | 210 | START | 210 | 286 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `52` | `37` | 587 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

*(No offensive player tracks)*

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 75 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 198 | 196 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 209 | 237 | 29 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 282 | 41 | inferred_complete_timeline |
| `Action_None` | 286 | 297 | 12 | inferred_complete_timeline |
| `Action_None` | 299 | 321 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 64 | 62 | inferred_complete_timeline |
| `Action_None` | 67 | 72 | 6 | inferred_complete_timeline |
| `Action_None` | 77 | 82 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 111 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 224 | 222 | inferred_complete_timeline |
| `Action_None` | 226 | 243 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 270 | 268 | inferred_complete_timeline |
| `Action_None` | 277 | 282 | 6 | inferred_complete_timeline |
| `Action_None` | 286 | 303 | 18 | inferred_complete_timeline |
| `Action_None` | 307 | 309 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 146 | 144 | inferred_complete_timeline |
| `Action_None` | 148 | 252 | 105 | inferred_complete_timeline |
| `Action_None` | 258 | 317 | 60 | inferred_complete_timeline |
| `Action_None` | 332 | 360 | 29 | inferred_complete_timeline |
| `Action_None` | 373 | 374 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 258 | 256 | inferred_complete_timeline |
| `Action_None` | 261 | 280 | 20 | inferred_complete_timeline |
| `Action_None` | 287 | 290 | 4 | inferred_complete_timeline |
| `Action_None` | 292 | 296 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–531
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 168 | 166 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 199 | 272 | 74 | inferred_complete_timeline |
| `Action_None` | 274 | 280 | 7 | inferred_complete_timeline |
| `Action_None` | 284 | 287 | 4 | inferred_complete_timeline |
| `Action_None` | 293 | 376 | 84 | inferred_complete_timeline |
| `Action_None` | 378 | 411 | 34 | inferred_complete_timeline |
| `Action_None` | 416 | 445 | 30 | inferred_complete_timeline |
| `Action_None` | 452 | 457 | 6 | inferred_complete_timeline |
| `Action_None` | 484 | 488 | 5 | inferred_complete_timeline |
| `Action_None` | 491 | 492 | 2 | inferred_complete_timeline |
| `Action_None` | 494 | 497 | 4 | inferred_complete_timeline |
| `Action_None` | 499 | 503 | 5 | inferred_complete_timeline |
| `Action_None` | 521 | 531 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–12 | 13 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 11–190 | 132 | 6 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 29–56 | 7 | 3 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 73–335 | 225 | 6 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 76–90 | 12 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 91–104 | 8 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 97–351 | 220 | 10 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 100–171 | 11 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 108–283 | 139 | 7 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 115–598 | 419 | 12 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 116–203 | 88 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 117–118 | 2 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 120–168 | 47 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 122–123 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 126–129 | 4 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 128–364 | 206 | 8 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 130–131 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 137–157 | 21 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 137–200 | 60 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 139–142 | 4 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 143–212 | 54 | 5 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 155–161 | 7 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 158–599 | 391 | 3 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 162–177 | 5 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 165–590 | 368 | 9 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 185–188 | 4 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 185–315 | 93 | 5 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 191–192 | 2 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 199–599 | 389 | 5 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 199–587 | 332 | 18 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 206–564 | 222 | 17 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 214–220 | 7 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 214–361 | 142 | 2 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 236–271 | 36 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 243–299 | 48 | 4 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 243–483 | 213 | 5 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 254–332 | 79 | 1 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 264–539 | 237 | 9 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 280–310 | 18 | 3 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 292–599 | 235 | 4 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 293–599 | 285 | 8 | Undefined position; Undefined team |
| `52` | `72` | Position_Unknown | Team_Unknown | 293–358 | 59 | 4 | Undefined position; Undefined team |
| `53` | `73` | Position_Unknown | Team_Unknown | 305–426 | 106 | 6 | Undefined position; Undefined team |
| `54` | `75` | Position_Unknown | Team_Unknown | 315–369 | 47 | 3 | Undefined position; Undefined team |
| `55` | `76` | Position_Unknown | Team_Unknown | 329–330 | 2 | 1 | Undefined position; Undefined team |
| `56` | `77` | Position_Unknown | Team_Unknown | 340–359 | 17 | 2 | Undefined position; Undefined team |
| `57` | `81` | Position_Unknown | Team_Unknown | 354–502 | 99 | 10 | Undefined position; Undefined team |
| `58` | `82` | Position_Unknown | Team_Unknown | 367–422 | 49 | 2 | Undefined position; Undefined team |
| `59` | `85` | Position_Unknown | Team_Unknown | 379–599 | 219 | 3 | Undefined position; Undefined team |
| `60` | `86` | Position_Unknown | Team_Unknown | 385–575 | 179 | 8 | Undefined position; Undefined team |
| `61` | `87` | Position_Unknown | Team_Unknown | 385–387 | 3 | 1 | Undefined position; Undefined team |
| `62` | `88` | Position_Unknown | Team_Unknown | 386–396 | 9 | 2 | Undefined position; Undefined team |
| `63` | `89` | Position_Unknown | Team_Unknown | 389–572 | 180 | 3 | Undefined position; Undefined team |
| `64` | `90` | Position_Unknown | Team_Unknown | 392–397 | 6 | 1 | Undefined position; Undefined team |
| `65` | `92` | Position_Unknown | Team_Unknown | 401–599 | 181 | 5 | Undefined position; Undefined team |
| `66` | `94` | Position_Unknown | Team_Unknown | 406–422 | 17 | 1 | Undefined position; Undefined team |
| `67` | `96` | Position_Unknown | Team_Unknown | 412–416 | 5 | 1 | Undefined position; Undefined team |
| `68` | `97` | Position_Unknown | Team_Unknown | 414–424 | 11 | 1 | Undefined position; Undefined team |
| `69` | `98` | Position_Unknown | Team_Unknown | 428–496 | 20 | 5 | Undefined position; Undefined team |
| `70` | `99` | Position_Unknown | Team_Unknown | 430–438 | 9 | 1 | Undefined position; Undefined team |
| `71` | `101` | Position_Unknown | Team_Unknown | 431–432 | 2 | 1 | Undefined position; Undefined team |
| `72` | `102` | Position_Unknown | Team_Unknown | 433–573 | 141 | 1 | Undefined position; Undefined team |
| `73` | `103` | Position_Unknown | Team_Unknown | 447–475 | 18 | 3 | Undefined position; Undefined team |
| `74` | `105` | Position_Unknown | Team_Unknown | 454–550 | 80 | 4 | Undefined position; Undefined team |
| `75` | `106` | Position_Unknown | Team_Unknown | 463–464 | 2 | 1 | Undefined position; Undefined team |
| `76` | `107` | Position_Unknown | Team_Unknown | 469–583 | 88 | 5 | Undefined position; Undefined team |
| `77` | `109` | Position_Unknown | Team_Unknown | 473–475 | 3 | 1 | Undefined position; Undefined team |
| `78` | `110` | Position_Unknown | Team_Unknown | 478–599 | 122 | 1 | Undefined position; Undefined team |
| `79` | `112` | Position_Unknown | Team_Unknown | 488–599 | 109 | 3 | Undefined position; Undefined team |
| `80` | `113` | Position_Unknown | Team_Unknown | 494–495 | 2 | 1 | Undefined position; Undefined team |
| `81` | `116` | Position_Unknown | Team_Unknown | 498–599 | 102 | 1 | Undefined position; Undefined team |
| `82` | `120` | Position_Unknown | Team_Unknown | 505–506 | 2 | 1 | Undefined position; Undefined team |
| `83` | `122` | Position_Unknown | Team_Unknown | 508–568 | 60 | 2 | Undefined position; Undefined team |
| `84` | `123` | Position_Unknown | Team_Unknown | 508–553 | 43 | 3 | Undefined position; Undefined team |
| `85` | `124` | Position_Unknown | Team_Unknown | 511–514 | 4 | 1 | Undefined position; Undefined team |
| `86` | `125` | Position_Unknown | Team_Unknown | 517–520 | 4 | 1 | Undefined position; Undefined team |
| `87` | `128` | Position_Unknown | Team_Unknown | 529–533 | 5 | 1 | Undefined position; Undefined team |
| `88` | `131` | Position_Unknown | Team_Unknown | 550–563 | 13 | 2 | Undefined position; Undefined team |
| `89` | `134` | Position_Unknown | Team_Unknown | 571–572 | 2 | 1 | Undefined position; Undefined team |
| `90` | `136` | Position_Unknown | Team_Unknown | 576–590 | 7 | 2 | Undefined position; Undefined team |
| `91` | `140` | Position_Unknown | Team_Unknown | 584–585 | 2 | 1 | Undefined position; Undefined team |
| `92` | `141` | Position_Unknown | Team_Unknown | 587–599 | 13 | 1 | Undefined position; Undefined team |
| `93` | `143` | Position_Unknown | Team_Unknown | 593–599 | 7 | 1 | Undefined position; Undefined team |
| `94` | `145` | Position_Unknown | Team_Unknown | 594–599 | 6 | 1 | Undefined position; Undefined team |
| `95` | `146` | Position_Unknown | Team_Unknown | 596–599 | 4 | 1 | Undefined position; Undefined team |
| `96` | `147` | Position_Unknown | Team_Unknown | 596–599 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `11` (3 segments found)
- ❌ Missing segment for action `Action_KickBall` on target `11` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_CatchKick` and target `52` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `52` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `52` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ 88 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 88 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 176 |
| Missing visible bounding boxes during action | 317 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_KickBall' for track '11' has invalid range: start=69, end=56. Clamping end to start.
- ⚠️ Segment 'Action_CrossGoalLine' for track '37' has invalid range: start=587, end=315. Clamping end to start.
- ⚠️ Action 'Action_None' range [3-168] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-272] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-280] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-376] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-411] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-445] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-457] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-488] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-497] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-503] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-531] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-224] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-243] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-111] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-198] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-237] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-282] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-297] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-321] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-270] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-303] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-252] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-317] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-360] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-258] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-280] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-72] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-75] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-12] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-106] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [29-30] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [51-53] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [55-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-154] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-313] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-335] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-85] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-119] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-232] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-279] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-313] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-351] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-224] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-283] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-270] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-308] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-400] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-598] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-203] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-127] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-168] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-285] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-294] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-364] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-157] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-192] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-195] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-161] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-283] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-322] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-599] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-182] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-204] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-222] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-236] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-310] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-371] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-590] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' for track '37' starts at frame 187, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_CatchKick' range [187-190] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [202-209] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [210-286] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [314-315] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-208] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-599] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-221] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-243] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-290] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-371] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-378] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-397] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-411] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-432] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-437] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-477] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-587] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-255] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-378] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-397] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-415] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-438] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-464] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-470] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-478] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-489] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-499] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-509] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-528] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-537] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-545] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-564] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-326] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-361] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-271] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-249] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-282] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-388] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-452] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-483] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-332] for track '47' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-277] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-310] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-386] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-397] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-473] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-478] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-509] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-539] for track '48' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-289] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-296] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-345] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-361] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-599] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-314] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-428] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-432] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-440] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-452] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-540] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-599] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-333] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-358] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-314] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-400] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-411] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-426] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-353] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-369] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-351] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-386] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-397] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-405] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-422] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-428] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-432] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-440] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-450] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-461] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-502] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-370] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-422] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-452] for track '59' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-457] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-599] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-442] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-475] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-480] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-506] for track '60' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-557] for track '60' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-571] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-575] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-387] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-392] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-450] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-569] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-572] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-397] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-479] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-557] for track '65' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-566] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-579] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-422] for track '66' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-416] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-424] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-446] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-462] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-478] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-496] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-438] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-573] for track '72' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-452] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-475] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-470] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-494] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-522] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-550] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-543] for track '76' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-563] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-567] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-583] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-475] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-599] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-533] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-542] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-599] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-568] for track '83' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-517] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-541] for track '84' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-553] for track '84' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-514] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-520] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-533] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-557] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-563] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-572] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-578] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-590] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-585] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-599] for track '92' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-599] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '82' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '82' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '83' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '83' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '84' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '84' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '85' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '85' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '86' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '86' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '87' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '87' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '88' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '88' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '89' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '89' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '90' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '90' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '91' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '91' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '92' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '92' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '93' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '93' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '94' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '94' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '95' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '95' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '96' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '96' has undefined team_side. Will map to Team_Unknown.

</details>