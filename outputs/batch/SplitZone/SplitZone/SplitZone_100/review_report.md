# Play-Annotation-Generator Annotation Review — SplitZone_100

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_100`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 122
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 106
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `0` | `Group` | 33 | START | 34 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 33 | START | 34 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 33 | START | 34 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 33 | START | 34 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 33 | START | 34 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 33 | START | 34 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 33 | START | 34 | 179 |
| ✅ EXACT | `Action_BallSnap` | C | `6` | `6` | 151 | START | 151 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `0` | `0` | 154 | START | 154 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 154 | START | 154 | 168 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `6` | `6` | 154 | START | 161 | 186 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `7` | 154 | START | 154 | 220 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `3` | 160 | END | 151 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `10` | `10` | 160 | START | 160 | 170 |
| ✅ EXACT | `Action_Handoff` | QB | `3` | `3` | 169 | START | 169 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `8` | 180 | START | 180 | 198 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 272 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 34–419
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 150 | 117 | inferred_complete_timeline |
| `Action_SnapReceive` | 151 | 160 | 10 | inferred_complete_timeline |
| `Action_None` | 161 | 168 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 169 | 179 | 11 | inferred_complete_timeline |
| `Action_None` | 180 | 235 | 56 | inferred_complete_timeline |
| `Action_None` | 237 | 264 | 28 | inferred_complete_timeline |
| `Action_None` | 276 | 419 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 34–250
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 179 | 146 | inferred_complete_timeline |
| `Action_BallCarry` | 180 | 198 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 205 | 250 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 34–244
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 159 | 126 | inferred_complete_timeline |
| `Action_SplitBlock` | 160 | 170 | 11 | inferred_complete_timeline |
| `Action_SplitBlock` | 174 | 244 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 34–344
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 153 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 220 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 231 | 241 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 272 | 27 | inferred_complete_timeline |
| `Action_None` | 273 | 291 | 19 | inferred_complete_timeline |
| `Action_None` | 295 | 344 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 34–419
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 150 | 117 | inferred_complete_timeline |
| `Action_BallSnap` | 151 | 160 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 186 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 212 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 257 | 39 | inferred_complete_timeline |
| `Action_None` | 341 | 396 | 56 | inferred_complete_timeline |
| `Action_None` | 411 | 419 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 34–419
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 153 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 181 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 263 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 267 | 272 | 6 | inferred_complete_timeline |
| `Action_None` | 273 | 419 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 34–373
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 153 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 168 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 191 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 197 | 272 | 76 | inferred_complete_timeline |
| `Action_None` | 273 | 373 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 34–225
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 150 | 117 | inferred_complete_timeline |
| `Action_None` | 151 | 225 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 46–368
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 63 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 150 | 80 | inferred_complete_timeline |
| `Action_None` | 151 | 159 | 9 | inferred_complete_timeline |
| `Action_None` | 169 | 232 | 64 | inferred_complete_timeline |
| `Action_None` | 235 | 237 | 3 | inferred_complete_timeline |
| `Action_None` | 239 | 331 | 93 | inferred_complete_timeline |
| `Action_None` | 333 | 368 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 34–84
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 84 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 39–334
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 39 | 150 | 112 | inferred_complete_timeline |
| `Action_None` | 151 | 159 | 9 | inferred_complete_timeline |
| `Action_None` | 181 | 189 | 9 | inferred_complete_timeline |
| `Action_None` | 192 | 215 | 24 | inferred_complete_timeline |
| `Action_None` | 218 | 256 | 39 | inferred_complete_timeline |
| `Action_None` | 262 | 316 | 55 | inferred_complete_timeline |
| `Action_None` | 318 | 330 | 13 | inferred_complete_timeline |
| `Action_None` | 333 | 334 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 34–189
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 150 | 117 | inferred_complete_timeline |
| `Action_None` | 151 | 189 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 34–171
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 71 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 150 | 77 | inferred_complete_timeline |
| `Action_None` | 151 | 171 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 34–178
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 51 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 150 | 97 | inferred_complete_timeline |
| `Action_None` | 151 | 178 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 63–400
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 63 | 65 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 73 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 150 | 71 | inferred_complete_timeline |
| `Action_None` | 151 | 170 | 20 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 301 | 95 | inferred_complete_timeline |
| `Action_None` | 304 | 321 | 18 | inferred_complete_timeline |
| `Action_None` | 324 | 335 | 12 | inferred_complete_timeline |
| `Action_None` | 341 | 379 | 39 | inferred_complete_timeline |
| `Action_None` | 382 | 400 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `18` | Position_Unknown | Team_Unknown | 103–357 | 226 | 8 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 187–192 | 6 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 206–419 | 209 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 210–419 | 174 | 4 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 220–240 | 21 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 220–317 | 93 | 2 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 236–324 | 71 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 237–269 | 33 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 248–419 | 172 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 265–419 | 147 | 2 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 268–316 | 43 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 276–369 | 90 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 290–330 | 41 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 304–306 | 3 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 310–311 | 2 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 321–322 | 2 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 321–390 | 6 | 3 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 335–336 | 2 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 335–337 | 3 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 357–419 | 60 | 2 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 358–411 | 28 | 2 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 373–374 | 2 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 383–419 | 33 | 3 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 396–419 | 24 | 1 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 397–398 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 95 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (RG) duration 119 frames exceeds threshold 90 frames [start=154, end=272].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 119 frames exceeds threshold 90 frames [start=154, end=272].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (C) duration 119 frames exceeds threshold 90 frames [start=154, end=272].
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [151–160], lower_priority='Action_ZoneBlock' annotated_start=154, effective_Action_ZoneBlock_start=161.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 119 frames exceeds threshold 90 frames [start=154, end=272].
- ⚠️ Action 'Action_ZoneBlock' range [154-181] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-263] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-419] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-225] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [170-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-373] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-235] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-264] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-189] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-51] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [161-186] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-212] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [219-257] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-396] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [223-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [231-241] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-291] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-344] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [180-198] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [205-250] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [160-170] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [174-244] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-71] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-215] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-256] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-316] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-330] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-232] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-331] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-368] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-301] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-321] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-335] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-379] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-400] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-138] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-209] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-345] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-357] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-255] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-266] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-377] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-419] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-285] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-317] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-324] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-419] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-301] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-419] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-287] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-316] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-294] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-369] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-330] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-413] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-376] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-411] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-397] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-403] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '39' has 1 frames without a visible bounding box.
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

</details>