# Play-Annotation-Generator Annotation Review — OutsideZoneRead_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_40`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 203 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 113 |
| ✅ EXACT | `Action_PressEdge` | RB | `14` | `14` | 112 | START | 112 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 112 | START | 112 | 118 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `18` | 112 | START | 112 | 151 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `20` | `20` | 112 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 112 | START | 112 | 134 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 112 | START | 112 | 151 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `9` | `9` | 114 | START | 114 | 124 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 125 | START | 125 | 142 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 114 | 124 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 125 | 142 | 18 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PressEdge` | 112 | 199 | 88 | inferred_complete_timeline |
| `Action_None` | 200 | 327 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 329 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 134 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 139 | 4 | inferred_complete_timeline |
| `Action_None` | 174 | 190 | 17 | inferred_complete_timeline |
| `Action_None` | 193 | 223 | 31 | inferred_complete_timeline |
| `Action_None` | 236 | 241 | 6 | inferred_complete_timeline |
| `Action_None` | 245 | 264 | 20 | inferred_complete_timeline |
| `Action_None` | 268 | 270 | 3 | inferred_complete_timeline |
| `Action_None` | 272 | 283 | 12 | inferred_complete_timeline |
| `Action_None` | 289 | 320 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 118 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 151 | 32 | inferred_complete_timeline |
| `Action_None` | 152 | 162 | 11 | inferred_complete_timeline |
| `Action_None` | 166 | 241 | 76 | inferred_complete_timeline |
| `Action_None` | 244 | 280 | 37 | inferred_complete_timeline |
| `Action_None` | 283 | 297 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 151 | 40 | inferred_complete_timeline |
| `Action_None` | 152 | 162 | 11 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 186 | 5 | inferred_complete_timeline |
| `Action_None` | 197 | 205 | 9 | inferred_complete_timeline |
| `Action_None` | 210 | 241 | 32 | inferred_complete_timeline |
| `Action_None` | 246 | 255 | 10 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 269 | 305 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 151 | 40 | inferred_complete_timeline |
| `Action_None` | 152 | 245 | 94 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_None` | 252 | 265 | 14 | inferred_complete_timeline |
| `Action_None` | 267 | 272 | 6 | inferred_complete_timeline |
| `Action_None` | 276 | 312 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 177 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 234 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 241 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 249 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 266 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 175 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 279 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 296 | 297 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 314 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 326 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–249 | 239 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 141–223 | 48 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 166–174 | 6 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 178–329 | 152 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 182–191 | 10 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 194–294 | 70 | 9 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 203–289 | 74 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 252–253 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 257–258 | 2 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 273–329 | 57 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 279–329 | 44 | 3 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 298–329 | 27 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 315–327 | 8 | 2 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 316–317 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `20` (LT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 82: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=112, end=107. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-240] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-245] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-265] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-312] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-296] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-314] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-326] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-279] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-175] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-306] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-241] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-280] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-297] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-327] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-177] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-234] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-241] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-162] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-241] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-255] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-305] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-203] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-190] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-264] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-283] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-320] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-157] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-223] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-174] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-231] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-241] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-252] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-280] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-290] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-294] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-222] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-289] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-281] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-293] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-304] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-316] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-327] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>