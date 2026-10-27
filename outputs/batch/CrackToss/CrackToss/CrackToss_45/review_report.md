# Play-Annotation-Generator Annotation Review — CrackToss_45

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_45`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 1
- **Action Segments:** 66
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `24` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_PullBlock` | TE | offense | `1` | `0` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 92 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `24` | `20` | 60 | START | 100 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `18` | `17` | 63 | START | 63 | 79 |
| ✅ EXACT | `Action_PullBlock` | TE | `1` | `0` | 63 | START | 63 | 108 |
| ✅ EXACT | `Action_PullBlock` | LT | `15` | `14` | 63 | START | 63 | 108 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 70 | END | 60 | 70 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 73 | START | 73 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 93 | START | 93 | 128 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 108 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_SnapReceive` | 60 | 70 | 11 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_Toss` | 73 | 92 | 20 | inferred_complete_timeline |
| `Action_None` | 93 | 126 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_BallCarry` | 93 | 128 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 139 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 142 | 150 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PullBlock` | 63 | 108 | 46 | inferred_complete_timeline |
| `Action_None` | 109 | 149 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PullBlock` | 63 | 108 | 46 | inferred_complete_timeline |
| `Action_None` | 109 | 150 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 150 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 141 | 82 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 150 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 74 | 15 | inferred_complete_timeline |
| `Action_None` | 76 | 83 | 8 | inferred_complete_timeline |
| `Action_None` | 86 | 136 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 150 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 122 | 63 | inferred_complete_timeline |
| `Action_None` | 130 | 150 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 150 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 102 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 42 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 59 | 13 | inferred_complete_timeline |
| `Action_None` | 60 | 150 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–150 | 148 | 4 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–69 | 70 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 3–142 | 126 | 6 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 55–150 | 94 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 90–150 | 61 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 96–142 | 43 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 100–150 | 51 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 104–118 | 11 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 105–150 | 46 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 126–142 | 17 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 139–150 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | 0 | 0 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `24` (Position_Unknown): Annotated start 60 != Inferred start 100
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 92: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '20' has invalid range: start=100, end=70. Clamping end to start.
- ⚠️ Action 'Action_PullBlock' range [63-108] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-83] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-136] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-102] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-150] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-42] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-59] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-150] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [93-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [142-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-39] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-142] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [63-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [82-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-142] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>