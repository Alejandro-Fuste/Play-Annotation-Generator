# Play-Annotation-Generator Annotation Review — InsideZoneStretch_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneStretch_1`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_InsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 158
- **Validation Warnings:** 150
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 137
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PressGap` | RB | offense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 203 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 181 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 182 | START | 182 | 190 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 190 | END | 182 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 191 | START | 191 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `16` | 191 | START | 191 | 197 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 191 | START | 191 | 192 |
| ✅ EXACT | `Action_PressGap` | RB | `3` | `3` | 204 | START | 204 | 222 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 222 | START | 222 | 231 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `3` | 232 | START | 232 | 265 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 66 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 181 | 114 | inferred_complete_timeline |
| `Action_SnapReceive` | 182 | 190 | 9 | inferred_complete_timeline |
| `Action_None` | 191 | 221 | 31 | inferred_complete_timeline |
| `Action_Handoff` | 222 | 231 | 10 | inferred_complete_timeline |
| `Action_None` | 232 | 419 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–331
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_PressGap` | 204 | 222 | 19 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 227 | 231 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 232 | 265 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 273 | 274 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 278 | 331 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 260 | 79 | inferred_complete_timeline |
| `Action_None` | 263 | 298 | 36 | inferred_complete_timeline |
| `Action_None` | 300 | 301 | 2 | inferred_complete_timeline |
| `Action_None` | 305 | 366 | 62 | inferred_complete_timeline |
| `Action_None` | 386 | 387 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 380 | 199 | inferred_complete_timeline |
| `Action_None` | 382 | 419 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 200 | 19 | inferred_complete_timeline |
| `Action_None` | 202 | 316 | 115 | inferred_complete_timeline |
| `Action_None` | 320 | 339 | 20 | inferred_complete_timeline |
| `Action_None` | 352 | 355 | 4 | inferred_complete_timeline |
| `Action_None` | 362 | 384 | 23 | inferred_complete_timeline |
| `Action_None` | 387 | 389 | 3 | inferred_complete_timeline |
| `Action_None` | 393 | 419 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 210 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–346
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 187 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 190 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 197 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 203 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 224 | 243 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 261 | 14 | inferred_complete_timeline |
| `Action_None` | 262 | 346 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_BallSnap` | 182 | 190 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 220 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 246 | 65 | inferred_complete_timeline |
| `Action_None` | 280 | 322 | 43 | inferred_complete_timeline |
| `Action_None` | 325 | 419 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 181 | 129 | inferred_complete_timeline |
| `Action_None` | 182 | 309 | 128 | inferred_complete_timeline |
| `Action_None` | 316 | 419 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 181 | 136 | inferred_complete_timeline |
| `Action_None` | 182 | 239 | 58 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 254 | 4 | inferred_complete_timeline |
| `Action_None` | 256 | 419 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–417
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 181 | 138 | inferred_complete_timeline |
| `Action_None` | 182 | 246 | 65 | inferred_complete_timeline |
| `Action_None` | 255 | 265 | 11 | inferred_complete_timeline |
| `Action_None` | 268 | 325 | 58 | inferred_complete_timeline |
| `Action_None` | 328 | 338 | 11 | inferred_complete_timeline |
| `Action_None` | 343 | 346 | 4 | inferred_complete_timeline |
| `Action_None` | 348 | 350 | 3 | inferred_complete_timeline |
| `Action_None` | 352 | 412 | 61 | inferred_complete_timeline |
| `Action_None` | 415 | 417 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 230 | 49 | inferred_complete_timeline |
| `Action_None` | 235 | 280 | 46 | inferred_complete_timeline |
| `Action_None` | 287 | 419 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–376
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 311 | 130 | inferred_complete_timeline |
| `Action_None` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_None` | 329 | 331 | 3 | inferred_complete_timeline |
| `Action_None` | 341 | 376 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 229 | 48 | inferred_complete_timeline |
| `Action_None` | 245 | 419 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 314 | 133 | inferred_complete_timeline |
| `Action_None` | 316 | 419 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 419 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 378 | 197 | inferred_complete_timeline |
| `Action_None` | 383 | 419 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–369
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 342 | 161 | inferred_complete_timeline |
| `Action_None` | 345 | 346 | 2 | inferred_complete_timeline |
| `Action_None` | 348 | 369 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–27 | 13 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 9–243 | 229 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 21–419 | 348 | 9 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 192–337 | 39 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 217–419 | 189 | 6 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 223–381 | 143 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 253–347 | 58 | 8 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 263–419 | 151 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 288–396 | 83 | 10 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 381–382 | 2 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 392–410 | 15 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 400–405 | 6 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 411–416 | 6 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 415–419 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 121 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_None' range [182-380] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-378] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [232-265] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [273-274] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [278-331] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-342] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-369] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-229] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-419] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-260] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-298] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-366] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-280] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-314] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-419] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-27] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-311] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-376] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-246] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-322] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-220] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-246] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-265] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-325] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-338] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-346] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-350] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-412] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-417] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [182-190] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-187] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-197] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [206-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-211] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [224-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [248-261] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-346] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-309] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-419] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-200] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-316] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-339] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-384] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-389] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-419] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [191-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-26] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-126] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-142] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-147] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-384] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-287] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-334] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-272] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-285] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-390] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-243] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-375] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-381] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-259] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-293] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-307] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-325] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-341] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-347] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-387] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-307] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-339] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-347] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-355] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-393] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-395] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-410] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-405] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-416] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>