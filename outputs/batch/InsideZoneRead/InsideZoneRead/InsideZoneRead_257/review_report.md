# Play-Annotation-Generator Annotation Review — InsideZoneRead_257

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_257`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Keep` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 0 | START | 0 | 14 |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `1` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `14` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `2` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `22` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `3` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 2 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 3 | START | 15 | 15 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `17` | 3 | START | 3 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 3 | START | 3 | 47 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `20` | 3 | START | 3 | 76 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 3 | START | 3 | 76 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 14 | END | 0 | 14 |
| ✅ EXACT | `Action_ReadDefender` | QB | `15` | `14` | 16 | START | 16 | 19 |
| ✅ EXACT | `Action_Keep` | QB | `15` | `14` | 20 | START | 20 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `15` | `14` | 44 | START | 44 | 234 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 76 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–330
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_SnapReceive` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 15 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_Keep` | 20 | 43 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 44 | 234 | 191 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 297 | 62 | inferred_complete_timeline |
| `Action_BallCarry` | 299 | 306 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 311 | 322 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 327 | 330 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–17
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 17 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 333 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–357
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 357 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_BallSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 15 | 15 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 30 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_None` | 90 | 105 | 16 | inferred_complete_timeline |
| `Action_None` | 107 | 359 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 3 | 76 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 348 | 272 | inferred_complete_timeline |
| `Action_None` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 3 | 47 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 75 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 353 | 354 | inferred_complete_timeline |
| `Action_None` | 359 | 359 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 37 | 359 | 323 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_None` | 82 | 101 | 20 | inferred_complete_timeline |
| `Action_None` | 111 | 359 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 325 | 326 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–332
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 324 | 325 | inferred_complete_timeline |
| `Action_None` | 326 | 332 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–332
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 332 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_None` | 207 | 348 | 142 | inferred_complete_timeline |
| `Action_None` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_None` | 96 | 132 | 37 | inferred_complete_timeline |
| `Action_None` | 138 | 324 | 187 | inferred_complete_timeline |
| `Action_None` | 326 | 334 | 9 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_None` | 341 | 347 | 7 | inferred_complete_timeline |
| `Action_None` | 350 | 352 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–193 | 188 | 4 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–97 | 98 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 38–336 | 299 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 47–359 | 269 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 122–124 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 132–359 | 226 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 168–332 | 130 | 11 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 233–359 | 58 | 12 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 274–279 | 6 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 336–356 | 21 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 338–349 | 12 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 342–349 | 8 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 346–359 | 14 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 514: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [0–14], lower_priority='Action_ZoneBlock' annotated_start=3, effective_Action_ZoneBlock_start=15.
- ⚠️ Action 'Action_None' range [0-353] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-177] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-333] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-325] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-97] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-359] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-324] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-332] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-324] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-334] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-347] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-205] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-348] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-359] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '13' starts at frame 15, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [15-15] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-70] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-105] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [44-234] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [236-297] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [299-306] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [311-322] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [327-330] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-19] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-332] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-357] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-101] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-359] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [3-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-348] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-17] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-336] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-312] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-187] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-262] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-308] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-332] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-255] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-341] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-353] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-279] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-356] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-349] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-349] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-359] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>