# Play-Annotation-Generator Annotation Review — SplitZone_82

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_82`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 479
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_SplitBlock` | WR | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 29 | START | 30 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 29 | START | 30 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 29 | START | 30 | 267 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 29 | START | 30 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 29 | START | 30 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 29 | START | 30 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 29 | START | 30 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `7` | `Group` | 29 | START | 30 | 241 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 237 | START | 237 | 252 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `11` | 240 | START | 240 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 240 | START | 240 | 265 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `15` | 240 | START | 253 | 268 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `4` | 240 | START | 240 | 330 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `6` | 240 | START | 240 | 265 |
| ✅ EXACT | `Action_SplitBlock` | WR | `7` | `7` | 242 | START | 242 | 262 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 252 | END | 237 | 252 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 256 | START | 256 | 267 |
| ✅ EXACT | `Action_BallCarry` | RB | `12` | `12` | 268 | START | 268 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `11` | `11` | 300 | START | 300 | 328 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 363 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 30–277
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 236 | 207 | inferred_complete_timeline |
| `Action_SnapReceive` | 237 | 252 | 16 | inferred_complete_timeline |
| `Action_None` | 253 | 255 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 256 | 267 | 12 | inferred_complete_timeline |
| `Action_None` | 268 | 277 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 30–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 267 | 238 | inferred_complete_timeline |
| `Action_BallCarry` | 268 | 299 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 30–262
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 241 | 212 | inferred_complete_timeline |
| `Action_SplitBlock` | 242 | 262 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 30–479
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 239 | 210 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 330 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 332 | 363 | 32 | inferred_complete_timeline |
| `Action_None` | 364 | 479 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 30–355
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 239 | 210 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 299 | 60 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 300 | 328 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 347 | 349 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 353 | 355 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 30–268
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 51 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 236 | 174 | inferred_complete_timeline |
| `Action_BallSnap` | 237 | 252 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 253 | 268 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 30–349
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 239 | 210 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 265 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 270 | 284 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 338 | 349 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 30–415
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 239 | 210 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 265 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 305 | 313 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 319 | 333 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 335 | 363 | 29 | inferred_complete_timeline |
| `Action_None` | 364 | 415 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 30–479
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 236 | 207 | inferred_complete_timeline |
| `Action_None` | 237 | 479 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 30–479
- **Visible Samples:** 431

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 236 | 207 | inferred_complete_timeline |
| `Action_None` | 237 | 342 | 106 | inferred_complete_timeline |
| `Action_None` | 362 | 479 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 30–271
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 236 | 207 | inferred_complete_timeline |
| `Action_None` | 237 | 271 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 30–380
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 236 | 207 | inferred_complete_timeline |
| `Action_None` | 237 | 241 | 5 | inferred_complete_timeline |
| `Action_None` | 243 | 380 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 30–479
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 236 | 207 | inferred_complete_timeline |
| `Action_None` | 237 | 244 | 8 | inferred_complete_timeline |
| `Action_None` | 248 | 317 | 70 | inferred_complete_timeline |
| `Action_None` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_None` | 326 | 327 | 2 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_None` | 333 | 344 | 12 | inferred_complete_timeline |
| `Action_None` | 352 | 368 | 17 | inferred_complete_timeline |
| `Action_None` | 370 | 479 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 30–367
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 235 | 206 | inferred_complete_timeline |
| `Action_None` | 237 | 330 | 94 | inferred_complete_timeline |
| `Action_None` | 356 | 367 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 30–355
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 213 | 184 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 236 | 21 | inferred_complete_timeline |
| `Action_None` | 237 | 312 | 76 | inferred_complete_timeline |
| `Action_None` | 346 | 355 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 30–479
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 236 | 207 | inferred_complete_timeline |
| `Action_None` | 237 | 353 | 117 | inferred_complete_timeline |
| `Action_None` | 355 | 479 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 188–262 | 75 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 200–277 | 76 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 278–479 | 200 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 280–479 | 188 | 4 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 280–292 | 13 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 282–355 | 74 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 286–479 | 193 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 289–443 | 155 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 296–376 | 81 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 301–350 | 50 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 328–337 | 6 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 342–371 | 30 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 364–369 | 6 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 426–479 | 54 | 1 | Undefined position; Undefined team |
| `30` | `52` | Position_Unknown | Team_Unknown | 450–452 | 3 | 1 | Undefined position; Undefined team |
| `31` | `61` | Position_Unknown | Team_Unknown | 458–479 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 240 != Inferred start 253
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 124 frames exceeds threshold 90 frames [start=240, end=363].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 124 frames exceeds threshold 90 frames [start=240, end=363].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 110 frames exceeds threshold 90 frames [start=240, end=349].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [237–252], lower_priority='Action_ZoneBlock' annotated_start=240, effective_Action_ZoneBlock_start=253.
- ⚠️ Action 'Action_PreSnap' range [30-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-312] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-355] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-353] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-317] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-344] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-368] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-330] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-367] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [240-330] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-479] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-342] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [240-265] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [305-313] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [319-333] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-415] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [242-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-380] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-277] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [300-328] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [347-349] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [353-355] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-267] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [268-299] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-271] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [240-265] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [270-284] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [338-349] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [253-268] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-236] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-262] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-277] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-350] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-332] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-350] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-359] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-292] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-355] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-342] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-479] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-443] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-376] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-350] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-371] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-369] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-452] for track '30' has 1 frames without a visible bounding box.
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