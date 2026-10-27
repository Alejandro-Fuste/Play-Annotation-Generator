# Play-Annotation-Generator Annotation Review — Counter_88

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_88`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 53
- **Validation Warnings:** 47
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 33
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 46 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `13` | `12` | 47 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 47 | START | 47 | 81 |
| ✅ EXACT | `Action_DownBlock` | LT | `14` | `13` | 47 | START | 47 | 136 |
| ✅ EXACT | `Action_DownBlock` | LG | `4` | `3` | 47 | START | 47 | 136 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `3` | `2` | 47 | START | 47 | 93 |
| ✅ EXACT | `Action_PullBlock` | RG | `2` | `1` | 47 | START | 47 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `10` | `9` | 47 | START | 47 | 117 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 63 | END | 47 | 63 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 72 | START | 72 | 93 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `2` | 94 | START | 94 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 136 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 63 | 17 | inferred_complete_timeline |
| `Action_None` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 72 | 93 | 22 | inferred_complete_timeline |
| `Action_None` | 94 | 150 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 47 | 93 | 47 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 180 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 141 | 95 | inferred_complete_timeline |
| `Action_None` | 143 | 180 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 47 | 136 | 90 | inferred_complete_timeline |
| `Action_None` | 137 | 169 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 47 | 136 | 90 | inferred_complete_timeline |
| `Action_None` | 137 | 152 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 47 | 81 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PullBlock` | 47 | 136 | 90 | inferred_complete_timeline |
| `Action_None` | 137 | 180 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 47 | 117 | 71 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 121 | 125 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 46 | 35 | inferred_complete_timeline |
| `Action_None` | 47 | 106 | 60 | inferred_complete_timeline |
| `Action_None` | 108 | 180 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 180 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 156 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 95 | 49 | inferred_complete_timeline |
| `Action_None` | 98 | 177 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 180 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 107 | 61 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 124 | 180 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 82 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 75–180 | 106 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 80–162 | 83 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 134–180 | 45 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 138–144 | 5 | 2 | Undefined position; Undefined team |
| `20` | `32` | Position_Unknown | Team_Unknown | 168–180 | 13 | 1 | Undefined position; Undefined team |
| `21` | `34` | Position_Unknown | Team_Unknown | 176–180 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `13` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Overlapping action conflict at frame 47 for track '12': 'Action_BallSnap' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
- ⚠️ Action 'Action_None' range [47-95] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-152] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-107] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [47-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [121-125] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [47-81] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '21' has 1 frames without a visible bounding box.
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

</details>