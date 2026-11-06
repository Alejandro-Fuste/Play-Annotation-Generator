# Play-Annotation-Generator Annotation Review — OutsideZoneRead_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_55`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `22` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `15` | 130 | START | 130 | 157 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 130 | START | 130 | 157 |
| ✅ EXACT | `Action_ZoneBlock` | C | `19` | `19` | 130 | START | 130 | 139 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `20` | `20` | 130 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `22` | 130 | START | 130 | 179 |
| ✅ EXACT | `Action_PressEdge` | RB | `6` | `6` | 136 | START | 136 | 183 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `18` | `18` | 141 | START | 141 | 149 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 150 | START | 150 | 161 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 141 | 149 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 150 | 161 | 12 | inferred_complete_timeline |
| `Action_None` | 162 | 329 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_PressEdge` | 136 | 183 | 48 | inferred_complete_timeline |
| `Action_None` | 184 | 201 | 18 | inferred_complete_timeline |
| `Action_None` | 205 | 218 | 14 | inferred_complete_timeline |
| `Action_None` | 220 | 223 | 4 | inferred_complete_timeline |
| `Action_None` | 225 | 264 | 40 | inferred_complete_timeline |
| `Action_None` | 266 | 329 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
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
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 228 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 157 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 139 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 179 | 50 | inferred_complete_timeline |
| `Action_None` | 180 | 188 | 9 | inferred_complete_timeline |
| `Action_None` | 190 | 329 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 157 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 179 | 11 | inferred_complete_timeline |
| `Action_None` | 180 | 326 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–305
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 175 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 185 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 295 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 305 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 220 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 242 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 329 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 170 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 255 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 277 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 321 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 325 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 284 | 285 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 306 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 322 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 276 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 292 | 293 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 312 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 325 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 278 | 279 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 294 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 301 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 314 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 329 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 325 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–127 | 115 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 7–40 | 7 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 21–22 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 191–326 | 136 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 195–219 | 25 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 205–252 | 39 | 5 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 243–325 | 48 | 7 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 248–296 | 39 | 4 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 251–325 | 66 | 4 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 258–320 | 63 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 258–327 | 66 | 3 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 274–306 | 17 | 5 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `20` (LT)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=130, end=129. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-292] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-312] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-325] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-201] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-264] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-242] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-284] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-306] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-322] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-276] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-278] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-294] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-301] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-314] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-163] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-185] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-295] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-305] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-325] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-170] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-255] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-277] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-321] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-325] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-326] for track '15' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-228] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-139] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-31] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-112] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-188] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-11] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-326] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-219] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-226] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-231] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-244] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-252] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-257] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-264] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-307] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-319] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-325] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-250] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-273] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-296] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-281] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-313] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-319] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-325] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-320] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-299] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-306] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-327] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-278] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-286] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-291] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-302] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-306] for track '33' has 1 frames without a visible bounding box.
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