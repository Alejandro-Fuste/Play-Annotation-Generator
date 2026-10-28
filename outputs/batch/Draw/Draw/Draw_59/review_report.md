# Play-Annotation-Generator Annotation Review — Draw_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_59`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 154
- **Validation Warnings:** 168
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 129
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 6 | START | 6 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 6 | START | 6 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 6 | START | 6 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 6 | START | 6 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 6 | START | 6 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 6 | START | 6 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 6 | START | 6 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 6 | START | 6 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 6 | START | 6 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 6 | START | 6 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 6 | START | 6 | 42 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 43 | START | 43 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `14` | `13` | 46 | START | 46 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `18` | 46 | START | 46 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `19` | 46 | START | 46 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `21` | `20` | 46 | START | 46 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `22` | `21` | 46 | START | 56 | 58 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 55 | END | 43 | 55 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `3` | `2` | 58 | START | 58 | 82 |
| ✅ EXACT | `Action_BallCarry` | QB | `3` | `2` | 83 | START | 83 | 128 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 157 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 6–128
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 55 | 13 | inferred_complete_timeline |
| `Action_None` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 58 | 82 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 83 | 128 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–406
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 118 | 76 | inferred_complete_timeline |
| `Action_None` | 120 | 191 | 72 | inferred_complete_timeline |
| `Action_None` | 193 | 215 | 23 | inferred_complete_timeline |
| `Action_None` | 217 | 360 | 144 | inferred_complete_timeline |
| `Action_None` | 388 | 390 | 3 | inferred_complete_timeline |
| `Action_None` | 402 | 406 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 6–120
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 107 | 65 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 361 | 319 | inferred_complete_timeline |
| `Action_None` | 364 | 365 | 2 | inferred_complete_timeline |
| `Action_None` | 371 | 390 | 20 | inferred_complete_timeline |
| `Action_None` | 392 | 419 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 6–164
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 92 | 50 | inferred_complete_timeline |
| `Action_None` | 94 | 164 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 419 | 377 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 45 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 157 | 112 | inferred_complete_timeline |
| `Action_None` | 158 | 419 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 6–350
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 45 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 116 | 71 | inferred_complete_timeline |
| `Action_PassBlock` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 123 | 144 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 184 | 27 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 199 | 9 | inferred_complete_timeline |
| `Action_None` | 202 | 207 | 6 | inferred_complete_timeline |
| `Action_None` | 216 | 344 | 129 | inferred_complete_timeline |
| `Action_None` | 349 | 350 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 6–288
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_BallSnap` | 43 | 55 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 157 | 31 | inferred_complete_timeline |
| `Action_None` | 158 | 232 | 75 | inferred_complete_timeline |
| `Action_None` | 238 | 288 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 6–387
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 45 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 73 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 79 | 157 | 79 | inferred_complete_timeline |
| `Action_None` | 158 | 387 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 45 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 145 | 100 | inferred_complete_timeline |
| `Action_PassBlock` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 153 | 157 | 5 | inferred_complete_timeline |
| `Action_None` | 158 | 419 | 262 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 6–270
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 91 | 49 | inferred_complete_timeline |
| `Action_None` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 144 | 45 | inferred_complete_timeline |
| `Action_None` | 146 | 262 | 117 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_None` | 269 | 270 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 6–147
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 92 | 50 | inferred_complete_timeline |
| `Action_None` | 115 | 131 | 17 | inferred_complete_timeline |
| `Action_None` | 140 | 147 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–413
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 109 | 67 | inferred_complete_timeline |
| `Action_None` | 117 | 296 | 180 | inferred_complete_timeline |
| `Action_None` | 299 | 395 | 97 | inferred_complete_timeline |
| `Action_None` | 399 | 400 | 2 | inferred_complete_timeline |
| `Action_None` | 405 | 413 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 419 | 377 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 6–381
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 381 | 339 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–168
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 168 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 87 | 45 | inferred_complete_timeline |
| `Action_None` | 91 | 220 | 130 | inferred_complete_timeline |
| `Action_None` | 222 | 231 | 10 | inferred_complete_timeline |
| `Action_None` | 236 | 267 | 32 | inferred_complete_timeline |
| `Action_None` | 271 | 279 | 9 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_None` | 294 | 297 | 4 | inferred_complete_timeline |
| `Action_None` | 308 | 310 | 3 | inferred_complete_timeline |
| `Action_None` | 313 | 419 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 6–137
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 137 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 42 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 185 | 143 | inferred_complete_timeline |
| `Action_None` | 194 | 419 | 226 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `10` | Position_Unknown | Team_Unknown | 6–248 | 243 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 6–73 | 66 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 83–419 | 337 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 83–96 | 14 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 95–419 | 325 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 123–409 | 255 | 7 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 145–199 | 49 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 161–419 | 254 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 162–175 | 7 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 192–194 | 3 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 209–419 | 211 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 212–419 | 208 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 230–254 | 11 | 3 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 234–386 | 147 | 3 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 247–414 | 132 | 8 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 280–308 | 29 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 298–419 | 122 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 300–303 | 4 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 301–373 | 39 | 9 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 328–330 | 3 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 345–346 | 2 | 1 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 396–399 | 4 | 1 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 398–419 | 22 | 1 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 419–419 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 115 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 118: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [43–55], lower_priority='Action_PassBlock' annotated_start=46, effective_Action_PassBlock_start=56.
- ⚠️ Action 'Action_None' range [43-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-164] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [83-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-87] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-220] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-267] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-279] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-131] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-107] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-262] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-118] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-191] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-360] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-390] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-406] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-361] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-390] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-419] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [147-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-296] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-395] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-413] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-381] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [120-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [123-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-199] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-344] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-73] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [79-157] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-387] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-288] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-419] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-96] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-419] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-278] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-291] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-352] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-409] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-158] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-199] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-365] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-419] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-419] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-243] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-243] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-383] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-278] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-307] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-329] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-353] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-372] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-389] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-414] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-308] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-317] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-335] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-367] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-373] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>