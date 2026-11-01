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
- **Action Segments:** 114
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
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
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `16` | `15` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `19` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 173 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 127 | START | 127 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 130 | START | 130 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `17` | 130 | START | 130 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `1` | 130 | START | 130 | 194 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `20` | `19` | 130 | START | 145 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 130 | START | 130 | 202 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 144 | END | 127 | 144 |
| ✅ EXACT | `Action_ReadDefender` | QB | `16` | `15` | 149 | START | 149 | 163 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `16` | `15` | 164 | START | 168 | 173 |
| ✅ EXACT | `Action_BallCarry` | RB | `8` | `7` | 174 | START | 174 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 246 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_SnapReceive` | 127 | 144 | 18 | inferred_complete_timeline |
| `Action_None` | 145 | 148 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 149 | 163 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 168 | 173 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 208 | 35 | inferred_complete_timeline |
| `Action_None` | 213 | 270 | 58 | inferred_complete_timeline |
| `Action_None` | 273 | 274 | 2 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_BallCarry` | 174 | 329 | 156 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 329 | 203 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 329 | 203 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 317 | 191 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 194 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 203 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 227 | 246 | 20 | inferred_complete_timeline |
| `Action_None` | 247 | 327 | 81 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 163 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 172 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 204 | 31 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_BallSnap` | 127 | 144 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 145 | 1 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 202 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 227 | 246 | 20 | inferred_complete_timeline |
| `Action_None` | 247 | 267 | 21 | inferred_complete_timeline |
| `Action_None` | 271 | 274 | 4 | inferred_complete_timeline |
| `Action_None` | 276 | 279 | 4 | inferred_complete_timeline |
| `Action_None` | 287 | 289 | 3 | inferred_complete_timeline |
| `Action_None` | 305 | 307 | 3 | inferred_complete_timeline |
| `Action_None` | 309 | 329 | 21 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 152 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 209 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 226 | 238 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 241 | 246 | 6 | inferred_complete_timeline |
| `Action_None` | 247 | 271 | 25 | inferred_complete_timeline |
| `Action_None` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_None` | 278 | 303 | 26 | inferred_complete_timeline |
| `Action_None` | 306 | 309 | 4 | inferred_complete_timeline |
| `Action_None` | 313 | 329 | 17 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 208 | 82 | inferred_complete_timeline |
| `Action_None` | 227 | 329 | 103 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 204 | 78 | inferred_complete_timeline |
| `Action_None` | 213 | 264 | 52 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 206 | 80 | inferred_complete_timeline |
| `Action_None` | 230 | 291 | 62 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 193 | 67 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 208 | 82 | inferred_complete_timeline |
| `Action_None` | 228 | 238 | 11 | inferred_complete_timeline |
| `Action_None` | 240 | 250 | 11 | inferred_complete_timeline |
| `Action_None` | 260 | 266 | 7 | inferred_complete_timeline |
| `Action_None` | 271 | 302 | 32 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 206 | 80 | inferred_complete_timeline |
| `Action_None` | 228 | 266 | 39 | inferred_complete_timeline |
| `Action_None` | 271 | 274 | 4 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 329 | 203 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 204 | 78 | inferred_complete_timeline |
| `Action_None` | 229 | 266 | 38 | inferred_complete_timeline |
| `Action_None` | 271 | 274 | 4 | inferred_complete_timeline |
| `Action_None` | 277 | 279 | 3 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 243 | 117 | inferred_complete_timeline |
| `Action_None` | 247 | 317 | 71 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 329 | 203 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 279 | 153 | inferred_complete_timeline |
| `Action_None` | 291 | 294 | 4 | inferred_complete_timeline |
| `Action_None` | 300 | 306 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 140–329 | 190 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 182–202 | 21 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 205–209 | 5 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 229–279 | 49 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 233–329 | 90 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 236–302 | 58 | 5 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 321–326 | 4 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 326–327 | 2 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (C): Annotated start 130 != Inferred start 145
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `16` (QB): Annotated start 164 != Inferred start 168

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
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 117 frames exceeds threshold 90 frames [start=130, end=246].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RT) duration 117 frames exceeds threshold 90 frames [start=130, end=246].
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [127–144], lower_priority='Action_ZoneBlock' annotated_start=130, effective_Action_ZoneBlock_start=145.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 117 frames exceeds threshold 90 frames [start=130, end=246].
- ⚠️ Action 'Action_None' range [127-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-203] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-327] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-208] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-317] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-206] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-291] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-204] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-264] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-243] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-317] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-250] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-302] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-318] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-279] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [174-204] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [149-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-270] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-206] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-266] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-209] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [226-238] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-271] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-303] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-329] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '19' starts at frame 145, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [145-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-202] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-267] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-279] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-270] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-289] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-311] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-251] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-271] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-279] for track '27' has 2 frames without a visible bounding box.
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

</details>