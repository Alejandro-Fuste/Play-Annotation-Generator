# Play-Annotation-Generator Annotation Review — CrackToss_91

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_91`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 124
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | DT1 | defense | `13` | `12` |
| ✅ EXACT | `Action_PullBlock` | DE2 | defense | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 319 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 295 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `13` | `12` | 293 | START | 293 | 295 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `9` | `8` | 296 | START | 296 | 390 |
| ✅ EXACT | `Action_PullBlock` | DT1 | `13` | `12` | 296 | START | 296 | 368 |
| ✅ EXACT | `Action_PullBlock` | DE2 | `18` | `17` | 296 | START | 296 | 369 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 300 | END | 293 | 300 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 306 | START | 306 | 319 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 320 | START | 320 | 378 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 292 | 55 | inferred_complete_timeline |
| `Action_SnapReceive` | 293 | 300 | 8 | inferred_complete_timeline |
| `Action_None` | 301 | 305 | 5 | inferred_complete_timeline |
| `Action_Toss` | 306 | 319 | 14 | inferred_complete_timeline |
| `Action_None` | 320 | 350 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 319 | 320 | inferred_complete_timeline |
| `Action_BallCarry` | 320 | 378 | 59 | inferred_complete_timeline |
| `Action_BallCarry` | 381 | 409 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 419 | 449 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 295 | 296 | inferred_complete_timeline |
| `Action_CrackBlock` | 296 | 390 | 95 | inferred_complete_timeline |
| `Action_CrackBlock` | 392 | 449 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 110 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 116 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 292 | 293 | inferred_complete_timeline |
| `Action_None` | 293 | 322 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–369
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 295 | 202 | inferred_complete_timeline |
| `Action_PullBlock` | 296 | 369 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–368
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 292 | 293 | inferred_complete_timeline |
| `Action_BallSnap` | 293 | 295 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 296 | 368 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 292 | 293 | inferred_complete_timeline |
| `Action_None` | 293 | 335 | 43 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_None` | 353 | 449 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 292 | 133 | inferred_complete_timeline |
| `Action_None` | 293 | 325 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 292 | 127 | inferred_complete_timeline |
| `Action_None` | 293 | 449 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 292 | 293 | inferred_complete_timeline |
| `Action_None` | 293 | 400 | 108 | inferred_complete_timeline |
| `Action_None` | 404 | 408 | 5 | inferred_complete_timeline |
| `Action_None` | 410 | 449 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 2–362
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 292 | 291 | inferred_complete_timeline |
| `Action_None` | 293 | 312 | 20 | inferred_complete_timeline |
| `Action_None` | 315 | 362 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 292 | 293 | inferred_complete_timeline |
| `Action_None` | 293 | 323 | 31 | inferred_complete_timeline |
| `Action_None` | 325 | 326 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–343 | 344 | 2 | Undefined position; Undefined team |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–308 | 302 | 6 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–312 | 313 | 2 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–343 | 344 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–313 | 314 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 115–353 | 237 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 118–337 | 220 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 153–279 | 127 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 196–198 | 3 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 224–226 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 233–238 | 6 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 309–359 | 51 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 326–449 | 121 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 326–375 | 50 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 331–345 | 15 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 338–348 | 11 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 341–449 | 102 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 363–364 | 2 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 385–449 | 65 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 401–449 | 49 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 403–404 | 2 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 411–421 | 10 | 2 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 434–443 | 4 | 2 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 441–442 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 337 targets track ID '378', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 184: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 184: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 184: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-292] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-343] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-122] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-136] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-285] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-308] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-312] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [320-378] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [381-409] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-343] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [296-390] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-116] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-322] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-325] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-292] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [296-368] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-335] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-400] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-408] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-235] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-292] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-350] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-323] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-295] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [296-369] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-292] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-313] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-312] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-362] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-332] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-353] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-292] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-337] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-279] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-359] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-350] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-360] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-375] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-345] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-348] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-345] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-449] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-418] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>