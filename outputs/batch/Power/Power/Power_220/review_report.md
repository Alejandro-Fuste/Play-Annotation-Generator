# Play-Annotation-Generator Annotation Review — Power_220

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_220`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 39
- **Ball Tracks:** 2
- **Action Segments:** 79
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 0
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_DownBlock` | LT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 10 | START | 10 | 264 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 10 | START | 10 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 10 | START | 10 | 253 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 10 | START | 10 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 10 | START | 10 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 10 | START | 10 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 10 | START | 10 | 221 |
| ⚠️ START CHANGED | `Action_DownBlock` | LT | `6` | `6` | 222 | START | 223 | 270 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `9` | `9` | 222 | START | 222 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `8` | `8` | 222 | START | 222 | 242 |

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
- **Visible Frames:** 10–479
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 264 | 255 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 269 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 479 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 10–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 479 | 470 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 10–270
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 221 | 212 | inferred_complete_timeline |
| `Action_DownBlock` | 223 | 270 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 10–254
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 221 | 212 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 230 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 232 | 241 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 244 | 247 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 253 | 254 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 10–348
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 253 | 244 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 267 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 296 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 310 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 318 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 348 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 10–249
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 221 | 212 | inferred_complete_timeline |
| `Action_PullBlock` | 222 | 242 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 244 | 249 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 10–479
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 224 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 425 | 187 | inferred_complete_timeline |
| `Action_PreSnap` | 429 | 479 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 75–248
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 75 | 110 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 248 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 10–479
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 244 | 235 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 255 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 479 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 10–479
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 250 | 241 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 266 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 296 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 479 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 10–479
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 338 | 329 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 479 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–479
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 289 | 280 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 392 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 395 | 479 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 10–384
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 384 | 375 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 10–288
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 288 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 10–291
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 291 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 10–462
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 462 | 453 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 10–379 | 368 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 10–479 | 468 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 220–269 | 20 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 258–264 | 7 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 270–479 | 210 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 276–342 | 67 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 283–479 | 193 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 288–479 | 188 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 302–479 | 178 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 306–479 | 174 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 352–479 | 103 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 354–479 | 126 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 361–365 | 5 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 361–479 | 111 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 363–479 | 105 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 380–381 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 382–479 | 96 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 388–479 | 92 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 391–394 | 4 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 399–401 | 3 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 404–414 | 9 | 2 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 417–479 | 60 | 2 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 422–479 | 58 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `33` | `43` | 388 | 389 | 2 | 100.0% | None |
| `37` | `48` | 402 | 403 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `6` (LT): Annotated start 222 != Inferred start 223
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 442: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 442: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [10-338] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-291] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-384] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-462] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-288] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-221] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [223-270] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-289] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-392] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-479] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [222-242] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [244-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [222-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [232-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [244-247] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [253-254] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-264] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-479] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-266] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-296] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-479] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-379] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-316] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-224] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-425] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-253] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-267] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-296] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-310] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-318] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-348] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-244] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-255] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-479] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-248] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-223] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-264] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-342] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-341] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-296] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-479] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-394] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-479] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-365] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-389] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-451] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-479] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-443] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-413] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-394] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-401] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-410] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-414] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-424] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>