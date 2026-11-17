# Play-Annotation-Generator Annotation Review — Power_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_43`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 27 | START | 27 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 27 | START | 27 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 27 | START | 27 | 270 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 27 | START | 27 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 27 | START | 27 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 27 | START | 27 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 27 | START | 27 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 27 | START | 27 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 27 | START | 27 | 322 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 27 | START | 27 | 336 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 27 | START | 27 | 213 |
| ✅ EXACT | `Action_DownBlock` | C | `18` | `18` | 214 | START | 214 | 249 |
| ✅ EXACT | `Action_PullBlock` | RG | `8` | `8` | 214 | START | 214 | 249 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 298 | 272 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 419 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 312 | 286 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 321 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 394 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 408 | 419 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 322 | 296 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 348 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 419 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 27–385
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 270 | 244 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 279 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 385 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 27–388
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 336 | 310 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 370 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 376 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 378 | 382 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 385 | 388 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 222 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 231 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 239 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 419 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 214 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 419 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 27–409
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 213 | 187 | inferred_complete_timeline |
| `Action_DownBlock` | 214 | 249 | 36 | inferred_complete_timeline |
| `Action_None` | 250 | 409 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 213 | 187 | inferred_complete_timeline |
| `Action_PullBlock` | 214 | 249 | 36 | inferred_complete_timeline |
| `Action_None` | 250 | 320 | 71 | inferred_complete_timeline |
| `Action_None` | 324 | 419 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 252 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 401 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 385 | 359 | inferred_complete_timeline |
| `Action_PreSnap` | 387 | 391 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 410 | 419 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 27–248
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 248 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 27–250
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 250 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 325 | 299 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 333 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 338 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 368 | 342 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 419 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 27–328
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 328 | 302 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 269 | 243 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 402 | 132 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 27–413
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 401 | 375 | inferred_complete_timeline |
| `Action_PreSnap` | 408 | 413 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 397 | 371 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 27–361
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 321 | 295 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 361 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 250–419 | 167 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 260–295 | 35 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 302–409 | 108 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 327–330 | 4 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 335–409 | 73 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 357–409 | 53 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 376–409 | 34 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 414–419 | 6 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 415–419 | 5 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 415–419 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 59 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [27-419] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-397] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-298] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-248] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-322] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-348] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-419] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-336] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-370] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-376] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-382] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-388] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-252] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-401] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-321] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-361] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-320] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-325] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-333] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-338] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-401] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-413] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-270] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-279] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-385] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-312] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-321] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-394] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-402] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-419] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-250] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-368] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-419] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-385] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-391] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-419] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-409] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-328] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-419] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-222] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-231] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-419] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-397] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-402] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-409] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-295] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-409] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-330] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-372] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-375] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-409] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-409] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-409] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-419] for track '30' has 1 frames without a visible bounding box.
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

</details>