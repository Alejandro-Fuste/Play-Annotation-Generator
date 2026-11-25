# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_99

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_99`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 59
- **Ball Tracks:** 0
- **Action Segments:** 210
- **Validation Warnings:** 263
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 197
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `7` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `11` | `11` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `45` | `31` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `45` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `0` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `1` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `10` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `11` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `13` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `15` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `2` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `3` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `4` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `7` | `Group` | 0 | START | 0 | 53 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `11` | `11` | 54 | START | 54 | 93 |
| ✅ EXACT | `Action_KickBall` | Kicker | `11` | `11` | 94 | START | 94 | 99 |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | `45` | `31` | 216 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `45` | `31` | 258 | START | 265 | 315 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 656

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_KickApproach` | 54 | 93 | 40 | inferred_complete_timeline |
| `Action_KickBall` | 94 | 99 | 6 | inferred_complete_timeline |
| `Action_None` | 100 | 100 | 1 | inferred_complete_timeline |
| `Action_None` | 104 | 117 | 14 | inferred_complete_timeline |
| `Action_None` | 119 | 659 | 541 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–375
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 375 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–625
- **Visible Samples:** 575

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 227 | 174 | inferred_complete_timeline |
| `Action_None` | 232 | 273 | 42 | inferred_complete_timeline |
| `Action_None` | 275 | 288 | 14 | inferred_complete_timeline |
| `Action_None` | 291 | 292 | 2 | inferred_complete_timeline |
| `Action_None` | 309 | 374 | 66 | inferred_complete_timeline |
| `Action_None` | 390 | 472 | 83 | inferred_complete_timeline |
| `Action_None` | 476 | 505 | 30 | inferred_complete_timeline |
| `Action_None` | 514 | 536 | 23 | inferred_complete_timeline |
| `Action_None` | 538 | 620 | 83 | inferred_complete_timeline |
| `Action_None` | 622 | 625 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 281 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 619

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 296 | 243 | inferred_complete_timeline |
| `Action_None` | 302 | 325 | 24 | inferred_complete_timeline |
| `Action_None` | 345 | 360 | 16 | inferred_complete_timeline |
| `Action_None` | 362 | 387 | 26 | inferred_complete_timeline |
| `Action_None` | 396 | 428 | 33 | inferred_complete_timeline |
| `Action_None` | 431 | 457 | 27 | inferred_complete_timeline |
| `Action_None` | 464 | 659 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 264 | 211 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–368
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 127 | 74 | inferred_complete_timeline |
| `Action_None` | 138 | 282 | 145 | inferred_complete_timeline |
| `Action_None` | 289 | 368 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 296 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 657

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 313 | 260 | inferred_complete_timeline |
| `Action_None` | 315 | 496 | 182 | inferred_complete_timeline |
| `Action_None` | 498 | 567 | 70 | inferred_complete_timeline |
| `Action_None` | 569 | 659 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 658

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 445 | 392 | inferred_complete_timeline |
| `Action_None` | 448 | 659 | 212 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 252 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 574

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 169 | 116 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 181 | 6 | inferred_complete_timeline |
| `Action_None` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_None` | 195 | 211 | 17 | inferred_complete_timeline |
| `Action_None` | 226 | 231 | 6 | inferred_complete_timeline |
| `Action_None` | 233 | 248 | 16 | inferred_complete_timeline |
| `Action_None` | 285 | 295 | 11 | inferred_complete_timeline |
| `Action_None` | 299 | 355 | 57 | inferred_complete_timeline |
| `Action_None` | 361 | 363 | 3 | inferred_complete_timeline |
| `Action_None` | 366 | 378 | 13 | inferred_complete_timeline |
| `Action_None` | 388 | 406 | 19 | inferred_complete_timeline |
| `Action_None` | 408 | 410 | 3 | inferred_complete_timeline |
| `Action_None` | 412 | 659 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 179 | 126 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 80 | 27 | inferred_complete_timeline |
| `Action_None` | 102 | 117 | 16 | inferred_complete_timeline |
| `Action_None` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 251 | 102 | inferred_complete_timeline |
| `Action_None` | 261 | 268 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 254 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 184 | 131 | inferred_complete_timeline |
| `Action_None` | 186 | 189 | 4 | inferred_complete_timeline |
| `Action_None` | 250 | 266 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 123 | 70 | inferred_complete_timeline |
| `Action_None` | 126 | 146 | 21 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 159 | 6 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_None` | 207 | 213 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 656

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 501 | 448 | inferred_complete_timeline |
| `Action_None` | 505 | 643 | 139 | inferred_complete_timeline |
| `Action_None` | 645 | 659 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 184 | 131 | inferred_complete_timeline |
| `Action_None` | 204 | 211 | 8 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 322 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 31–643 | 600 | 7 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 65–111 | 14 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 124–659 | 516 | 5 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 129–156 | 14 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 142–148 | 7 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 190–194 | 4 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 216–227 | 12 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 217–315 | 87 | 3 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 218–220 | 3 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 235–281 | 47 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 247–279 | 26 | 3 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 265–315 | 51 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 297–393 | 46 | 3 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 311–342 | 28 | 2 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 321–659 | 255 | 8 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 323–395 | 56 | 4 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 330–446 | 113 | 3 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 332–353 | 22 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 344–659 | 290 | 2 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 350–389 | 40 | 1 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 352–385 | 26 | 4 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 363–631 | 239 | 4 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 369–612 | 244 | 1 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 386–594 | 186 | 2 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 402–659 | 236 | 6 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 414–422 | 9 | 1 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 423–554 | 51 | 12 | Undefined position; Undefined team |
| `47` | `72` | Position_Unknown | Team_Unknown | 454–603 | 145 | 3 | Undefined position; Undefined team |
| `48` | `73` | Position_Unknown | Team_Unknown | 456–659 | 197 | 2 | Undefined position; Undefined team |
| `49` | `74` | Position_Unknown | Team_Unknown | 459–659 | 189 | 4 | Undefined position; Undefined team |
| `50` | `77` | Position_Unknown | Team_Unknown | 461–659 | 195 | 4 | Undefined position; Undefined team |
| `51` | `79` | Position_Unknown | Team_Unknown | 467–531 | 65 | 1 | Undefined position; Undefined team |
| `52` | `80` | Position_Unknown | Team_Unknown | 468–556 | 89 | 1 | Undefined position; Undefined team |
| `53` | `81` | Position_Unknown | Team_Unknown | 471–659 | 181 | 3 | Undefined position; Undefined team |
| `54` | `87` | Position_Unknown | Team_Unknown | 530–568 | 19 | 3 | Undefined position; Undefined team |
| `55` | `88` | Position_Unknown | Team_Unknown | 531–576 | 17 | 3 | Undefined position; Undefined team |
| `56` | `91` | Position_Unknown | Team_Unknown | 610–634 | 22 | 4 | Undefined position; Undefined team |
| `57` | `92` | Position_Unknown | Team_Unknown | 610–616 | 7 | 1 | Undefined position; Undefined team |
| `58` | `93` | Position_Unknown | Team_Unknown | 616–618 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CatchKick` on target `45` (Position_Unknown)
- ⚠️ `Action_BallCarry` for actor_track_id `45` (Position_Unknown): Annotated start 258 != Inferred start 265

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 101, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '663,670,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 180 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Segment 'Action_CatchKick' for track '31' has invalid range: start=265, end=227. Clamping end to start.
- ⚠️ Action 'Action_None' range [54-281] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-296] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-313] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-496] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-567] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-282] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-368] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-211] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-501] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-643] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-445] for track '7' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-659] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-248] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-295] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-355] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-378] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-406] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-410] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-184] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-266] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-296] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-325] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-360] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-387] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-428] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-457] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [54-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 100, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [100-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-659] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-254] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-375] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-179] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-227] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-288] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-374] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-472] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-505] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-536] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-620] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-625] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-123] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-146] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-252] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-117] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-251] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-361] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-394] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-402] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-493] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-503] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-643] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-73] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-232] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-246] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-326] for track '22' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-338] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-659] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-156] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-227] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-288] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-315] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-281] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-279] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [265-315] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-306] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-355] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-393] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-342] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-330] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-346] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-443] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-515] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-612] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-617] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-659] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-330] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-342] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-360] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-395] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-348] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-446] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-353] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-358] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-389] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-364] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-371] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-385] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-410] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-596] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-602] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-631] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-612] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-414] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-594] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-537] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-577] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-585] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-612] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-619] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-422] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-427] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-433] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-446] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-454] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-465] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-491] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-498] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-503] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-511] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-533] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-527] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-603] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-499] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-467] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-479] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-506] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-473] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-529] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-653] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-531] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-556] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-495] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-523] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-542] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-568] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-540] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-568] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-576] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-612] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-617] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-625] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-634] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-616] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-618] for track '58' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_99'; source metadata written as null.

</details>