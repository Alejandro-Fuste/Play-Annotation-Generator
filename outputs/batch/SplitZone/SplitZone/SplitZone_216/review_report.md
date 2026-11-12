# Play-Annotation-Generator Annotation Review — SplitZone_216

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_216`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 116
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE1 | defense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `4` | `4` |
| ✅ EXACT | `Action_BallCarry` | LB2 | defense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DE1 | defense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 23 | START | 24 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 23 | START | 24 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 23 | START | 24 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 23 | START | 24 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 23 | START | 85 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 23 | START | 24 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 23 | START | 24 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 23 | START | 24 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 23 | START | 24 | 172 |
| ✅ EXACT | `Action_BallSnap` | DE1 | `3` | `3` | 173 | START | 173 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `0` | `0` | 176 | START | 176 | 240 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `1` | `1` | 176 | START | 176 | 274 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `14` | 176 | START | 176 | 209 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `5` | `5` | 176 | START | 176 | 226 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 176 | START | 176 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | `13` | `13` | 178 | START | 178 | 187 |
| ✅ EXACT | `Action_SnapReceive` | RB | `4` | `4` | 187 | END | 173 | 187 |
| ✅ EXACT | `Action_Handoff` | RB | `4` | `4` | 191 | START | 191 | 202 |
| ✅ EXACT | `Action_BallCarry` | LB2 | `8` | `8` | 203 | START | 203 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DE1 | `3` | `3` | 209 | START | 209 | 219 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 274 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 24–379
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 172 | 149 | inferred_complete_timeline |
| `Action_None` | 173 | 221 | 49 | inferred_complete_timeline |
| `Action_None` | 223 | 256 | 34 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 379 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 24–209
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 172 | 149 | inferred_complete_timeline |
| `Action_SnapReceive` | 173 | 187 | 15 | inferred_complete_timeline |
| `Action_None` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 191 | 202 | 12 | inferred_complete_timeline |
| `Action_None` | 203 | 209 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 85–419
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 85 | 172 | 88 | inferred_complete_timeline |
| `Action_None` | 173 | 399 | 227 | inferred_complete_timeline |
| `Action_None` | 410 | 419 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 24–367
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 113 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 123 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 172 | 48 | inferred_complete_timeline |
| `Action_None` | 173 | 367 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 24–360
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 175 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 240 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 274 | 27 | inferred_complete_timeline |
| `Action_None` | 276 | 360 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 24–419
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 175 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 237 | 62 | inferred_complete_timeline |
| `Action_None` | 287 | 419 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 24–419
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 175 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 226 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 230 | 274 | 45 | inferred_complete_timeline |
| `Action_None` | 275 | 275 | 1 | inferred_complete_timeline |
| `Action_None` | 280 | 326 | 47 | inferred_complete_timeline |
| `Action_None` | 328 | 419 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 24–367
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 175 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 274 | 99 | inferred_complete_timeline |
| `Action_None` | 275 | 301 | 27 | inferred_complete_timeline |
| `Action_None` | 304 | 308 | 5 | inferred_complete_timeline |
| `Action_None` | 310 | 351 | 42 | inferred_complete_timeline |
| `Action_None` | 356 | 367 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 24–400
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 175 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 209 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 262 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_None` | 307 | 318 | 12 | inferred_complete_timeline |
| `Action_None` | 321 | 383 | 63 | inferred_complete_timeline |
| `Action_None` | 389 | 390 | 2 | inferred_complete_timeline |
| `Action_None` | 392 | 400 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 24–419
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 172 | 149 | inferred_complete_timeline |
| `Action_BallSnap` | 173 | 187 | 15 | inferred_complete_timeline |
| `Action_None` | 188 | 208 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 209 | 219 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 224 | 274 | 51 | inferred_complete_timeline |
| `Action_None` | 275 | 285 | 11 | inferred_complete_timeline |
| `Action_None` | 288 | 301 | 14 | inferred_complete_timeline |
| `Action_None` | 305 | 419 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 24–300
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 172 | 149 | inferred_complete_timeline |
| `Action_None` | 173 | 237 | 65 | inferred_complete_timeline |
| `Action_None` | 252 | 284 | 33 | inferred_complete_timeline |
| `Action_None` | 287 | 300 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 24–419
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 172 | 149 | inferred_complete_timeline |
| `Action_None` | 173 | 298 | 126 | inferred_complete_timeline |
| `Action_None` | 304 | 321 | 18 | inferred_complete_timeline |
| `Action_None` | 338 | 370 | 33 | inferred_complete_timeline |
| `Action_None` | 373 | 376 | 4 | inferred_complete_timeline |
| `Action_None` | 381 | 419 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 24–356
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 172 | 149 | inferred_complete_timeline |
| `Action_None` | 173 | 356 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 24–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 202 | 179 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 239 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 24–269
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 172 | 149 | inferred_complete_timeline |
| `Action_None` | 173 | 185 | 13 | inferred_complete_timeline |
| `Action_None` | 200 | 203 | 4 | inferred_complete_timeline |
| `Action_None` | 223 | 252 | 30 | inferred_complete_timeline |
| `Action_None` | 256 | 269 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 48–168
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 48 | 64 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 76 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 133 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 24–279 | 256 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 24–261 | 196 | 8 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 114–419 | 303 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 214–419 | 206 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 246–284 | 36 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 248–298 | 51 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 249–419 | 170 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 251–419 | 169 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 289–419 | 125 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 294–302 | 9 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 294–419 | 126 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 308–419 | 110 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 309–419 | 104 | 4 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 317–419 | 100 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 322–419 | 98 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 411–419 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | 93 | 174 | 71 | 86.6% | 96–98, 100–105, 107, 110 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (LT) duration 99 frames exceeds threshold 90 frames [start=176, end=274].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 99 frames exceeds threshold 90 frames [start=176, end=274].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (C) duration 99 frames exceeds threshold 90 frames [start=176, end=274].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LG) duration 99 frames exceeds threshold 90 frames [start=176, end=274].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RT) duration 99 frames exceeds threshold 90 frames [start=176, end=274].
- ⚠️ Action 'Action_ZoneBlock' range [176-240] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [248-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-360] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-301] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-308] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-351] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-367] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-237] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-284] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-300] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [209-219] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-285] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-301] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [176-226] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '5' starts at frame 275, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [275-275] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-326] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-279] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [176-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-419] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-239] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-256] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-379] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-252] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-269] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-356] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-298] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-321] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-370] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-419] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-60] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [178-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [189-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [210-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [253-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [260-261] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [176-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-262] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [269-270] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [272-274] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-318] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-383] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-400] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-367] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-64] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-399] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-419] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-283] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-290] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-419] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-272] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-284] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-298] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-276] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-419] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-407] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-302] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-402] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-316] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-407] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>