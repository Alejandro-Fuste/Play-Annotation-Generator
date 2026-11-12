# Play-Annotation-Generator Annotation Review — SplitZone_266

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_266`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 181
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 112
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `4` | `4` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `0` | `Group` | 29 | START | 29 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 29 | START | 29 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 29 | START | 29 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 29 | START | 34 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 29 | START | 29 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 29 | START | 29 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 29 | START | 29 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 29 | START | 29 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 29 | START | 29 | 277 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `0` | `0` | 198 | START | 198 | 284 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 198 | START | 198 | 280 |
| ✅ EXACT | `Action_ZoneBlock` | C | `15` | `14` | 198 | START | 198 | 219 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 198 | START | 198 | 284 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `3` | 198 | START | 198 | 284 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 200 | END | 200 | 200 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `4` | `4` | 200 | START | 200 | 284 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `11` | `11` | 204 | START | 208 | 227 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `15` | `14` | 220 | START | 220 | 225 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `6` | 228 | START | 228 | 266 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 284 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 29–377
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 199 | 171 | inferred_complete_timeline |
| `Action_SnapReceive` | 200 | 200 | 1 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 208 | 227 | 20 | inferred_complete_timeline |
| `Action_None` | 228 | 300 | 73 | inferred_complete_timeline |
| `Action_None` | 303 | 377 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 29–279
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 227 | 199 | inferred_complete_timeline |
| `Action_BallCarry` | 228 | 266 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 278 | 279 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 29–366
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 277 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 286 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 339 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 366 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 29–301
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 199 | 171 | inferred_complete_timeline |
| `Action_SplitBlock` | 200 | 284 | 85 | inferred_complete_timeline |
| `Action_None` | 285 | 301 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 29–280
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 197 | 169 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 280 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 29–327
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 197 | 169 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 284 | 87 | inferred_complete_timeline |
| `Action_None` | 285 | 296 | 12 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_None` | 311 | 315 | 5 | inferred_complete_timeline |
| `Action_None` | 319 | 323 | 5 | inferred_complete_timeline |
| `Action_None` | 326 | 327 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 34–225
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 73 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 197 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 219 | 22 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 220 | 225 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 29–342
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 197 | 169 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 284 | 87 | inferred_complete_timeline |
| `Action_None` | 285 | 311 | 27 | inferred_complete_timeline |
| `Action_None` | 331 | 334 | 4 | inferred_complete_timeline |
| `Action_None` | 341 | 342 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 29–479
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 197 | 169 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 284 | 87 | inferred_complete_timeline |
| `Action_None` | 285 | 479 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 29–317
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 203 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 261 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 273 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 278 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 294 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 297 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 317 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 29–240
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 46 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 73 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 146 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 204 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 240 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 29–284
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 192 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 284 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 39–191
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 39 | 124 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 186 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 191 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 29–378
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 122 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 225 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 378 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 29–273
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 273 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 36–479
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 271 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 304 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 346 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 479 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 29–318
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 289 | 261 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 310 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 318 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 202–284 | 83 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 205–479 | 275 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 221–250 | 14 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 236–479 | 172 | 7 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 236–479 | 198 | 6 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 242–252 | 4 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 245–262 | 18 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 253–267 | 15 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 268–479 | 208 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 273–479 | 200 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 274–293 | 20 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 280–308 | 29 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 286–470 | 173 | 4 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 296–479 | 159 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 305–373 | 69 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 306–433 | 127 | 2 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 324–392 | 48 | 3 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 327–462 | 103 | 3 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 327–367 | 39 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 342–472 | 90 | 6 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 343–393 | 51 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 347–412 | 66 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 369–479 | 111 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 371–456 | 75 | 4 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 378–478 | 100 | 2 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 383–471 | 87 | 3 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 386–415 | 19 | 2 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 393–421 | 9 | 3 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 398–479 | 77 | 3 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 408–432 | 25 | 1 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 422–479 | 58 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_Handoff` for actor_track_id `11` (QB): Annotated start 204 != Inferred start 208
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 117 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [285-296] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-315] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [198-280] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-311] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-301] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-203] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-261] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-273] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-278] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-294] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-317] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-266] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [278-279] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-273] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-277] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-339] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-366] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-289] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-310] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-318] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-284] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-300] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-377] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-146] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-204] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-240] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-225] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-378] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [220-225] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-271] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-304] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-346] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-479] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-284] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-479] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-232] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-286] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-308] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-362] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-424] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-465] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-276] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-379] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-389] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-417] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-458] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-267] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-472] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-278] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-479] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-293] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-308] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-320] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-331] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-435] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-470] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-322] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-328] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-373] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-325] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-433] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-330] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-369] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-392] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-388] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-434] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-462] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-348] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-367] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-376] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-398] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-432] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-441] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-464] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-472] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-393] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-412] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-374] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-377] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-436] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-456] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-460] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [462-478] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-390] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-467] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [469-471] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-387] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-415] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-395] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-410] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-421] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-407] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-413] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-432] for track '46' has 1 frames without a visible bounding box.
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

</details>