# Play-Annotation-Generator Annotation Review — SplitZone_185

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_185`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `25` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 16 | START | 17 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 16 | START | 17 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 16 | START | 17 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 16 | START | 17 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 16 | START | 17 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 16 | START | 17 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `21` | `Group` | 16 | START | 17 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `25` | `Group` | 16 | START | 73 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `4` | `Group` | 16 | START | 17 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 16 | START | 17 | 242 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 16 | START | 17 | 209 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 210 | START | 210 | 217 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `25` | `23` | 213 | START | 213 | 254 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 213 | START | 218 | 335 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `16` | `16` | 213 | START | 213 | 232 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 213 | START | 213 | 290 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 213 | START | 213 | 246 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `20` | 213 | START | 213 | 370 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 217 | END | 210 | 217 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 230 | START | 230 | 242 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `6` | 243 | START | 243 | 389 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 370 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 17–281
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_SnapReceive` | 210 | 217 | 8 | inferred_complete_timeline |
| `Action_None` | 218 | 229 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 230 | 242 | 13 | inferred_complete_timeline |
| `Action_None` | 243 | 281 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 17–389
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 242 | 226 | inferred_complete_timeline |
| `Action_BallCarry` | 243 | 389 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 17–449
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 361 | 152 | inferred_complete_timeline |
| `Action_None` | 364 | 369 | 6 | inferred_complete_timeline |
| `Action_None` | 376 | 449 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `25`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 73–254
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 73 | 212 | 140 | inferred_complete_timeline |
| `Action_SplitBlock` | 213 | 254 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 17–240
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 240 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 17–449
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 256 | 47 | inferred_complete_timeline |
| `Action_None` | 261 | 449 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 17–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 212 | 196 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 370 | 158 | inferred_complete_timeline |
| `Action_None` | 371 | 449 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 17–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 212 | 196 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 290 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 297 | 352 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 354 | 370 | 17 | inferred_complete_timeline |
| `Action_None` | 371 | 449 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 17–396
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_BallSnap` | 210 | 217 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 335 | 118 | inferred_complete_timeline |
| `Action_ZoneBlock` | 338 | 340 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 343 | 370 | 28 | inferred_complete_timeline |
| `Action_None` | 371 | 396 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 17–449
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 212 | 196 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 246 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 254 | 312 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 343 | 365 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 368 | 370 | 3 | inferred_complete_timeline |
| `Action_None` | 371 | 449 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 17–259
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 53 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 212 | 158 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 232 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 239 | 259 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 17–309
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 309 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 17–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 449 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 17–236
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 236 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 17–449
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 25 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 209 | 177 | inferred_complete_timeline |
| `Action_None` | 210 | 306 | 97 | inferred_complete_timeline |
| `Action_None` | 322 | 408 | 87 | inferred_complete_timeline |
| `Action_None` | 410 | 449 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 17–342
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 329 | 120 | inferred_complete_timeline |
| `Action_None` | 334 | 342 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 17–449
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 45 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 209 | 141 | inferred_complete_timeline |
| `Action_None` | 210 | 279 | 70 | inferred_complete_timeline |
| `Action_None` | 284 | 287 | 4 | inferred_complete_timeline |
| `Action_None` | 289 | 449 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 17–260
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 252 | 43 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 17–449
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 310 | 101 | inferred_complete_timeline |
| `Action_None` | 312 | 314 | 3 | inferred_complete_timeline |
| `Action_None` | 322 | 449 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 17–449
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 270 | 61 | inferred_complete_timeline |
| `Action_None` | 278 | 308 | 31 | inferred_complete_timeline |
| `Action_None` | 313 | 449 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 17–449
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 344 | 135 | inferred_complete_timeline |
| `Action_None` | 352 | 353 | 2 | inferred_complete_timeline |
| `Action_None` | 355 | 368 | 14 | inferred_complete_timeline |
| `Action_None` | 380 | 400 | 21 | inferred_complete_timeline |
| `Action_None` | 406 | 449 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 17–440
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 209 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 440 | 231 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 17–74 | 58 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 17–18 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 239–449 | 196 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 268–352 | 59 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 270–280 | 5 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 296–449 | 154 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 297–432 | 134 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 305–449 | 145 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 313–449 | 137 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 317–449 | 131 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 330–449 | 120 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 357–449 | 87 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 378–403 | 23 | 2 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 379–380 | 2 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 395–449 | 55 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 419–425 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF3` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 158 frames exceeds threshold 90 frames [start=213, end=370].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [210–217], lower_priority='Action_ZoneBlock' annotated_start=213, effective_Action_ZoneBlock_start=218.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 158 frames exceeds threshold 90 frames [start=213, end=370].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 158 frames exceeds threshold 90 frames [start=213, end=370].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 158 frames exceeds threshold 90 frames [start=213, end=370].
- ⚠️ Action 'Action_None' range [210-252] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-270] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-308] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-236] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-256] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-344] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-368] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-400] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [243-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-240] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-440] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-329] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-342] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-310] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-281] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [218-335] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [338-340] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [343-370] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-396] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-45] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-279] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-309] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-232] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [239-259] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-290] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [292-293] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [297-352] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-306] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-408] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-449] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-246] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [254-312] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [343-365] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-361] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-369] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-449] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [213-254] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-310] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-286] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-347] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-352] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-426] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-449] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-327] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-369] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-398] for track '34' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-425] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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

</details>