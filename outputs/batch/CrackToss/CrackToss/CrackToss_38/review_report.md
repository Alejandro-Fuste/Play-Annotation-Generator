# Play-Annotation-Generator Annotation Review — CrackToss_38

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_38`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 144
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 27 | START | 27 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `13` | `12` | 30 | START | 30 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `15` | `14` | 30 | START | 42 | 43 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 37 | END | 27 | 37 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 44 | START | 44 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 57 | START | 57 | 113 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 37 | 11 | inferred_complete_timeline |
| `Action_None` | 38 | 43 | 6 | inferred_complete_timeline |
| `Action_Toss` | 44 | 56 | 13 | inferred_complete_timeline |
| `Action_None` | 57 | 150 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 57 | 113 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 126 | 129 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 146 | 150 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 150 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 29 | 14 | inferred_complete_timeline |
| `Action_CrackBlock` | 30 | 61 | 32 | inferred_complete_timeline |
| `Action_CrackBlock` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_CrackBlock` | 68 | 69 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 80 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 37 | 65 | 29 | inferred_complete_timeline |
| `Action_None` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_None` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_None` | 83 | 88 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 37 | 11 | inferred_complete_timeline |
| `Action_None` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_None` | 45 | 51 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 49 | 56 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 58 | 65 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 67 | 71 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 76 | 81 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 85 | 92 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 96 | 113 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 136 | 150 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 36 | 72 | 37 | inferred_complete_timeline |
| `Action_None` | 76 | 81 | 6 | inferred_complete_timeline |
| `Action_None` | 93 | 98 | 6 | inferred_complete_timeline |
| `Action_None` | 110 | 150 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_None` | 48 | 65 | 18 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 81 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 56 | 77 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 86 | 60 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 79 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 39 | 13 | inferred_complete_timeline |
| `Action_None` | 42 | 65 | 24 | inferred_complete_timeline |
| `Action_None` | 67 | 71 | 5 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 150 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 113 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 150 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 121 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–109 | 55 | 7 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–150 | 78 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 43–61 | 19 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 45–69 | 19 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 48–56 | 9 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 68–148 | 17 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 84–150 | 61 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 97–150 | 39 | 6 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 97–150 | 54 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 107–113 | 5 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 107–132 | 19 | 4 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 107–150 | 44 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 108–109 | 2 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 108–150 | 26 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 132–133 | 2 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 132–150 | 19 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 142–150 | 9 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 145–146 | 2 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 148–150 | 3 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `15` (10 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 80 targets track ID '116', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 101 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 78: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '14' (RT) duration 121 frames exceeds threshold 90 frames [start=30, end=150].
- ⚠️ Action 'Action_None' range [27-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-113] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-86] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-121] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [57-113] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [126-129] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [133-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [146-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-79] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-37] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-71] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-72] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-81] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-29] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [30-61] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [64-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [68-69] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-71] for track '13' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-150] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [42-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [45-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [49-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [58-65] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [67-71] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [76-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [85-92] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [96-113] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [133-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [136-150] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-51] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-44] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-65] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-65] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-39] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-65] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-71] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-61] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-61] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-56] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-88] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-113] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-123] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>