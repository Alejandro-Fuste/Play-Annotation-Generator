# Play-Annotation-Generator Annotation Review — OutsideZoneRead_30

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_30`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 479
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 121
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadEdgeDefender` | RB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | RB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 295 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 249 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 247 | START | 247 | 280 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `2` | 247 | START | 247 | 280 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 247 | START | 247 | 280 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `7` | 247 | START | 247 | 280 |
| ✅ EXACT | `Action_PressEdge` | RB | `9` | `9` | 250 | START | 250 | 257 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadEdgeDefender` | RB | `9` | `9` | 258 | START | 258 | 269 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | RB | `9` | `9` | 278 | START | 278 | 378 |

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
- **Visible Frames:** 0–472
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 295 | 296 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 327 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 472 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_PressEdge` | 250 | 257 | 8 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 258 | 269 | 12 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 274 | 277 | 4 | inferred_complete_timeline |
| `Action_Keep` | 278 | 378 | 101 | inferred_complete_timeline |
| `Action_Keep` | 380 | 398 | 19 | inferred_complete_timeline |
| `Action_Keep` | 406 | 479 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 95 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 280 | 34 | inferred_complete_timeline |
| `Action_None` | 281 | 325 | 45 | inferred_complete_timeline |
| `Action_None` | 332 | 479 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–459
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 280 | 34 | inferred_complete_timeline |
| `Action_None` | 281 | 284 | 4 | inferred_complete_timeline |
| `Action_None` | 288 | 459 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–471
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 280 | 34 | inferred_complete_timeline |
| `Action_None` | 281 | 471 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 280 | 34 | inferred_complete_timeline |
| `Action_None` | 281 | 305 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 65 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 258 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–438
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 290 | 291 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 438 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 248 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 280 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 245 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 143 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–340
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 277 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 291 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 340 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 301 | 302 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 302 | 303 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 316 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–433 | 398 | 8 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 255–459 | 199 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 263–314 | 47 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 271–479 | 202 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 289–479 | 157 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 300–412 | 111 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 308–347 | 40 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 330–479 | 150 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 335–414 | 79 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 349–479 | 75 | 5 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 351–360 | 10 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 357–426 | 64 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 361–476 | 86 | 4 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 363–479 | 117 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 371–479 | 103 | 2 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 380–479 | 88 | 3 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 383–389 | 7 | 1 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 408–479 | 72 | 1 | Undefined position; Undefined team |
| `35` | `37` | Position_Unknown | Team_Unknown | 416–420 | 5 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 454–479 | 26 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ReadEdgeDefender` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 62: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-65] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-258] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [247-280] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-325] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-459] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-95] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-143] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-305] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-301] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-471] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-248] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-280] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [258-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [278-378] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [380-398] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [406-479] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-302] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-316] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-295] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-327] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-472] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-277] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-291] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-340] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-290] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-438] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-146] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-245] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-242] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-276] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-297] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-336] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-433] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-281] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-408] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-412] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-459] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-275] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-283] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-314] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-293] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-395] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-446] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-385] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-383] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-412] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-347] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-387] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-414] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-364] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-421] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-453] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [456-464] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-360] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-367] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-426] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-377] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-417] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-454] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [462-476] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-432] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-410] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-441] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-389] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-479] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-420] for track '35' has 1 frames without a visible bounding box.
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

</details>