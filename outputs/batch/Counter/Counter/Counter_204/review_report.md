# Play-Annotation-Generator Annotation Review — Counter_204

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_204`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | defense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 126 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `11` | `10` | 127 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `11` | `10` | 127 | START | 127 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `5` | `4` | 127 | START | 127 | 172 |
| ✅ EXACT | `Action_PullBlock` | LG | `2` | `1` | 127 | START | 127 | 182 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `10` | `9` | 127 | START | 127 | 217 |
| ✅ EXACT | `Action_SnapReceive` | RB | `8` | `7` | 144 | END | 127 | 144 |
| ✅ EXACT | `Action_Handoff` | RB | `8` | `7` | 159 | START | 159 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | `7` | `6` | 176 | START | 176 | 292 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 217 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_SnapReceive` | 127 | 144 | 18 | inferred_complete_timeline |
| `Action_None` | 145 | 158 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 159 | 175 | 17 | inferred_complete_timeline |
| `Action_None` | 176 | 285 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 327 | 201 | inferred_complete_timeline |
| `Action_None` | 330 | 359 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 127 | 217 | 91 | inferred_complete_timeline |
| `Action_None` | 218 | 359 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PullBlock` | 127 | 182 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_DownBlock` | 127 | 162 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 165 | 168 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–313
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_DownBlock` | 127 | 172 | 46 | inferred_complete_timeline |
| `Action_DownBlock` | 177 | 182 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 185 | 209 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 211 | 217 | 7 | inferred_complete_timeline |
| `Action_None` | 218 | 313 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 207 | 81 | inferred_complete_timeline |
| `Action_None` | 209 | 217 | 9 | inferred_complete_timeline |
| `Action_None` | 220 | 359 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_BallCarry` | 176 | 292 | 117 | inferred_complete_timeline |
| `Action_BallCarry` | 299 | 300 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 304 | 309 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 334 | 338 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 342 | 346 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 349 | 350 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 352 | 359 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 170 | 44 | inferred_complete_timeline |
| `Action_None` | 182 | 186 | 5 | inferred_complete_timeline |
| `Action_None` | 188 | 308 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 126 | 80 | inferred_complete_timeline |
| `Action_None` | 127 | 155 | 29 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 149 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 209 | 83 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |
| `Action_None` | 223 | 359 | 137 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `14` | Position_Unknown | Team_Unknown | 4–291 | 224 | 11 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 14–359 | 346 | 2 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 24–168 | 105 | 5 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 67–359 | 291 | 3 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 111–179 | 69 | 2 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 201–312 | 112 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 201–359 | 159 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 202–321 | 113 | 3 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 223–336 | 112 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 225–280 | 50 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 238–359 | 122 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 253–359 | 107 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 260–359 | 100 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 280–359 | 72 | 4 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 295–359 | 65 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 341–359 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `11` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (8 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 410: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (RG) duration 91 frames exceeds threshold 90 frames [start=127, end=217].
- ⚠️ Overlapping action conflict at frame 127 for track '10': 'Action_BallSnap' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
- ⚠️ Action 'Action_None' range [127-327] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [127-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-209] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-308] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [127-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [177-182] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [185-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-313] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '6' starts at frame 176, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [176-292] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [299-300] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [304-309] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [330-331] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [334-338] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [342-346] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [349-350] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-285] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [127-217] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [127-162] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [165-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-155] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-23] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-29] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-49] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-291] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-27] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-312] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-241] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-321] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-323] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-336] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-272] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-301] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-321] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-346] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-346] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>