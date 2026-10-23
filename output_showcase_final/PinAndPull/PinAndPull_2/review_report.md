# Play-Annotation-Generator Annotation Review — PinAndPull_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PinAndPull_2`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT2 | defense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 11 | START | 11 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT2 | `4` | `3` | 14 | START | 14 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `10` | `9` | 14 | START | 14 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | C | `16` | `15` | 14 | START | 23 | 26 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 22 | END | 11 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `7` | `6` | 28 | START | 28 | 35 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `11` | `10` | 41 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 105 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 22 | 12 | inferred_complete_timeline |
| `Action_None` | 23 | 27 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 28 | 35 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 38 | 40 | 3 | inferred_complete_timeline |
| `Action_None` | 41 | 92 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 85 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 20 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 57 | 47 | inferred_complete_timeline |
| `Action_None` | 59 | 119 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 22 | 12 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 23 | 26 | 4 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 32 | 53 | 22 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 67 | 79 | 13 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 99 | 105 | 7 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 120 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 14 | 31 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 59 | 95 | 37 | inferred_complete_timeline |
| `Action_None` | 112 | 119 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 21 | 11 | inferred_complete_timeline |
| `Action_None` | 31 | 120 | 90 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 120 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 120 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 52 | 42 | inferred_complete_timeline |
| `Action_None` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_None` | 96 | 120 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 14 | 50 | 37 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 105 | 54 | inferred_complete_timeline |
| `Action_None` | 106 | 120 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 50 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 45 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_None` | 48 | 57 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 100 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 24 | 14 | inferred_complete_timeline |
| `Action_None` | 30 | 112 | 83 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–21
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 9 | 5 | inferred_complete_timeline |
| `Action_None` | 11 | 21 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–120 | 121 | 2 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–120 | 121 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 6–59 | 50 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 17–120 | 89 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 35–90 | 12 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 39–120 | 62 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 43–120 | 64 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 47–62 | 16 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 67–120 | 54 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 68–120 | 53 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 70–120 | 51 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `7` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `11` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 6: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 6: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (DT2) duration 92 frames exceeds threshold 90 frames [start=14, end=105].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '9' (RG) duration 92 frames exceeds threshold 90 frames [start=14, end=105].
- ⚠️ Segment 'Action_BallCarry' for track '10' has invalid range: start=41, end=40. Clamping end to start.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [11–22], lower_priority='Action_PullLeadBlock' annotated_start=14, effective_Action_PullLeadBlock_start=23.
- ⚠️ Action 'Action_None' range [11-45] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-50] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-44] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-57] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [14-50] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-100] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [28-35] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-92] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [14-31] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [59-95] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-57] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [23-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [32-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [67-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [99-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-24] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-21] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-120] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-9] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-27] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-59] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-120] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-44] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-45] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-68] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-46] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-57] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-62] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-120] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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