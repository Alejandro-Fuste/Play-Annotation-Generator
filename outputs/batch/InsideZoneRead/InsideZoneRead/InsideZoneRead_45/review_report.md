# Play-Annotation-Generator Annotation Review — InsideZoneRead_45

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_45`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 136
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 129 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 128 | START | 128 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `16` | 130 | START | 130 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 130 | START | 130 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `20` | 130 | START | 130 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `7` | `6` | 130 | START | 145 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `8` | 130 | START | 130 | 135 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 144 | END | 128 | 144 |
| ✅ EXACT | `Action_ReadDefender` | QB | `15` | `14` | 152 | START | 152 | 163 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 164 | START | 164 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `7` | `6` | 167 | START | 167 | 195 |
| ✅ EXACT | `Action_BallCarry` | RB | `16` | `15` | 177 | START | 177 | 309 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 210 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_SnapReceive` | 128 | 144 | 17 | inferred_complete_timeline |
| `Action_None` | 145 | 151 | 7 | inferred_complete_timeline |
| `Action_ReadDefender` | 152 | 163 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 164 | 176 | 13 | inferred_complete_timeline |
| `Action_None` | 177 | 195 | 19 | inferred_complete_timeline |
| `Action_None` | 200 | 202 | 3 | inferred_complete_timeline |
| `Action_None` | 205 | 449 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–309
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 176 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 177 | 309 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 449 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 362 | 235 | inferred_complete_timeline |
| `Action_None` | 367 | 374 | 8 | inferred_complete_timeline |
| `Action_None` | 378 | 387 | 10 | inferred_complete_timeline |
| `Action_None` | 390 | 398 | 9 | inferred_complete_timeline |
| `Action_None` | 402 | 433 | 32 | inferred_complete_timeline |
| `Action_None` | 438 | 442 | 5 | inferred_complete_timeline |
| `Action_None` | 444 | 449 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 200 | 73 | inferred_complete_timeline |
| `Action_None` | 205 | 292 | 88 | inferred_complete_timeline |
| `Action_None` | 296 | 311 | 16 | inferred_complete_timeline |
| `Action_None` | 313 | 449 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 449 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 135 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 153 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 173 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–445
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 153 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 180 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 210 | 19 | inferred_complete_timeline |
| `Action_None` | 211 | 268 | 58 | inferred_complete_timeline |
| `Action_None` | 270 | 324 | 55 | inferred_complete_timeline |
| `Action_None` | 326 | 340 | 15 | inferred_complete_timeline |
| `Action_None` | 346 | 445 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_BallSnap` | 128 | 144 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 153 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 161 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 167 | 195 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 197 | 207 | 11 | inferred_complete_timeline |
| `Action_None` | 223 | 325 | 103 | inferred_complete_timeline |
| `Action_None` | 328 | 374 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–383
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 135 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 152 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 181 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 189 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 210 | 19 | inferred_complete_timeline |
| `Action_None` | 211 | 329 | 119 | inferred_complete_timeline |
| `Action_None` | 337 | 363 | 27 | inferred_complete_timeline |
| `Action_None` | 365 | 368 | 4 | inferred_complete_timeline |
| `Action_None` | 372 | 383 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 135 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 162 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 178 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 207 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 210 | 1 | inferred_complete_timeline |
| `Action_None` | 211 | 312 | 102 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–447
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 133 | 6 | inferred_complete_timeline |
| `Action_None` | 141 | 153 | 13 | inferred_complete_timeline |
| `Action_None` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_None` | 168 | 180 | 13 | inferred_complete_timeline |
| `Action_None` | 185 | 197 | 13 | inferred_complete_timeline |
| `Action_None` | 199 | 437 | 239 | inferred_complete_timeline |
| `Action_None` | 440 | 447 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–392
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 345 | 218 | inferred_complete_timeline |
| `Action_None` | 351 | 392 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 133 | 6 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 153 | 13 | inferred_complete_timeline |
| `Action_None` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_None` | 170 | 178 | 9 | inferred_complete_timeline |
| `Action_None` | 192 | 262 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–360
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 267 | 140 | inferred_complete_timeline |
| `Action_None` | 269 | 360 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 329 | 202 | inferred_complete_timeline |
| `Action_None` | 332 | 341 | 10 | inferred_complete_timeline |
| `Action_None` | 347 | 365 | 19 | inferred_complete_timeline |
| `Action_None` | 367 | 382 | 16 | inferred_complete_timeline |
| `Action_None` | 385 | 449 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 449 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–336
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 153 | 26 | inferred_complete_timeline |
| `Action_None` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_None` | 165 | 336 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 449 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 449 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 351 | 224 | inferred_complete_timeline |
| `Action_None` | 353 | 449 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 9–198 | 178 | 7 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 200–449 | 248 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 210–376 | 161 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 215–218 | 4 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 278–365 | 88 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 278–279 | 2 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 312–403 | 56 | 7 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 420–440 | 9 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (10 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (6 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [128–144], lower_priority='Action_ZoneBlock' annotated_start=130, effective_Action_ZoneBlock_start=145.
- ⚠️ Action 'Action_None' range [128-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-292] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-311] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-336] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-449] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [128-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-153] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [167-195] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [197-207] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-325] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-374] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-362] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-374] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-387] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-398] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-433] for track '7' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-442] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-135] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-178] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-312] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-341] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-365] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-382] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-153] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-437] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-447] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-267] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-360] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-345] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-392] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-195] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-449] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [177-309] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-363] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-368] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-383] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-153] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-178] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-262] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-351] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-153] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [165-180] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [185-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-268] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-324] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-340] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-445] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-153] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-153] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-189] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-219] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-449] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-361] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-368] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-376] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-365] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-322] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-337] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-363] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-392] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-403] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-422] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-440] for track '28' has 2 frames without a visible bounding box.
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

</details>