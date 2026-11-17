# Play-Annotation-Generator Annotation Review — Power_297

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_297`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 25 | START | 25 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 25 | START | 25 | 455 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 25 | START | 25 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 25 | START | 25 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 25 | START | 25 | 240 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 25 | START | 25 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 25 | START | 25 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 25 | START | 28 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 25 | START | 25 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 25 | START | 25 | 479 |
| ✅ EXACT | `Action_DownBlock` | C | `19` | `19` | 216 | START | 216 | 297 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `20` | `20` | 216 | START | 216 | 236 |
| ✅ EXACT | `Action_DownBlock` | RT | `21` | `21` | 216 | START | 216 | 265 |
| ✅ EXACT | `Action_PullBlock` | LG | `3` | `3` | 216 | START | 216 | 297 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 25–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 479 | 455 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 25–473
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 240 | 216 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 371 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 469 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 472 | 473 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 25–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 479 | 455 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 25–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 479 | 455 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 25–479
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 455 | 431 | inferred_complete_timeline |
| `Action_PreSnap` | 458 | 459 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 462 | 479 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 25–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 479 | 455 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 25–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 215 | 191 | inferred_complete_timeline |
| `Action_PullBlock` | 216 | 297 | 82 | inferred_complete_timeline |
| `Action_None` | 298 | 479 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 25–479
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 215 | 191 | inferred_complete_timeline |
| `Action_DownBlock` | 216 | 297 | 82 | inferred_complete_timeline |
| `Action_None` | 298 | 358 | 61 | inferred_complete_timeline |
| `Action_None` | 360 | 479 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 25–244
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 215 | 191 | inferred_complete_timeline |
| `Action_DownBlock` | 216 | 236 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 242 | 244 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 28–265
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 215 | 188 | inferred_complete_timeline |
| `Action_DownBlock` | 216 | 265 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 25–473
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 389 | 365 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 473 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 25–479
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 282 | 258 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 479 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 25–367
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 263 | 239 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 363 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 365 | 367 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 25–479
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 258 | 234 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 317 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 479 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 25–479
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 279 | 255 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 297 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 321 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 329 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 479 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 25–479
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 322 | 298 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 357 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 479 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 25–479
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 377 | 353 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 380 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 479 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 25–479
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 427 | 403 | inferred_complete_timeline |
| `Action_PreSnap` | 431 | 479 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 25–479
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 240 | 216 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 479 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 25–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 479 | 455 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 25–293
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 293 | 269 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 25–479 | 449 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 253–254 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 257–479 | 223 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 278–479 | 201 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 353–479 | 125 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 375–390 | 15 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 375–479 | 105 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 458–461 | 4 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 466–478 | 8 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 470–479 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 594: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [25-455] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-459] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-427] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-479] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-479] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-240] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-479] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-293] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-282] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-377] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-399] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-479] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-263] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-363] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-367] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-389] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-473] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-479] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-317] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-279] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-321] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-322] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-357] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-240] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-371] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-469] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-473] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-358] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [216-236] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [242-244] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [216-265] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-254] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-479] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-393] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-357] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-386] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-390] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-461] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-469] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [475-478] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>