# Play-Annotation-Generator Annotation Review — SplitZone_48

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_48`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 161
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `8` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 187 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 185 | START | 185 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 188 | START | 198 | 214 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `3` | 188 | START | 188 | 322 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 188 | START | 188 | 318 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `7` | 188 | START | 188 | 265 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `9` | 188 | START | 188 | 279 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 197 | END | 185 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | `6` | `6` | 198 | START | 198 | 223 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 205 | START | 205 | 222 |
| ✅ EXACT | `Action_BallCarry` | RB | `8` | `8` | 223 | START | 223 | 320 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 327 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_SnapReceive` | 185 | 197 | 13 | inferred_complete_timeline |
| `Action_None` | 198 | 204 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 205 | 222 | 18 | inferred_complete_timeline |
| `Action_None` | 223 | 298 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 320 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 318 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–322
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 322 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–331
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_BallSnap` | 185 | 197 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 214 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 221 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 224 | 226 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 228 | 327 | 100 | inferred_complete_timeline |
| `Action_None` | 328 | 331 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 265 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 279 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 255 | 71 | inferred_complete_timeline |
| `Action_None` | 269 | 292 | 24 | inferred_complete_timeline |
| `Action_None` | 305 | 321 | 17 | inferred_complete_timeline |
| `Action_None` | 324 | 326 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 287 | 103 | inferred_complete_timeline |
| `Action_None` | 290 | 352 | 63 | inferred_complete_timeline |
| `Action_None` | 363 | 419 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 245 | 61 | inferred_complete_timeline |
| `Action_None` | 253 | 269 | 17 | inferred_complete_timeline |
| `Action_None` | 271 | 273 | 3 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 302 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 277 | 93 | inferred_complete_timeline |
| `Action_None` | 279 | 419 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 277 | 93 | inferred_complete_timeline |
| `Action_None` | 281 | 283 | 3 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |
| `Action_None` | 302 | 324 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–341
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 271 | 87 | inferred_complete_timeline |
| `Action_None` | 285 | 341 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 291 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–230 | 229 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 183–249 | 67 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 227–321 | 78 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 243–335 | 73 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 249–339 | 91 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 254–257 | 4 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 272–325 | 36 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 278–310 | 11 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 278–419 | 141 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 282–419 | 138 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 283–336 | 49 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 289–359 | 71 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 306–317 | 12 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 318–419 | 102 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 350–351 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 370–419 | 50 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 373–408 | 10 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 376–377 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 378–380 | 3 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 381–419 | 39 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 390–414 | 23 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 393–408 | 16 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 394–407 | 14 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 394–410 | 16 | 2 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 395–417 | 15 | 2 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 396–410 | 13 | 2 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 396–398 | 3 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 398–400 | 3 | 1 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 401–412 | 12 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 401–410 | 10 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 401–406 | 6 | 1 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 402–414 | 13 | 1 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 402–408 | 7 | 1 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 404–405 | 2 | 1 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 405–419 | 15 | 1 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 411–412 | 2 | 1 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 417–419 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 135 frames exceeds threshold 90 frames [start=188, end=322].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 131 frames exceeds threshold 90 frames [start=188, end=318].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 92 frames exceeds threshold 90 frames [start=188, end=279].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 140 frames exceeds threshold 90 frames [start=188, end=327].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [185–197], lower_priority='Action_ZoneBlock' annotated_start=188, effective_Action_ZoneBlock_start=198.
- ⚠️ Action 'Action_None' range [185-271] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-341] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-277] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-277] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-324] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-322] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-318] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-255] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-292] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-321] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [198-223] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [226-230] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-265] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-320] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-279] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-302] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-287] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-352] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-419] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-291] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [198-214] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [218-221] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [224-226] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-234] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-292] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-321] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-335] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-339] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-281] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-325] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-315] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-419] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-330] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-317] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-408] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-414] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-408] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-407] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-410] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-407] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-410] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-398] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-400] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-412] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-410] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-406] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-414] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-408] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.

</details>