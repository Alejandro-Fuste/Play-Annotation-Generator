# Play-Annotation-Generator Annotation Review — CrackToss_79

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_79`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE1 | defense | `15` | `14` |
| ✅ EXACT | `Action_CrackBlock` | TE | offense | `12` | `11` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `2` | `1` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 77 |
| ✅ EXACT | `Action_BallSnap` | DE1 | `15` | `14` | 75 | START | 75 | 85 |
| ✅ EXACT | `Action_CrackBlock` | TE | `12` | `11` | 78 | START | 78 | 138 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `2` | `1` | 78 | START | 78 | 138 |
| ✅ EXACT | `Action_PullBlock` | LT | `4` | `3` | 78 | START | 78 | 138 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 85 | END | 75 | 85 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 90 | START | 90 | 107 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `9` | 108 | START | 108 | 199 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 138 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_SnapReceive` | 75 | 85 | 11 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_Toss` | 90 | 107 | 18 | inferred_complete_timeline |
| `Action_None` | 108 | 139 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_BallCarry` | 108 | 199 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_CrackBlock` | 78 | 138 | 61 | inferred_complete_timeline |
| `Action_None` | 139 | 194 | 56 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PullBlock` | 78 | 138 | 61 | inferred_complete_timeline |
| `Action_None` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 200 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 156 | 82 | inferred_complete_timeline |
| `Action_None` | 158 | 200 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 200 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 117 | 43 | inferred_complete_timeline |
| `Action_None` | 121 | 200 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_BallSnap` | 75 | 85 | 11 | inferred_complete_timeline |
| `Action_None` | 86 | 147 | 62 | inferred_complete_timeline |
| `Action_None` | 154 | 200 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 200 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 87 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 96 | 22 | inferred_complete_timeline |
| `Action_None` | 113 | 200 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 117 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 200 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 117 | 43 | inferred_complete_timeline |
| `Action_None` | 122 | 200 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 167 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 172 | 98 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 200 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–200 | 201 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–200 | 200 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 3–25 | 19 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 7–92 | 34 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 92–115 | 24 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 94–142 | 46 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 105–114 | 6 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 107–121 | 7 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 118–200 | 79 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 123–200 | 78 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 143–171 | 26 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 154–200 | 47 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 197–200 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 160: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [75-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-200] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-156] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-200] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-200] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [108-199] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [78-138] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-194] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-147] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-200] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-181] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-96] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-11] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-22] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-9] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-92] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-115] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-129] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-186] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-200] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-171] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-200] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.

</details>