# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_79

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_79`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 66
- **Ball Tracks:** 0
- **Action Segments:** 192
- **Validation Warnings:** 249
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 175
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `51` | `38` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `51` | `38` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `51` | `38` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `1` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `14` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `15` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `16` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `19` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `20` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `19` | `19` | 52 | START | 52 | 70 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 77 | END | 77 | 77 |
| ✅ EXACT | `Action_PuntBall` | Punter | `12` | `12` | 101 | START | 101 | 112 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `51` | `38` | 233 | START | 233 | 241 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `51` | `38` | 271 | START | 271 | 272 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `51` | `38` | 589 | START | 589 | 597 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 199 | 148 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 134 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–438
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 115 | 64 | inferred_complete_timeline |
| `Action_None` | 124 | 140 | 17 | inferred_complete_timeline |
| `Action_None` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_None` | 149 | 189 | 41 | inferred_complete_timeline |
| `Action_None` | 196 | 218 | 23 | inferred_complete_timeline |
| `Action_None` | 230 | 234 | 5 | inferred_complete_timeline |
| `Action_None` | 240 | 257 | 18 | inferred_complete_timeline |
| `Action_None` | 276 | 387 | 112 | inferred_complete_timeline |
| `Action_None` | 389 | 438 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_LongSnap` | 52 | 70 | 19 | inferred_complete_timeline |
| `Action_LongSnap` | 72 | 100 | 29 | inferred_complete_timeline |
| `Action_None` | 101 | 133 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–314
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 187 | 136 | inferred_complete_timeline |
| `Action_None` | 193 | 196 | 4 | inferred_complete_timeline |
| `Action_None` | 201 | 218 | 18 | inferred_complete_timeline |
| `Action_None` | 248 | 273 | 26 | inferred_complete_timeline |
| `Action_None` | 282 | 314 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–322
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 106 | 55 | inferred_complete_timeline |
| `Action_None` | 134 | 322 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 185 | 134 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 77 | 1 | inferred_complete_timeline |
| `Action_None` | 78 | 100 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 101 | 112 | 12 | inferred_complete_timeline |
| `Action_None` | 113 | 166 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–454
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 78 | 27 | inferred_complete_timeline |
| `Action_None` | 80 | 454 | 375 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 141 | 90 | inferred_complete_timeline |
| `Action_None` | 144 | 219 | 76 | inferred_complete_timeline |
| `Action_None` | 222 | 226 | 5 | inferred_complete_timeline |
| `Action_None` | 228 | 231 | 4 | inferred_complete_timeline |
| `Action_None` | 237 | 240 | 4 | inferred_complete_timeline |
| `Action_None` | 244 | 439 | 196 | inferred_complete_timeline |
| `Action_None` | 452 | 453 | 2 | inferred_complete_timeline |
| `Action_None` | 465 | 599 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 132 | 81 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–436
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 232 | 181 | inferred_complete_timeline |
| `Action_None` | 234 | 274 | 41 | inferred_complete_timeline |
| `Action_None` | 279 | 431 | 153 | inferred_complete_timeline |
| `Action_None` | 435 | 436 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–465
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 91 | 40 | inferred_complete_timeline |
| `Action_None` | 93 | 237 | 145 | inferred_complete_timeline |
| `Action_None` | 240 | 465 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 105 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 73 | 22 | inferred_complete_timeline |
| `Action_None` | 76 | 79 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 91 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 142 | 91 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 221 | 73 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 228 | 239 | 12 | inferred_complete_timeline |
| `Action_None` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 274 | 223 | inferred_complete_timeline |
| `Action_None` | 276 | 278 | 3 | inferred_complete_timeline |
| `Action_None` | 280 | 599 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 74 | 23 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 273 | 222 | inferred_complete_timeline |
| `Action_None` | 279 | 308 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–462
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 232 | 181 | inferred_complete_timeline |
| `Action_None` | 234 | 273 | 40 | inferred_complete_timeline |
| `Action_None` | 277 | 282 | 6 | inferred_complete_timeline |
| `Action_None` | 284 | 462 | 179 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 72–424 | 336 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 85–293 | 201 | 6 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 93–104 | 5 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 100–433 | 334 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 109–112 | 4 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 120–153 | 33 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 123–156 | 7 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 127–237 | 99 | 6 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 148–362 | 170 | 8 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 160–324 | 159 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 164–172 | 9 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 164–169 | 6 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 164–286 | 122 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 203–206 | 4 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 214–266 | 53 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 214–228 | 14 | 2 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 215–599 | 383 | 7 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 239–246 | 8 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 249–445 | 197 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 255–599 | 340 | 4 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 257–374 | 112 | 4 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 272–599 | 324 | 3 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 273–309 | 11 | 3 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 304–467 | 159 | 3 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 323–325 | 3 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 338–391 | 54 | 1 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 370–599 | 229 | 2 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 381–599 | 216 | 2 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 386–436 | 47 | 3 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 386–599 | 213 | 2 | Undefined position; Undefined team |
| `52` | `78` | Position_Unknown | Team_Unknown | 397–599 | 203 | 1 | Undefined position; Undefined team |
| `53` | `80` | Position_Unknown | Team_Unknown | 412–431 | 6 | 3 | Undefined position; Undefined team |
| `54` | `81` | Position_Unknown | Team_Unknown | 432–599 | 168 | 1 | Undefined position; Undefined team |
| `55` | `82` | Position_Unknown | Team_Unknown | 437–599 | 162 | 2 | Undefined position; Undefined team |
| `56` | `83` | Position_Unknown | Team_Unknown | 444–502 | 13 | 3 | Undefined position; Undefined team |
| `57` | `84` | Position_Unknown | Team_Unknown | 454–496 | 43 | 1 | Undefined position; Undefined team |
| `58` | `94` | Position_Unknown | Team_Unknown | 506–599 | 94 | 1 | Undefined position; Undefined team |
| `59` | `95` | Position_Unknown | Team_Unknown | 506–507 | 2 | 1 | Undefined position; Undefined team |
| `60` | `97` | Position_Unknown | Team_Unknown | 511–599 | 89 | 1 | Undefined position; Undefined team |
| `61` | `101` | Position_Unknown | Team_Unknown | 528–537 | 10 | 1 | Undefined position; Undefined team |
| `62` | `103` | Position_Unknown | Team_Unknown | 535–549 | 12 | 2 | Undefined position; Undefined team |
| `63` | `107` | Position_Unknown | Team_Unknown | 546–562 | 6 | 2 | Undefined position; Undefined team |
| `64` | `110` | Position_Unknown | Team_Unknown | 580–599 | 20 | 1 | Undefined position; Undefined team |
| `65` | `113` | Position_Unknown | Team_Unknown | 598–599 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `51` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 45 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 45 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 90 |
| Missing visible bounding boxes during action | 156 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [52-187] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-218] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-273] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-314] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-115] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-140] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-218] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-387] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-438] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-237] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-465] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-273] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-308] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-274] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-431] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-232] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-273] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-462] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-219] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-439] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-599] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-142] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-221] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-274] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-599] for track '11' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-166] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-322] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-454] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [52-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-134] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-292] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-424] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-215] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-273] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-282] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-433] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-141] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-153] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-158] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-234] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-164] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-178] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-274] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-362] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-203] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-324] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-172] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-274] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-286] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-266] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-223] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-232] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-269] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [271-272] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [274-588] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-246] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-445] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-272] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-599] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-347] for track '42' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-362] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-374] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-473] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-424] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-467] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-391] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-578] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-438] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-436] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-430] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-599] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-599] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-418] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-538] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-448] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-496] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-496] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-599] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-507] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-537] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-543] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-549] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-549] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-562] for track '63' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>