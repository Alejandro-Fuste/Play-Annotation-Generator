# Play-Annotation-Generator Annotation Review — SplitZone_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_76`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 71
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 259 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 87 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `8` | 232 | START | 232 | 243 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `10` | 235 | START | 235 | 316 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `14` | 235 | START | 235 | 310 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 235 | START | 235 | 329 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 235 | START | 235 | 329 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `8` | `8` | 235 | START | 244 | 292 |
| ✅ EXACT | `Action_SplitBlock` | TE | `3` | `3` | 240 | START | 240 | 329 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 243 | END | 232 | 243 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 249 | START | 249 | 259 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `5` | 260 | START | 260 | 275 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 329 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_SnapReceive` | 232 | 243 | 12 | inferred_complete_timeline |
| `Action_None` | 244 | 248 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 249 | 259 | 11 | inferred_complete_timeline |
| `Action_None` | 260 | 388 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–351
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_BallCarry` | 260 | 275 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 290 | 318 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 320 | 322 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 350 | 351 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |
| `Action_SplitBlock` | 240 | 329 | 90 | inferred_complete_timeline |
| `Action_None` | 330 | 419 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–370
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_ZoneBlock` | 235 | 329 | 95 | inferred_complete_timeline |
| `Action_None` | 330 | 370 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_ZoneBlock` | 235 | 310 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 324 | 329 | 6 | inferred_complete_timeline |
| `Action_None` | 330 | 359 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–373
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 231 | 140 | inferred_complete_timeline |
| `Action_BallSnap` | 232 | 243 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 244 | 292 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 304 | 329 | 26 | inferred_complete_timeline |
| `Action_None` | 330 | 344 | 15 | inferred_complete_timeline |
| `Action_None` | 349 | 373 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–316
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_ZoneBlock` | 235 | 316 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–414
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_ZoneBlock` | 235 | 329 | 95 | inferred_complete_timeline |
| `Action_None` | 330 | 414 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 249 | 18 | inferred_complete_timeline |
| `Action_None` | 251 | 284 | 34 | inferred_complete_timeline |
| `Action_None` | 288 | 297 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–409
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 342 | 111 | inferred_complete_timeline |
| `Action_None` | 344 | 409 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–305
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 237 | 6 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 305 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 244 | 13 | inferred_complete_timeline |
| `Action_None` | 248 | 342 | 95 | inferred_complete_timeline |
| `Action_None` | 345 | 419 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–385
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 298 | 67 | inferred_complete_timeline |
| `Action_None` | 322 | 385 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–379
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 300 | 69 | inferred_complete_timeline |
| `Action_None` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_None` | 312 | 342 | 31 | inferred_complete_timeline |
| `Action_None` | 345 | 349 | 5 | inferred_complete_timeline |
| `Action_None` | 351 | 379 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–330
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 330 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 131–133 | 3 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 282–414 | 133 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 306–370 | 65 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 323–419 | 97 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 333–419 | 87 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 350–389 | 38 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 361–419 | 59 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 393–394 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 412–419 | 8 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 415–419 | 5 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 417–419 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 95 frames exceeds threshold 90 frames [start=235, end=329].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 95 frames exceeds threshold 90 frames [start=235, end=329].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (C) duration 95 frames exceeds threshold 90 frames [start=235, end=329].
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [232–243], lower_priority='Action_ZoneBlock' annotated_start=235, effective_Action_ZoneBlock_start=244.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (LG) duration 95 frames exceeds threshold 90 frames [start=235, end=329].
- ⚠️ Action 'Action_None' range [232-298] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-385] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-300] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-342] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-349] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-379] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [235-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-414] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-370] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [260-275] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [290-318] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [320-322] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [335-336] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [350-351] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-342] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [244-292] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-344] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-373] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-342] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-409] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [235-316] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-388] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-330] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-231] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-305] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [235-310] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [321-322] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-359] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-284] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-297] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-414] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-370] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-380] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-389] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '23' has 1 frames without a visible bounding box.
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

</details>