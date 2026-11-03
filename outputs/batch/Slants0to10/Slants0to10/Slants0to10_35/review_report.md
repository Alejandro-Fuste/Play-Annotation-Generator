# Play-Annotation-Generator Annotation Review — Slants0to10_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_35`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 142
- **Validation Warnings:** 147
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 124
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunSlantRoute` | TE | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_BallCarry` | TE | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 13 | START | 13 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `12` | `12` | 16 | START | 16 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 16 | START | 29 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 16 | START | 16 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `7` | `7` | 16 | START | 16 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunSlantRoute` | TE | `19` | `19` | 28 | START | 28 | 89 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 28 | END | 13 | 28 |
| ✅ EXACT | `Action_ThrowPass` | QB | `2` | `2` | 65 | START | 65 | 71 |
| ✅ EXACT | `Action_BallCarry` | TE | `19` | `19` | 97 | START | 97 | 117 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 13 | 28 | 16 | inferred_complete_timeline |
| `Action_None` | 29 | 64 | 36 | inferred_complete_timeline |
| `Action_ThrowPass` | 65 | 71 | 7 | inferred_complete_timeline |
| `Action_None` | 72 | 180 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 87 | 75 | inferred_complete_timeline |
| `Action_None` | 150 | 156 | 7 | inferred_complete_timeline |
| `Action_None` | 159 | 180 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 136 | 124 | inferred_complete_timeline |
| `Action_None` | 138 | 154 | 17 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 100 | 88 | inferred_complete_timeline |
| `Action_None` | 102 | 117 | 16 | inferred_complete_timeline |
| `Action_None` | 119 | 126 | 8 | inferred_complete_timeline |
| `Action_None` | 128 | 139 | 12 | inferred_complete_timeline |
| `Action_None` | 141 | 152 | 12 | inferred_complete_timeline |
| `Action_None` | 157 | 173 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 28 | 89 | 62 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 91 | 91 | 1 | inferred_complete_timeline |
| `Action_None` | 92 | 96 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 117 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 40 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 79 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 121 | 132 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 13 | 27 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 31 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 89 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 20 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 65 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 136 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 138 | 146 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 171 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 173 | 180 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 89 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–23
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 23 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–23
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 23 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 23 | 11 | inferred_complete_timeline |
| `Action_None` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_None` | 54 | 73 | 20 | inferred_complete_timeline |
| `Action_None` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_None` | 84 | 87 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 180 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 40 | 28 | inferred_complete_timeline |
| `Action_None` | 42 | 74 | 33 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 62 | 50 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 82 | 96 | 15 | inferred_complete_timeline |
| `Action_None` | 121 | 139 | 19 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 167 | 7 | inferred_complete_timeline |
| `Action_None` | 169 | 174 | 6 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 27 | 15 | inferred_complete_timeline |
| `Action_None` | 29 | 38 | 10 | inferred_complete_timeline |
| `Action_None` | 47 | 93 | 47 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 156 | 42 | inferred_complete_timeline |
| `Action_None` | 166 | 172 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 73 | 61 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_None` | 119 | 156 | 38 | inferred_complete_timeline |
| `Action_None` | 161 | 168 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 113 | 101 | inferred_complete_timeline |
| `Action_None` | 115 | 180 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 180 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 139 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 151 | 139 | inferred_complete_timeline |
| `Action_None` | 162 | 180 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–85 | 75 | 6 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–69 | 60 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 43–180 | 58 | 8 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 55–180 | 115 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 79–180 | 98 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 116–180 | 64 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 120–180 | 56 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 122–180 | 59 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 123–180 | 58 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 123–124 | 2 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 127–171 | 11 | 3 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 139–180 | 42 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 152–166 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (9 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunSlantRoute` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 116 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 35: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ Row 36: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [13–28], lower_priority='Action_PassBlock' annotated_start=16, effective_Action_PassBlock_start=29.
- ⚠️ Action 'Action_None' range [13-100] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-139] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-27] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-38] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-93] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-156] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-64] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-62] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-96] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-136] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-40] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-74] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-31] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-40] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-79] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [121-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-87] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-156] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-31] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-39] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-73] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-23] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-31] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-34] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-89] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-73] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-156] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-168] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [13-27] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-31] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-23] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-73] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-23] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunSlantRoute' range [28-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-20] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-65] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [138-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [149-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-171] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [173-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-27] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-31] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-38] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-74] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-89] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-66] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-74] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-89] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-107] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-163] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-180] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-166] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>