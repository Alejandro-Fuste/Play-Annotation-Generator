# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_4`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 70
- **Ball Tracks:** 0
- **Action Segments:** 414
- **Validation Warnings:** 498
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 400
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage6 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Position_Unknown | Team_Unknown | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_KickBall` | Position_Unknown | Team_Unknown | `14` | `14` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `26` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `43` | `33` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `43` | `33` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `10` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `12` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `3` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage6 | `4` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `6` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `7` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `8` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `9` | `Group` | 0 | START | 0 | 43 |
| ✅ EXACT | `Action_KickApproach` | Position_Unknown | `14` | `14` | 44 | START | 44 | 67 |
| ❌ MISSING SEGMENT | `Action_KickBall` | Position_Unknown | `14` | `14` | 86 | START | N/A | N/A |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `26` | `22` | 199 | START | 199 | 225 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `43` | `33` | 254 | START | 254 | 422 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `43` | `33` | 651 | START | 651 | 659 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Coverage1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 193 | 150 | inferred_complete_timeline |
| `Action_None` | 248 | 308 | 61 | inferred_complete_timeline |
| `Action_None` | 320 | 433 | 114 | inferred_complete_timeline |
| `Action_None` | 435 | 578 | 144 | inferred_complete_timeline |
| `Action_None` | 581 | 583 | 3 | inferred_complete_timeline |
| `Action_None` | 589 | 599 | 11 | inferred_complete_timeline |
| `Action_None` | 601 | 606 | 6 | inferred_complete_timeline |
| `Action_None` | 609 | 633 | 25 | inferred_complete_timeline |
| `Action_None` | 635 | 644 | 10 | inferred_complete_timeline |
| `Action_None` | 648 | 659 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 74 | 31 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 84 | 143 | 60 | inferred_complete_timeline |
| `Action_None` | 145 | 166 | 22 | inferred_complete_timeline |
| `Action_None` | 173 | 227 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 67 | 24 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 225 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 608

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 67 | 24 | inferred_complete_timeline |
| `Action_None` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 111 | 6 | inferred_complete_timeline |
| `Action_None` | 113 | 172 | 60 | inferred_complete_timeline |
| `Action_None` | 178 | 229 | 52 | inferred_complete_timeline |
| `Action_None` | 232 | 292 | 61 | inferred_complete_timeline |
| `Action_None` | 296 | 303 | 8 | inferred_complete_timeline |
| `Action_None` | 305 | 654 | 350 | inferred_complete_timeline |
| `Action_None` | 659 | 659 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 91 | 48 | inferred_complete_timeline |
| `Action_None` | 93 | 108 | 16 | inferred_complete_timeline |
| `Action_None` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_None` | 123 | 141 | 19 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 188 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage6 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 245 | 202 | inferred_complete_timeline |
| `Action_None` | 250 | 298 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 78 | 35 | inferred_complete_timeline |
| `Action_None` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_None` | 88 | 133 | 46 | inferred_complete_timeline |
| `Action_None` | 136 | 242 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 614

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 40 | 7 | inferred_complete_timeline |
| `Action_None` | 51 | 78 | 28 | inferred_complete_timeline |
| `Action_None` | 90 | 131 | 42 | inferred_complete_timeline |
| `Action_None` | 135 | 145 | 11 | inferred_complete_timeline |
| `Action_None` | 147 | 273 | 127 | inferred_complete_timeline |
| `Action_None` | 281 | 291 | 11 | inferred_complete_timeline |
| `Action_None` | 293 | 659 | 367 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 180 | 137 | inferred_complete_timeline |
| `Action_None` | 188 | 199 | 12 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_None` | 215 | 226 | 12 | inferred_complete_timeline |
| `Action_None` | 229 | 274 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 120 | 77 | inferred_complete_timeline |
| `Action_None` | 122 | 126 | 5 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 158 | 20 | inferred_complete_timeline |
| `Action_None` | 161 | 172 | 12 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 633

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 161 | 118 | inferred_complete_timeline |
| `Action_None` | 163 | 175 | 13 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_None` | 184 | 189 | 6 | inferred_complete_timeline |
| `Action_None` | 193 | 224 | 32 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |
| `Action_None` | 231 | 234 | 4 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 247 | 8 | inferred_complete_timeline |
| `Action_None` | 251 | 466 | 216 | inferred_complete_timeline |
| `Action_None` | 468 | 478 | 11 | inferred_complete_timeline |
| `Action_None` | 482 | 490 | 9 | inferred_complete_timeline |
| `Action_None` | 494 | 504 | 11 | inferred_complete_timeline |
| `Action_None` | 506 | 510 | 5 | inferred_complete_timeline |
| `Action_None` | 512 | 518 | 7 | inferred_complete_timeline |
| `Action_None` | 520 | 659 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 140 | 97 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 166 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 43 | 32 | inferred_complete_timeline |
| `Action_None` | 44 | 62 | 19 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_None` | 93 | 171 | 79 | inferred_complete_timeline |
| `Action_None` | 173 | 271 | 99 | inferred_complete_timeline |
| `Action_None` | 273 | 274 | 2 | inferred_complete_timeline |
| `Action_None` | 276 | 404 | 129 | inferred_complete_timeline |
| `Action_None` | 406 | 430 | 25 | inferred_complete_timeline |
| `Action_None` | 434 | 447 | 14 | inferred_complete_timeline |
| `Action_None` | 454 | 461 | 8 | inferred_complete_timeline |
| `Action_None` | 464 | 465 | 2 | inferred_complete_timeline |
| `Action_None` | 468 | 584 | 117 | inferred_complete_timeline |
| `Action_None` | 586 | 597 | 12 | inferred_complete_timeline |
| `Action_None` | 600 | 614 | 15 | inferred_complete_timeline |
| `Action_None` | 619 | 620 | 2 | inferred_complete_timeline |
| `Action_None` | 622 | 656 | 35 | inferred_complete_timeline |
| `Action_None` | 658 | 659 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 5–659 | 557 | 20 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 29–659 | 505 | 25 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 36–659 | 587 | 12 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 50–659 | 543 | 14 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 76–283 | 182 | 6 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 95–365 | 217 | 5 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 101–291 | 65 | 7 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 101–102 | 2 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 108–123 | 16 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 120–237 | 111 | 6 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 122–659 | 480 | 15 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 126–348 | 189 | 7 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 153–181 | 15 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 158–241 | 75 | 5 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 193–659 | 454 | 8 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 202–228 | 27 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 224–659 | 429 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 227–338 | 102 | 5 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 248–659 | 412 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 254–659 | 369 | 13 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 256–498 | 223 | 7 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 288–291 | 4 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 288–659 | 358 | 3 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 289–611 | 305 | 6 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 310–659 | 296 | 14 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 328–447 | 53 | 7 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 336–503 | 121 | 17 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 339–530 | 142 | 12 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 346–348 | 3 | 1 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 350–659 | 304 | 5 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 353–491 | 133 | 5 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 356–383 | 24 | 3 | Undefined position; Undefined team |
| `47` | `69` | Position_Unknown | Team_Unknown | 373–389 | 13 | 3 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 376–379 | 4 | 1 | Undefined position; Undefined team |
| `49` | `72` | Position_Unknown | Team_Unknown | 382–388 | 7 | 1 | Undefined position; Undefined team |
| `50` | `73` | Position_Unknown | Team_Unknown | 389–390 | 2 | 1 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 394–513 | 120 | 1 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 430–454 | 25 | 1 | Undefined position; Undefined team |
| `53` | `76` | Position_Unknown | Team_Unknown | 440–659 | 100 | 17 | Undefined position; Undefined team |
| `54` | `77` | Position_Unknown | Team_Unknown | 467–600 | 92 | 4 | Undefined position; Undefined team |
| `55` | `79` | Position_Unknown | Team_Unknown | 515–516 | 2 | 1 | Undefined position; Undefined team |
| `56` | `80` | Position_Unknown | Team_Unknown | 517–543 | 10 | 4 | Undefined position; Undefined team |
| `57` | `84` | Position_Unknown | Team_Unknown | 539–659 | 105 | 4 | Undefined position; Undefined team |
| `58` | `88` | Position_Unknown | Team_Unknown | 556–577 | 18 | 3 | Undefined position; Undefined team |
| `59` | `90` | Position_Unknown | Team_Unknown | 568–654 | 57 | 4 | Undefined position; Undefined team |
| `60` | `91` | Position_Unknown | Team_Unknown | 572–577 | 6 | 1 | Undefined position; Undefined team |
| `61` | `92` | Position_Unknown | Team_Unknown | 573–589 | 7 | 3 | Undefined position; Undefined team |
| `62` | `96` | Position_Unknown | Team_Unknown | 589–659 | 68 | 2 | Undefined position; Undefined team |
| `63` | `97` | Position_Unknown | Team_Unknown | 615–659 | 45 | 1 | Undefined position; Undefined team |
| `64` | `98` | Position_Unknown | Team_Unknown | 630–659 | 21 | 4 | Undefined position; Undefined team |
| `65` | `99` | Position_Unknown | Team_Unknown | 633–651 | 15 | 3 | Undefined position; Undefined team |
| `66` | `100` | Position_Unknown | Team_Unknown | 633–637 | 5 | 1 | Undefined position; Undefined team |
| `67` | `101` | Position_Unknown | Team_Unknown | 636–655 | 11 | 2 | Undefined position; Undefined team |
| `68` | `102` | Position_Unknown | Team_Unknown | 641–651 | 10 | 2 | Undefined position; Undefined team |
| `69` | `104` | Position_Unknown | Team_Unknown | 647–654 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_KickBall` on target `14` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `43` (12 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ 57 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 57 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 114 |
| Missing visible bounding boxes during action | 383 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action 'Action_None' range [44-161] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-224] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-247] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-466] for track '0' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-478] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-490] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-504] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-510] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-518] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-158] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-226] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-274] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-308] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-433] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-578] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-583] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-599] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-606] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-633] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-644] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-245] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-298] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-140] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-166] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-74] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-143] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-166] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-227] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-78] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-133] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-242] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-225] for track '8' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-141] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-67] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-172] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-229] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-292] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-303] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-654] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-43] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-62] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-271] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-404] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-430] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-447] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-461] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-584] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-597] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-614] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-620] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-656] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-40] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-78] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-131] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-145] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-273] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-291] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-659] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-18] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-132] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-205] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-376] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-382] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-396] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-415] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-469] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-475] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-483] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-492] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [44-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-202] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-314] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-325] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-333] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-345] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-502] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-507] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-514] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-525] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-535] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-553] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-572] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-585] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-597] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-626] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-642] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-659] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-142] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-179] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-198] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-282] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-367] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-373] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-222] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-269] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-363] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-376] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-383] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-452] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-480] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-611] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-627] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-659] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-219] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-234] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-283] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-107] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-129] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-248] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-365] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-165] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-126] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-192] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-234] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-211] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-228] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-394] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-426] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-459] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-498] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-518] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-659] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-169] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-348] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-181] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-169] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-214] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-310] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-321] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-450] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-462] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-468] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-659] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-228] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-316] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-659] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-299] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-329] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [254-422] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [429-433] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [440-446] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [451-468] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [472-547] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [550-597] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [599-601] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [605-611] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [613-626] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [629-632] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [635-640] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-309] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-410] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-436] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-473] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-491] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-498] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-388] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-409] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-659] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-304] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-516] for track '37' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-577] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-606] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-611] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-345] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-355] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-420] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-428] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-437] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-441] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-469] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-474] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-531] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-564] for track '38' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-620] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-627] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-354] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-364] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-382] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-429] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-447] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-383] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-394] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-413] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-423] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-438] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-456] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-461] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-468] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-500] for track '41' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-358] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-403] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-412] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-433] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-477] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-530] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-497] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-524] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-529] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-581] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-377] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-383] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-412] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-453] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-491] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-383] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-377] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-389] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-379] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-388] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-513] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-454] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-444] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-456] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-477] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-497] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-503] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-508] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-511] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-539] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-563] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-575] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-588] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-595] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [640-646] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-474] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-534] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-584] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-600] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-516] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-524] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-543] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-544] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-588] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-559] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-564] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-577] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-583] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-618] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-639] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-654] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-577] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-585] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-589] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-606] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-659] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-638] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-648] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-652] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-638] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [640-642] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-651] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-637] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-644] for track '67' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-655] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-644] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-651] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-654] for track '69' has 1 frames without a visible bounding box.
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

</details>