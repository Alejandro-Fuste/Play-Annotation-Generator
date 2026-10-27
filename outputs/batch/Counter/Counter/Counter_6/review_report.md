# Play-Annotation-Generator Annotation Review — Counter_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_6`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `6` | `5` |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `17` | `15` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `17` | `15` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `13` | `12` | 45 | START | 45 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `1` | `0` | 52 | START | 52 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 52 | START | 74 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `5` | `4` | 52 | START | 52 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `4` | `3` | 52 | START | 52 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `6` | `5` | 52 | START | 52 | 81 |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | `17` | `15` | 60 | END | 69 | 69 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `17` | `15` | 70 | START | 70 | 82 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `16` | `14` | 83 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 125 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 52 | 81 | 30 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 88 | 100 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 81 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 87 | 95 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 125 | 19 | inferred_complete_timeline |
| `Action_None` | 126 | 137 | 12 | inferred_complete_timeline |
| `Action_None` | 148 | 165 | 18 | inferred_complete_timeline |
| `Action_None` | 172 | 189 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 67 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 71 | 125 | 55 | inferred_complete_timeline |
| `Action_None` | 126 | 238 | 113 | inferred_complete_timeline |
| `Action_None` | 240 | 245 | 6 | inferred_complete_timeline |
| `Action_None` | 247 | 269 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_BallSnap` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 51 | 58 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 74 | 82 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 89 | 98 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 105 | 110 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 119 | 125 | 7 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 269 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PullBlock` | 52 | 79 | 28 | inferred_complete_timeline |
| `Action_PullBlock` | 81 | 86 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 91 | 92 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 74 | 30 | inferred_complete_timeline |
| `Action_None` | 77 | 139 | 63 | inferred_complete_timeline |
| `Action_None` | 141 | 164 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 44 | 23 | inferred_complete_timeline |
| `Action_None` | 45 | 53 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–8
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 134 | 39 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 89 | 45 | inferred_complete_timeline |
| `Action_None` | 94 | 101 | 8 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_None` | 116 | 269 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_None` | 50 | 86 | 37 | inferred_complete_timeline |
| `Action_None` | 89 | 158 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 86 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 260 | 216 | inferred_complete_timeline |
| `Action_None` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 6–148 | 138 | 4 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 67–77 | 11 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 69–130 | 59 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 81–266 | 143 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 92–269 | 162 | 7 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 94–269 | 168 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 95–268 | 173 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 123–269 | 141 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 143–269 | 122 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 149–167 | 12 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 217–240 | 24 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 227–269 | 43 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 264–269 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `6` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `16` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 13: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [45–60], lower_priority='Action_DownBlock' annotated_start=52, effective_Action_DownBlock_start=61.
- ⚠️ Segment 'Action_BallCarry' for track '14' has invalid range: start=83, end=77. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '15' has invalid range: start=69, end=60. Clamping end to start.
- ⚠️ Action 'Action_DownBlock' range [52-67] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-238] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-245] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-260] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-86] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [52-79] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [81-86] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [91-92] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [52-81] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [87-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-189] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [52-81] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [88-100] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-164] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-86] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-89] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-53] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-134] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-44] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [45-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [51-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [74-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [89-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [114-117] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [119-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 45, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [45-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [70-82] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-130] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-266] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-128] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-193] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-224] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-240] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-146] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-197] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-126] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-268] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-240] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '25' has 1 frames without a visible bounding box.
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

</details>