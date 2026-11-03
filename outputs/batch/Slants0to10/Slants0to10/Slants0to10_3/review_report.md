# Play-Annotation-Generator Annotation Review — Slants0to10_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_3`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 57
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB2 | defense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | CB2 | `11` | `11` | 6 | START | 6 | 25 |
| ✅ EXACT | `Action_PassBlock` | RG | `17` | `17` | 9 | START | 9 | 210 |
| ✅ EXACT | `Action_PassBlock` | RT | `2` | `2` | 9 | START | 9 | 210 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 9 | START | 9 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `21` | `21` | 9 | START | 9 | 65 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `5` | `5` | 25 | START | 25 | 60 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 25 | END | 6 | 25 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 55 | START | 55 | 65 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `5` | `5` | 70 | START | 70 | 199 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 6 | 25 | 20 | inferred_complete_timeline |
| `Action_None` | 26 | 54 | 29 | inferred_complete_timeline |
| `Action_ThrowPass` | 55 | 65 | 11 | inferred_complete_timeline |
| `Action_None` | 66 | 210 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 25 | 60 | 36 | inferred_complete_timeline |
| `Action_None` | 61 | 69 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 199 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 63 | 77 | 15 | inferred_complete_timeline |
| `Action_None` | 82 | 114 | 33 | inferred_complete_timeline |
| `Action_None` | 120 | 210 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 65 | 57 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 98 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_None` | 50 | 53 | 4 | inferred_complete_timeline |
| `Action_None` | 63 | 65 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 36 | 31 | inferred_complete_timeline |
| `Action_None` | 38 | 210 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 91 | 86 | inferred_complete_timeline |
| `Action_None` | 102 | 108 | 7 | inferred_complete_timeline |
| `Action_None` | 121 | 210 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 103 | 210 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 84 | 79 | inferred_complete_timeline |
| `Action_None` | 87 | 90 | 4 | inferred_complete_timeline |
| `Action_None` | 94 | 99 | 6 | inferred_complete_timeline |
| `Action_None` | 102 | 110 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 6 | 25 | 20 | inferred_complete_timeline |
| `Action_None` | 26 | 109 | 84 | inferred_complete_timeline |
| `Action_None` | 113 | 210 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 103 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 189 | 184 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_None` | 199 | 206 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 73–210 | 136 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 109–210 | 102 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 114–210 | 97 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 115–117 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 4: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [6-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-43] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-77] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-114] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-36] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-109] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-103] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>