# Play-Annotation-Generator Annotation Review — Power_303

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_303`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `0` | `0` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `28` | `23` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `0` | `Group` | 18 | START | 18 | 283 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 18 | START | 18 | 381 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 18 | START | 18 | 323 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 18 | START | 18 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 18 | START | 18 | 283 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 18 | START | 18 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 18 | START | 18 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `25` | `Group` | 18 | START | 37 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 18 | START | 18 | 330 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 18 | START | 18 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 18 | START | 18 | 419 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `0` | `0` | 284 | START | 284 | 300 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | `28` | `23` | 284 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | RG | `17` | `17` | 284 | START | 284 | 334 |

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
- **Visible Frames:** 18–419
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 323 | 306 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 419 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 18–330
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 330 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 18–419
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 381 | 364 | inferred_complete_timeline |
| `Action_PreSnap` | 387 | 419 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 18–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 419 | 402 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 18–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 419 | 402 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 18–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 419 | 402 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 18–377
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 43 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 325 | 266 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 339 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 351 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 359 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 374 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 377 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `25`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 37–419
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 50 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 309 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 348 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 419 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 18–325
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 283 | 266 | inferred_complete_timeline |
| `Action_DownBlock` | 284 | 300 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 311 | 318 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 323 | 325 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 18–411
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 283 | 266 | inferred_complete_timeline |
| `Action_PullBlock` | 284 | 334 | 51 | inferred_complete_timeline |
| `Action_None` | 335 | 411 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 18–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 419 | 402 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 18–346
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 82 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 107 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 126 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 304 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 309 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 327 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 346 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 18–312
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 40 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 49 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 56 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 312 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 18–419
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 349 | 332 | inferred_complete_timeline |
| `Action_PreSnap` | 352 | 419 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 18–419
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 291 | 274 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 419 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 18–419
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 330 | 313 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 419 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 18–401
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 396 | 379 | inferred_complete_timeline |
| `Action_PreSnap` | 398 | 401 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 18–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 419 | 402 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 18–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 24 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 380 | 355 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 387 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 391 | 419 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 18–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 419 | 402 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 22–322
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 308 | 287 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 322 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 18–419
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 394 | 377 | inferred_complete_timeline |
| `Action_PreSnap` | 407 | 419 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 23–38 | 10 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 69–74 | 4 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 120–121 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 286–419 | 124 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 323–419 | 97 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 326–419 | 94 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 332–419 | 81 | 4 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 338–339 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 347–419 | 73 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 379–419 | 41 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `0` (3 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `28` (Position_Unknown)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '23' has invalid range: start=284, end=74. Clamping end to start.
- ⚠️ Action 'Action_DownBlock' range [284-300] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [311-318] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [323-325] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-381] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-330] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-82] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-126] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-304] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-309] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-327] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-346] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-419] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-24] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-380] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-387] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-419] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-323] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-394] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-330] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-40] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-49] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-312] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-43] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-325] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-339] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-351] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-359] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-374] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-377] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-291] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-419] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-396] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-401] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-411] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-349] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-308] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-322] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-50] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-309] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-348] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-295] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-335] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-340] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-351] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-339] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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