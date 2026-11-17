# Play-Annotation-Generator Annotation Review — Power_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_5`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 16 | START | 16 | 336 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `10` | `Group` | 16 | START | 16 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 16 | START | 16 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 16 | START | 16 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 16 | START | 16 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 16 | START | 16 | 296 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 16 | START | 16 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 16 | START | 16 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 16 | START | 16 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 16 | START | 16 | 335 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 16 | START | 16 | 278 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `19` | `19` | 220 | START | 220 | 227 |
| ✅ EXACT | `Action_PullBlock` | RG | `20` | `20` | 220 | START | 220 | 283 |

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
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 16–236
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 236 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 278 | 263 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 305 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 389 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 335 | 320 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 356 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 369 | 376 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 389 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 16–365
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 336 | 321 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 348 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 354 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 365 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 244 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 261 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 341 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 389 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 16–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 219 | 204 | inferred_complete_timeline |
| `Action_DownBlock` | 220 | 227 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 16–277
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 225 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 277 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 219 | 204 | inferred_complete_timeline |
| `Action_PullBlock` | 220 | 283 | 64 | inferred_complete_timeline |
| `Action_None` | 296 | 389 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 16–376
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 296 | 281 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 370 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 372 | 376 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 304 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 389 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 350 | 335 | inferred_complete_timeline |
| `Action_PreSnap` | 352 | 353 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 389 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 16–310
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 241 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 248 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 272 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 279 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 300 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 310 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 272 | 257 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 296 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 301 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 389 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 288 | 273 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 345 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 348 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 389 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 229 | 214 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 389 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 16–383
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 367 | 352 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 383 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 381 | 366 | inferred_complete_timeline |
| `Action_PreSnap` | 385 | 389 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 325 | 310 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 331 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 340 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 344 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 368 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 372 | 389 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 245–380 | 124 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 271–389 | 68 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 291–389 | 99 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 295–298 | 4 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 317–389 | 72 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 369–389 | 21 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 386–389 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 67 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [16-336] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-348] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-354] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-365] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-325] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-331] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-340] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-344] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-368] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-389] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-381] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-304] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-350] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-353] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-389] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-367] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-383] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-335] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-356] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-376] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-278] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-305] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-229] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-272] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-296] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-301] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-389] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-288] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-345] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-348] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-389] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-244] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-261] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-341] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-241] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-248] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-272] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-279] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-300] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-310] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-296] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-370] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-376] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [220-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [232-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [238-269] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [220-283] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-225] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-277] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-350] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-368] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-377] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-334] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-389] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-319] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-389] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-389] for track '28' has 1 frames without a visible bounding box.
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