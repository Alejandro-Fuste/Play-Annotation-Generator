# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_68

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_68`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 210
- **Validation Warnings:** 260
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 197
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `1` | `1` |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner1 | defense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `12` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `15` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `16` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `6` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `9` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `5` | `5` | 5 | START | 5 | 78 |
| ✅ EXACT | `Action_KickBall` | Kicker | `5` | `5` | 79 | START | 79 | 85 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `1` | `1` | 185 | START | 185 | 199 |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner1 | `1` | `1` | 228 | START | 228 | 599 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner1 | `1` | `1` | 600 | START | N/A | N/A |

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
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_KickApproach` | 5 | 78 | 74 | inferred_complete_timeline |
| `Action_KickBall` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_None` | 86 | 161 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 56 | 52 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 108 | 24 | inferred_complete_timeline |
| `Action_None` | 115 | 197 | 83 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 219 | 223 | 5 | inferred_complete_timeline |
| `Action_None` | 225 | 228 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 173 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 56 | 52 | inferred_complete_timeline |
| `Action_None` | 68 | 150 | 83 | inferred_complete_timeline |
| `Action_None` | 173 | 241 | 69 | inferred_complete_timeline |
| `Action_None` | 244 | 591 | 348 | inferred_complete_timeline |
| `Action_None` | 593 | 599 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–540
- **Visible Samples:** 516

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 129 | 125 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_None` | 145 | 155 | 11 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 180 | 8 | inferred_complete_timeline |
| `Action_None` | 182 | 540 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–555
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 110 | 106 | inferred_complete_timeline |
| `Action_None` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_None` | 124 | 165 | 42 | inferred_complete_timeline |
| `Action_None` | 183 | 198 | 16 | inferred_complete_timeline |
| `Action_None` | 200 | 246 | 47 | inferred_complete_timeline |
| `Action_None` | 251 | 301 | 51 | inferred_complete_timeline |
| `Action_None` | 305 | 555 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 109 | 105 | inferred_complete_timeline |
| `Action_None` | 118 | 124 | 7 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_None` | 134 | 200 | 67 | inferred_complete_timeline |
| `Action_None` | 209 | 272 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–505
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 143 | 139 | inferred_complete_timeline |
| `Action_None` | 149 | 167 | 19 | inferred_complete_timeline |
| `Action_None` | 175 | 505 | 331 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 352 | 348 | inferred_complete_timeline |
| `Action_None` | 356 | 599 | 244 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 441 | 437 | inferred_complete_timeline |
| `Action_None` | 446 | 599 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–561
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 226 | 222 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 241 | 4 | inferred_complete_timeline |
| `Action_None` | 243 | 561 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–350
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 97 | 93 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 111 | 7 | inferred_complete_timeline |
| `Action_None` | 113 | 191 | 79 | inferred_complete_timeline |
| `Action_None` | 193 | 196 | 4 | inferred_complete_timeline |
| `Action_None` | 198 | 202 | 5 | inferred_complete_timeline |
| `Action_None` | 204 | 312 | 109 | inferred_complete_timeline |
| `Action_None` | 319 | 330 | 12 | inferred_complete_timeline |
| `Action_None` | 332 | 335 | 4 | inferred_complete_timeline |
| `Action_None` | 338 | 350 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–432
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 219 | 215 | inferred_complete_timeline |
| `Action_None` | 221 | 255 | 35 | inferred_complete_timeline |
| `Action_None` | 258 | 268 | 11 | inferred_complete_timeline |
| `Action_None` | 275 | 432 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_CatchKick` | 185 | 199 | 15 | inferred_complete_timeline |
| `Action_None` | 200 | 227 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 228 | 599 | 372 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–546
- **Visible Samples:** 546

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 281 | 277 | inferred_complete_timeline |
| `Action_None` | 283 | 546 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–538
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 307 | 303 | inferred_complete_timeline |
| `Action_None` | 310 | 538 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 394 | 390 | inferred_complete_timeline |
| `Action_None` | 400 | 599 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–423
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 423 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 190 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–301 | 233 | 11 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 48–253 | 158 | 7 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 53–89 | 34 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 81–535 | 342 | 10 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 92–95 | 4 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 95–96 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 106–129 | 12 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 120–597 | 471 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 150–170 | 20 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 164–333 | 159 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 182–245 | 17 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 186–599 | 412 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 193–517 | 271 | 7 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 203–333 | 52 | 8 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 210–242 | 27 | 5 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 213–230 | 11 | 4 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 261–562 | 299 | 4 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 261–263 | 3 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 292–599 | 307 | 2 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 296–346 | 51 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 303–586 | 284 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 327–333 | 4 | 2 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 337–422 | 33 | 9 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 344–599 | 256 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 368–371 | 4 | 1 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 370–599 | 230 | 1 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 396–439 | 31 | 5 | Undefined position; Undefined team |
| `46` | `72` | Position_Unknown | Team_Unknown | 456–457 | 2 | 1 | Undefined position; Undefined team |
| `47` | `73` | Position_Unknown | Team_Unknown | 468–479 | 11 | 2 | Undefined position; Undefined team |
| `48` | `74` | Position_Unknown | Team_Unknown | 473–474 | 2 | 1 | Undefined position; Undefined team |
| `49` | `75` | Position_Unknown | Team_Unknown | 482–587 | 86 | 5 | Undefined position; Undefined team |
| `50` | `78` | Position_Unknown | Team_Unknown | 544–546 | 3 | 1 | Undefined position; Undefined team |
| `51` | `80` | Position_Unknown | Team_Unknown | 555–556 | 2 | 1 | Undefined position; Undefined team |
| `52` | `81` | Position_Unknown | Team_Unknown | 567–574 | 8 | 1 | Undefined position; Undefined team |
| `53` | `82` | Position_Unknown | Team_Unknown | 568–570 | 3 | 1 | Undefined position; Undefined team |
| `54` | `83` | Position_Unknown | Team_Unknown | 568–577 | 9 | 2 | Undefined position; Undefined team |
| `55` | `86` | Position_Unknown | Team_Unknown | 575–576 | 2 | 1 | Undefined position; Undefined team |
| `56` | `89` | Position_Unknown | Team_Unknown | 596–599 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CrossGoalLine` on target `1` (Kick_Returner1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 181 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '1' has invalid range: start=600, end=599. Clamping end to start.
- ⚠️ Action 'Action_None' range [5-226] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-561] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-441] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-307] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-538] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-423] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-173] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-394] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-190] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-129] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-155] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-540] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-281] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-546] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-219] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-255] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-432] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-200] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-272] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-191] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-312] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-330] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-350] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-143] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-505] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-165] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-198] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-246] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-301] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-555] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-241] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-591] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-599] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-352] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 5, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [5-5] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-117] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-132] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-183] for track '19' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-296] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-123] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-92] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-119] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-383] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-409] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-535] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-597] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-163] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-190] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-323] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-194] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-205] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-342] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-231] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-447] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-452] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-517] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-220] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-238] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-256] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-235] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-346] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-358] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-562] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-599] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-346] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-586] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-350] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-358] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-364] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-368] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-379] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-599] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-599] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-422] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-434] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-439] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-474] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-479] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-532] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-562] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-587] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-546] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-556] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-574] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-570] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-572] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-577] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-576] for track '55' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 600. Video range is [0, 599].

</details>