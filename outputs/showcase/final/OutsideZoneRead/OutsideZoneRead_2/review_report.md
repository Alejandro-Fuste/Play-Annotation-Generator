# Play-Annotation-Generator Annotation Review — OutsideZoneRead_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_2`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 120
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | Team_Unknown | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | Team_Unknown | `22` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 336 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 277 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | `12` | `12` | 200 | START | 200 | 231 |
| ✅ EXACT | `Action_ZoneBlock` | C | `10` | `10` | 205 | START | 205 | 244 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 205 | START | 205 | 244 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `14` | 205 | START | 205 | 244 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `5` | 205 | START | 205 | 244 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `8` | `8` | 212 | START | 212 | 222 |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | `22` | `19` | 222 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 212 | 222 | 11 | inferred_complete_timeline |
| `Action_None` | 223 | 286 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 277 | 278 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 449 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 336 | 337 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 244 | 40 | inferred_complete_timeline |
| `Action_None` | 245 | 449 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 244 | 40 | inferred_complete_timeline |
| `Action_None` | 245 | 350 | 106 | inferred_complete_timeline |
| `Action_None` | 356 | 449 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 244 | 40 | inferred_complete_timeline |
| `Action_None` | 245 | 449 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 244 | 40 | inferred_complete_timeline |
| `Action_None` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 80 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 119 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 299 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 449 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–434
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 434 | 435 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 279 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 449 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–430
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 269 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 276 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 367 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 419 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 422 | 430 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 435 | 436 | inferred_complete_timeline |
| `Action_PreSnap` | 442 | 449 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 276 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 399 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 401 | 403 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 405 | 449 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–449 | 447 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–449 | 425 | 5 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 2–84 | 82 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 204–209 | 6 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 229–449 | 217 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 241–449 | 185 | 4 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 254–449 | 195 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 275–276 | 2 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 284–447 | 152 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 294–445 | 139 | 5 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 297–429 | 117 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 306–307 | 2 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 336–339 | 4 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 358–443 | 42 | 5 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 363–449 | 87 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 369–446 | 62 | 4 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 377–391 | 6 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 386–388 | 3 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 401–427 | 16 | 2 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 410–411 | 2 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 415–416 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `12` (2 segments found)
- ❌ Missing segment for action `Action_Handoff` on target `19` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 6: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Segment 'Action_Handoff' for track '19' has invalid range: start=222, end=209. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-247] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-276] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-367] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-419] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-430] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-265] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-265] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-336] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-277] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-323] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-449] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-435] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-449] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-218] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-279] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-350] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-276] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-399] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-403] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [200-231] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-421] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-449] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-434] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-80] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-119] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-209] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-267] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-334] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-407] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-419] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-338] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-276] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-431] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-447] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-394] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-425] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-431] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-435] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-445] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-332] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-429] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-339] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-373] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-410] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-418] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-443] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-413] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-420] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-427] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-446] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-384] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-391] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-388] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-412] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-427] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-411] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-416] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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