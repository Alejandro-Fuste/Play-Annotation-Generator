# Play-Annotation-Generator Annotation Review — SplitZone_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_60`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 159
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 122
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `7` | `7` |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | Team_Unknown | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | HB | offense | `12` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 11 | START | 12 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `12` | `Group` | 11 | START | 79 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 11 | START | 12 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 11 | START | 12 | 177 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `11` | `11` | 175 | START | 178 | 192 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `0` | `0` | 178 | START | 178 | 300 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `4` | 178 | START | 178 | 261 |
| ✅ EXACT | `Action_SplitBlock` | HB | `12` | `12` | 181 | START | 181 | 198 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `7` | `7` | 192 | END | 190 | 192 |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | `7` | `7` | 196 | START | 198 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `3` | 203 | START | 203 | 213 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | HB | `12` | `12` | 205 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 300 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 12–415
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 126 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 202 | 74 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 213 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 230 | 261 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 274 | 333 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 341 | 415 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 79–198
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 79 | 102 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 133 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 180 | 45 | inferred_complete_timeline |
| `Action_SplitBlock` | 181 | 198 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 12–396
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 177 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 300 | 123 | inferred_complete_timeline |
| `Action_None` | 301 | 396 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–273
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 177 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 261 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 265 | 273 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 12–230
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 174 | 163 | inferred_complete_timeline |
| `Action_None` | 175 | 230 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 12–419
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 174 | 163 | inferred_complete_timeline |
| `Action_None` | 175 | 280 | 106 | inferred_complete_timeline |
| `Action_None` | 283 | 317 | 35 | inferred_complete_timeline |
| `Action_None` | 319 | 323 | 5 | inferred_complete_timeline |
| `Action_None` | 325 | 363 | 39 | inferred_complete_timeline |
| `Action_None` | 366 | 369 | 4 | inferred_complete_timeline |
| `Action_None` | 371 | 419 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–419
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 131 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 174 | 42 | inferred_complete_timeline |
| `Action_None` | 175 | 277 | 103 | inferred_complete_timeline |
| `Action_None` | 285 | 413 | 129 | inferred_complete_timeline |
| `Action_None` | 415 | 419 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–419
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 161 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 174 | 12 | inferred_complete_timeline |
| `Action_None` | 175 | 195 | 21 | inferred_complete_timeline |
| `Action_None` | 198 | 299 | 102 | inferred_complete_timeline |
| `Action_None` | 304 | 340 | 37 | inferred_complete_timeline |
| `Action_None` | 349 | 351 | 3 | inferred_complete_timeline |
| `Action_None` | 355 | 357 | 3 | inferred_complete_timeline |
| `Action_None` | 365 | 419 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 12–271
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 135 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 174 | 36 | inferred_complete_timeline |
| `Action_None` | 175 | 271 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 12–322
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 174 | 163 | inferred_complete_timeline |
| `Action_None` | 175 | 318 | 144 | inferred_complete_timeline |
| `Action_None` | 320 | 322 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–419
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 141 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 174 | 21 | inferred_complete_timeline |
| `Action_None` | 175 | 211 | 37 | inferred_complete_timeline |
| `Action_None` | 217 | 240 | 24 | inferred_complete_timeline |
| `Action_None` | 243 | 274 | 32 | inferred_complete_timeline |
| `Action_None` | 288 | 357 | 70 | inferred_complete_timeline |
| `Action_None` | 361 | 380 | 20 | inferred_complete_timeline |
| `Action_None` | 382 | 419 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 12–394 | 264 | 22 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 12–205 | 91 | 11 | Undefined position; Undefined team |
| `13` | `17` | Position_Unknown | Team_Unknown | 195–419 | 215 | 3 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 206–247 | 42 | 1 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 219–223 | 5 | 1 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 223–413 | 189 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 231–262 | 32 | 1 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 244–410 | 159 | 5 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 249–298 | 47 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 261–265 | 5 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 279–419 | 137 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 281–406 | 120 | 3 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 291–419 | 95 | 9 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 291–419 | 120 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 297–419 | 107 | 4 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 321–419 | 97 | 3 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 340–375 | 36 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 348–419 | 69 | 2 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 354–419 | 63 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 381–403 | 22 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 406–413 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `11` (Position_Unknown): Annotated start 175 != Inferred start 178
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `7` (Position_Unknown): Annotated start 196 != Inferred start 198
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (5 segments found)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `12` (HB)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 113 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (LT) duration 123 frames exceeds threshold 90 frames [start=178, end=300].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 96 frames exceeds threshold 90 frames [start=178, end=273].
- ⚠️ Segment 'Action_BlockSecondLevel' for track '12' has invalid range: start=205, end=198. Clamping end to start.
- ⚠️ Action 'Action_None' range [301-396] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-318] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-280] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-317] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-363] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-213] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [221-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [274-333] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [341-415] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [178-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [265-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-161] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-299] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-340] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-357] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-419] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-277] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-413] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-27] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-36] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-62] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-66] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-110] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-131] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-268] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-375] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-394] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-240] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-274] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-357] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-380] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-16] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-28] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-40] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-83] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [178-192] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-133] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [181-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-291] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-419] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-247] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-403] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-413] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-262] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-264] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-315] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-344] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-410] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-292] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-343] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-407] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-394] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-403] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-309] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-320] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-328] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-361] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-375] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-386] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-419] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-321] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-383] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-337] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-351] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-339] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-390] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-375] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-375] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-394] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-383] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-403] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-413] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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