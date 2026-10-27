# Play-Annotation-Generator Annotation Review — CrackToss_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_59`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_CrackBlock` | WR2 | offense | `14` | `13` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `21` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 47 | START | 47 | 51 |
| ✅ EXACT | `Action_CrackBlock` | WR2 | `14` | `13` | 50 | START | 50 | 107 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `21` | `19` | 50 | START | 50 | 107 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 51 | END | 47 | 51 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 61 | START | 61 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `1` | 77 | START | 77 | 141 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 107 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–175
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 46 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_None` | 52 | 60 | 9 | inferred_complete_timeline |
| `Action_Toss` | 61 | 76 | 16 | inferred_complete_timeline |
| `Action_None` | 77 | 175 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 141 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 145 | 151 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 158 | 163 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 49 | 33 | inferred_complete_timeline |
| `Action_CrackBlock` | 50 | 107 | 58 | inferred_complete_timeline |
| `Action_None` | 108 | 149 | 42 | inferred_complete_timeline |
| `Action_None` | 153 | 157 | 5 | inferred_complete_timeline |
| `Action_None` | 160 | 166 | 7 | inferred_complete_timeline |
| `Action_None` | 169 | 175 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 175 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 175 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 175 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 13 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 46 | 27 | inferred_complete_timeline |
| `Action_None` | 47 | 71 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_None` | 52 | 175 | 124 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 46 | 23 | inferred_complete_timeline |
| `Action_None` | 47 | 141 | 95 | inferred_complete_timeline |
| `Action_None` | 145 | 151 | 7 | inferred_complete_timeline |
| `Action_None` | 153 | 175 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 135 | 89 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 175 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 126 | 80 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 151 | 10 | inferred_complete_timeline |
| `Action_None` | 153 | 175 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 175 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 110 | 64 | inferred_complete_timeline |
| `Action_None` | 115 | 118 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 159 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 175 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 137 | 91 | inferred_complete_timeline |
| `Action_None` | 139 | 175 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–175 | 176 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 23–175 | 153 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 24–77 | 53 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 24–175 | 152 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 24–175 | 152 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 24–97 | 72 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 84–175 | 92 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 87–175 | 83 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 91–175 | 80 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 120–175 | 56 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 168–175 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (4 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 120: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [47-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-141] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [145-151] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [155-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [158-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-175] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-137] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-126] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-135] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-175] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-141] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-175] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-175] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-77] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-92] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-92] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-151] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-175] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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