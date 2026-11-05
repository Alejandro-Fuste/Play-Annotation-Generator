# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_3`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 105
- **Ball Tracks:** 0
- **Action Segments:** 300
- **Validation Warnings:** 430
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 284
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `42` | `31` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `42` | `31` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `42` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `0` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `10` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `11` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `13` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `14` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `15` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `17` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `20` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `7` | `Group` | 0 | START | 0 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `18` | `18` | 29 | START | 29 | 48 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `11` | `11` | 55 | END | 55 | 55 |
| ✅ EXACT | `Action_PuntBall` | Punter | `11` | `11` | 74 | START | 74 | 89 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `42` | `31` | 204 | START | 204 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `42` | `31` | 213 | START | 213 | 449 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `42` | `31` | 551 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 54 | 26 | inferred_complete_timeline |
| `Action_None` | 74 | 235 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–467
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 226 | 198 | inferred_complete_timeline |
| `Action_None` | 229 | 399 | 171 | inferred_complete_timeline |
| `Action_None` | 401 | 467 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–433
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 79 | 51 | inferred_complete_timeline |
| `Action_None` | 82 | 154 | 73 | inferred_complete_timeline |
| `Action_None` | 156 | 206 | 51 | inferred_complete_timeline |
| `Action_None` | 208 | 211 | 4 | inferred_complete_timeline |
| `Action_None` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |
| `Action_None` | 241 | 433 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–469
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 277 | 249 | inferred_complete_timeline |
| `Action_None` | 282 | 469 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_LongSnap` | 29 | 48 | 20 | inferred_complete_timeline |
| `Action_LongSnap` | 52 | 73 | 22 | inferred_complete_timeline |
| `Action_None` | 74 | 76 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 160 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 140 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–360
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 220 | 192 | inferred_complete_timeline |
| `Action_None` | 223 | 266 | 44 | inferred_complete_timeline |
| `Action_None` | 268 | 360 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_SnapReceive` | 55 | 55 | 1 | inferred_complete_timeline |
| `Action_None` | 56 | 73 | 18 | inferred_complete_timeline |
| `Action_PuntBall` | 74 | 89 | 16 | inferred_complete_timeline |
| `Action_None` | 90 | 149 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 134 | 106 | inferred_complete_timeline |
| `Action_None` | 136 | 147 | 12 | inferred_complete_timeline |
| `Action_None` | 149 | 153 | 5 | inferred_complete_timeline |
| `Action_None` | 155 | 192 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 505 | 477 | inferred_complete_timeline |
| `Action_None` | 507 | 539 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–430
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 46 | 18 | inferred_complete_timeline |
| `Action_None` | 50 | 97 | 48 | inferred_complete_timeline |
| `Action_None` | 99 | 105 | 7 | inferred_complete_timeline |
| `Action_None` | 107 | 121 | 15 | inferred_complete_timeline |
| `Action_None` | 123 | 134 | 12 | inferred_complete_timeline |
| `Action_None` | 137 | 150 | 14 | inferred_complete_timeline |
| `Action_None` | 160 | 164 | 5 | inferred_complete_timeline |
| `Action_None` | 170 | 317 | 148 | inferred_complete_timeline |
| `Action_None` | 321 | 418 | 98 | inferred_complete_timeline |
| `Action_None` | 428 | 430 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–413
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 132 | 104 | inferred_complete_timeline |
| `Action_None` | 135 | 294 | 160 | inferred_complete_timeline |
| `Action_None` | 296 | 413 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 74 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 59 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 97 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 132 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–460
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 110 | 82 | inferred_complete_timeline |
| `Action_None` | 112 | 349 | 238 | inferred_complete_timeline |
| `Action_None` | 352 | 354 | 3 | inferred_complete_timeline |
| `Action_None` | 360 | 362 | 3 | inferred_complete_timeline |
| `Action_None` | 364 | 379 | 16 | inferred_complete_timeline |
| `Action_None` | 381 | 397 | 17 | inferred_complete_timeline |
| `Action_None` | 399 | 460 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 82 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–505
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 106 | 78 | inferred_complete_timeline |
| `Action_None` | 108 | 121 | 14 | inferred_complete_timeline |
| `Action_None` | 127 | 134 | 8 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 160 | 20 | inferred_complete_timeline |
| `Action_None` | 163 | 186 | 24 | inferred_complete_timeline |
| `Action_None` | 188 | 226 | 39 | inferred_complete_timeline |
| `Action_None` | 228 | 232 | 5 | inferred_complete_timeline |
| `Action_None` | 237 | 241 | 5 | inferred_complete_timeline |
| `Action_None` | 244 | 245 | 2 | inferred_complete_timeline |
| `Action_None` | 259 | 354 | 96 | inferred_complete_timeline |
| `Action_None` | 357 | 408 | 52 | inferred_complete_timeline |
| `Action_None` | 412 | 423 | 12 | inferred_complete_timeline |
| `Action_None` | 426 | 439 | 14 | inferred_complete_timeline |
| `Action_None` | 442 | 505 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 64 | 36 | inferred_complete_timeline |
| `Action_None` | 70 | 91 | 22 | inferred_complete_timeline |
| `Action_None` | 95 | 132 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 73–163 | 91 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 76–164 | 34 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 81–111 | 31 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 93–482 | 390 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 110–199 | 66 | 8 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 112–140 | 29 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 117–449 | 280 | 12 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 122–124 | 3 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 131–512 | 363 | 8 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 140–146 | 7 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 160–539 | 367 | 10 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 175–185 | 9 | 2 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 195–489 | 284 | 5 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 223–507 | 284 | 2 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 233–270 | 38 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 275–509 | 235 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 313–314 | 2 | 1 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 330–449 | 120 | 1 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 331–467 | 137 | 1 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 335–501 | 155 | 4 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 336–351 | 13 | 3 | Undefined position; Undefined team |
| `42` | `63` | Position_Unknown | Team_Unknown | 346–539 | 188 | 2 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 346–347 | 2 | 1 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 348–349 | 2 | 1 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 350–364 | 12 | 2 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 350–460 | 101 | 5 | Undefined position; Undefined team |
| `47` | `69` | Position_Unknown | Team_Unknown | 352–487 | 114 | 6 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 353–473 | 120 | 2 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 359–361 | 3 | 1 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 363–365 | 3 | 1 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 370–444 | 68 | 4 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 393–402 | 6 | 3 | Undefined position; Undefined team |
| `53` | `77` | Position_Unknown | Team_Unknown | 400–401 | 2 | 1 | Undefined position; Undefined team |
| `54` | `78` | Position_Unknown | Team_Unknown | 408–409 | 2 | 1 | Undefined position; Undefined team |
| `55` | `80` | Position_Unknown | Team_Unknown | 412–487 | 76 | 1 | Undefined position; Undefined team |
| `56` | `83` | Position_Unknown | Team_Unknown | 425–436 | 10 | 2 | Undefined position; Undefined team |
| `57` | `84` | Position_Unknown | Team_Unknown | 433–436 | 4 | 1 | Undefined position; Undefined team |
| `58` | `85` | Position_Unknown | Team_Unknown | 433–473 | 37 | 3 | Undefined position; Undefined team |
| `59` | `86` | Position_Unknown | Team_Unknown | 435–436 | 2 | 1 | Undefined position; Undefined team |
| `60` | `87` | Position_Unknown | Team_Unknown | 446–489 | 37 | 2 | Undefined position; Undefined team |
| `61` | `93` | Position_Unknown | Team_Unknown | 458–500 | 30 | 5 | Undefined position; Undefined team |
| `62` | `94` | Position_Unknown | Team_Unknown | 458–539 | 66 | 5 | Undefined position; Undefined team |
| `63` | `95` | Position_Unknown | Team_Unknown | 459–501 | 43 | 1 | Undefined position; Undefined team |
| `64` | `96` | Position_Unknown | Team_Unknown | 461–503 | 36 | 3 | Undefined position; Undefined team |
| `65` | `98` | Position_Unknown | Team_Unknown | 461–520 | 24 | 3 | Undefined position; Undefined team |
| `66` | `99` | Position_Unknown | Team_Unknown | 461–522 | 12 | 3 | Undefined position; Undefined team |
| `67` | `103` | Position_Unknown | Team_Unknown | 470–496 | 27 | 1 | Undefined position; Undefined team |
| `68` | `109` | Position_Unknown | Team_Unknown | 478–509 | 28 | 2 | Undefined position; Undefined team |
| `69` | `110` | Position_Unknown | Team_Unknown | 481–500 | 18 | 2 | Undefined position; Undefined team |
| `70` | `111` | Position_Unknown | Team_Unknown | 483–539 | 47 | 5 | Undefined position; Undefined team |
| `71` | `112` | Position_Unknown | Team_Unknown | 483–539 | 43 | 5 | Undefined position; Undefined team |
| `72` | `113` | Position_Unknown | Team_Unknown | 483–515 | 15 | 4 | Undefined position; Undefined team |
| `73` | `115` | Position_Unknown | Team_Unknown | 484–539 | 48 | 5 | Undefined position; Undefined team |
| `74` | `116` | Position_Unknown | Team_Unknown | 486–496 | 8 | 2 | Undefined position; Undefined team |
| `75` | `119` | Position_Unknown | Team_Unknown | 489–539 | 31 | 4 | Undefined position; Undefined team |
| `76` | `120` | Position_Unknown | Team_Unknown | 490–510 | 13 | 3 | Undefined position; Undefined team |
| `77` | `121` | Position_Unknown | Team_Unknown | 490–492 | 3 | 1 | Undefined position; Undefined team |
| `78` | `123` | Position_Unknown | Team_Unknown | 494–534 | 20 | 3 | Undefined position; Undefined team |
| `79` | `124` | Position_Unknown | Team_Unknown | 494–509 | 13 | 4 | Undefined position; Undefined team |
| `80` | `126` | Position_Unknown | Team_Unknown | 496–500 | 5 | 1 | Undefined position; Undefined team |
| `81` | `127` | Position_Unknown | Team_Unknown | 496–497 | 2 | 1 | Undefined position; Undefined team |
| `82` | `130` | Position_Unknown | Team_Unknown | 497–539 | 43 | 1 | Undefined position; Undefined team |
| `83` | `133` | Position_Unknown | Team_Unknown | 497–539 | 40 | 2 | Undefined position; Undefined team |
| `84` | `135` | Position_Unknown | Team_Unknown | 498–499 | 2 | 1 | Undefined position; Undefined team |
| `85` | `136` | Position_Unknown | Team_Unknown | 500–539 | 33 | 3 | Undefined position; Undefined team |
| `86` | `137` | Position_Unknown | Team_Unknown | 500–539 | 38 | 2 | Undefined position; Undefined team |
| `87` | `138` | Position_Unknown | Team_Unknown | 501–513 | 11 | 3 | Undefined position; Undefined team |
| `88` | `141` | Position_Unknown | Team_Unknown | 506–509 | 4 | 1 | Undefined position; Undefined team |
| `89` | `142` | Position_Unknown | Team_Unknown | 510–514 | 5 | 1 | Undefined position; Undefined team |
| `90` | `143` | Position_Unknown | Team_Unknown | 512–539 | 11 | 2 | Undefined position; Undefined team |
| `91` | `150` | Position_Unknown | Team_Unknown | 517–539 | 19 | 2 | Undefined position; Undefined team |
| `92` | `151` | Position_Unknown | Team_Unknown | 519–539 | 21 | 1 | Undefined position; Undefined team |
| `93` | `152` | Position_Unknown | Team_Unknown | 519–538 | 12 | 2 | Undefined position; Undefined team |
| `94` | `157` | Position_Unknown | Team_Unknown | 525–539 | 15 | 1 | Undefined position; Undefined team |
| `95` | `159` | Position_Unknown | Team_Unknown | 526–527 | 2 | 1 | Undefined position; Undefined team |
| `96` | `160` | Position_Unknown | Team_Unknown | 528–539 | 12 | 1 | Undefined position; Undefined team |
| `97` | `161` | Position_Unknown | Team_Unknown | 528–539 | 12 | 1 | Undefined position; Undefined team |
| `98` | `162` | Position_Unknown | Team_Unknown | 529–537 | 8 | 2 | Undefined position; Undefined team |
| `99` | `163` | Position_Unknown | Team_Unknown | 529–539 | 11 | 1 | Undefined position; Undefined team |
| `100` | `165` | Position_Unknown | Team_Unknown | 530–539 | 10 | 1 | Undefined position; Undefined team |
| `101` | `166` | Position_Unknown | Team_Unknown | 532–533 | 2 | 1 | Undefined position; Undefined team |
| `102` | `167` | Position_Unknown | Team_Unknown | 534–539 | 6 | 1 | Undefined position; Undefined team |
| `103` | `170` | Position_Unknown | Team_Unknown | 538–539 | 2 | 1 | Undefined position; Undefined team |
| `104` | `172` | Position_Unknown | Team_Unknown | 539–539 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `42` (7 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `42` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Guard` position mapped to `offense` team
- ⚠️ 84 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 84 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 168 |
| Missing visible bounding boxes during action | 257 |
| Track-related warning | 1 |
| Other | 4 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CrossGoalLine' for track '31' has invalid range: start=551, end=539. Clamping end to start.
- ⚠️ Action 'Action_None' range [29-226] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-399] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-467] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-79] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-154] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-206] for track '1' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-433] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-64] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-132] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-110] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-349] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-354] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-379] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-397] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-460] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-132] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-74] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-59] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-106] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-160] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-226] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-354] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-408] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-423] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-439] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-505] for track '9' has 9 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-360] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-277] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-469] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-192] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-505] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-97] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-121] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-317] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-418] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-430] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [29-48] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [52-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-294] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-413] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-163] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-109] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-111] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-482] for track '24' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-137] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-158] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-122] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-200] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-211] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-241] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-424] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-442] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-449] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-351] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-364] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-388] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-397] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-411] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-453] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-512] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-203] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [213-449] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [453-463] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [466-468] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [472-476] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [478-520] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [524-525] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-201] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-411] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-489] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-402] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-507] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-270] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-509] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-449] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-467] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-428] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-436] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-448] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-501] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-342] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-423] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-358] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-364] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-372] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-411] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-460] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-443] for track '47' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-451] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-480] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-487] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-464] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-473] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-419] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-434] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-444] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-487] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-430] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-436] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-436] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-452] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-467] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-473] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-449] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-489] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-460] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-480] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-500] for track '61' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-460] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-469] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-478] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-486] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-539] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-501] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-485] for track '64' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-503] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-463] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-485] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-463] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-469] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-522] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-496] for track '67' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-485] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-509] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-482] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-500] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-490] for track '70' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-501] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-508] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-513] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-539] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-488] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-497] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-509] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-539] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-496] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-515] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-496] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-517] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-531] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-489] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-496] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-508] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-493] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-499] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-510] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-492] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-502] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-508] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-534] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-497] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-502] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-505] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-509] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-500] for track '80' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-503] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-539] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-499] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-517] for track '85' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-524] for track '86' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-539] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-509] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-513] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-509] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-514] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-513] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-539] for track '90' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-519] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-527] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-538] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '95' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-533] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-537] for track '98' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '101' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '82' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '82' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '83' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '83' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '84' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '84' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '85' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '85' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '86' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '86' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '87' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '87' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '88' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '88' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '89' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '89' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '90' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '90' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '91' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '91' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '92' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '92' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '93' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '93' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '94' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '94' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '95' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '95' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '96' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '96' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '97' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '97' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '98' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '98' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '99' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '99' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '100' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '100' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '101' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '101' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '102' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '102' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '103' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '103' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '104' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '104' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 551. Video range is [0, 539].
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>