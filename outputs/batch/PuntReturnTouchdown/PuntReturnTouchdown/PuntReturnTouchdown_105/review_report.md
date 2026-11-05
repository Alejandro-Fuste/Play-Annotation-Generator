# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_105

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_105`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 54
- **Ball Tracks:** 0
- **Action Segments:** 214
- **Validation Warnings:** 254
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 196
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `0` | `0` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `0` | `0` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `41` | `34` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `41` | `34` |
| ✅ EXACT | `Action_CrossGoalLine` | Personal_Protector1 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `0` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 253 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `10` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `16` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `2` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `3` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `5` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `6` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `9` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `10` | `10` | 33 | START | 33 | 96 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `0` | `0` | 63 | END | 63 | 63 |
| ✅ EXACT | `Action_PuntBall` | Punter | `0` | `0` | 97 | START | 97 | 104 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `41` | `34` | 224 | START | 224 | 236 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `41` | `34` | 245 | START | 245 | 260 |
| ✅ EXACT | `Action_CrossGoalLine` | Personal_Protector1 | `1` | `1` | 624 | START | 624 | 629 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 96 | 64 | inferred_complete_timeline |
| `Action_None` | 117 | 122 | 6 | inferred_complete_timeline |
| `Action_None` | 125 | 129 | 5 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 180 | 42 | inferred_complete_timeline |
| `Action_None` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_None` | 192 | 195 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–515
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 407 | 375 | inferred_complete_timeline |
| `Action_None` | 412 | 515 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 109 | 77 | inferred_complete_timeline |
| `Action_None` | 112 | 128 | 17 | inferred_complete_timeline |
| `Action_None` | 131 | 273 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 171 | 139 | inferred_complete_timeline |
| `Action_None` | 181 | 278 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 605

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_LongSnap` | 33 | 96 | 64 | inferred_complete_timeline |
| `Action_None` | 97 | 118 | 22 | inferred_complete_timeline |
| `Action_None` | 120 | 127 | 8 | inferred_complete_timeline |
| `Action_None` | 133 | 471 | 339 | inferred_complete_timeline |
| `Action_None` | 473 | 581 | 109 | inferred_complete_timeline |
| `Action_None` | 586 | 594 | 9 | inferred_complete_timeline |
| `Action_None` | 598 | 601 | 4 | inferred_complete_timeline |
| `Action_None` | 606 | 615 | 10 | inferred_complete_timeline |
| `Action_None` | 623 | 629 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 619

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 623 | 357 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 624 | 629 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 88 | 56 | inferred_complete_timeline |
| `Action_None` | 91 | 97 | 7 | inferred_complete_timeline |
| `Action_None` | 99 | 407 | 309 | inferred_complete_timeline |
| `Action_None` | 412 | 440 | 29 | inferred_complete_timeline |
| `Action_None` | 442 | 446 | 5 | inferred_complete_timeline |
| `Action_None` | 451 | 546 | 96 | inferred_complete_timeline |
| `Action_None` | 548 | 574 | 27 | inferred_complete_timeline |
| `Action_None` | 592 | 616 | 25 | inferred_complete_timeline |
| `Action_None` | 620 | 629 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–444
- **Visible Samples:** 431

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_SnapReceive` | 63 | 63 | 1 | inferred_complete_timeline |
| `Action_None` | 64 | 96 | 33 | inferred_complete_timeline |
| `Action_PuntBall` | 97 | 104 | 8 | inferred_complete_timeline |
| `Action_None` | 105 | 256 | 152 | inferred_complete_timeline |
| `Action_None` | 259 | 265 | 7 | inferred_complete_timeline |
| `Action_None` | 278 | 444 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 128 | 96 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_None` | 144 | 150 | 7 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 92 | 60 | inferred_complete_timeline |
| `Action_None` | 111 | 116 | 6 | inferred_complete_timeline |
| `Action_None` | 118 | 150 | 33 | inferred_complete_timeline |
| `Action_None` | 153 | 168 | 16 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_None` | 181 | 385 | 205 | inferred_complete_timeline |
| `Action_None` | 388 | 500 | 113 | inferred_complete_timeline |
| `Action_None` | 503 | 524 | 22 | inferred_complete_timeline |
| `Action_None` | 529 | 537 | 9 | inferred_complete_timeline |
| `Action_None` | 539 | 584 | 46 | inferred_complete_timeline |
| `Action_None` | 588 | 629 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 72 | 40 | inferred_complete_timeline |
| `Action_None` | 74 | 268 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–402
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 220 | 188 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 325 | 80 | inferred_complete_timeline |
| `Action_None` | 330 | 399 | 70 | inferred_complete_timeline |
| `Action_None` | 401 | 402 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 54 | 22 | inferred_complete_timeline |
| `Action_None` | 76 | 313 | 238 | inferred_complete_timeline |
| `Action_None` | 315 | 326 | 12 | inferred_complete_timeline |
| `Action_None` | 334 | 417 | 84 | inferred_complete_timeline |
| `Action_None` | 422 | 629 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 15 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 32 | 16 | inferred_complete_timeline |
| `Action_None` | 33 | 62 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 622

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 90 | 58 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 629 | 525 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 81 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 82 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 97 | 65 | inferred_complete_timeline |
| `Action_None` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 141 | 7 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 11–83 | 47 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 22–112 | 91 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 58–103 | 46 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 62–118 | 56 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 108–116 | 8 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 114–209 | 94 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 115–629 | 498 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 120–132 | 7 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 122–488 | 358 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 135–277 | 141 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 146–620 | 463 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 150–629 | 472 | 4 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 150–162 | 13 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 156–163 | 8 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 192–303 | 94 | 4 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 199–260 | 62 | 4 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 208–298 | 28 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 220–629 | 387 | 5 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 269–547 | 275 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 272–595 | 320 | 3 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 281–629 | 326 | 6 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 285–629 | 328 | 6 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 290–298 | 9 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 305–629 | 320 | 3 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 313–629 | 313 | 2 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 319–374 | 18 | 3 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 339–629 | 268 | 7 | Undefined position; Undefined team |
| `46` | `58` | Position_Unknown | Team_Unknown | 347–629 | 282 | 2 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 429–629 | 177 | 6 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 456–459 | 4 | 1 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 468–629 | 162 | 1 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 510–575 | 57 | 7 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 518–627 | 73 | 7 | Undefined position; Undefined team |
| `52` | `73` | Position_Unknown | Team_Unknown | 565–595 | 30 | 2 | Undefined position; Undefined team |
| `53` | `74` | Position_Unknown | Team_Unknown | 573–629 | 42 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 178 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 211: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [105-256] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-444] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-623] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-407] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-515] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-92] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-150] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-385] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-500] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-524] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-537] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-584] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-90] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-128] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-273] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-171] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-278] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-81] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-118] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-127] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-471] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-581] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-594] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-601] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-615] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-268] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-122] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-180] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-220] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-325] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-399] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-313] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-326] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-417] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-97] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-407] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-440] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-446] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-546] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-574] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-616] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-15] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-62] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-15] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-112] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-450] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-470] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-629] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-473] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-478] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-257] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-277] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-377] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-581] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-607] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-620] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-166] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-372] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-601] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-629] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-162] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-163] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-238] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-267] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-277] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-303] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [245-260] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-298] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-244] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-509] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-597] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-521] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-547] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-336] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-376] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-595] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-312] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-356] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-479] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-487] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-539] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-629] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-311] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-391] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-561] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-604] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-607] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-298] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-519] for track '42' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-629] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-608] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-629] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-374] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-344] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-434] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-601] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-607] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-615] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-462] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-629] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-467] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-476] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-567] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-580] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-586] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-459] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-629] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-525] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-532] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-536] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-547] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-555] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-559] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-575] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-530] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-572] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-582] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-591] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-601] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-613] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-627] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-575] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-595] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-620] for track '53' has 6 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>