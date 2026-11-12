# Play-Annotation-Generator Annotation Review — SplitZone_250

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_250`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 599
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `0` | `Group` | 11 | START | 12 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 11 | START | 12 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 11 | START | 12 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 11 | START | 12 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 11 | START | 12 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 11 | START | 12 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 11 | START | 12 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 11 | START | 12 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 11 | START | 12 | 185 |
| ✅ EXACT | `Action_BallSnap` | RG | `9` | `9` | 186 | START | 186 | 188 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 189 | START | 189 | 263 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `12` | 189 | START | 189 | 245 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `13` | 189 | START | 189 | 305 |
| ✅ EXACT | `Action_ZoneBlock` | C | `16` | `16` | 189 | START | 189 | 305 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `9` | 189 | START | 189 | 275 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `2` | `2` | 198 | START | 198 | 305 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 203 | END | 186 | 203 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 210 | START | 210 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `14` | 220 | START | 220 | 227 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 305 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 12–308
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 185 | 174 | inferred_complete_timeline |
| `Action_SnapReceive` | 186 | 203 | 18 | inferred_complete_timeline |
| `Action_None` | 204 | 209 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 210 | 219 | 10 | inferred_complete_timeline |
| `Action_None` | 220 | 308 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 12–599
- **Visible Samples:** 583

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 219 | 208 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 227 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 230 | 500 | 271 | inferred_complete_timeline |
| `Action_BallCarry` | 502 | 518 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 521 | 599 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–317
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 197 | 186 | inferred_complete_timeline |
| `Action_SplitBlock` | 198 | 305 | 108 | inferred_complete_timeline |
| `Action_None` | 306 | 317 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 12–374
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 185 | 174 | inferred_complete_timeline |
| `Action_None` | 186 | 374 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 12–398
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 188 | 177 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 245 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 255 | 267 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 274 | 305 | 32 | inferred_complete_timeline |
| `Action_None` | 306 | 398 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 12–365
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 188 | 177 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 305 | 117 | inferred_complete_timeline |
| `Action_None` | 306 | 365 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 12–599
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 188 | 177 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 305 | 117 | inferred_complete_timeline |
| `Action_None` | 306 | 525 | 220 | inferred_complete_timeline |
| `Action_None` | 533 | 594 | 62 | inferred_complete_timeline |
| `Action_None` | 596 | 599 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 12–396
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 185 | 174 | inferred_complete_timeline |
| `Action_BallSnap` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 275 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 278 | 296 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 299 | 304 | 6 | inferred_complete_timeline |
| `Action_None` | 307 | 392 | 86 | inferred_complete_timeline |
| `Action_None` | 395 | 396 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 12–263
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 188 | 177 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 263 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–296
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 185 | 174 | inferred_complete_timeline |
| `Action_None` | 186 | 296 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–324
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 185 | 174 | inferred_complete_timeline |
| `Action_None` | 186 | 324 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 12–473
- **Visible Samples:** 460

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 185 | 174 | inferred_complete_timeline |
| `Action_None` | 186 | 414 | 229 | inferred_complete_timeline |
| `Action_None` | 416 | 460 | 45 | inferred_complete_timeline |
| `Action_None` | 462 | 473 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 12–375
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 185 | 174 | inferred_complete_timeline |
| `Action_None` | 186 | 210 | 25 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_None` | 238 | 244 | 7 | inferred_complete_timeline |
| `Action_None` | 248 | 274 | 27 | inferred_complete_timeline |
| `Action_None` | 277 | 375 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–227
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 185 | 174 | inferred_complete_timeline |
| `Action_None` | 186 | 227 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 12–315
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 185 | 174 | inferred_complete_timeline |
| `Action_None` | 186 | 285 | 100 | inferred_complete_timeline |
| `Action_None` | 290 | 315 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 185 | 174 | inferred_complete_timeline |
| `Action_None` | 186 | 260 | 75 | inferred_complete_timeline |
| `Action_None` | 263 | 599 | 337 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–599
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 185 | 174 | inferred_complete_timeline |
| `Action_None` | 186 | 599 | 414 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 182–325 | 143 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 196–599 | 395 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 198–260 | 63 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 250–252 | 3 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 258–324 | 67 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 282–283 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 295–599 | 305 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 295–599 | 305 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 296–332 | 37 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 297–599 | 287 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 297–400 | 104 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 304–357 | 29 | 5 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 325–326 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 326–369 | 44 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 367–368 | 2 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 383–384 | 2 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 390–599 | 210 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 418–538 | 82 | 6 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 426–599 | 159 | 3 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 435–436 | 2 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 445–446 | 2 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 447–599 | 146 | 2 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 490–491 | 2 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 520–521 | 2 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 583–587 | 5 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 586–587 | 2 | 1 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 591–595 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RG) duration 117 frames exceeds threshold 90 frames [start=189, end=305].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (LT) duration 117 frames exceeds threshold 90 frames [start=189, end=305].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LG) duration 117 frames exceeds threshold 90 frames [start=189, end=305].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 117 frames exceeds threshold 90 frames [start=189, end=305].
- ⚠️ Action 'Action_None' range [186-374] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-414] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-460] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-473] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-317] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-285] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-315] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-324] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-296] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-227] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-308] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-275] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [278-296] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [299-304] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-392] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-263] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-260] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [250-251] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [255-267] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-398] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-365] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-227] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-500] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [502-518] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [521-599] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-244] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-274] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-375] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-305] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-525] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-594] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-218] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-325] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-273] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-319] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-499] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-260] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-324] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-332] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-307] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-564] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-599] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-400] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-313] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-369] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-444] for track '34' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-517] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-521] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-527] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-531] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-538] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-437] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-568] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-455] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-599] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-587] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-595] for track '43' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>