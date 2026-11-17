# Play-Annotation-Generator Annotation Review — Power_326

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_326`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 58
- **Validation Warnings:** 75
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 17 | START | 17 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 17 | START | 17 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 17 | START | 17 | 314 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 17 | START | 17 | 314 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 17 | START | 17 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 17 | START | 17 | 337 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 17 | START | 17 | 436 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `11` | `11` | 315 | START | 315 | 337 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `13` | `13` | 315 | START | 315 | 353 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `12` | `12` | 315 | START | 315 | 409 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 17–436
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 436 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 17–415
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 337 | 321 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 415 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 17–442
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_PullBlock` | 315 | 409 | 95 | inferred_complete_timeline |
| `Action_PullBlock` | 419 | 422 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 425 | 442 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 17–449
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 162 | 146 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 314 | 146 | inferred_complete_timeline |
| `Action_DownBlock` | 315 | 337 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 340 | 449 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 17–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 449 | 433 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 17–449
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_DownBlock` | 315 | 353 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 358 | 449 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 17–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 449 | 433 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 17–385
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 324 | 308 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 330 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 368 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 385 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 17–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 449 | 433 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 17–317
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 308 | 292 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 317 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 17–358
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 305 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 358 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 17–355
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 355 | 339 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 17–392
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 392 | 376 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 17–414
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 414 | 398 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 17–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 449 | 433 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 17–109
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 109 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 17–434 | 417 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 17–20 | 4 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 332–369 | 18 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 341–449 | 99 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 344–430 | 45 | 5 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 360–449 | 45 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 400–449 | 49 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 408–449 | 42 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 410–447 | 38 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 418–449 | 31 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 420–449 | 30 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 424–449 | 26 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 426–449 | 24 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 438–449 | 12 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 442–449 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (3 segments found)

### Track Identity Issues

- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (LG) duration 135 frames exceeds threshold 90 frames [start=315, end=449].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '12' (LT) duration 128 frames exceeds threshold 90 frames [start=315, end=442].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (RG) duration 135 frames exceeds threshold 90 frames [start=315, end=449].
- ⚠️ Action 'Action_PreSnap' range [17-109] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-424] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-434] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-337] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-415] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-392] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-324] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-330] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-368] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-385] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-414] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-436] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-449] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-305] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-358] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [315-337] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [315-409] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [419-422] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [425-442] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [315-353] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [358-449] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-355] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-308] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-311] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-369] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-373] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-383] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-352] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-356] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-367] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-400] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-430] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-381] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-407] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-404] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-447] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-419] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>