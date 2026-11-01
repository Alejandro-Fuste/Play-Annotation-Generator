# Play-Annotation-Generator Annotation Review — InsideZoneRead_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_60`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 117 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 194 | START | 194 | 207 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `1` | `0` | 196 | START | 196 | 232 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 196 | START | 211 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `2` | 196 | START | 196 | 244 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `4` | 196 | START | 196 | 270 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `5` | 196 | START | 196 | 261 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 208 | END | 194 | 208 |
| ✅ EXACT | `Action_ReadDefender` | QB | `2` | `1` | 211 | START | 211 | 224 |
| ✅ EXACT | `Action_Handoff` | QB | `2` | `1` | 225 | START | 225 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `1` | `0` | 233 | START | 233 | 266 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `12` | `11` | 236 | START | 237 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 294 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_SnapReceive` | 194 | 208 | 15 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 211 | 224 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 225 | 235 | 11 | inferred_complete_timeline |
| `Action_None` | 236 | 283 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–366
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 270 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 280 | 294 | 15 | inferred_complete_timeline |
| `Action_None` | 295 | 366 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 195 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 244 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 294 | 49 | inferred_complete_timeline |
| `Action_None` | 295 | 299 | 5 | inferred_complete_timeline |
| `Action_None` | 307 | 389 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 193 | 53 | inferred_complete_timeline |
| `Action_BallSnap` | 194 | 207 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 245 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 268 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–346
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 232 | 37 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 233 | 266 | 34 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 275 | 294 | 20 | inferred_complete_timeline |
| `Action_None` | 295 | 335 | 41 | inferred_complete_timeline |
| `Action_None` | 338 | 342 | 5 | inferred_complete_timeline |
| `Action_None` | 345 | 346 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–362
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 195 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 261 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 265 | 294 | 30 | inferred_complete_timeline |
| `Action_None` | 295 | 354 | 60 | inferred_complete_timeline |
| `Action_None` | 357 | 359 | 3 | inferred_complete_timeline |
| `Action_None` | 361 | 362 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–377
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 377 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 113 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 193 | 79 | inferred_complete_timeline |
| `Action_None` | 194 | 333 | 140 | inferred_complete_timeline |
| `Action_None` | 344 | 389 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 256 | 63 | inferred_complete_timeline |
| `Action_None` | 260 | 341 | 82 | inferred_complete_timeline |
| `Action_None` | 350 | 389 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 236 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–382
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 323 | 130 | inferred_complete_timeline |
| `Action_None` | 326 | 341 | 16 | inferred_complete_timeline |
| `Action_None` | 343 | 349 | 7 | inferred_complete_timeline |
| `Action_None` | 359 | 362 | 4 | inferred_complete_timeline |
| `Action_None` | 364 | 365 | 2 | inferred_complete_timeline |
| `Action_None` | 372 | 382 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 109–389 | 267 | 5 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 111–251 | 141 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 226–237 | 12 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 254–292 | 38 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 258–387 | 114 | 5 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 259–369 | 106 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 265–389 | 90 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 269–385 | 109 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 298–389 | 89 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 301–369 | 63 | 3 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 351–352 | 2 | 1 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 357–371 | 13 | 2 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 377–385 | 8 | 2 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 389–389 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LG) duration 99 frames exceeds threshold 90 frames [start=196, end=294].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 99 frames exceeds threshold 90 frames [start=196, end=294].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 99 frames exceeds threshold 90 frames [start=196, end=294].
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [194–208], lower_priority='Action_ZoneBlock' annotated_start=196, effective_Action_ZoneBlock_start=209.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [233-266] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [268-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-335] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-342] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-193] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-283] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-323] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-341] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-349] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-362] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-382] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-270] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-366] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-261] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-354] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-236] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-256] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-341] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-377] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [194-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [211-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [248-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-113] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-333] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-232] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [237-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [302-366] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [369-376] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-251] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-289] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-278] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-317] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-366] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-381] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-387] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-280] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-369] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-273] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-310] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-350] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-280] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-385] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-334] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-314] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-325] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-369] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-365] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-382] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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