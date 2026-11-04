# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_59`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 69
- **Ball Tracks:** 0
- **Action Segments:** 295
- **Validation Warnings:** 379
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 281
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `6` | `6` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `6` | `6` |
| ⚠️ START CHANGED | `Action_CatchKick` | Position_Unknown | Team_Unknown | `37` | `32` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `37` | `32` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `37` | `32` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `0` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `10` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `11` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `13` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `14` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `4` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `6` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `6` | `6` | 26 | START | 26 | 79 |
| ✅ EXACT | `Action_KickBall` | Kicker | `6` | `6` | 80 | START | 80 | 82 |
| ⚠️ START CHANGED | `Action_CatchKick` | Position_Unknown | `37` | `32` | 198 | START | 199 | 218 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `37` | `32` | 219 | START | 219 | 239 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `37` | `32` | 595 | START | 595 | 599 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–400
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_KickApproach` | 26 | 79 | 54 | inferred_complete_timeline |
| `Action_KickBall` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_None` | 83 | 392 | 310 | inferred_complete_timeline |
| `Action_None` | 394 | 400 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 58 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 54 | 29 | inferred_complete_timeline |
| `Action_None` | 57 | 67 | 11 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_None` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 82 | 124 | 43 | inferred_complete_timeline |
| `Action_None` | 126 | 268 | 143 | inferred_complete_timeline |
| `Action_None` | 274 | 290 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 47 | 94 | 48 | inferred_complete_timeline |
| `Action_None` | 96 | 237 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 136 | 111 | inferred_complete_timeline |
| `Action_None` | 138 | 146 | 9 | inferred_complete_timeline |
| `Action_None` | 148 | 152 | 5 | inferred_complete_timeline |
| `Action_None` | 154 | 241 | 88 | inferred_complete_timeline |
| `Action_None` | 252 | 254 | 3 | inferred_complete_timeline |
| `Action_None` | 278 | 282 | 5 | inferred_complete_timeline |
| `Action_None` | 289 | 297 | 9 | inferred_complete_timeline |
| `Action_None` | 317 | 323 | 7 | inferred_complete_timeline |
| `Action_None` | 325 | 406 | 82 | inferred_complete_timeline |
| `Action_None` | 412 | 599 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 50 | 25 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 57 | 133 | 77 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 192 | 45 | inferred_complete_timeline |
| `Action_None` | 196 | 205 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 36 | 38 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 138 | 113 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–554
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 386 | 361 | inferred_complete_timeline |
| `Action_None` | 392 | 393 | 2 | inferred_complete_timeline |
| `Action_None` | 395 | 404 | 10 | inferred_complete_timeline |
| `Action_None` | 407 | 443 | 37 | inferred_complete_timeline |
| `Action_None` | 446 | 526 | 81 | inferred_complete_timeline |
| `Action_None` | 530 | 534 | 5 | inferred_complete_timeline |
| `Action_None` | 538 | 554 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 223 | 198 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 216 | 191 | inferred_complete_timeline |
| `Action_None` | 220 | 227 | 8 | inferred_complete_timeline |
| `Action_None` | 229 | 234 | 6 | inferred_complete_timeline |
| `Action_None` | 242 | 258 | 17 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 276 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 192 | 202 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 193 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 202 | 177 | inferred_complete_timeline |
| `Action_None` | 204 | 218 | 15 | inferred_complete_timeline |
| `Action_None` | 230 | 234 | 5 | inferred_complete_timeline |
| `Action_None` | 249 | 266 | 18 | inferred_complete_timeline |
| `Action_None` | 282 | 599 | 318 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 216 | 191 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 230 | 8 | inferred_complete_timeline |
| `Action_None` | 232 | 234 | 3 | inferred_complete_timeline |
| `Action_None` | 236 | 245 | 10 | inferred_complete_timeline |
| `Action_None` | 250 | 256 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 31–44 | 14 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 59–293 | 220 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 63–315 | 210 | 6 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 64–569 | 479 | 10 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 76–268 | 120 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 124–587 | 432 | 13 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 124–263 | 140 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 130–290 | 157 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 145–146 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 155–161 | 7 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 155–599 | 408 | 15 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 162–239 | 40 | 7 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 190–599 | 392 | 4 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 199–599 | 346 | 20 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 224–599 | 356 | 8 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 229–255 | 14 | 3 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 230–468 | 156 | 8 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 247–599 | 346 | 6 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 249–307 | 57 | 3 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 269–550 | 278 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 278–599 | 307 | 7 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 288–314 | 26 | 2 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 303–309 | 7 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 304–546 | 153 | 12 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 306–599 | 286 | 2 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 323–599 | 217 | 16 | Undefined position; Undefined team |
| `46` | `58` | Position_Unknown | Team_Unknown | 328–599 | 260 | 4 | Undefined position; Undefined team |
| `47` | `59` | Position_Unknown | Team_Unknown | 337–599 | 259 | 4 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 337–339 | 3 | 1 | Undefined position; Undefined team |
| `49` | `61` | Position_Unknown | Team_Unknown | 338–340 | 3 | 1 | Undefined position; Undefined team |
| `50` | `64` | Position_Unknown | Team_Unknown | 341–348 | 8 | 1 | Undefined position; Undefined team |
| `51` | `65` | Position_Unknown | Team_Unknown | 343–363 | 6 | 2 | Undefined position; Undefined team |
| `52` | `66` | Position_Unknown | Team_Unknown | 351–599 | 204 | 11 | Undefined position; Undefined team |
| `53` | `69` | Position_Unknown | Team_Unknown | 356–562 | 190 | 3 | Undefined position; Undefined team |
| `54` | `71` | Position_Unknown | Team_Unknown | 383–599 | 207 | 3 | Undefined position; Undefined team |
| `55` | `76` | Position_Unknown | Team_Unknown | 427–429 | 3 | 1 | Undefined position; Undefined team |
| `56` | `78` | Position_Unknown | Team_Unknown | 443–463 | 16 | 3 | Undefined position; Undefined team |
| `57` | `79` | Position_Unknown | Team_Unknown | 455–480 | 8 | 4 | Undefined position; Undefined team |
| `58` | `80` | Position_Unknown | Team_Unknown | 498–599 | 91 | 2 | Undefined position; Undefined team |
| `59` | `82` | Position_Unknown | Team_Unknown | 549–552 | 4 | 1 | Undefined position; Undefined team |
| `60` | `83` | Position_Unknown | Team_Unknown | 553–554 | 2 | 1 | Undefined position; Undefined team |
| `61` | `85` | Position_Unknown | Team_Unknown | 557–590 | 4 | 2 | Undefined position; Undefined team |
| `62` | `87` | Position_Unknown | Team_Unknown | 563–566 | 4 | 1 | Undefined position; Undefined team |
| `63` | `88` | Position_Unknown | Team_Unknown | 565–599 | 35 | 1 | Undefined position; Undefined team |
| `64` | `89` | Position_Unknown | Team_Unknown | 565–567 | 3 | 1 | Undefined position; Undefined team |
| `65` | `91` | Position_Unknown | Team_Unknown | 578–584 | 7 | 1 | Undefined position; Undefined team |
| `66` | `92` | Position_Unknown | Team_Unknown | 581–599 | 19 | 1 | Undefined position; Undefined team |
| `67` | `93` | Position_Unknown | Team_Unknown | 590–599 | 10 | 1 | Undefined position; Undefined team |
| `68` | `94` | Position_Unknown | Team_Unknown | 596–597 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_CatchKick` for actor_track_id `37` (Position_Unknown): Annotated start 198 != Inferred start 199
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `37` (18 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ 54 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 54 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 108 |
| Missing visible bounding boxes during action | 270 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [26-136] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-146] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-241] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-282] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-297] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-323] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-406] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-227] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-258] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-276] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-245] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-386] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-393] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-404] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-443] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-526] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-534] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-554] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-392] for track '6' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-400] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-218] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-266] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-599] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-193] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-237] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-58] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-133] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-192] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-54] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-67] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-124] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-268] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-290] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-72] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-223] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-263] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-293] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-156] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-315] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-268] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-399] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-532] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-537] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-548] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-554] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-564] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-569] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-189] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-262] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-276] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-290] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-387] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-433] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-449] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-455] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-461] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-587] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-263] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-161] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-246] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-285] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-293] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-377] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-410] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-420] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-425] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-430] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-446] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-454] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-471] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-578] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-599] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-174] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-254] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-273] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-599] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [219-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [250-286] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [291-313] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [318-410] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [412-416] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [420-430] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [432-444] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [446-447] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [457-506] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [513-514] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [516-518] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [521-523] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [527-534] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [536-539] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [542-544] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [546-548] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [552-567] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-291] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-307] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-399] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-406] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-483] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-599] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-248] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-342] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-461] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-468] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-266] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-314] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-323] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-567] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-599] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-277] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-291] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-307] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-300] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-550] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-509] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-516] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-524] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-534] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-547] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-564] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-306] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-314] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-309] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-339] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-434] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-440] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-488] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-497] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-514] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-534] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-546] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-356] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-599] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-331] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-384] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-407] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-425] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-435] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-452] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-467] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-483] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-492] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-558] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-567] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-576] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-587] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-554] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-575] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-599] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-341] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-516] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-599] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-339] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-348] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-346] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-353] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-378] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-426] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-443] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-454] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-468] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-488] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-493] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-531] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-552] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-599] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-537] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-556] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-562] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-405] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-429] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-452] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-457] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-480] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-582] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-552] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-590] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-566] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-567] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-584] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-599] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-597] for track '68' has 1 frames without a visible bounding box.
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

</details>