# Play-Annotation-Generator Annotation Review — InsideZoneRead_289

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_289`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Keep` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 19 | START | 19 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `11` | 22 | START | 22 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `12` | 22 | START | 22 | 107 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 22 | START | 36 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 22 | START | 22 | 51 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 35 | END | 19 | 35 |
| ✅ EXACT | `Action_ReadDefender` | QB | `19` | `18` | 42 | START | 42 | 50 |
| ✅ EXACT | `Action_Keep` | QB | `19` | `18` | 51 | START | 51 | 69 |
| ✅ EXACT | `Action_BallCarry` | QB | `19` | `18` | 70 | START | 70 | 362 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 107 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–362
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 35 | 17 | inferred_complete_timeline |
| `Action_None` | 36 | 41 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 42 | 50 | 9 | inferred_complete_timeline |
| `Action_Keep` | 51 | 69 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 362 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 375 | 357 | inferred_complete_timeline |
| `Action_None` | 377 | 387 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 69 | 51 | inferred_complete_timeline |
| `Action_None` | 74 | 340 | 267 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_None` | 362 | 370 | 9 | inferred_complete_timeline |
| `Action_None` | 381 | 382 | 2 | inferred_complete_timeline |
| `Action_None` | 384 | 389 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 204 | 186 | inferred_complete_timeline |
| `Action_None` | 206 | 265 | 60 | inferred_complete_timeline |
| `Action_None` | 269 | 389 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 389 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 59 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 107 | 86 | inferred_complete_timeline |
| `Action_None` | 108 | 326 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 51 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 107 | 52 | inferred_complete_timeline |
| `Action_None` | 108 | 389 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 35 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 40 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 47 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 100 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 79 | 61 | inferred_complete_timeline |
| `Action_None` | 81 | 389 | 309 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 79 | 61 | inferred_complete_timeline |
| `Action_None` | 83 | 389 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 72 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 96 | 23 | inferred_complete_timeline |
| `Action_None` | 99 | 110 | 12 | inferred_complete_timeline |
| `Action_None` | 119 | 389 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 45 | 27 | inferred_complete_timeline |
| `Action_None` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_None` | 50 | 98 | 49 | inferred_complete_timeline |
| `Action_None` | 102 | 389 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 326 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 81 | 63 | inferred_complete_timeline |
| `Action_None` | 85 | 91 | 7 | inferred_complete_timeline |
| `Action_None` | 96 | 389 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 76 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 131 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 389 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 375 | 357 | inferred_complete_timeline |
| `Action_None` | 378 | 389 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 154 | 136 | inferred_complete_timeline |
| `Action_None` | 159 | 169 | 11 | inferred_complete_timeline |
| `Action_None` | 176 | 389 | 214 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 6–53 | 42 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 56–389 | 334 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 64–389 | 325 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 68–264 | 197 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 86–210 | 125 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 89–193 | 40 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 105–148 | 42 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 105–107 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 112–118 | 7 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 127–326 | 195 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 143–146 | 4 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 203–389 | 182 | 2 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 217–389 | 163 | 4 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 241–389 | 148 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 286–288 | 3 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 319–320 | 2 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 327–389 | 62 | 2 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 327–389 | 47 | 5 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 327–328 | 2 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 328–389 | 59 | 2 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 328–330 | 3 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 349–351 | 3 | 1 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 351–389 | 39 | 1 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 364–367 | 4 | 1 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 369–370 | 2 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 378–385 | 7 | 2 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 378–381 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 22 != Inferred start 36
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [19–35], lower_priority='Action_ZoneBlock' annotated_start=22, effective_Action_ZoneBlock_start=36.
- ⚠️ Action 'Action_None' range [19-69] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-340] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-370] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-204] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-265] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-326] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-72] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-96] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-81] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-375] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-375] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-387] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-326] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-98] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-389] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-154] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-169] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-389] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-389] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-362] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-79] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-389] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-51] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-9] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-389] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-264] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-143] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-326] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-389] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-232] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-359] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-382] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-259] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-389] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-366] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-389] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-353] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-358] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-376] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-378] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-389] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-367] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-382] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-381] for track '47' has 1 frames without a visible bounding box.
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

</details>