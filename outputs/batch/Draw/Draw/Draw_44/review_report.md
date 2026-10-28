# Play-Annotation-Generator Annotation Review — Draw_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_44`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 20
- **Ball Tracks:** 0
- **Action Segments:** 49
- **Validation Warnings:** 49
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 6
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 32
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `3` | `2` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 65 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 63 | START | 63 | 76 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `10` | `9` | 66 | START | 77 | 130 |
| ✅ EXACT | `Action_PassBlock` | RG | `12` | `11` | 66 | START | 66 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `3` | `2` | 66 | START | 66 | 94 |
| ✅ EXACT | `Action_PassBlock` | LG | `5` | `4` | 66 | START | 66 | 130 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 76 | END | 63 | 76 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `2` | `1` | 80 | START | 80 | 101 |
| ✅ EXACT | `Action_BallCarry` | QB | `2` | `1` | 102 | START | 102 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 130 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_SnapReceive` | 63 | 76 | 14 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 80 | 101 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 239 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 130 | 65 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_BallSnap` | 63 | 76 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 130 | 54 | inferred_complete_timeline |
| `Action_None` | 131 | 143 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 130 | 65 | inferred_complete_timeline |
| `Action_None` | 131 | 219 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 94 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 104 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 115 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 120 | 130 | 11 | inferred_complete_timeline |
| `Action_None` | 131 | 237 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 108 | 46 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 239 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 101 | 39 | inferred_complete_timeline |
| `Action_None` | 104 | 120 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 228 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 122 | 60 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 219 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–215 | 216 | 2 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 15–16 | 2 | 1 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 105–108 | 4 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 121–202 | 75 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 123–201 | 78 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 125–177 | 53 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 148–229 | 82 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 158–239 | 82 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 205–239 | 35 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `10` (C): Annotated start 66 != Inferred start 77
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (4 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 28 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 88: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [63–76], lower_priority='Action_PassBlock' annotated_start=66, effective_Action_PassBlock_start=77.
- ⚠️ Action 'Action_None' range [63-122] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-219] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-94] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-115] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-237] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-215] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-228] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-120] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-219] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-133] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>