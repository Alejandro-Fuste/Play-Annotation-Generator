# Play-Annotation-Generator Annotation Review — Counter_356

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_356`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 89
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
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `17` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 273 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 238 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 236 | START | 236 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `1` | `0` | 239 | START | 239 | 320 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `17` | `14` | 239 | START | 262 | 265 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `2` | `1` | 239 | START | 239 | 270 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `11` | `10` | 239 | START | 239 | 261 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `8` | `7` | 239 | START | 239 | 295 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 246 | END | 236 | 246 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 263 | START | 263 | 278 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 279 | START | 280 | 285 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 320 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_SnapReceive` | 236 | 246 | 11 | inferred_complete_timeline |
| `Action_None` | 247 | 262 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 263 | 278 | 16 | inferred_complete_timeline |
| `Action_None` | 279 | 419 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_BallCarry` | 280 | 285 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 287 | 290 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 293 | 315 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 319 | 419 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–408
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 239 | 295 | 57 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 312 | 320 | 9 | inferred_complete_timeline |
| `Action_None` | 321 | 349 | 29 | inferred_complete_timeline |
| `Action_None` | 354 | 371 | 18 | inferred_complete_timeline |
| `Action_None` | 407 | 408 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 38 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 49 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 94 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 176 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 232 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 239 | 261 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 269 | 271 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_BallSnap` | 236 | 246 | 11 | inferred_complete_timeline |
| `Action_None` | 247 | 253 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_DownBlock` | 239 | 320 | 82 | inferred_complete_timeline |
| `Action_None` | 321 | 335 | 15 | inferred_complete_timeline |
| `Action_None` | 368 | 419 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–417
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_DownBlock` | 239 | 270 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 318 | 320 | 3 | inferred_complete_timeline |
| `Action_None` | 321 | 331 | 11 | inferred_complete_timeline |
| `Action_None` | 343 | 396 | 54 | inferred_complete_timeline |
| `Action_None` | 403 | 408 | 6 | inferred_complete_timeline |
| `Action_None` | 414 | 417 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_None` | 236 | 281 | 46 | inferred_complete_timeline |
| `Action_None` | 283 | 300 | 18 | inferred_complete_timeline |
| `Action_None` | 302 | 325 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_None` | 236 | 247 | 12 | inferred_complete_timeline |
| `Action_None` | 277 | 292 | 16 | inferred_complete_timeline |
| `Action_None` | 296 | 322 | 27 | inferred_complete_timeline |
| `Action_None` | 329 | 419 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_None` | 236 | 257 | 22 | inferred_complete_timeline |
| `Action_None` | 261 | 419 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_None` | 236 | 316 | 81 | inferred_complete_timeline |
| `Action_None` | 327 | 419 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–335
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_None` | 236 | 335 | 100 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 2–419 | 416 | 3 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 248–419 | 172 | 1 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 262–419 | 148 | 4 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 264–320 | 56 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 271–419 | 139 | 6 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 298–335 | 30 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 308–315 | 8 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 324–419 | 96 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 327–397 | 66 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 334–419 | 86 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 341–419 | 79 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 348–358 | 11 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 388–419 | 32 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 394–419 | 26 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 395–419 | 25 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 407–419 | 13 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 409–419 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 54 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_DownBlock' range [239-320] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-335] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [239-270] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-331] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-396] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-408] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-417] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-335] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-273] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [280-285] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [287-290] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [293-315] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-257] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-281] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-300] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-325] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [239-295] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-349] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-371] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-316] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-247] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-292] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-322] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-419] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-38] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-49] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-176] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-188] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-232] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [239-261] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [269-271] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-242] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [262-265] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [270-277] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-316] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-296] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-304] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-310] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-317] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-335] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-315] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-355] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-360] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-397] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-419] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-358] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>