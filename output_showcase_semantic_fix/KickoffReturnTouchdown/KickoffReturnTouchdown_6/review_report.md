# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_6`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 689
- **Player Tracks:** 56
- **Ball Tracks:** 1
- **Action Segments:** 259
- **Validation Warnings:** 320
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 244
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `8` | `8` |
| ⚠️ START CHANGED | `Action_CatchKick` | Position_Unknown | Team_Unknown | `50` | `33` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `50` | `33` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `50` | `33` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `0` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `1` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `11` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `16` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `2` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `3` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `5` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `6` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `7` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `8` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `9` | `Group` | 0 | START | 0 | 71 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `8` | `8` | 72 | START | 72 | 136 |
| ✅ EXACT | `Action_KickBall` | Kicker | `8` | `8` | 137 | START | 137 | 143 |
| ⚠️ START CHANGED | `Action_CatchKick` | Position_Unknown | `50` | `33` | 249 | START | 278 | 278 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `50` | `33` | 283 | START | 286 | 287 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `50` | `33` | 687 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–417
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_KickApproach` | 72 | 136 | 65 | inferred_complete_timeline |
| `Action_KickBall` | 137 | 143 | 7 | inferred_complete_timeline |
| `Action_None` | 144 | 385 | 242 | inferred_complete_timeline |
| `Action_None` | 387 | 417 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–408
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 171 | 100 | inferred_complete_timeline |
| `Action_None` | 173 | 181 | 9 | inferred_complete_timeline |
| `Action_None` | 183 | 186 | 4 | inferred_complete_timeline |
| `Action_None` | 196 | 207 | 12 | inferred_complete_timeline |
| `Action_None` | 209 | 249 | 41 | inferred_complete_timeline |
| `Action_None` | 252 | 290 | 39 | inferred_complete_timeline |
| `Action_None` | 292 | 329 | 38 | inferred_complete_timeline |
| `Action_None` | 333 | 371 | 39 | inferred_complete_timeline |
| `Action_None` | 376 | 382 | 7 | inferred_complete_timeline |
| `Action_None` | 387 | 408 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–372
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 165 | 94 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 248 | 75 | inferred_complete_timeline |
| `Action_None` | 251 | 282 | 32 | inferred_complete_timeline |
| `Action_None` | 284 | 296 | 13 | inferred_complete_timeline |
| `Action_None` | 299 | 326 | 28 | inferred_complete_timeline |
| `Action_None` | 329 | 345 | 17 | inferred_complete_timeline |
| `Action_None` | 364 | 372 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–396
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 248 | 177 | inferred_complete_timeline |
| `Action_None` | 254 | 262 | 9 | inferred_complete_timeline |
| `Action_None` | 265 | 333 | 69 | inferred_complete_timeline |
| `Action_None` | 336 | 354 | 19 | inferred_complete_timeline |
| `Action_None` | 359 | 372 | 14 | inferred_complete_timeline |
| `Action_None` | 375 | 396 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 251 | 180 | inferred_complete_timeline |
| `Action_None` | 253 | 353 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 84 | 195 | 112 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 258 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–421
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 131 | 60 | inferred_complete_timeline |
| `Action_None` | 133 | 239 | 107 | inferred_complete_timeline |
| `Action_None` | 244 | 329 | 86 | inferred_complete_timeline |
| `Action_None` | 331 | 421 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 110 | 39 | inferred_complete_timeline |
| `Action_None` | 113 | 136 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 133 | 62 | inferred_complete_timeline |
| `Action_None` | 135 | 247 | 113 | inferred_complete_timeline |
| `Action_None` | 250 | 264 | 15 | inferred_complete_timeline |
| `Action_None` | 266 | 287 | 22 | inferred_complete_timeline |
| `Action_None` | 289 | 307 | 19 | inferred_complete_timeline |
| `Action_None` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_None` | 313 | 329 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 628

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 176 | 105 | inferred_complete_timeline |
| `Action_None` | 184 | 187 | 4 | inferred_complete_timeline |
| `Action_None` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 218 | 5 | inferred_complete_timeline |
| `Action_None` | 220 | 234 | 15 | inferred_complete_timeline |
| `Action_None` | 242 | 247 | 6 | inferred_complete_timeline |
| `Action_None` | 259 | 290 | 32 | inferred_complete_timeline |
| `Action_None` | 297 | 354 | 58 | inferred_complete_timeline |
| `Action_None` | 356 | 363 | 8 | inferred_complete_timeline |
| `Action_None` | 367 | 453 | 87 | inferred_complete_timeline |
| `Action_None` | 456 | 479 | 24 | inferred_complete_timeline |
| `Action_None` | 482 | 488 | 7 | inferred_complete_timeline |
| `Action_None` | 491 | 667 | 177 | inferred_complete_timeline |
| `Action_None` | 670 | 671 | 2 | inferred_complete_timeline |
| `Action_None` | 674 | 689 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–339
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 181 | 110 | inferred_complete_timeline |
| `Action_None` | 183 | 193 | 11 | inferred_complete_timeline |
| `Action_None` | 197 | 284 | 88 | inferred_complete_timeline |
| `Action_None` | 290 | 300 | 11 | inferred_complete_timeline |
| `Action_None` | 302 | 339 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–368
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 181 | 110 | inferred_complete_timeline |
| `Action_None` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_None` | 191 | 198 | 8 | inferred_complete_timeline |
| `Action_None` | 207 | 209 | 3 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 226 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 265 | 38 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_None` | 281 | 283 | 3 | inferred_complete_timeline |
| `Action_None` | 285 | 289 | 5 | inferred_complete_timeline |
| `Action_None` | 299 | 368 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–461
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 110 | 39 | inferred_complete_timeline |
| `Action_None` | 119 | 131 | 13 | inferred_complete_timeline |
| `Action_None` | 133 | 163 | 31 | inferred_complete_timeline |
| `Action_None` | 168 | 177 | 10 | inferred_complete_timeline |
| `Action_None` | 198 | 242 | 45 | inferred_complete_timeline |
| `Action_None` | 311 | 341 | 31 | inferred_complete_timeline |
| `Action_None` | 343 | 461 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–22
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 22 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–425
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 205 | 134 | inferred_complete_timeline |
| `Action_None` | 207 | 266 | 60 | inferred_complete_timeline |
| `Action_None` | 275 | 279 | 5 | inferred_complete_timeline |
| `Action_None` | 283 | 295 | 13 | inferred_complete_timeline |
| `Action_None` | 298 | 304 | 7 | inferred_complete_timeline |
| `Action_None` | 307 | 380 | 74 | inferred_complete_timeline |
| `Action_None` | 382 | 417 | 36 | inferred_complete_timeline |
| `Action_None` | 424 | 425 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–658
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 71 | 42 | inferred_complete_timeline |
| `Action_None` | 72 | 179 | 108 | inferred_complete_timeline |
| `Action_None` | 182 | 195 | 14 | inferred_complete_timeline |
| `Action_None` | 199 | 248 | 50 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |
| `Action_None` | 262 | 285 | 24 | inferred_complete_timeline |
| `Action_None` | 289 | 337 | 49 | inferred_complete_timeline |
| `Action_None` | 347 | 351 | 5 | inferred_complete_timeline |
| `Action_None` | 380 | 391 | 12 | inferred_complete_timeline |
| `Action_None` | 402 | 407 | 6 | inferred_complete_timeline |
| `Action_None` | 417 | 418 | 2 | inferred_complete_timeline |
| `Action_None` | 420 | 421 | 2 | inferred_complete_timeline |
| `Action_None` | 423 | 457 | 35 | inferred_complete_timeline |
| `Action_None` | 459 | 643 | 185 | inferred_complete_timeline |
| `Action_None` | 654 | 658 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–375
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 326 | 255 | inferred_complete_timeline |
| `Action_None` | 329 | 375 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 38–439 | 180 | 16 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 43–235 | 142 | 6 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 79–97 | 13 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 124–237 | 52 | 11 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 127–596 | 428 | 13 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 141–356 | 207 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 146–158 | 13 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 160–164 | 5 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 192–206 | 15 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 193–233 | 8 | 4 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 232–269 | 37 | 2 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 238–258 | 20 | 2 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 260–415 | 92 | 4 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 260–397 | 125 | 5 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 274–275 | 2 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 278–589 | 299 | 7 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 297–429 | 129 | 3 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 306–627 | 309 | 7 | Undefined position; Undefined team |
| `36` | `60` | Position_Unknown | Team_Unknown | 344–409 | 42 | 5 | Undefined position; Undefined team |
| `37` | `61` | Position_Unknown | Team_Unknown | 347–689 | 341 | 3 | Undefined position; Undefined team |
| `38` | `63` | Position_Unknown | Team_Unknown | 356–365 | 10 | 1 | Undefined position; Undefined team |
| `39` | `65` | Position_Unknown | Team_Unknown | 370–421 | 46 | 2 | Undefined position; Undefined team |
| `40` | `66` | Position_Unknown | Team_Unknown | 383–405 | 21 | 2 | Undefined position; Undefined team |
| `41` | `69` | Position_Unknown | Team_Unknown | 391–399 | 9 | 1 | Undefined position; Undefined team |
| `42` | `72` | Position_Unknown | Team_Unknown | 452–619 | 157 | 5 | Undefined position; Undefined team |
| `43` | `73` | Position_Unknown | Team_Unknown | 471–663 | 186 | 2 | Undefined position; Undefined team |
| `44` | `74` | Position_Unknown | Team_Unknown | 484–486 | 3 | 1 | Undefined position; Undefined team |
| `45` | `75` | Position_Unknown | Team_Unknown | 486–551 | 66 | 1 | Undefined position; Undefined team |
| `46` | `77` | Position_Unknown | Team_Unknown | 493–497 | 5 | 1 | Undefined position; Undefined team |
| `47` | `79` | Position_Unknown | Team_Unknown | 526–665 | 137 | 2 | Undefined position; Undefined team |
| `48` | `80` | Position_Unknown | Team_Unknown | 529–689 | 161 | 1 | Undefined position; Undefined team |
| `49` | `81` | Position_Unknown | Team_Unknown | 535–622 | 87 | 2 | Undefined position; Undefined team |
| `50` | `82` | Position_Unknown | Team_Unknown | 539–581 | 43 | 1 | Undefined position; Undefined team |
| `51` | `83` | Position_Unknown | Team_Unknown | 543–620 | 78 | 1 | Undefined position; Undefined team |
| `52` | `84` | Position_Unknown | Team_Unknown | 559–560 | 2 | 1 | Undefined position; Undefined team |
| `54` | `88` | Position_Unknown | Team_Unknown | 585–592 | 8 | 1 | Undefined position; Undefined team |
| `55` | `90` | Position_Unknown | Team_Unknown | 607–641 | 28 | 3 | Undefined position; Undefined team |
| `56` | `93` | Position_Unknown | Team_Unknown | 682–689 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `53` | `87` | 572 | 572 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_CatchKick` for actor_track_id `50` (Position_Unknown): Annotated start 249 != Inferred start 278
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `50` (5 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `50` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 239 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Segment 'Action_CatchKick' for track '33' has invalid range: start=278, end=253. Clamping end to start.
- ⚠️ Segment 'Action_CrossGoalLine' for track '33' has invalid range: start=687, end=589. Clamping end to start.
- ⚠️ Action 'Action_None' range [72-133] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-247] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-264] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-287] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-307] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-176] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-290] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-354] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-363] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-453] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-479] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-488] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-667] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [670-671] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-181] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-193] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-284] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-300] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-339] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-181] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-198] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-265] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-289] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-368] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-171] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-181] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-207] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-249] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-290] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-329] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-371] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-382] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-408] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-248] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-262] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-333] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-354] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-372] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-396] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-248] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-282] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-296] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-326] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-345] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-372] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-385] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-417] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-239] for track '9' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-421] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-110] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-242] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-341] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-461] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-251] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-353] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-326] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-375] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-205] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-266] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-295] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-380] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-417] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-179] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-195] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-248] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-285] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-337] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-391] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-407] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-418] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-457] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-643] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-658] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-22] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-195] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-258] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-49] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-214] for track '17' has 9 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-224] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-343] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-436] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-164] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-182] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-224] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-86] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-201] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-246] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-263] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-293] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-326] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-345] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-384] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-465] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-596] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-338] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-348] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-206] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-269] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-254] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-266] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-336] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-415] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-373] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-385] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-397] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [286-287] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [289-294] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [296-298] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [303-584] for track '33' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [588-589] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-349] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-416] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-429] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-324] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-355] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-603] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-606] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-610] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-618] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-627] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-377] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-394] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-401] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-409] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-386] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-400] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-689] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-365] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-384] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-421] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-401] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-399] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-464] for track '42' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-604] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-609] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-616] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-619] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-492] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-663] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-486] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-551] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-497] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-629] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-665] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-689] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-604] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-622] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-581] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-620] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-592] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-609] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-638] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [640-641] for track '55' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.

</details>