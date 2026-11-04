# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_43`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 689
- **Player Tracks:** 60
- **Ball Tracks:** 0
- **Action Segments:** 199
- **Validation Warnings:** 257
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
- **Inferred Coverage Segments (Action_None):** 184
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `16` | `16` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `16` | `16` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `23` | `22` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `22` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `23` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `0` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `1` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `10` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `11` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `12` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `7` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `8` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `9` | `Group` | 0 | START | 0 | 2 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `16` | `16` | 3 | START | 3 | 87 |
| ✅ EXACT | `Action_KickBall` | Kicker | `16` | `16` | 88 | START | 88 | 93 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `23` | `22` | 183 | START | 183 | 212 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `23` | `22` | 251 | START | 251 | 310 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `23` | `22` | 679 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 662

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_KickApproach` | 3 | 87 | 85 | inferred_complete_timeline |
| `Action_KickBall` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_None` | 94 | 182 | 89 | inferred_complete_timeline |
| `Action_None` | 184 | 402 | 219 | inferred_complete_timeline |
| `Action_None` | 415 | 430 | 16 | inferred_complete_timeline |
| `Action_None` | 439 | 488 | 50 | inferred_complete_timeline |
| `Action_None` | 495 | 497 | 3 | inferred_complete_timeline |
| `Action_None` | 499 | 689 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 220 | 218 | inferred_complete_timeline |
| `Action_None` | 222 | 301 | 80 | inferred_complete_timeline |
| `Action_None` | 323 | 325 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–368
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 262 | 260 | inferred_complete_timeline |
| `Action_None` | 316 | 317 | 2 | inferred_complete_timeline |
| `Action_None` | 355 | 368 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 60 | 58 | inferred_complete_timeline |
| `Action_None` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_None` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_None` | 82 | 98 | 17 | inferred_complete_timeline |
| `Action_None` | 101 | 294 | 194 | inferred_complete_timeline |
| `Action_None` | 296 | 313 | 18 | inferred_complete_timeline |
| `Action_None` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_None` | 323 | 324 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–339
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 96 | 94 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 258 | 153 | inferred_complete_timeline |
| `Action_None` | 261 | 335 | 75 | inferred_complete_timeline |
| `Action_None` | 338 | 339 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–302
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 175 | 173 | inferred_complete_timeline |
| `Action_None` | 177 | 299 | 123 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 99 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 62 | 60 | inferred_complete_timeline |
| `Action_None` | 68 | 96 | 29 | inferred_complete_timeline |
| `Action_None` | 98 | 277 | 180 | inferred_complete_timeline |
| `Action_None` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 293 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–308
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 64 | 62 | inferred_complete_timeline |
| `Action_None` | 67 | 247 | 181 | inferred_complete_timeline |
| `Action_None` | 252 | 299 | 48 | inferred_complete_timeline |
| `Action_None` | 301 | 304 | 4 | inferred_complete_timeline |
| `Action_None` | 306 | 308 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–409
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 193 | 191 | inferred_complete_timeline |
| `Action_None` | 196 | 222 | 27 | inferred_complete_timeline |
| `Action_None` | 224 | 230 | 7 | inferred_complete_timeline |
| `Action_None` | 297 | 308 | 12 | inferred_complete_timeline |
| `Action_None` | 310 | 321 | 12 | inferred_complete_timeline |
| `Action_None` | 323 | 328 | 6 | inferred_complete_timeline |
| `Action_None` | 330 | 333 | 4 | inferred_complete_timeline |
| `Action_None` | 381 | 398 | 18 | inferred_complete_timeline |
| `Action_None` | 402 | 409 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 68 | 66 | inferred_complete_timeline |
| `Action_None` | 71 | 231 | 161 | inferred_complete_timeline |
| `Action_None` | 235 | 286 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 146 | 144 | inferred_complete_timeline |
| `Action_None` | 148 | 222 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 249 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–412
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 97 | 95 | inferred_complete_timeline |
| `Action_None` | 103 | 231 | 129 | inferred_complete_timeline |
| `Action_None` | 236 | 412 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 144 | 142 | inferred_complete_timeline |
| `Action_None` | 147 | 173 | 27 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 220 | 40 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–686
- **Visible Samples:** 678

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 233 | 231 | inferred_complete_timeline |
| `Action_None` | 235 | 280 | 46 | inferred_complete_timeline |
| `Action_None` | 283 | 286 | 4 | inferred_complete_timeline |
| `Action_None` | 289 | 394 | 106 | inferred_complete_timeline |
| `Action_None` | 397 | 679 | 283 | inferred_complete_timeline |
| `Action_None` | 682 | 686 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 220 | 218 | inferred_complete_timeline |
| `Action_None` | 225 | 229 | 5 | inferred_complete_timeline |
| `Action_None` | 231 | 253 | 23 | inferred_complete_timeline |
| `Action_None` | 258 | 319 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 110–229 | 119 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 112–318 | 192 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 128–265 | 138 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 132–269 | 138 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 145–689 | 507 | 10 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 168–310 | 143 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 246–253 | 8 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 250–310 | 59 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 262–351 | 90 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 263–689 | 397 | 6 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 268–312 | 43 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 274–342 | 69 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 298–321 | 24 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 302–689 | 386 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 307–682 | 364 | 4 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 332–689 | 339 | 7 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 335–368 | 17 | 3 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 336–363 | 28 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 344–427 | 16 | 2 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 355–689 | 335 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 356–382 | 25 | 3 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 356–689 | 315 | 7 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 361–689 | 328 | 2 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 361–689 | 320 | 2 | Undefined position; Undefined team |
| `42` | `47` | Position_Unknown | Team_Unknown | 375–671 | 292 | 4 | Undefined position; Undefined team |
| `43` | `50` | Position_Unknown | Team_Unknown | 381–689 | 292 | 6 | Undefined position; Undefined team |
| `44` | `51` | Position_Unknown | Team_Unknown | 393–689 | 297 | 1 | Undefined position; Undefined team |
| `45` | `53` | Position_Unknown | Team_Unknown | 395–396 | 2 | 1 | Undefined position; Undefined team |
| `46` | `54` | Position_Unknown | Team_Unknown | 400–681 | 273 | 2 | Undefined position; Undefined team |
| `47` | `55` | Position_Unknown | Team_Unknown | 411–441 | 10 | 3 | Undefined position; Undefined team |
| `48` | `57` | Position_Unknown | Team_Unknown | 416–689 | 274 | 1 | Undefined position; Undefined team |
| `49` | `58` | Position_Unknown | Team_Unknown | 422–515 | 94 | 1 | Undefined position; Undefined team |
| `50` | `59` | Position_Unknown | Team_Unknown | 422–495 | 74 | 1 | Undefined position; Undefined team |
| `51` | `60` | Position_Unknown | Team_Unknown | 426–689 | 261 | 3 | Undefined position; Undefined team |
| `52` | `61` | Position_Unknown | Team_Unknown | 429–689 | 261 | 1 | Undefined position; Undefined team |
| `53` | `64` | Position_Unknown | Team_Unknown | 443–689 | 247 | 1 | Undefined position; Undefined team |
| `54` | `65` | Position_Unknown | Team_Unknown | 444–639 | 196 | 1 | Undefined position; Undefined team |
| `55` | `66` | Position_Unknown | Team_Unknown | 449–609 | 104 | 5 | Undefined position; Undefined team |
| `56` | `67` | Position_Unknown | Team_Unknown | 502–509 | 8 | 1 | Undefined position; Undefined team |
| `57` | `68` | Position_Unknown | Team_Unknown | 514–516 | 3 | 1 | Undefined position; Undefined team |
| `58` | `69` | Position_Unknown | Team_Unknown | 546–548 | 3 | 1 | Undefined position; Undefined team |
| `59` | `71` | Position_Unknown | Team_Unknown | 677–689 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CrossGoalLine` on target `23` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kicker` position mapped to `offense` team
- ⚠️ 43 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 43 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 86 |
| Missing visible bounding boxes during action | 169 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '22' has invalid range: start=679, end=310. Clamping end to start.
- ⚠️ Action 'Action_None' range [3-220] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-301] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-68] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-231] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-286] for track '1' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-173] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-220] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-233] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-280] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-394] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-679] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-686] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-146] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-253] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-319] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-249] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-175] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-299] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-262] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-368] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-335] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-193] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-308] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-321] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-333] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-398] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-409] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-98] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-294] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-313] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-247] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-96] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-277] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-293] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-231] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-412] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-182] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-402] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-430] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-488] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-497] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-166] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-271] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-284] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-313] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-322] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-369] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-378] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-382] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-420] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-689] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [183-212] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [251-310] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-283] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-302] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-310] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-351] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-319] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-364] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-390] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-684] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-308] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-342] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-321] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-415] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-411] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-673] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-682] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-372] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-381] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-398] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-402] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-422] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-339] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-349] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-368] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-363] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-353] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-427] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-689] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-358] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-372] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-382] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-362] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-392] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-614] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-619] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-624] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-671] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-376] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-689] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-380] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-388] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-430] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-671] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-383] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-387] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-401] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-650] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-689] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-689] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-412] for track '46' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-681] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-432] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-441] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-689] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-515] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-495] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-674] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-685] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-689] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-639] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-520] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-541] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-547] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-569] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-609] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-509] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-516] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-548] for track '58' has 1 frames without a visible bounding box.
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

</details>