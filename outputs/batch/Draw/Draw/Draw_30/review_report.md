# Play-Annotation-Generator Annotation Review — Draw_30

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_30`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `1` | `0` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 16 | START | 16 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 16 | START | 16 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 16 | START | 16 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 16 | START | 16 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 16 | START | 16 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 16 | START | 16 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 16 | START | 16 | 58 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 59 | START | 59 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `1` | `0` | 62 | START | 62 | 95 |
| ✅ EXACT | `Action_PassBlock` | LT | `10` | `9` | 62 | START | 62 | 166 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `12` | `11` | 62 | START | 75 | 166 |
| ✅ EXACT | `Action_PassBlock` | RG | `3` | `2` | 62 | START | 62 | 166 |
| ✅ EXACT | `Action_PassBlock` | RT | `5` | `4` | 62 | START | 62 | 166 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 74 | END | 59 | 74 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `11` | `10` | 89 | START | 89 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `11` | `10` | 108 | START | 108 | 300 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 166 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 16–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 59 | 74 | 16 | inferred_complete_timeline |
| `Action_None` | 75 | 88 | 14 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 89 | 107 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 108 | 300 | 193 | inferred_complete_timeline |
| `Action_BallCarry` | 302 | 359 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 16–97
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_None` | 59 | 97 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 16–309
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 61 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 166 | 105 | inferred_complete_timeline |
| `Action_None` | 167 | 309 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 16–359
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 61 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 95 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 166 | 52 | inferred_complete_timeline |
| `Action_None` | 167 | 359 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 16–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_BallSnap` | 59 | 74 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 166 | 92 | inferred_complete_timeline |
| `Action_None` | 167 | 359 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 16–319
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 61 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 166 | 105 | inferred_complete_timeline |
| `Action_None` | 167 | 213 | 47 | inferred_complete_timeline |
| `Action_None` | 220 | 319 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 16–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 61 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 166 | 105 | inferred_complete_timeline |
| `Action_None` | 167 | 359 | 193 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 16–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_None` | 59 | 359 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 16–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_None` | 59 | 359 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 16–118
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_None` | 59 | 107 | 49 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 16–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_None` | 59 | 359 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 16–112
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_None` | 59 | 112 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 16–359
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 58 | 43 | inferred_complete_timeline |
| `Action_None` | 59 | 269 | 211 | inferred_complete_timeline |
| `Action_None` | 272 | 359 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `16` | Position_Unknown | Team_Unknown | 102–356 | 245 | 4 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 107–359 | 251 | 2 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 144–194 | 48 | 3 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 165–346 | 181 | 2 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 192–201 | 7 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 195–204 | 10 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 202–213 | 11 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 218–317 | 100 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 228–353 | 59 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 231–359 | 129 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 267–359 | 93 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 283–354 | 72 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 285–359 | 73 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 291–293 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 295–345 | 45 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 332–359 | 19 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `12` (C): Annotated start 62 != Inferred start 75
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [59–74], lower_priority='Action_PassBlock' annotated_start=62, effective_Action_PassBlock_start=75.
- ⚠️ Action 'Action_PassBlock' range [62-95] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-269] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-213] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-319] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-359] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-359] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-309] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [108-300] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-166] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-359] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-260] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-350] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-194] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-217] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-346] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-204] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-317] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-280] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-353] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-354] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-307] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-345] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-336] for track '28' has 1 frames without a visible bounding box.
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

</details>