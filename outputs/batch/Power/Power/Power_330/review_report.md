# Play-Annotation-Generator Annotation Review — Power_330

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_330`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 23 | START | 23 | 319 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 23 | START | 23 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 23 | START | 23 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 23 | START | 23 | 278 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 23 | START | 23 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 23 | START | 124 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 23 | START | 23 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 23 | START | 23 | 340 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `11` | `11` | 279 | START | 279 | 288 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `2` | `2` | 279 | START | 279 | 305 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `10` | `10` | 279 | START | 279 | 299 |

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
- **Visible Frames:** 23–449
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 340 | 318 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 449 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 23–319
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 319 | 297 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 23–449
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 112 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 130 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 307 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 334 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 431 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 433 | 436 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 438 | 449 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 23–331
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 90 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 331 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 23–415
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 99 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 278 | 176 | inferred_complete_timeline |
| `Action_PullBlock` | 279 | 299 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 301 | 332 | 32 | inferred_complete_timeline |
| `Action_None` | 333 | 415 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 23–342
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 278 | 256 | inferred_complete_timeline |
| `Action_DownBlock` | 279 | 288 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 290 | 332 | 43 | inferred_complete_timeline |
| `Action_None` | 333 | 342 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 124–340
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 124 | 299 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 328 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 340 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 23–449
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 107 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 148 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 307 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 324 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 436 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 438 | 439 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 442 | 443 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 446 | 449 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 23–328
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 328 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 23–449
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 299 | 277 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 307 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 314 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 449 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 23–338
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 338 | 316 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 23–285
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 126 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 285 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 23–338
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 79 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 332 | 246 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 338 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 23–449
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 298 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 322 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 348 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 449 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 23–120
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 120 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 23–357 | 331 | 5 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 23–335 | 301 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 23–431 | 401 | 5 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 27–449 | 401 | 6 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 29–36 | 8 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 266–363 | 78 | 6 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 269–449 | 176 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 330–337 | 8 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 343–449 | 91 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 343–449 | 107 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 348–447 | 86 | 4 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 353–380 | 28 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 355–449 | 94 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 368–374 | 7 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 398–449 | 52 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 401–418 | 18 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 421–425 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 660: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [23-319] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-307] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-334] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-431] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-436] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-449] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-132] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [279-305] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-357] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-79] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-332] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-338] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-314] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-449] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-298] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-322] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-348] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-90] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-331] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-340] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-68] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-320] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-335] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [279-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-415] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-278] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [279-288] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-342] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-107] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-307] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-324] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-436] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-439] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-443] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-449] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-285] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-328] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-335] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-343] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-431] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-338] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-30] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-198] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-209] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-288] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-449] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-328] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-340] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-313] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-327] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-330] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-338] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-352] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-363] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-384] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-443] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-449] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-337] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-381] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-430] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-449] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-381] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-388] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-439] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-447] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-380] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-390] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-374] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-418] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-425] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>