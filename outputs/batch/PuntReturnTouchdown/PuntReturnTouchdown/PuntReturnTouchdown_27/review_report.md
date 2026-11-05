# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_27

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_27`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 689
- **Player Tracks:** 75
- **Ball Tracks:** 2
- **Action Segments:** 166
- **Validation Warnings:** 242
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 149
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `32` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `32` | `25` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `32` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `11` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `12` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `14` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `15` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `16` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `17` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `3` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `6` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `7` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `9` | `Group` | 0 | START | 0 | 72 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `15` | `15` | 73 | START | 73 | 134 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 103 | END | 103 | 103 |
| ✅ EXACT | `Action_PuntBall` | Punter | `8` | `8` | 135 | START | 135 | 144 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `32` | `25` | 225 | START | 225 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `32` | `25` | 245 | START | 245 | 651 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `32` | `25` | 683 | START | 683 | 689 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 118 | 46 | inferred_complete_timeline |
| `Action_None` | 125 | 246 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–560
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 252 | 180 | inferred_complete_timeline |
| `Action_None` | 254 | 560 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–535
- **Visible Samples:** 517

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 226 | 154 | inferred_complete_timeline |
| `Action_None` | 229 | 241 | 13 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 296 | 37 | inferred_complete_timeline |
| `Action_None` | 298 | 535 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 204 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–567
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_LongSnap` | 73 | 134 | 62 | inferred_complete_timeline |
| `Action_None` | 135 | 283 | 149 | inferred_complete_timeline |
| `Action_None` | 287 | 551 | 265 | inferred_complete_timeline |
| `Action_None` | 559 | 567 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 260 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–549
- **Visible Samples:** 541

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 476 | 404 | inferred_complete_timeline |
| `Action_None` | 480 | 482 | 3 | inferred_complete_timeline |
| `Action_None` | 489 | 549 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 255 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_SnapReceive` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_None` | 104 | 134 | 31 | inferred_complete_timeline |
| `Action_PuntBall` | 135 | 144 | 10 | inferred_complete_timeline |
| `Action_None` | 145 | 252 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–510
- **Visible Samples:** 511

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 510 | 438 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–344
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 344 | 272 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–615
- **Visible Samples:** 615

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 226 | 154 | inferred_complete_timeline |
| `Action_None` | 228 | 615 | 388 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 25 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 49 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 107 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–487
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 147 | 75 | inferred_complete_timeline |
| `Action_None` | 151 | 160 | 10 | inferred_complete_timeline |
| `Action_None` | 162 | 168 | 7 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 188 | 13 | inferred_complete_timeline |
| `Action_None` | 191 | 203 | 13 | inferred_complete_timeline |
| `Action_None` | 205 | 236 | 32 | inferred_complete_timeline |
| `Action_None` | 240 | 268 | 29 | inferred_complete_timeline |
| `Action_None` | 273 | 378 | 106 | inferred_complete_timeline |
| `Action_None` | 380 | 487 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 190 | 118 | inferred_complete_timeline |
| `Action_None` | 202 | 207 | 6 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 313 | 100 | inferred_complete_timeline |
| `Action_None` | 315 | 316 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–628
- **Visible Samples:** 626

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 290 | 218 | inferred_complete_timeline |
| `Action_None` | 292 | 296 | 5 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_None` | 301 | 628 | 328 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 193 | 121 | inferred_complete_timeline |
| `Action_None` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 301 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 687

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 138 | 66 | inferred_complete_timeline |
| `Action_None` | 142 | 689 | 548 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 198 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 98–318 | 219 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 108–233 | 126 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 203–207 | 5 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 212–249 | 38 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 214–474 | 261 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 225–689 | 461 | 5 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 238–689 | 447 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 258–277 | 20 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 294–310 | 17 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 297–406 | 105 | 4 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 299–305 | 7 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 299–308 | 10 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 301–310 | 10 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 314–327 | 14 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 316–317 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 324–332 | 8 | 2 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 334–547 | 210 | 2 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 357–689 | 333 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 358–689 | 325 | 5 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 359–599 | 237 | 2 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 359–381 | 8 | 3 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 359–611 | 253 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 363–387 | 19 | 2 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 399–400 | 2 | 1 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 401–678 | 278 | 1 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 401–689 | 289 | 1 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 405–407 | 3 | 1 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 407–639 | 233 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 412–689 | 278 | 1 | Undefined position; Undefined team |
| `50` | `76` | Position_Unknown | Team_Unknown | 435–585 | 151 | 1 | Undefined position; Undefined team |
| `51` | `80` | Position_Unknown | Team_Unknown | 461–474 | 11 | 2 | Undefined position; Undefined team |
| `52` | `82` | Position_Unknown | Team_Unknown | 464–465 | 2 | 1 | Undefined position; Undefined team |
| `53` | `83` | Position_Unknown | Team_Unknown | 464–465 | 2 | 1 | Undefined position; Undefined team |
| `54` | `84` | Position_Unknown | Team_Unknown | 464–474 | 7 | 2 | Undefined position; Undefined team |
| `55` | `85` | Position_Unknown | Team_Unknown | 475–476 | 2 | 1 | Undefined position; Undefined team |
| `56` | `86` | Position_Unknown | Team_Unknown | 475–552 | 73 | 4 | Undefined position; Undefined team |
| `57` | `91` | Position_Unknown | Team_Unknown | 529–545 | 14 | 2 | Undefined position; Undefined team |
| `59` | `94` | Position_Unknown | Team_Unknown | 544–570 | 27 | 1 | Undefined position; Undefined team |
| `60` | `96` | Position_Unknown | Team_Unknown | 553–555 | 3 | 1 | Undefined position; Undefined team |
| `61` | `98` | Position_Unknown | Team_Unknown | 582–584 | 3 | 1 | Undefined position; Undefined team |
| `62` | `99` | Position_Unknown | Team_Unknown | 601–602 | 2 | 1 | Undefined position; Undefined team |
| `63` | `101` | Position_Unknown | Team_Unknown | 632–633 | 2 | 1 | Undefined position; Undefined team |
| `64` | `105` | Position_Unknown | Team_Unknown | 639–653 | 13 | 2 | Undefined position; Undefined team |
| `65` | `106` | Position_Unknown | Team_Unknown | 642–689 | 17 | 4 | Undefined position; Undefined team |
| `66` | `108` | Position_Unknown | Team_Unknown | 645–646 | 2 | 1 | Undefined position; Undefined team |
| `67` | `110` | Position_Unknown | Team_Unknown | 653–675 | 23 | 1 | Undefined position; Undefined team |
| `68` | `111` | Position_Unknown | Team_Unknown | 660–689 | 14 | 3 | Undefined position; Undefined team |
| `69` | `112` | Position_Unknown | Team_Unknown | 663–685 | 13 | 4 | Undefined position; Undefined team |
| `70` | `113` | Position_Unknown | Team_Unknown | 663–679 | 15 | 3 | Undefined position; Undefined team |
| `71` | `115` | Position_Unknown | Team_Unknown | 677–679 | 3 | 1 | Undefined position; Undefined team |
| `72` | `118` | Position_Unknown | Team_Unknown | 679–689 | 11 | 1 | Undefined position; Undefined team |
| `73` | `119` | Position_Unknown | Team_Unknown | 682–689 | 8 | 1 | Undefined position; Undefined team |
| `74` | `120` | Position_Unknown | Team_Unknown | 683–689 | 7 | 1 | Undefined position; Undefined team |
| `75` | `121` | Position_Unknown | Team_Unknown | 683–689 | 7 | 1 | Undefined position; Undefined team |
| `76` | `127` | Position_Unknown | Team_Unknown | 689–689 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `49` | `74` | 424 | 431 | 7 | 87.5% | 429 |
| `58` | `93` | 538 | 538 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `32` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ 55 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 55 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 110 |
| Missing visible bounding boxes during action | 129 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [73-198] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-190] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-313] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-147] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-160] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-203] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-236] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-378] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-487] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-204] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-107] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-689] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-344] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-252] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-560] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-252] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-290] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-628] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-255] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-241] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-296] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-535] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-193] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-301] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-510] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-551] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-567] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-260] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-476] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-482] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-549] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-615] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-318] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-233] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-249] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-474] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-243] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [245-651] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-380] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-277] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-310] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-356] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-373] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-406] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-305] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-308] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-310] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-327] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-329] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-371] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-547] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-473] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-480] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-491] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-512] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-498] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-599] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-362] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-611] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-387] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-678] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-407] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-639] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-585] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-463] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-474] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-468] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-506] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-521] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-552] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-531] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-545] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-570] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-555] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-584] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-602] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-633] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-647] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-653] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-649] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-679] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-683] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-646] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-675] for track '67' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [660-661] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-670] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [663-667] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-676] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-679] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-685] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [663-664] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-673] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-679] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-679] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [679-689] for track '72' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>