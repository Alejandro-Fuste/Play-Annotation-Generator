# Play-Annotation-Generator Annotation Review — Duo_16

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_16`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 1
- **Action Segments:** 70
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

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
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `15` | `15` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_ComboBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | FB | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `3` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `15` | `15` | 47 | START | 47 | 86 |
| ✅ EXACT | `Action_ComboBlock` | C | `17` | `17` | 47 | START | 47 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | `7` | `7` | 47 | START | 47 | 52 |
| ✅ EXACT | `Action_ComboBlock` | RT | `8` | `8` | 47 | START | 47 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | FB | `3` | `3` | 60 | START | 60 | 87 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 86 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 60 | 87 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 99 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 111 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 76 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ComboBlock` | 47 | 66 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ComboBlock` | 47 | 52 | 6 | inferred_complete_timeline |
| `Action_ComboBlock` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 61 | 79 | 19 | inferred_complete_timeline |
| `Action_None` | 87 | 112 | 26 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ComboBlock` | 47 | 86 | 40 | inferred_complete_timeline |
| `Action_None` | 87 | 102 | 16 | inferred_complete_timeline |
| `Action_None` | 104 | 149 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 149 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 45 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 62 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 69 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 69 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 148 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 86 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 119 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 139 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 149 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 149 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–102 | 103 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–78 | 72 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 50–122 | 47 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 66–149 | 84 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 91–142 | 50 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 101–104 | 4 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 112–137 | 20 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | 15 | 16 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 33: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 34: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 34: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 34: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-106] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-114] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [60-87] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-45] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-69] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-69] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [47-52] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [57-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [61-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-112] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [47-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-102] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-149] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-148] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-139] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-86] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-101] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-111] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-149] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [47-66] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-78] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-70] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-109] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-142] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>