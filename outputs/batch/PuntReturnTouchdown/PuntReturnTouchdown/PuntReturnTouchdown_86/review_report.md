# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_86

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_86`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 91
- **Ball Tracks:** 0
- **Action Segments:** 333
- **Validation Warnings:** 448
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 318
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Position_Unknown | Team_Unknown | `21` | `19` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `15` | `15` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `15` | `15` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `29` | `25` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `29` | `25` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `49` | `39` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `0` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `12` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `15` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `4` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `6` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Position_Unknown | `21` | `19` | 39 | START | 39 | 46 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `15` | `15` | 64 | END | 64 | 64 |
| ✅ EXACT | `Action_PuntBall` | Punter | `15` | `15` | 95 | START | 95 | 106 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `29` | `25` | 216 | START | 216 | 225 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `29` | `25` | 236 | START | 241 | 242 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `49` | `39` | 610 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 72 | 34 | inferred_complete_timeline |
| `Action_None` | 82 | 108 | 27 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 172 | 50 | inferred_complete_timeline |
| `Action_None` | 177 | 185 | 9 | inferred_complete_timeline |
| `Action_None` | 193 | 203 | 11 | inferred_complete_timeline |
| `Action_None` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_None` | 218 | 235 | 18 | inferred_complete_timeline |
| `Action_None` | 278 | 283 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 178 | 140 | inferred_complete_timeline |
| `Action_None` | 180 | 256 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–309
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 172 | 134 | inferred_complete_timeline |
| `Action_None` | 175 | 192 | 18 | inferred_complete_timeline |
| `Action_None` | 194 | 305 | 112 | inferred_complete_timeline |
| `Action_None` | 307 | 309 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 174 | 136 | inferred_complete_timeline |
| `Action_None` | 177 | 188 | 12 | inferred_complete_timeline |
| `Action_None` | 190 | 238 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–322
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 322 | 284 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–425
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 345 | 307 | inferred_complete_timeline |
| `Action_None` | 352 | 362 | 11 | inferred_complete_timeline |
| `Action_None` | 364 | 393 | 30 | inferred_complete_timeline |
| `Action_None` | 395 | 400 | 6 | inferred_complete_timeline |
| `Action_None` | 424 | 425 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–559
- **Visible Samples:** 543

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_None` | 65 | 94 | 30 | inferred_complete_timeline |
| `Action_PuntBall` | 95 | 106 | 12 | inferred_complete_timeline |
| `Action_None` | 107 | 474 | 368 | inferred_complete_timeline |
| `Action_None` | 480 | 482 | 3 | inferred_complete_timeline |
| `Action_None` | 485 | 511 | 27 | inferred_complete_timeline |
| `Action_None` | 513 | 517 | 5 | inferred_complete_timeline |
| `Action_None` | 520 | 539 | 20 | inferred_complete_timeline |
| `Action_None` | 543 | 552 | 10 | inferred_complete_timeline |
| `Action_None` | 557 | 559 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 70 | 32 | inferred_complete_timeline |
| `Action_None` | 74 | 77 | 4 | inferred_complete_timeline |
| `Action_None` | 95 | 193 | 99 | inferred_complete_timeline |
| `Action_None` | 200 | 232 | 33 | inferred_complete_timeline |
| `Action_None` | 239 | 244 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 77 | 39 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_None` | 100 | 142 | 43 | inferred_complete_timeline |
| `Action_None` | 145 | 173 | 29 | inferred_complete_timeline |
| `Action_None` | 176 | 179 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 204 | 166 | inferred_complete_timeline |
| `Action_None` | 210 | 215 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Left_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–523
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 320 | 282 | inferred_complete_timeline |
| `Action_None` | 330 | 335 | 6 | inferred_complete_timeline |
| `Action_None` | 342 | 360 | 19 | inferred_complete_timeline |
| `Action_None` | 362 | 364 | 3 | inferred_complete_timeline |
| `Action_None` | 368 | 421 | 54 | inferred_complete_timeline |
| `Action_None` | 423 | 523 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 115 | 77 | inferred_complete_timeline |
| `Action_None` | 117 | 207 | 91 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 222 | 10 | inferred_complete_timeline |
| `Action_None` | 225 | 237 | 13 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 244 | 3 | inferred_complete_timeline |
| `Action_None` | 249 | 297 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 582

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 250 | 212 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 264 | 5 | inferred_complete_timeline |
| `Action_None` | 266 | 280 | 15 | inferred_complete_timeline |
| `Action_None` | 287 | 306 | 20 | inferred_complete_timeline |
| `Action_None` | 315 | 320 | 6 | inferred_complete_timeline |
| `Action_None` | 322 | 325 | 4 | inferred_complete_timeline |
| `Action_None` | 332 | 345 | 14 | inferred_complete_timeline |
| `Action_None` | 347 | 374 | 28 | inferred_complete_timeline |
| `Action_None` | 387 | 475 | 89 | inferred_complete_timeline |
| `Action_None` | 477 | 479 | 3 | inferred_complete_timeline |
| `Action_None` | 485 | 629 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 144 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 77 | 39 | inferred_complete_timeline |
| `Action_None` | 82 | 122 | 41 | inferred_complete_timeline |
| `Action_None` | 125 | 139 | 15 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 244 | 93 | inferred_complete_timeline |
| `Action_None` | 246 | 253 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 133 | 95 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support6 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–409
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 409 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support7 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 150 | 112 | inferred_complete_timeline |
| `Action_None` | 179 | 209 | 31 | inferred_complete_timeline |
| `Action_None` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_None` | 217 | 230 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–3 | 4 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 38–61 | 20 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 51–53 | 3 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 51–410 | 336 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 75–83 | 9 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 83–249 | 135 | 12 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 109–629 | 521 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 139–242 | 95 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 163–215 | 53 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 163–332 | 109 | 6 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 166–193 | 17 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 179–236 | 16 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 214–222 | 8 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 239–249 | 10 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 243–244 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 247–249 | 3 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 258–380 | 122 | 2 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 260–419 | 152 | 6 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 267–629 | 289 | 9 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 273–394 | 102 | 10 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 276–601 | 311 | 3 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 276–437 | 129 | 8 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 281–282 | 2 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 289–600 | 235 | 15 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 291–335 | 41 | 3 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 294–423 | 15 | 3 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 298–333 | 29 | 4 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 298–320 | 23 | 1 | Undefined position; Undefined team |
| `47` | `60` | Position_Unknown | Team_Unknown | 302–429 | 111 | 7 | Undefined position; Undefined team |
| `48` | `61` | Position_Unknown | Team_Unknown | 306–343 | 33 | 2 | Undefined position; Undefined team |
| `49` | `62` | Position_Unknown | Team_Unknown | 307–309 | 3 | 1 | Undefined position; Undefined team |
| `50` | `63` | Position_Unknown | Team_Unknown | 329–333 | 4 | 2 | Undefined position; Undefined team |
| `51` | `64` | Position_Unknown | Team_Unknown | 334–629 | 290 | 2 | Undefined position; Undefined team |
| `52` | `67` | Position_Unknown | Team_Unknown | 337–629 | 289 | 2 | Undefined position; Undefined team |
| `53` | `68` | Position_Unknown | Team_Unknown | 338–495 | 128 | 4 | Undefined position; Undefined team |
| `54` | `72` | Position_Unknown | Team_Unknown | 353–370 | 17 | 2 | Undefined position; Undefined team |
| `55` | `73` | Position_Unknown | Team_Unknown | 353–354 | 2 | 1 | Undefined position; Undefined team |
| `56` | `74` | Position_Unknown | Team_Unknown | 359–360 | 2 | 1 | Undefined position; Undefined team |
| `57` | `76` | Position_Unknown | Team_Unknown | 364–389 | 22 | 2 | Undefined position; Undefined team |
| `58` | `78` | Position_Unknown | Team_Unknown | 369–629 | 227 | 9 | Undefined position; Undefined team |
| `59` | `79` | Position_Unknown | Team_Unknown | 384–405 | 21 | 2 | Undefined position; Undefined team |
| `60` | `80` | Position_Unknown | Team_Unknown | 400–410 | 11 | 1 | Undefined position; Undefined team |
| `61` | `81` | Position_Unknown | Team_Unknown | 421–423 | 3 | 1 | Undefined position; Undefined team |
| `62` | `82` | Position_Unknown | Team_Unknown | 424–428 | 5 | 1 | Undefined position; Undefined team |
| `63` | `83` | Position_Unknown | Team_Unknown | 426–624 | 176 | 6 | Undefined position; Undefined team |
| `64` | `84` | Position_Unknown | Team_Unknown | 428–629 | 143 | 4 | Undefined position; Undefined team |
| `65` | `85` | Position_Unknown | Team_Unknown | 437–627 | 173 | 4 | Undefined position; Undefined team |
| `66` | `86` | Position_Unknown | Team_Unknown | 441–488 | 45 | 3 | Undefined position; Undefined team |
| `67` | `87` | Position_Unknown | Team_Unknown | 442–629 | 175 | 4 | Undefined position; Undefined team |
| `68` | `88` | Position_Unknown | Team_Unknown | 456–491 | 32 | 4 | Undefined position; Undefined team |
| `69` | `89` | Position_Unknown | Team_Unknown | 458–462 | 4 | 2 | Undefined position; Undefined team |
| `70` | `90` | Position_Unknown | Team_Unknown | 462–629 | 167 | 2 | Undefined position; Undefined team |
| `71` | `92` | Position_Unknown | Team_Unknown | 486–629 | 136 | 2 | Undefined position; Undefined team |
| `72` | `93` | Position_Unknown | Team_Unknown | 490–629 | 117 | 5 | Undefined position; Undefined team |
| `73` | `94` | Position_Unknown | Team_Unknown | 492–493 | 2 | 1 | Undefined position; Undefined team |
| `74` | `95` | Position_Unknown | Team_Unknown | 496–557 | 60 | 2 | Undefined position; Undefined team |
| `75` | `96` | Position_Unknown | Team_Unknown | 518–525 | 8 | 1 | Undefined position; Undefined team |
| `76` | `98` | Position_Unknown | Team_Unknown | 528–578 | 24 | 4 | Undefined position; Undefined team |
| `77` | `99` | Position_Unknown | Team_Unknown | 541–542 | 2 | 1 | Undefined position; Undefined team |
| `78` | `100` | Position_Unknown | Team_Unknown | 543–629 | 81 | 3 | Undefined position; Undefined team |
| `79` | `101` | Position_Unknown | Team_Unknown | 549–629 | 56 | 9 | Undefined position; Undefined team |
| `80` | `103` | Position_Unknown | Team_Unknown | 553–554 | 2 | 1 | Undefined position; Undefined team |
| `81` | `105` | Position_Unknown | Team_Unknown | 574–575 | 2 | 1 | Undefined position; Undefined team |
| `82` | `106` | Position_Unknown | Team_Unknown | 582–629 | 39 | 4 | Undefined position; Undefined team |
| `83` | `107` | Position_Unknown | Team_Unknown | 584–595 | 12 | 1 | Undefined position; Undefined team |
| `84` | `111` | Position_Unknown | Team_Unknown | 596–598 | 3 | 1 | Undefined position; Undefined team |
| `85` | `112` | Position_Unknown | Team_Unknown | 603–629 | 27 | 1 | Undefined position; Undefined team |
| `86` | `114` | Position_Unknown | Team_Unknown | 621–629 | 6 | 2 | Undefined position; Undefined team |
| `87` | `115` | Position_Unknown | Team_Unknown | 622–629 | 8 | 1 | Undefined position; Undefined team |
| `88` | `116` | Position_Unknown | Team_Unknown | 622–623 | 2 | 1 | Undefined position; Undefined team |
| `89` | `117` | Position_Unknown | Team_Unknown | 626–629 | 3 | 2 | Undefined position; Undefined team |
| `90` | `118` | Position_Unknown | Team_Unknown | 628–629 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `21` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `29` (Position_Unknown): Annotated start 236 != Inferred start 241
- ❌ Missing segment for action `Action_CrossGoalLine` on target `49` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punt_Support6` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punt_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Support5` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punt_Support7` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 73 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 73 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 146 |
| Missing visible bounding boxes during action | 297 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 174: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CrossGoalLine' for track '39' has invalid range: start=610, end=601. Clamping end to start.
- ⚠️ Action 'Action_None' range [39-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-409] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-250] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-280] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-306] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-345] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-374] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-475] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-479] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-237] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-297] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-345] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-362] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-393] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-400] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-320] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-335] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-360] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-364] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-421] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-523] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-192] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-305] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-77] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-139] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-244] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-188] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-238] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-209] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-230] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-322] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-70] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-193] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-232] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-95] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-142] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-474] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-482] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-511] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-517] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-539] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-552] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-559] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-203] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-235] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-283] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-178] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-256] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' for track '19' starts at frame 39, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_LongSnap' range [39-46] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [51-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-54] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-250] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-392] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-83] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-101] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-133] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-193] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-206] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [241-242] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-215] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-192] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-260] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-277] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-325] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-193] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-236] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-219] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-376] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-377] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-388] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-402] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-412] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-348] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-370] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-467] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-585] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-601] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-619] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-629] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-285] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-300] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-332] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-339] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-347] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-366] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-373] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-377] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-384] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-394] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-332] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-591] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [595-601] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-307] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-317] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-395] for track '40' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-406] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-437] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-410] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-426] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-436] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-448] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-455] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-467] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-554] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-588] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-593] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-600] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-295] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-335] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-423] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-303] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-312] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-322] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-333] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-320] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-307] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-327] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-417] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-421] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-333] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-618] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-346] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-392] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-495] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-366] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-370] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-377] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-389] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-460] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-475] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-483] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-508] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-545] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-548] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-565] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-578] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-391] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-405] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-410] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-428] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-430] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-567] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-624] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-504] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-611] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-461] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-483] for track '65' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-503] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-627] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-461] for track '66' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-476] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-488] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-455] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-473] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-459] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-485] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-613] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-489] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-537] for track '72' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-542] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-564] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-583] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-629] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-493] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-539] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-557] for track '74' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-525] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-536] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-557] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-578] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-542] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-575] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-591] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-554] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-562] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-573] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-595] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-606] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-615] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-619] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-629] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-575] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-589] for track '82' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-596] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-607] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-595] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-598] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-623] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-629] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-623] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-627] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-629] for track '90' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>