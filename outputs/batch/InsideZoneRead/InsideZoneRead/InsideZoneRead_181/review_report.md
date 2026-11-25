# Play-Annotation-Generator Annotation Review — InsideZoneRead_181

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_181`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 123
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `21` | `18` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `21` | `18` |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | Team_Unknown | `21` | `18` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 64 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `18` | `17` | 62 | START | 90 | 90 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `0` | 65 | START | 65 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 65 | START | 65 | 140 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `13` | `12` | 65 | START | 65 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `7` | 65 | START | 65 | 140 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 65 | START | 65 | 139 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `21` | `18` | 73 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `21` | `18` | 79 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | `21` | `18` | 88 | START | 122 | 122 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `22` | `19` | 101 | START | 122 | 161 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 140 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 199 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 272 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 223 | 162 | inferred_complete_timeline |
| `Action_None` | 245 | 268 | 24 | inferred_complete_timeline |
| `Action_None` | 272 | 276 | 5 | inferred_complete_timeline |
| `Action_None` | 278 | 280 | 3 | inferred_complete_timeline |
| `Action_None` | 286 | 297 | 12 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 139 | 75 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_None` | 168 | 173 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 140 | 76 | inferred_complete_timeline |
| `Action_None` | 141 | 168 | 28 | inferred_complete_timeline |
| `Action_None` | 173 | 329 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 140 | 76 | inferred_complete_timeline |
| `Action_None` | 141 | 176 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 140 | 76 | inferred_complete_timeline |
| `Action_None` | 141 | 144 | 4 | inferred_complete_timeline |
| `Action_None` | 154 | 259 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 138 | 74 | inferred_complete_timeline |
| `Action_None` | 143 | 195 | 53 | inferred_complete_timeline |
| `Action_None` | 199 | 221 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 61 | 37 | inferred_complete_timeline |
| `Action_None` | 62 | 329 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 229 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 161 | 100 | inferred_complete_timeline |
| `Action_None` | 167 | 329 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 42 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 61 | 8 | inferred_complete_timeline |
| `Action_None` | 62 | 77 | 16 | inferred_complete_timeline |
| `Action_None` | 80 | 171 | 92 | inferred_complete_timeline |
| `Action_None` | 173 | 276 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 329 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 194 | 133 | inferred_complete_timeline |
| `Action_None` | 200 | 309 | 110 | inferred_complete_timeline |
| `Action_None` | 313 | 329 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 158 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 8–9 | 2 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 59–160 | 99 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 90–328 | 238 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 122–196 | 28 | 5 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 122–161 | 40 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 171–329 | 151 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 174–176 | 3 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 198–201 | 4 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 201–263 | 63 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 204–329 | 126 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 204–243 | 35 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 258–297 | 26 | 4 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 281–282 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 283–324 | 22 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 285–329 | 42 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 285–288 | 4 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 292–302 | 11 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 296–329 | 34 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 318–329 | 11 | 2 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 321–325 | 5 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 324–327 | 4 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `18` (Position_Unknown): Annotated start 62 != Inferred start 90
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `21` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `21` (Position_Unknown)
- ⚠️ `Action_Handoff` for actor_track_id `21` (Position_Unknown): Annotated start 88 != Inferred start 122
- ⚠️ `Action_BallCarry` for actor_track_id `22` (Position_Unknown): Annotated start 101 != Inferred start 122

### Track Identity Issues

- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=90, end=73. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '18' has invalid range: start=122, end=73. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '18' has invalid range: start=122, end=87. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '18' has invalid range: start=122, end=100. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [65-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-195] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-221] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-223] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-268] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-297] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-229] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-194] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-309] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-158] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-272] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-168] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-199] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-259] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-77] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-276] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-160] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-328] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [122-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-216] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-263] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-282] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-303] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-305] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-313] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-302] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-325] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '38' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_181'; source metadata written as null.

</details>