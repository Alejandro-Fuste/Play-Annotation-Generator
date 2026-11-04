# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_11`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 71
- **Ball Tracks:** 0
- **Action Segments:** 215
- **Validation Warnings:** 303
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 206
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Position_Unknown | Team_Unknown | `26` | `21` |
| ❌ MISSING SEGMENT | `Action_KickBall` | Position_Unknown | Team_Unknown | `26` | `21` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `61` | `45` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `61` | `45` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `61` | `45` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `0` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `10` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `11` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `12` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `13` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `8` | `Group` | 0 | START | 0 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Position_Unknown | `26` | `21` | 108 | START | 150 | 152 |
| ❌ MISSING SEGMENT | `Action_KickBall` | Position_Unknown | `26` | `21` | 182 | START | N/A | N/A |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `61` | `45` | 284 | START | 284 | 288 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `61` | `45` | 302 | START | 302 | 629 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `61` | `45` | 630 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 141 | 34 | inferred_complete_timeline |
| `Action_None` | 219 | 229 | 11 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 249 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 155 | 48 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–14
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 154 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 500 | 393 | inferred_complete_timeline |
| `Action_None` | 502 | 507 | 6 | inferred_complete_timeline |
| `Action_None` | 510 | 629 | 120 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 170 | 63 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 619

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 243 | 136 | inferred_complete_timeline |
| `Action_None` | 245 | 431 | 187 | inferred_complete_timeline |
| `Action_None` | 433 | 474 | 42 | inferred_complete_timeline |
| `Action_None` | 476 | 481 | 6 | inferred_complete_timeline |
| `Action_None` | 488 | 502 | 15 | inferred_complete_timeline |
| `Action_None` | 505 | 629 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 199 | 92 | inferred_complete_timeline |
| `Action_None` | 207 | 209 | 3 | inferred_complete_timeline |
| `Action_None` | 211 | 221 | 11 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_None` | 229 | 236 | 8 | inferred_complete_timeline |
| `Action_None` | 238 | 313 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 319 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 434 | 327 | inferred_complete_timeline |
| `Action_None` | 437 | 440 | 4 | inferred_complete_timeline |
| `Action_None` | 443 | 509 | 67 | inferred_complete_timeline |
| `Action_None` | 512 | 629 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–562
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 173 | 66 | inferred_complete_timeline |
| `Action_None` | 200 | 214 | 15 | inferred_complete_timeline |
| `Action_None` | 222 | 229 | 8 | inferred_complete_timeline |
| `Action_None` | 233 | 367 | 135 | inferred_complete_timeline |
| `Action_None` | 371 | 562 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 629 | 522 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 191 | 84 | inferred_complete_timeline |
| `Action_None` | 193 | 418 | 226 | inferred_complete_timeline |
| `Action_None` | 420 | 495 | 76 | inferred_complete_timeline |
| `Action_None` | 497 | 501 | 5 | inferred_complete_timeline |
| `Action_None` | 506 | 525 | 20 | inferred_complete_timeline |
| `Action_None` | 527 | 530 | 4 | inferred_complete_timeline |
| `Action_None` | 533 | 538 | 6 | inferred_complete_timeline |
| `Action_None` | 544 | 549 | 6 | inferred_complete_timeline |
| `Action_None` | 552 | 562 | 11 | inferred_complete_timeline |
| `Action_None` | 566 | 568 | 3 | inferred_complete_timeline |
| `Action_None` | 574 | 578 | 5 | inferred_complete_timeline |
| `Action_None` | 588 | 594 | 7 | inferred_complete_timeline |
| `Action_None` | 596 | 601 | 6 | inferred_complete_timeline |
| `Action_None` | 603 | 629 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 12–131 | 83 | 6 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 14–543 | 525 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 22–31 | 7 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 70–168 | 61 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 115–351 | 227 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 150–187 | 32 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 173–185 | 13 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 182–197 | 16 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 203–339 | 132 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 204–475 | 269 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 209–629 | 420 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 213–629 | 395 | 6 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 216–220 | 5 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 219–272 | 39 | 4 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 222–229 | 8 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 231–344 | 87 | 5 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 237–629 | 385 | 6 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 237–378 | 135 | 4 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 244–245 | 2 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 244–418 | 171 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 248–249 | 2 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 252–336 | 85 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 260–351 | 83 | 4 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 262–264 | 3 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 265–291 | 10 | 3 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 268–271 | 4 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 270–629 | 360 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 274–375 | 92 | 3 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 275–629 | 355 | 4 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 294–347 | 53 | 2 | Undefined position; Undefined team |
| `48` | `64` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |
| `49` | `65` | Position_Unknown | Team_Unknown | 322–629 | 305 | 2 | Undefined position; Undefined team |
| `50` | `66` | Position_Unknown | Team_Unknown | 326–336 | 5 | 2 | Undefined position; Undefined team |
| `51` | `67` | Position_Unknown | Team_Unknown | 328–333 | 6 | 1 | Undefined position; Undefined team |
| `52` | `69` | Position_Unknown | Team_Unknown | 336–337 | 2 | 1 | Undefined position; Undefined team |
| `53` | `70` | Position_Unknown | Team_Unknown | 338–537 | 188 | 2 | Undefined position; Undefined team |
| `54` | `72` | Position_Unknown | Team_Unknown | 350–629 | 261 | 7 | Undefined position; Undefined team |
| `55` | `73` | Position_Unknown | Team_Unknown | 366–526 | 136 | 13 | Undefined position; Undefined team |
| `56` | `74` | Position_Unknown | Team_Unknown | 366–629 | 252 | 3 | Undefined position; Undefined team |
| `57` | `76` | Position_Unknown | Team_Unknown | 379–382 | 4 | 1 | Undefined position; Undefined team |
| `58` | `78` | Position_Unknown | Team_Unknown | 395–629 | 219 | 4 | Undefined position; Undefined team |
| `59` | `79` | Position_Unknown | Team_Unknown | 406–628 | 216 | 4 | Undefined position; Undefined team |
| `60` | `80` | Position_Unknown | Team_Unknown | 412–413 | 2 | 1 | Undefined position; Undefined team |
| `61` | `81` | Position_Unknown | Team_Unknown | 433–629 | 183 | 5 | Undefined position; Undefined team |
| `62` | `83` | Position_Unknown | Team_Unknown | 452–534 | 83 | 1 | Undefined position; Undefined team |
| `63` | `90` | Position_Unknown | Team_Unknown | 497–619 | 106 | 8 | Undefined position; Undefined team |
| `64` | `92` | Position_Unknown | Team_Unknown | 500–575 | 64 | 3 | Undefined position; Undefined team |
| `65` | `95` | Position_Unknown | Team_Unknown | 522–524 | 3 | 1 | Undefined position; Undefined team |
| `66` | `96` | Position_Unknown | Team_Unknown | 522–525 | 4 | 1 | Undefined position; Undefined team |
| `67` | `99` | Position_Unknown | Team_Unknown | 545–629 | 85 | 1 | Undefined position; Undefined team |
| `68` | `103` | Position_Unknown | Team_Unknown | 557–629 | 65 | 3 | Undefined position; Undefined team |
| `69` | `108` | Position_Unknown | Team_Unknown | 598–604 | 7 | 1 | Undefined position; Undefined team |
| `70` | `110` | Position_Unknown | Team_Unknown | 609–611 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `26` (2 segments found)
- ❌ Missing segment for action `Action_KickBall` on target `26` (Position_Unknown)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `61` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ 55 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 55 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 110 |
| Missing visible bounding boxes during action | 189 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 24: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '45' has invalid range: start=630, end=629. Clamping end to start.
- ⚠️ Action 'Action_None' range [108-500] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-507] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-434] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-440] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-509] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-629] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-629] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-243] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-431] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-474] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-481] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-502] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-173] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-214] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-229] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-367] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-562] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-191] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-418] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-495] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-501] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-525] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-530] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-538] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-549] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-562] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-568] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-578] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-594] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-601] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-319] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-199] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-221] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-236] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-313] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-131] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-334] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-445] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-543] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-341] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [150-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [155-181] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-185] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-197] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-339] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-241] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-440] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-471] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-475] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-486] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-629] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-433] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-561] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-570] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-601] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-261] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-229] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-266] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-272] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-289] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-313] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-344] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-341] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-471] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-535] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-629] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-351] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-372] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-378] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-418] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-336] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-323] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-336] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-351] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-629] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-357] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-372] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [302-629] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-301] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-347] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-429] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-352] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-537] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-474] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-536] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-562] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-570] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-374] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-380] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-393] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-400] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-427] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-473] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-506] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-512] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-519] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-526] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-396] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-597] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-411] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-542] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-431] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-485] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-628] for track '59' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-505] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-595] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-599] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-621] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-534] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-501] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-524] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-539] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-559] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-573] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-604] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-614] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-619] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-553] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-565] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-575] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-524] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-525] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-629] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-565] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-578] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-629] for track '68' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-604] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-611] for track '70' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 630. Video range is [0, 629].

</details>