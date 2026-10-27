# Play-Annotation-Generator Annotation Review — CrackToss_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_33`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 143
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `6` | `5` |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `0` |
| ✅ EXACT | `Action_Toss` | QB | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `6` | `5` | 16 | START | 16 | 20 |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | `13` | `12` | 19 | START | 19 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `4` | `3` | 19 | START | 19 | 19 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `0` | 24 | END | 16 | 24 |
| ✅ EXACT | `Action_Toss` | QB | `1` | `0` | 29 | START | 29 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `2` | 49 | START | 49 | 79 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 88 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–150
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 24 | 9 | inferred_complete_timeline |
| `Action_None` | 25 | 28 | 4 | inferred_complete_timeline |
| `Action_Toss` | 29 | 48 | 20 | inferred_complete_timeline |
| `Action_None` | 49 | 68 | 20 | inferred_complete_timeline |
| `Action_None` | 70 | 87 | 18 | inferred_complete_timeline |
| `Action_None` | 92 | 98 | 7 | inferred_complete_timeline |
| `Action_None` | 100 | 112 | 13 | inferred_complete_timeline |
| `Action_None` | 115 | 125 | 11 | inferred_complete_timeline |
| `Action_None` | 127 | 134 | 8 | inferred_complete_timeline |
| `Action_None` | 139 | 150 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_BallCarry` | 49 | 79 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 89 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 100 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 20 | 5 | inferred_complete_timeline |
| `Action_None` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_None` | 38 | 71 | 34 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 33 | 18 | inferred_complete_timeline |
| `Action_None` | 38 | 42 | 5 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 15 | 2 | inferred_complete_timeline |
| `Action_None` | 16 | 90 | 75 | inferred_complete_timeline |
| `Action_None` | 93 | 97 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_None` | 44 | 53 | 10 | inferred_complete_timeline |
| `Action_None` | 55 | 67 | 13 | inferred_complete_timeline |
| `Action_None` | 72 | 100 | 29 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PullBlock` | 19 | 19 | 1 | inferred_complete_timeline |
| `Action_PullBlock` | 21 | 38 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 41 | 57 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 76 | 87 | 12 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 108 | 15 | inferred_complete_timeline |
| `Action_None` | 113 | 115 | 3 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 26 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–17
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 17 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 22 | 7 | inferred_complete_timeline |
| `Action_None` | 32 | 64 | 33 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 115 | 19 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_None` | 142 | 150 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–7
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 7 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–140 | 120 | 6 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 3–28 | 23 | 4 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 3–42 | 24 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 4–31 | 15 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 9–148 | 110 | 9 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 30–150 | 56 | 5 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 39–88 | 50 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 53–70 | 18 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 56–124 | 38 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 68–76 | 8 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 73–86 | 9 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 76–150 | 75 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 85–98 | 12 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 104–150 | 40 | 4 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 110–150 | 31 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 119–150 | 25 | 4 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 122–129 | 8 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 145–149 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 105 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 67: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [49-68] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-87] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-112] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-33] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-42] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [49-79] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-100] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' for track '3' starts at frame 19, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PullBlock' range [19-19] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [21-38] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [41-57] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [76-87] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-108] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-40] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-53] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-67] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-100] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [16-20] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-41] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-131] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-26] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-22] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-115] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-17] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-90] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-20] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-35] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-71] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-9] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-15] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [19-28] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-10] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-42] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-7] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-15] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-100] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-70] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-124] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-92] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-135] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-129] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.

</details>