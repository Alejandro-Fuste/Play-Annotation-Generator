# Play-Annotation-Generator Annotation Review — OutsideZoneRead_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_37`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 26
- **Ball Tracks:** 2
- **Action Segments:** 67
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 147 |
| ✅ EXACT | `Action_PressEdge` | RB | `12` | `12` | 148 | START | 148 | 189 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 148 | START | 148 | 200 |
| ✅ EXACT | `Action_ZoneBlock` | C | `4` | `4` | 148 | START | 148 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `5` | 148 | START | 148 | 178 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `8` | 148 | START | 148 | 200 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `9` | 148 | START | 148 | 200 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `16` | `15` | 159 | START | 159 | 178 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `7` | `7` | 169 | START | 169 | 178 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 169 | 178 | 10 | inferred_complete_timeline |
| `Action_None` | 179 | 235 | 57 | inferred_complete_timeline |
| `Action_None` | 239 | 253 | 15 | inferred_complete_timeline |
| `Action_None` | 257 | 387 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 62 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 90 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 127 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 147 | 14 | inferred_complete_timeline |
| `Action_PressEdge` | 148 | 189 | 42 | inferred_complete_timeline |
| `Action_None` | 190 | 198 | 9 | inferred_complete_timeline |
| `Action_None` | 201 | 365 | 165 | inferred_complete_timeline |
| `Action_None` | 369 | 375 | 7 | inferred_complete_timeline |
| `Action_None` | 378 | 389 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 200 | 53 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_None` | 237 | 247 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 200 | 53 | inferred_complete_timeline |
| `Action_None` | 201 | 250 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 200 | 53 | inferred_complete_timeline |
| `Action_None` | 201 | 220 | 20 | inferred_complete_timeline |
| `Action_None` | 235 | 262 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 200 | 53 | inferred_complete_timeline |
| `Action_None` | 201 | 208 | 8 | inferred_complete_timeline |
| `Action_None` | 211 | 265 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 178 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 195 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 254 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 273 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 270 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 223 | 224 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 227 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 236 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 246 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 58–270 | 213 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 68–203 | 136 | 3 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 220–389 | 167 | 2 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 227–233 | 6 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 251–254 | 4 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 257–389 | 130 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 262–318 | 57 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 275–336 | 62 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 325–389 | 65 | 1 | Undefined position; Undefined team |
| `24` | `39` | Position_Unknown | Team_Unknown | 368–376 | 4 | 2 | Undefined position; Undefined team |
| `25` | `42` | Position_Unknown | Team_Unknown | 376–378 | 3 | 1 | Undefined position; Undefined team |
| `26` | `43` | Position_Unknown | Team_Unknown | 376–389 | 14 | 1 | Undefined position; Undefined team |
| `27` | `45` | Position_Unknown | Team_Unknown | 384–389 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | 52 | 56 | 5 | 100.0% | None |
| `22` | `31` | 322 | 322 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 51 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-211] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-206] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-254] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-273] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-270] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-247] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-220] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-262] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-195] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-236] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-246] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [169-178] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-253] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-387] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-250] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-208] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-265] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-223] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-36] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-62] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-127] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-147] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-365] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-375] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-270] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' for track '15' starts at frame 159, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Handoff' range [159-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-203] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-295] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-254] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-380] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-318] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-336] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-369] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-378] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-385] for track '27' has 1 frames without a visible bounding box.
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