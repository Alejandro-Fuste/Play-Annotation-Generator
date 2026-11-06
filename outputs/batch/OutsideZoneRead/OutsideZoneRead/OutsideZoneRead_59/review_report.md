# Play-Annotation-Generator Annotation Review — OutsideZoneRead_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_59`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_PressEdge` | DT2 | defense | `11` | `11` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 329 |
| ✅ EXACT | `Action_PressEdge` | DT2 | `11` | `11` | 133 | START | 133 | 172 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `19` | `19` | 138 | START | 138 | 147 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 148 | START | 148 | 160 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `15` | `15` | 170 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | C | `20` | `20` | 170 | START | 170 | 172 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 170 | START | 170 | 172 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 138 | 147 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 148 | 160 | 13 | inferred_complete_timeline |
| `Action_None` | 161 | 198 | 38 | inferred_complete_timeline |
| `Action_None` | 202 | 311 | 110 | inferred_complete_timeline |
| `Action_None` | 313 | 320 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

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
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 320 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 329 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 169 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_None` | 192 | 196 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_None` | 173 | 329 | 157 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 202 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 222 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 309 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PressEdge` | 133 | 172 | 40 | inferred_complete_timeline |
| `Action_None` | 173 | 216 | 44 | inferred_complete_timeline |
| `Action_None` | 218 | 226 | 9 | inferred_complete_timeline |
| `Action_None` | 228 | 230 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 273 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 329 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 329 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 226 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 255 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 266 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 307 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 329 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 329 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 243 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 297 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 215 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 221 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 263 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 326 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–192 | 182 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 161–225 | 56 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 196–329 | 129 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 215–308 | 80 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 231–232 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 238–302 | 65 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 242–326 | 83 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 243–322 | 80 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 256–321 | 64 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 295–297 | 3 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `15` (LT)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 120: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '15' has invalid range: start=170, end=137. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-194] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-215] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-263] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-326] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-205] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-320] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-273] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-222] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-216] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-173] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-234] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-297] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-255] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-266] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-307] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-329] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-311] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-320] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [170-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-225] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-199] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-280] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-263] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-273] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-303] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-308] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-302] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-326] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-322] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-272] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-321] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-297] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>