# Play-Annotation-Generator Annotation Review — Counter_310

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_310`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `3` | `2` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 54 |
| ✅ EXACT | `Action_BallSnap` | C | `6` | `5` | 52 | START | 52 | 65 |
| ✅ EXACT | `Action_DownBlock` | RT | `3` | `2` | 55 | START | 55 | 137 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `6` | `5` | 55 | START | 66 | 137 |
| ✅ EXACT | `Action_PullBlock` | LG | `14` | `13` | 55 | START | 55 | 137 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `8` | `7` | 55 | START | 55 | 137 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `7` | `6` | 61 | START | 61 | 95 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 65 | END | 52 | 65 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 76 | START | 76 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 96 | START | 96 | 186 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 137 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_SnapReceive` | 52 | 65 | 14 | inferred_complete_timeline |
| `Action_None` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 76 | 95 | 20 | inferred_complete_timeline |
| `Action_None` | 96 | 210 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 61 | 95 | 35 | inferred_complete_timeline |
| `Action_BallCarry` | 96 | 186 | 91 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 195 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 197 | 202 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 210 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 55 | 137 | 83 | inferred_complete_timeline |
| `Action_None` | 138 | 210 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PullBlock` | 55 | 137 | 83 | inferred_complete_timeline |
| `Action_None` | 138 | 210 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_BallSnap` | 52 | 65 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 66 | 137 | 72 | inferred_complete_timeline |
| `Action_None` | 138 | 210 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_DownBlock` | 55 | 137 | 83 | inferred_complete_timeline |
| `Action_None` | 138 | 146 | 9 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 139 | 88 | inferred_complete_timeline |
| `Action_None` | 142 | 210 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 59 | 8 | inferred_complete_timeline |
| `Action_None` | 62 | 126 | 65 | inferred_complete_timeline |
| `Action_None` | 128 | 150 | 23 | inferred_complete_timeline |
| `Action_None` | 155 | 159 | 5 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_None` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_None` | 59 | 157 | 99 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 134 | 83 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 173 | 29 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 120 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 210 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 70 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 210 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 114 | 63 | inferred_complete_timeline |
| `Action_None` | 116 | 197 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–40 | 41 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 93–210 | 114 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 112–123 | 9 | 2 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 127–133 | 7 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 127–210 | 80 | 2 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 128–210 | 75 | 4 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 149–210 | 62 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 150–164 | 10 | 3 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 152–210 | 59 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 156–161 | 6 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 186–210 | 25 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 201–210 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `6` (C): Annotated start 55 != Inferred start 66
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 622: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [52–65], lower_priority='Action_DownBlock' annotated_start=55, effective_Action_DownBlock_start=66.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [55-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-146] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [96-186] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [189-195] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [197-202] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-134] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [55-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-126] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-154] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-190] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>