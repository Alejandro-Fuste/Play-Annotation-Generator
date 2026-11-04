# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_34

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_34`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 54
- **Ball Tracks:** 0
- **Action Segments:** 187
- **Validation Warnings:** 220
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 171
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage6 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `21` | `21` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `21` | `21` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `20` | `20` |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner1 | defense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `0` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `10` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `18` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `2` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `4` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage6 | `5` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `6` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `8` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `21` | `21` | 15 | START | 15 | 76 |
| ✅ EXACT | `Action_KickBall` | Kicker | `21` | `21` | 77 | START | 77 | 80 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `20` | `20` | 194 | START | 194 | 200 |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner1 | `20` | `20` | 210 | START | 210 | 569 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | `20` | `20` | 570 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 14 | 12 | inferred_complete_timeline |
| `Action_KickApproach` | 15 | 76 | 62 | inferred_complete_timeline |
| `Action_KickBall` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 81 | 569 | 489 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 123 | 109 | inferred_complete_timeline |
| `Action_None` | 129 | 288 | 160 | inferred_complete_timeline |
| `Action_None` | 294 | 569 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–371
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 22 | 8 | inferred_complete_timeline |
| `Action_None` | 25 | 240 | 216 | inferred_complete_timeline |
| `Action_None` | 242 | 280 | 39 | inferred_complete_timeline |
| `Action_None` | 282 | 371 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 128 | 114 | inferred_complete_timeline |
| `Action_None` | 135 | 138 | 4 | inferred_complete_timeline |
| `Action_None` | 143 | 171 | 29 | inferred_complete_timeline |
| `Action_None` | 175 | 569 | 395 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_None` | 116 | 261 | 146 | inferred_complete_timeline |
| `Action_None` | 263 | 276 | 14 | inferred_complete_timeline |
| `Action_None` | 278 | 284 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 117 | 103 | inferred_complete_timeline |
| `Action_None` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |
| `Action_None` | 138 | 151 | 14 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_None` | 168 | 182 | 15 | inferred_complete_timeline |
| `Action_None` | 186 | 190 | 5 | inferred_complete_timeline |
| `Action_None` | 192 | 195 | 4 | inferred_complete_timeline |
| `Action_None` | 198 | 218 | 21 | inferred_complete_timeline |
| `Action_None` | 224 | 531 | 308 | inferred_complete_timeline |
| `Action_None` | 537 | 549 | 13 | inferred_complete_timeline |
| `Action_None` | 556 | 558 | 3 | inferred_complete_timeline |
| `Action_None` | 560 | 562 | 3 | inferred_complete_timeline |
| `Action_None` | 566 | 569 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage6 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–432
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 357 | 343 | inferred_complete_timeline |
| `Action_None` | 414 | 419 | 6 | inferred_complete_timeline |
| `Action_None` | 426 | 432 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 82 | 68 | inferred_complete_timeline |
| `Action_None` | 84 | 88 | 5 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 258 | 164 | inferred_complete_timeline |
| `Action_None` | 261 | 276 | 16 | inferred_complete_timeline |
| `Action_None` | 278 | 284 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 75 | 61 | inferred_complete_timeline |
| `Action_None` | 79 | 90 | 12 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 138 | 26 | inferred_complete_timeline |
| `Action_None` | 141 | 148 | 8 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 169 | 16 | inferred_complete_timeline |
| `Action_None` | 188 | 193 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 555

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 77 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 99 | 20 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 109 | 114 | 6 | inferred_complete_timeline |
| `Action_None` | 116 | 256 | 141 | inferred_complete_timeline |
| `Action_None` | 265 | 569 | 305 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 76 | 62 | inferred_complete_timeline |
| `Action_None` | 81 | 109 | 29 | inferred_complete_timeline |
| `Action_None` | 111 | 203 | 93 | inferred_complete_timeline |
| `Action_None` | 205 | 221 | 17 | inferred_complete_timeline |
| `Action_None` | 224 | 261 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 289 | 275 | inferred_complete_timeline |
| `Action_None` | 298 | 301 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–421
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 230 | 216 | inferred_complete_timeline |
| `Action_None` | 239 | 335 | 97 | inferred_complete_timeline |
| `Action_None` | 338 | 421 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 569 | 555 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 211 | 197 | inferred_complete_timeline |
| `Action_None` | 214 | 569 | 356 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 207 | 193 | inferred_complete_timeline |
| `Action_None` | 212 | 537 | 326 | inferred_complete_timeline |
| `Action_None` | 542 | 569 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 193 | 163 | inferred_complete_timeline |
| `Action_CatchKick` | 194 | 200 | 7 | inferred_complete_timeline |
| `Action_None` | 201 | 209 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 210 | 569 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–566
- **Visible Samples:** 546

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 303 | 289 | inferred_complete_timeline |
| `Action_None` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_None` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_None` | 322 | 325 | 4 | inferred_complete_timeline |
| `Action_None` | 329 | 330 | 2 | inferred_complete_timeline |
| `Action_None` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_None` | 335 | 544 | 210 | inferred_complete_timeline |
| `Action_None` | 546 | 548 | 3 | inferred_complete_timeline |
| `Action_None` | 550 | 566 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–566
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 321 | 307 | inferred_complete_timeline |
| `Action_None` | 327 | 557 | 231 | inferred_complete_timeline |
| `Action_None` | 559 | 566 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 395 | 381 | inferred_complete_timeline |
| `Action_None` | 398 | 569 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 569 | 555 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 569 | 555 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 34–215 | 90 | 11 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 41–126 | 72 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 147–191 | 21 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 199–296 | 98 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 267–569 | 303 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 276–293 | 18 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 286–289 | 4 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 302–386 | 85 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 310–569 | 260 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 318–328 | 8 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 324–351 | 15 | 4 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 333–338 | 6 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 349–391 | 31 | 3 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 354–397 | 27 | 7 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 355–569 | 215 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 358–395 | 12 | 4 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 360–361 | 2 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 385–386 | 2 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 394–398 | 5 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 431–432 | 2 | 1 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 449–569 | 117 | 3 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 475–478 | 4 | 1 | Undefined position; Undefined team |
| `47` | `71` | Position_Unknown | Team_Unknown | 494–569 | 76 | 1 | Undefined position; Undefined team |
| `48` | `73` | Position_Unknown | Team_Unknown | 520–525 | 6 | 1 | Undefined position; Undefined team |
| `49` | `76` | Position_Unknown | Team_Unknown | 529–542 | 11 | 2 | Undefined position; Undefined team |
| `50` | `78` | Position_Unknown | Team_Unknown | 530–569 | 26 | 4 | Undefined position; Undefined team |
| `51` | `80` | Position_Unknown | Team_Unknown | 537–569 | 27 | 4 | Undefined position; Undefined team |
| `52` | `83` | Position_Unknown | Team_Unknown | 553–569 | 9 | 2 | Undefined position; Undefined team |
| `53` | `84` | Position_Unknown | Team_Unknown | 560–561 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CrossGoalLine` on target `20` (Kick_Returner1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Kicker` position mapped to `offense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 153 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '20' has invalid range: start=570, end=569. Clamping end to start.
- ⚠️ Action 'Action_None' range [15-117] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-151] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-182] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-218] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-531] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-549] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-558] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-562] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-211] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-77] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-99] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-256] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-109] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-203] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-357] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-432] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-75] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-138] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-148] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-169] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-321] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-557] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-566] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-258] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-276] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-284] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-569] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-288] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-569] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-395] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-569] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-230] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-335] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-421] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-207] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-537] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-128] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-171] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-569] for track '14' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-289] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-303] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-544] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-548] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-566] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-569] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-110] for track '18' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-276] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-284] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-22] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-240] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-280] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-371] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [210-569] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [15-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-569] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-39] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-46] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-71] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-83] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-130] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-191] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-296] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-293] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-386] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-569] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-330] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-338] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-356] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-391] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-365] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-387] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-393] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-569] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-361] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-373] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-395] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-398] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-516] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-532] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-569] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-478] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-525] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-533] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-542] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-535] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-547] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-557] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-538] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-553] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-561] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-569] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-557] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '53' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 570. Video range is [0, 569].

</details>