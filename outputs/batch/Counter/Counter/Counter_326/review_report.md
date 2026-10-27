# Play-Annotation-Generator Annotation Review — Counter_326

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_326`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | offense | `1` | `0` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 48 | START | 48 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | `1` | `0` | 51 | START | 51 | 127 |
| ✅ EXACT | `Action_DownBlock` | RG | `10` | `9` | 51 | START | 51 | 169 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `7` | `6` | 51 | START | 64 | 169 |
| ✅ EXACT | `Action_PullBlock` | LG | `2` | `1` | 51 | START | 51 | 169 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `3` | `2` | 51 | START | 51 | 169 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `14` | `13` | 63 | END | 48 | 63 |
| ✅ EXACT | `Action_BallCarry` | QB | `4` | `3` | 96 | START | 96 | 419 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 169 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_BallCarry` | 96 | 419 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 96 | 49 | inferred_complete_timeline |
| `Action_None` | 98 | 419 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_DownBlock` | 51 | 127 | 77 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 137 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 140 | 169 | 30 | inferred_complete_timeline |
| `Action_None` | 170 | 419 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 51 | 169 | 119 | inferred_complete_timeline |
| `Action_None` | 170 | 419 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PullBlock` | 51 | 169 | 119 | inferred_complete_timeline |
| `Action_None` | 170 | 247 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–301
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 63 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 64 | 169 | 106 | inferred_complete_timeline |
| `Action_None` | 170 | 301 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–304
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_DownBlock` | 51 | 169 | 119 | inferred_complete_timeline |
| `Action_None` | 170 | 294 | 125 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 95 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 203 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 73 | 26 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_None` | 94 | 419 | 326 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 418 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 150 | 103 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–373
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 373 | 326 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 25–69 | 40 | 4 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 29–88 | 60 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 33–41 | 4 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 58–95 | 28 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 75–108 | 34 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 105–111 | 7 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 114–311 | 192 | 3 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 146–419 | 272 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 147–419 | 266 | 4 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 171–244 | 74 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 178–248 | 71 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 179–419 | 241 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 187–231 | 14 | 4 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 199–419 | 219 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 215–419 | 202 | 3 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 225–419 | 194 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 271–273 | 3 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 311–419 | 109 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 368–370 | 3 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 368–370 | 3 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 376–419 | 44 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 391–396 | 6 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 412–413 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (3 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `7` (C): Annotated start 51 != Inferred start 64

### Track Identity Issues

- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '0' (TE) duration 119 frames exceeds threshold 90 frames [start=51, end=169].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '1' (LG) duration 119 frames exceeds threshold 90 frames [start=51, end=169].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '6' (C) duration 119 frames exceeds threshold 90 frames [start=51, end=169].
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [48–63], lower_priority='Action_DownBlock' annotated_start=51, effective_Action_DownBlock_start=64.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (RG) duration 119 frames exceeds threshold 90 frames [start=51, end=169].
- ⚠️ Action 'Action_DownBlock' range [51-127] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [132-137] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-247] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-373] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [64-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-301] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-294] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-73] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-419] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-203] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-418] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-27] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-65] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-108] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-290] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-311] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-153] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-244] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-248] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-419] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-393] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-262] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-247] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-370] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-370] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-396] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>