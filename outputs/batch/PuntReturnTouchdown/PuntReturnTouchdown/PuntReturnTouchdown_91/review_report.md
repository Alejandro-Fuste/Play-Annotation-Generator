# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_91

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_91`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 55
- **Ball Tracks:** 0
- **Action Segments:** 199
- **Validation Warnings:** 235
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 183
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `52` | `36` |
| ⚠️ START CHANGED | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `44` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `11` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `12` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `18` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `2` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `3` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `4` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `6` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `9` | `Group` | 0 | START | 0 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `16` | `16` | 82 | START | 82 | 101 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `11` | `11` | 112 | END | 112 | 112 |
| ✅ EXACT | `Action_PuntBall` | Punter | `11` | `11` | 133 | START | 133 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `52` | `36` | 310 | START | 310 | 315 |
| ⚠️ START CHANGED | `Action_CrossGoalLine` | Position_Unknown | `44` | `31` | 591 | START | 592 | 598 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–434
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 97 | 16 | inferred_complete_timeline |
| `Action_None` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 142 | 20 | inferred_complete_timeline |
| `Action_None` | 152 | 163 | 12 | inferred_complete_timeline |
| `Action_None` | 169 | 176 | 8 | inferred_complete_timeline |
| `Action_None` | 178 | 189 | 12 | inferred_complete_timeline |
| `Action_None` | 194 | 288 | 95 | inferred_complete_timeline |
| `Action_None` | 291 | 384 | 94 | inferred_complete_timeline |
| `Action_None` | 387 | 410 | 24 | inferred_complete_timeline |
| `Action_None` | 413 | 416 | 4 | inferred_complete_timeline |
| `Action_None` | 425 | 434 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–420
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 420 | 339 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 132 | 51 | inferred_complete_timeline |
| `Action_None` | 134 | 136 | 3 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–593
- **Visible Samples:** 499

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_LongSnap` | 82 | 101 | 20 | inferred_complete_timeline |
| `Action_LongSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_LongSnap` | 109 | 132 | 24 | inferred_complete_timeline |
| `Action_None` | 133 | 172 | 40 | inferred_complete_timeline |
| `Action_None` | 231 | 471 | 241 | inferred_complete_timeline |
| `Action_None` | 473 | 540 | 68 | inferred_complete_timeline |
| `Action_None` | 546 | 557 | 12 | inferred_complete_timeline |
| `Action_None` | 563 | 565 | 3 | inferred_complete_timeline |
| `Action_None` | 568 | 572 | 5 | inferred_complete_timeline |
| `Action_None` | 592 | 593 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 133 | 52 | inferred_complete_timeline |
| `Action_None` | 152 | 194 | 43 | inferred_complete_timeline |
| `Action_None` | 196 | 202 | 7 | inferred_complete_timeline |
| `Action_None` | 210 | 481 | 272 | inferred_complete_timeline |
| `Action_None` | 486 | 541 | 56 | inferred_complete_timeline |
| `Action_None` | 546 | 599 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 134 | 53 | inferred_complete_timeline |
| `Action_None` | 136 | 143 | 8 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 121 | 40 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_SnapReceive` | 112 | 112 | 1 | inferred_complete_timeline |
| `Action_None` | 113 | 132 | 20 | inferred_complete_timeline |
| `Action_PuntBall` | 133 | 146 | 14 | inferred_complete_timeline |
| `Action_None` | 147 | 160 | 14 | inferred_complete_timeline |
| `Action_None` | 165 | 169 | 5 | inferred_complete_timeline |
| `Action_None` | 171 | 180 | 10 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 229 | 31 | inferred_complete_timeline |
| `Action_None` | 231 | 237 | 7 | inferred_complete_timeline |
| `Action_None` | 239 | 253 | 15 | inferred_complete_timeline |
| `Action_None` | 256 | 263 | 8 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_None` | 273 | 522 | 250 | inferred_complete_timeline |
| `Action_None` | 527 | 599 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 124 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 264 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 102 | 21 | inferred_complete_timeline |
| `Action_None` | 107 | 131 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 131 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 88 | 7 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_None` | 96 | 260 | 165 | inferred_complete_timeline |
| `Action_None` | 266 | 293 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 178 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 581

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 195 | 114 | inferred_complete_timeline |
| `Action_None` | 200 | 243 | 44 | inferred_complete_timeline |
| `Action_None` | 245 | 257 | 13 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |
| `Action_None` | 271 | 275 | 5 | inferred_complete_timeline |
| `Action_None` | 277 | 315 | 39 | inferred_complete_timeline |
| `Action_None` | 326 | 599 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 122 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 110 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 132 | 51 | inferred_complete_timeline |
| `Action_None` | 134 | 197 | 64 | inferred_complete_timeline |
| `Action_None` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 584

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 301 | 220 | inferred_complete_timeline |
| `Action_None` | 312 | 498 | 187 | inferred_complete_timeline |
| `Action_None` | 501 | 507 | 7 | inferred_complete_timeline |
| `Action_None` | 510 | 511 | 2 | inferred_complete_timeline |
| `Action_None` | 514 | 599 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 107 | 26 | inferred_complete_timeline |
| `Action_None` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_None` | 115 | 119 | 5 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 139 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 581

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 174 | 93 | inferred_complete_timeline |
| `Action_None` | 182 | 301 | 120 | inferred_complete_timeline |
| `Action_None` | 303 | 562 | 260 | inferred_complete_timeline |
| `Action_None` | 570 | 572 | 3 | inferred_complete_timeline |
| `Action_None` | 577 | 599 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `24` | Position_Unknown | Team_Unknown | 141–314 | 160 | 8 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 172–210 | 19 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 177–315 | 134 | 4 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 179–576 | 384 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 185–588 | 381 | 10 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 186–564 | 337 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 197–217 | 21 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 200–217 | 18 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 212–599 | 347 | 9 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 219–599 | 367 | 3 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 223–593 | 354 | 6 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 241–598 | 358 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 254–406 | 146 | 4 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 279–528 | 250 | 1 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 295–599 | 301 | 3 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 300–508 | 209 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 333–599 | 262 | 2 | Undefined position; Undefined team |
| `42` | `63` | Position_Unknown | Team_Unknown | 336–340 | 5 | 1 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 338–599 | 260 | 2 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 361–596 | 233 | 2 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 368–373 | 6 | 1 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 394–395 | 2 | 1 | Undefined position; Undefined team |
| `47` | `69` | Position_Unknown | Team_Unknown | 415–416 | 2 | 1 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 426–585 | 160 | 1 | Undefined position; Undefined team |
| `49` | `72` | Position_Unknown | Team_Unknown | 429–599 | 171 | 1 | Undefined position; Undefined team |
| `50` | `73` | Position_Unknown | Team_Unknown | 434–599 | 162 | 3 | Undefined position; Undefined team |
| `51` | `76` | Position_Unknown | Team_Unknown | 516–599 | 77 | 3 | Undefined position; Undefined team |
| `52` | `79` | Position_Unknown | Team_Unknown | 552–599 | 42 | 3 | Undefined position; Undefined team |
| `53` | `80` | Position_Unknown | Team_Unknown | 559–562 | 4 | 1 | Undefined position; Undefined team |
| `54` | `82` | Position_Unknown | Team_Unknown | 599–599 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `52` (3 segments found)
- ⚠️ `Action_CrossGoalLine` for actor_track_id `44` (Position_Unknown): Annotated start 591 != Inferred start 592

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 34 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 34 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 68 |
| Missing visible bounding boxes during action | 164 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [82-132] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-197] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-239] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-131] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-133] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-194] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-481] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-541] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-264] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-420] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-301] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-498] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-507] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-511] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-599] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-132] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-257] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-315] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-599] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-178] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-97] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-142] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-189] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-288] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-384] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-410] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-416] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-434] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-131] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-160] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-253] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-522] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-134] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-301] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-562] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-572] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-260] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-293] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [82-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [103-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-471] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-540] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-557] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-565] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-572] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-593] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-124] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-247] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-273] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-296] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-314] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-188] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-288] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-309] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-315] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-320] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-522] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-576] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-199] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-225] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-309] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-369] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-483] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-498] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-588] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-564] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-217] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-317] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-521] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [524-541] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-550] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [570-571] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [577-578] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [580-585] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [592-598] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '31' starts at frame 599, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [599-599] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-367] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-495] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-565] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-570] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-578] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-593] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-598] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [310-315] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [321-395] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [398-406] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-528] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-338] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-384] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-508] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-392] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-599] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-594] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-536] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-596] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-373] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-585] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-577] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-581] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-599] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-543] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-596] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-580] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-588] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-562] for track '53' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>