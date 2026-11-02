# Play-Annotation-Generator Annotation Review — JetSweep_72

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_72`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 539
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `10` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `22` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 166 |
| ✅ EXACT | `Action_JetMotion` | WR3 | `10` | `9` | 72 | START | 72 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `9` | `8` | 167 | START | 167 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `16` | 168 | START | 168 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 168 | START | 168 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 168 | START | 168 | 211 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `2` | 168 | START | 168 | 274 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `9` | `8` | 168 | START | 185 | 195 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 182 | END | 167 | 182 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 188 | START | 188 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `10` | `9` | 199 | START | 199 | 260 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `17` | `16` | 203 | START | 203 | 274 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 274 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_SnapReceive` | 167 | 182 | 16 | inferred_complete_timeline |
| `Action_None` | 183 | 187 | 5 | inferred_complete_timeline |
| `Action_Toss` | 188 | 198 | 11 | inferred_complete_timeline |
| `Action_None` | 199 | 248 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 274 | 108 | inferred_complete_timeline |
| `Action_None` | 276 | 539 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–503
- **Visible Samples:** 483

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 452 | 286 | inferred_complete_timeline |
| `Action_None` | 458 | 459 | 2 | inferred_complete_timeline |
| `Action_None` | 469 | 475 | 7 | inferred_complete_timeline |
| `Action_None` | 482 | 497 | 16 | inferred_complete_timeline |
| `Action_None` | 499 | 503 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–537
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_JetMotion` | 72 | 198 | 127 | inferred_complete_timeline |
| `Action_BallCarry` | 199 | 260 | 62 | inferred_complete_timeline |
| `Action_BallCarry` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 266 | 537 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–341
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 198 | 32 | inferred_complete_timeline |
| `Action_None` | 200 | 341 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–408
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 203 | 37 | inferred_complete_timeline |
| `Action_None` | 205 | 265 | 61 | inferred_complete_timeline |
| `Action_None` | 268 | 298 | 31 | inferred_complete_timeline |
| `Action_None` | 316 | 408 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 222 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–450
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 194 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 202 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 203 | 274 | 72 | inferred_complete_timeline |
| `Action_None` | 275 | 450 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_BallSnap` | 167 | 179 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 195 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–421
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 211 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 274 | 62 | inferred_complete_timeline |
| `Action_None` | 275 | 421 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–411
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 274 | 107 | inferred_complete_timeline |
| `Action_None` | 275 | 384 | 110 | inferred_complete_timeline |
| `Action_None` | 387 | 411 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 247 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–443
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 302 | 136 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 321 | 436 | 116 | inferred_complete_timeline |
| `Action_None` | 438 | 440 | 3 | inferred_complete_timeline |
| `Action_None` | 442 | 443 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–466
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 256 | 90 | inferred_complete_timeline |
| `Action_None` | 258 | 466 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 225 | 59 | inferred_complete_timeline |
| `Action_None` | 227 | 274 | 48 | inferred_complete_timeline |
| `Action_None` | 279 | 325 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 448 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–447
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 243 | 77 | inferred_complete_timeline |
| `Action_None` | 246 | 426 | 181 | inferred_complete_timeline |
| `Action_None` | 430 | 434 | 5 | inferred_complete_timeline |
| `Action_None` | 436 | 447 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 539 | 373 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–384
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 384 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 315 | 149 | inferred_complete_timeline |
| `Action_None` | 317 | 355 | 39 | inferred_complete_timeline |
| `Action_None` | 357 | 479 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–452
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 348 | 182 | inferred_complete_timeline |
| `Action_None` | 355 | 361 | 7 | inferred_complete_timeline |
| `Action_None` | 450 | 452 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–403
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 291 | 125 | inferred_complete_timeline |
| `Action_None` | 293 | 295 | 3 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |
| `Action_None` | 315 | 317 | 3 | inferred_complete_timeline |
| `Action_None` | 344 | 350 | 7 | inferred_complete_timeline |
| `Action_None` | 365 | 379 | 15 | inferred_complete_timeline |
| `Action_None` | 384 | 403 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 214–330 | 104 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 219–227 | 7 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 221–276 | 55 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 248–252 | 5 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 288–539 | 231 | 4 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 306–393 | 84 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 322–476 | 140 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 343–507 | 162 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 380–478 | 99 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 391–473 | 83 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 409–418 | 9 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 412–481 | 66 | 2 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 444–468 | 23 | 2 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 529–539 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `9` (C): Annotated start 168 != Inferred start 185
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 107 frames exceeds threshold 90 frames [start=168, end=274].
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [167–182], lower_priority='Action_ZoneBlock' annotated_start=168, effective_Action_ZoneBlock_start=183.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 107 frames exceeds threshold 90 frames [start=168, end=274].
- ⚠️ Action 'Action_None' range [167-452] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-475] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-497] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-503] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-256] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-466] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-274] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-384] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-411] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-315] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-355] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-479] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-243] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-426] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-434] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-447] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-291] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-350] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-379] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-403] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-274] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [167-179] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [181-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [185-195] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [199-260] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [263-264] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [266-537] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-302] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-436] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-440] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-274] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-325] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-384] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-341] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-248] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-194] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-450] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-348] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-361] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-452] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-448] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-421] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-203] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-265] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-298] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-408] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-258] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-330] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-268] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-276] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-316] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-539] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-342] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-355] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-393] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-364] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-381] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-476] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-444] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-507] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-478] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-473] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-415] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-418] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-470] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-481] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-463] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-468] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-530] for track '35' has 1 frames without a visible bounding box.
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

</details>