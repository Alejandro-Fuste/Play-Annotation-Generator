# Play-Annotation-Generator Annotation Review — OutsideZoneRead_68

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_68`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `9` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `5` | `5` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `9` | `9` | 186 | START | 186 | 210 |
| ✅ EXACT | `Action_ZoneBlock` | C | `10` | `10` | 186 | START | 186 | 226 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `11` | 186 | START | 186 | 226 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `13` | `13` | 186 | START | 186 | 193 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 186 | START | 186 | 223 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `6` | 186 | START | 186 | 226 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `5` | `5` | 191 | START | 191 | 199 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `5` | `5` | 200 | START | 207 | 208 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 191 | 199 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 209 | 291 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PressEdge` | 186 | 210 | 25 | inferred_complete_timeline |
| `Action_PressEdge` | 250 | 252 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 223 | 38 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–398
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 226 | 41 | inferred_complete_timeline |
| `Action_None` | 227 | 246 | 20 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 292 | 42 | inferred_complete_timeline |
| `Action_None` | 297 | 359 | 63 | inferred_complete_timeline |
| `Action_None` | 366 | 369 | 4 | inferred_complete_timeline |
| `Action_None` | 371 | 378 | 8 | inferred_complete_timeline |
| `Action_None` | 383 | 386 | 4 | inferred_complete_timeline |
| `Action_None` | 397 | 398 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–403
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 226 | 41 | inferred_complete_timeline |
| `Action_None` | 227 | 403 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 193 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–366
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 226 | 41 | inferred_complete_timeline |
| `Action_None` | 227 | 261 | 35 | inferred_complete_timeline |
| `Action_None` | 264 | 366 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–398
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 319 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 346 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 397 | 398 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–382
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 254 | 255 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 295 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 382 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 227 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 275 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–411
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 252 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 401 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 403 | 407 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 410 | 411 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 419 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 263 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 274 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 342 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 387 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 397 | 400 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 410 | 419 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–385
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 277 | 278 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 299 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 385 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–419 | 408 | 4 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 221–243 | 16 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 229–410 | 180 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 230–231 | 2 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 236–419 | 182 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 241–410 | 167 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 243–419 | 154 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 255–419 | 165 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 258–261 | 4 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 277–398 | 122 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 286–419 | 115 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 313–419 | 107 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 388–419 | 25 | 4 | Undefined position; Undefined team |
| `27` | `45` | Position_Unknown | Team_Unknown | 419–419 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `9` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `5` (QB): Annotated start 200 != Inferred start 207

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 138: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-319] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-346] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-398] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-240] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-263] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-274] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-342] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-387] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-400] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-277] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-385] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-254] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-295] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-382] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-223] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [191-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-291] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-246] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-292] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-378] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-386] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-227] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-275] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [186-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [250-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-403] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-366] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-252] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-401] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-407] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-411] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-193] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-191] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-257] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-269] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-246] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-314] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-410] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-271] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-410] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-248] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-419] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-261] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-398] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-386] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-395] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-398] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-413] for track '26' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.

</details>