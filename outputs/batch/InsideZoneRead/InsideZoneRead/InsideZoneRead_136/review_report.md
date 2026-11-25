# Play-Annotation-Generator Annotation Review — InsideZoneRead_136

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_136`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | CB2 | defense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `8` | `7` |
| ✅ EXACT | `Action_ReadDefender` | RB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 273 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `19` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 273 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 319 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 273 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | CB2 | `15` | `14` | 274 | START | 274 | 274 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `14` | `13` | 276 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `17` | 276 | START | 278 | 303 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 276 | START | 276 | 327 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `20` | `19` | 276 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 276 | START | 276 | 279 |
| ✅ EXACT | `Action_SnapReceive` | RB | `8` | `7` | 287 | END | 274 | 287 |
| ✅ EXACT | `Action_ReadDefender` | RB | `8` | `7` | 290 | START | 290 | 304 |
| ✅ EXACT | `Action_Handoff` | RB | `8` | `7` | 305 | START | 305 | 319 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `6` | `5` | 320 | START | 320 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 374 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 208 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 270 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 273 | 1 | inferred_complete_timeline |
| `Action_None` | 274 | 274 | 1 | inferred_complete_timeline |
| `Action_None` | 277 | 282 | 6 | inferred_complete_timeline |
| `Action_None` | 323 | 326 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_SnapReceive` | 274 | 287 | 14 | inferred_complete_timeline |
| `Action_None` | 288 | 289 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 290 | 304 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 305 | 319 | 15 | inferred_complete_timeline |
| `Action_None` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 329 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 319 | 320 | inferred_complete_timeline |
| `Action_BallCarry` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 317 | 44 | inferred_complete_timeline |
| `Action_None` | 319 | 324 | 6 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 203 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 275 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 276 | 327 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 172 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 204 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 267 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 274 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 276 | 279 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 287 | 289 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 305 | 307 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 309 | 329 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 209 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 238 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 271 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 278 | 303 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 306 | 309 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 313 | 329 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 273 | 47 | inferred_complete_timeline |
| `Action_None` | 274 | 329 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 264 | 52 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 273 | 44 | inferred_complete_timeline |
| `Action_None` | 274 | 291 | 18 | inferred_complete_timeline |
| `Action_None` | 316 | 317 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 238 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 250 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 266 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 273 | 3 | inferred_complete_timeline |
| `Action_None` | 274 | 302 | 29 | inferred_complete_timeline |
| `Action_None` | 304 | 318 | 15 | inferred_complete_timeline |
| `Action_None` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 266 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 273 | 3 | inferred_complete_timeline |
| `Action_None` | 274 | 274 | 1 | inferred_complete_timeline |
| `Action_None` | 277 | 279 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 329 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 266 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 273 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 274 | 274 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 277 | 279 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 281 | 282 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 273 | 27 | inferred_complete_timeline |
| `Action_None` | 274 | 317 | 44 | inferred_complete_timeline |
| `Action_None` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 329 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 279 | 6 | inferred_complete_timeline |
| `Action_None` | 291 | 294 | 4 | inferred_complete_timeline |
| `Action_None` | 300 | 306 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 140–329 | 190 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 182–202 | 21 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 205–209 | 5 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 229–279 | 49 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 233–329 | 90 | 5 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 236–302 | 58 | 6 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 321–326 | 4 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 326–327 | 2 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `15` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `14` (LG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `20` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '13' has invalid range: start=276, end=204. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '19' has invalid range: start=276, end=145. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-273] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-203] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [276-327] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-317] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-206] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-273] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-291] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-204] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-264] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-273] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-243] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-273] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-317] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-250] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-302] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-318] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-279] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-204] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-273] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' for track '14' starts at frame 274, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallSnap' range [274-274] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [277-279] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [281-282] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-270] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 274, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [274-274] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-206] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-266] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-273] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 274, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [274-274] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-209] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-238] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-271] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [278-303] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [306-309] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [313-329] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-202] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-267] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-274] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [276-279] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [287-289] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [305-307] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-279] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-270] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-289] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-311] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-251] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-271] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '27' starts at frame 274, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [274-279] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-302] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_None' has invalid start frame 374. Video range is [0, 329].
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_136'; source metadata written as null.

</details>