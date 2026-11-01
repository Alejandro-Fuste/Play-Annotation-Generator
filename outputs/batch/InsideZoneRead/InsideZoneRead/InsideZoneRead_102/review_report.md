# Play-Annotation-Generator Annotation Review — InsideZoneRead_102

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_102`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 204 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 202 | START | 202 | 213 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `9` | 205 | START | 205 | 228 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `10` | 205 | START | 205 | 283 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `11` | 205 | START | 205 | 271 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 205 | START | 214 | 283 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `3` | 205 | START | 205 | 226 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 213 | END | 202 | 213 |
| ✅ EXACT | `Action_ReadDefender` | QB | `13` | `12` | 216 | START | 216 | 243 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `13` | `12` | 254 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 283 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_SnapReceive` | 202 | 213 | 12 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 216 | 243 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_None` | 202 | 242 | 41 | inferred_complete_timeline |
| `Action_None` | 245 | 276 | 32 | inferred_complete_timeline |
| `Action_None` | 279 | 389 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–342
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 226 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 230 | 283 | 54 | inferred_complete_timeline |
| `Action_None` | 284 | 342 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 271 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_BallSnap` | 202 | 213 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 214 | 283 | 70 | inferred_complete_timeline |
| `Action_None` | 284 | 309 | 26 | inferred_complete_timeline |
| `Action_None` | 314 | 388 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 228 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 237 | 283 | 47 | inferred_complete_timeline |
| `Action_None` | 284 | 389 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 283 | 79 | inferred_complete_timeline |
| `Action_None` | 284 | 306 | 23 | inferred_complete_timeline |
| `Action_None` | 308 | 363 | 56 | inferred_complete_timeline |
| `Action_None` | 365 | 387 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_None` | 202 | 250 | 49 | inferred_complete_timeline |
| `Action_None` | 267 | 314 | 48 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_None` | 202 | 242 | 41 | inferred_complete_timeline |
| `Action_None` | 250 | 260 | 11 | inferred_complete_timeline |
| `Action_None` | 263 | 298 | 36 | inferred_complete_timeline |
| `Action_None` | 306 | 389 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_None` | 202 | 222 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_None` | 202 | 255 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_None` | 202 | 268 | 67 | inferred_complete_timeline |
| `Action_None` | 271 | 323 | 53 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_None` | 331 | 333 | 3 | inferred_complete_timeline |
| `Action_None` | 335 | 389 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_None` | 202 | 328 | 127 | inferred_complete_timeline |
| `Action_None` | 333 | 389 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–222 | 223 | 2 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–33 | 34 | 1 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–5 | 6 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 251–365 | 52 | 7 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 254–338 | 51 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 262–314 | 46 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 262–283 | 15 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 265–389 | 124 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 285–344 | 39 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 286–389 | 103 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 289–357 | 62 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 302–389 | 88 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 307–389 | 74 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 308–389 | 79 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 319–369 | 51 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 321–389 | 69 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 327–389 | 63 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 339–389 | 25 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 355–389 | 34 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 377–382 | 6 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 377–389 | 13 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 378–379 | 2 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 384–389 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 205 != Inferred start 214
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `13` (QB)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '12' has invalid range: start=254, end=243. Clamping end to start.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [202–213], lower_priority='Action_ZoneBlock' annotated_start=205, effective_Action_ZoneBlock_start=214.
- ⚠️ Action 'Action_None' range [202-268] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-323] for track '0' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-328] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-389] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-250] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-314] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [205-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-342] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-222] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-260] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-298] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-389] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [205-228] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [237-283] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-306] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-363] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-387] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [205-271] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [216-243] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-309] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-388] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-255] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-242] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-276] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-270] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-290] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-302] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-310] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-280] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-309] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-283] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-346] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-317] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-344] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-389] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-295] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-357] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-389] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-330] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-351] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-317] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-347] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-369] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-389] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-382] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-389] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-389] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>