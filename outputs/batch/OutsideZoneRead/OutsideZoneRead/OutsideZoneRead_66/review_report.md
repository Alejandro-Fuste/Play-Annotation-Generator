# Play-Annotation-Generator Annotation Review — OutsideZoneRead_66

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_66`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 33
- **Ball Tracks:** 1
- **Action Segments:** 85
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_PressEdge` | LB2 | defense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `0` | `0` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `0` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 239 |
| ✅ EXACT | `Action_PressEdge` | LB2 | `13` | `13` | 240 | START | 240 | 283 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `1` | 240 | START | 240 | 283 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `11` | `11` | 240 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `2` | 240 | START | 240 | 283 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `5` | `5` | 240 | START | 240 | 254 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 240 | START | 240 | 283 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `0` | `0` | 248 | START | 248 | 255 |
| ✅ EXACT | `Action_Handoff` | QB | `0` | `0` | 258 | START | 258 | 268 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 248 | 255 | 8 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 258 | 268 | 11 | inferred_complete_timeline |
| `Action_None` | 269 | 299 | 31 | inferred_complete_timeline |
| `Action_None` | 303 | 305 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 283 | 44 | inferred_complete_timeline |
| `Action_None` | 284 | 387 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–379
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 239 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 283 | 44 | inferred_complete_timeline |
| `Action_None` | 284 | 302 | 19 | inferred_complete_timeline |
| `Action_None` | 304 | 379 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 199 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–373
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 254 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 271 | 283 | 13 | inferred_complete_timeline |
| `Action_None` | 284 | 311 | 28 | inferred_complete_timeline |
| `Action_None` | 313 | 373 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 283 | 44 | inferred_complete_timeline |
| `Action_None` | 284 | 449 | 166 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–368
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 368 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 241 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 335 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 449 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 246 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 248 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 239 | 237 | inferred_complete_timeline |
| `Action_PressEdge` | 240 | 283 | 44 | inferred_complete_timeline |
| `Action_None` | 284 | 310 | 27 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 449 | 450 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–449 | 379 | 10 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 6–262 | 257 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 82–449 | 368 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 109–165 | 57 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 174–280 | 107 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 217–382 | 166 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 252–357 | 106 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 258–431 | 170 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 269–438 | 169 | 2 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 278–316 | 17 | 2 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 288–395 | 105 | 2 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 294–351 | 54 | 2 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 306–449 | 127 | 4 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 308–309 | 2 | 1 | Undefined position; Undefined team |
| `28` | `44` | Position_Unknown | Team_Unknown | 363–449 | 87 | 1 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 369–441 | 65 | 4 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 371–398 | 28 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 374–449 | 67 | 4 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 387–449 | 63 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 423–448 | 22 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | 38 | 95 | 19 | 32.8% | 42–47, 52–54, 64–87, 89–94 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `11` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '11' has invalid range: start=240, end=199. Clamping end to start.
- ⚠️ Action 'Action_None' range [269-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-449] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-302] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-379] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-241] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-335] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-368] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [240-254] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-311] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-373] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-118] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-134] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-195] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-236] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-245] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-256] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-321] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-449] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-248] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-387] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-246] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-310] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-262] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-449] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-280] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-382] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-357] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-353] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-431] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-342] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-438] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-316] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-321] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-395] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-331] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-351] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-331] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-337] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-422] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-449] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-449] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-411] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-433] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-437] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-441] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-398] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-411] for track '31' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-431] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-442] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-439] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-448] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>