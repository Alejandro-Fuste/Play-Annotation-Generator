# Play-Annotation-Generator Annotation Review — Counter_75

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_75`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `20` | `19` |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | Team_Unknown | `31` | `24` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 43 | START | 43 | 54 |
| ✅ EXACT | `Action_DownBlock` | RT | `20` | `19` | 46 | START | 46 | 144 |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | `31` | `24` | 46 | START | 139 | 144 |
| ✅ EXACT | `Action_PullBlock` | LG | `9` | `8` | 46 | START | 46 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `8` | `7` | 46 | START | 46 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `5` | `4` | 52 | START | 52 | 73 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 54 | END | 43 | 54 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 76 | START | 76 | 89 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `4` | 90 | START | 90 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 144 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 54 | 12 | inferred_complete_timeline |
| `Action_None` | 55 | 75 | 21 | inferred_complete_timeline |
| `Action_Handoff` | 76 | 89 | 14 | inferred_complete_timeline |
| `Action_None` | 90 | 210 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 52 | 73 | 22 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 79 | 89 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 210 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 46 | 74 | 29 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 76 | 144 | 69 | inferred_complete_timeline |
| `Action_None` | 145 | 210 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 46 | 127 | 82 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_BallSnap` | 43 | 54 | 12 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 95 | 53 | inferred_complete_timeline |
| `Action_None` | 109 | 122 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_DownBlock` | 46 | 144 | 99 | inferred_complete_timeline |
| `Action_None` | 145 | 145 | 1 | inferred_complete_timeline |
| `Action_None` | 157 | 165 | 9 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 184 | 5 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 73 | 31 | inferred_complete_timeline |
| `Action_None` | 82 | 210 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 106 | 64 | inferred_complete_timeline |
| `Action_None` | 130 | 148 | 19 | inferred_complete_timeline |
| `Action_None` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 60 | 18 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 73 | 82 | 10 | inferred_complete_timeline |
| `Action_None` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_None` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 131 | 19 | inferred_complete_timeline |
| `Action_None` | 133 | 153 | 21 | inferred_complete_timeline |
| `Action_None` | 155 | 209 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 101 | 59 | inferred_complete_timeline |
| `Action_None` | 106 | 182 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 161 | 119 | inferred_complete_timeline |
| `Action_None` | 163 | 197 | 35 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 207 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 162 | 120 | inferred_complete_timeline |
| `Action_None` | 166 | 210 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 65–73 | 9 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 82–161 | 80 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 139–210 | 72 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 139–210 | 57 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 142–168 | 4 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 167–205 | 39 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 189–191 | 3 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 190–210 | 15 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `31` (Position_Unknown): Annotated start 46 != Inferred start 139
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '8' (LG) duration 99 frames exceeds threshold 90 frames [start=46, end=144].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (RT) duration 99 frames exceeds threshold 90 frames [start=46, end=144].
- ⚠️ Action 'Action_None' range [43-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [52-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-73] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [46-74] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [46-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [76-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-82] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-131] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-153] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-209] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-197] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [46-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 145, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [145-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-165] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-95] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-73] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-161] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '29' has 1 frames without a visible bounding box.
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