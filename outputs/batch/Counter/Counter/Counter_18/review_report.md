# Play-Annotation-Generator Annotation Review — Counter_18

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_18`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 55
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `10` | `9` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 39 | START | 39 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `13` | `12` | 46 | START | 46 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 46 | START | 58 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `15` | `14` | 46 | START | 46 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `10` | `9` | 46 | START | 46 | 56 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `8` | `7` | 46 | START | 46 | 127 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `5` | `4` | 57 | START | 57 | 79 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 57 | END | 39 | 57 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 64 | START | 64 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `4` | 80 | START | 80 | 131 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 127 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_SnapReceive` | 39 | 57 | 19 | inferred_complete_timeline |
| `Action_None` | 58 | 63 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 64 | 79 | 16 | inferred_complete_timeline |
| `Action_None` | 80 | 91 | 12 | inferred_complete_timeline |
| `Action_None` | 94 | 180 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 57 | 79 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 80 | 131 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 134 | 180 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 102 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 46 | 127 | 82 | inferred_complete_timeline |
| `Action_None` | 128 | 180 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 59 | 70 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 79 | 127 | 49 | inferred_complete_timeline |
| `Action_None` | 128 | 180 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_BallSnap` | 39 | 57 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 58 | 80 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 82 | 127 | 46 | inferred_complete_timeline |
| `Action_None` | 128 | 163 | 36 | inferred_complete_timeline |
| `Action_None` | 171 | 180 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_DownBlock` | 46 | 79 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 82 | 127 | 46 | inferred_complete_timeline |
| `Action_None` | 128 | 180 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_DownBlock` | 46 | 97 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 127 | 28 | inferred_complete_timeline |
| `Action_None` | 128 | 180 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 101 | 63 | inferred_complete_timeline |
| `Action_None` | 115 | 180 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 90 | 52 | inferred_complete_timeline |
| `Action_None` | 92 | 97 | 6 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 180 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 101 | 63 | inferred_complete_timeline |
| `Action_None` | 109 | 138 | 30 | inferred_complete_timeline |
| `Action_None` | 140 | 180 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 164 | 126 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 171 | 178 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 180 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 180 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 73 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 180 | 142 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `19` | Position_Unknown | Team_Unknown | 117–180 | 62 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 125–180 | 56 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 149–180 | 32 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 150–180 | 31 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 155–180 | 26 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 165–180 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [39–57], lower_priority='Action_DownBlock' annotated_start=46, effective_Action_DownBlock_start=58.
- ⚠️ Action 'Action_None' range [39-73] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [80-131] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [134-180] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-180] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [46-127] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [46-56] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [59-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-91] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-180] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-102] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [46-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [58-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [46-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-164] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-178] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-180] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '21' has 1 frames without a visible bounding box.
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

</details>