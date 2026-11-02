# Play-Annotation-Generator Annotation Review — PinAndPull_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PinAndPull_1`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | RG | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `0` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `1` | `0` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `21` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 10 | START | 10 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `12` | `11` | 13 | START | 13 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `22` | `21` | 13 | START | 24 | 99 |
| ✅ EXACT | `Action_PullLeadBlock` | RG | `13` | `12` | 13 | START | 13 | 90 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `0` | 23 | END | 10 | 23 |
| ✅ EXACT | `Action_Handoff` | QB | `1` | `0` | 26 | START | 26 | 40 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `5` | `4` | 41 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 109 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 23 | 14 | inferred_complete_timeline |
| `Action_None` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_None` | 41 | 111 | 71 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 24 | 15 | inferred_complete_timeline |
| `Action_None` | 31 | 120 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 43 | 34 | inferred_complete_timeline |
| `Action_None` | 47 | 120 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 21 | 12 | inferred_complete_timeline |
| `Action_None` | 41 | 98 | 58 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 26 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 23 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 24 | 99 | 76 | inferred_complete_timeline |
| `Action_PullBlock` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 120 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 13 | 90 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 13 | 45 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 48 | 109 | 62 | inferred_complete_timeline |
| `Action_None` | 110 | 120 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 25 | 16 | inferred_complete_timeline |
| `Action_None` | 27 | 28 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 30 | 21 | inferred_complete_timeline |
| `Action_None` | 80 | 107 | 28 | inferred_complete_timeline |
| `Action_None` | 109 | 120 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 78 | 69 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 79 | 70 | inferred_complete_timeline |
| `Action_None` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 120 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 40 | 31 | inferred_complete_timeline |
| `Action_None` | 48 | 51 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 93 | 84 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 111 | 120 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 80 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 22 | 13 | inferred_complete_timeline |
| `Action_None` | 27 | 120 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 120 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 120 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 30 | 21 | inferred_complete_timeline |
| `Action_None` | 37 | 77 | 41 | inferred_complete_timeline |
| `Action_None` | 79 | 118 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–120 | 108 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 34–118 | 74 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 35–105 | 71 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 54–67 | 6 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 76–120 | 45 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 77–120 | 44 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 108–110 | 3 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 115–120 | 6 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `5` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 4: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '4' has invalid range: start=41, end=28. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (RT) duration 97 frames exceeds threshold 90 frames [start=13, end=109].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (C) duration 97 frames exceeds threshold 90 frames [start=13, end=109].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [10–23], lower_priority='Action_PullBlock' annotated_start=13, effective_Action_PullBlock_start=24.
- ⚠️ Action 'Action_None' range [41-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-95] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-120] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-43] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-120] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-22] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-120] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-55] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-100] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-120] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-21] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-26] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-79] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-120] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [13-45] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [48-109] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [13-90] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-107] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-120] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-80] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-28] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-30] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-77] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-118] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-93] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-120] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-78] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-24] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [24-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [105-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-41] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-109] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-120] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>