# Play-Annotation-Generator Annotation Review — Counter_250

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_250`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | CB | defense | `2` | `1` |
| ✅ EXACT | `Action_Handoff` | CB | defense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `20` | `Group` | 0 | START | 75 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 79 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 78 | START | 78 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `10` | `9` | 80 | START | 80 | 108 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `12` | `11` | 80 | START | 93 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `9` | `8` | 80 | START | 80 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `5` | `4` | 80 | START | 80 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `15` | `14` | 80 | START | 80 | 125 |
| ✅ EXACT | `Action_SnapReceive` | CB | `2` | `1` | 92 | END | 78 | 92 |
| ✅ EXACT | `Action_Handoff` | CB | `2` | `1` | 108 | START | 108 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `13` | 127 | START | 127 | 249 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 177 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_BallCarry` | 127 | 249 | 123 | inferred_complete_timeline |
| `Action_BallCarry` | 251 | 253 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 75–135
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_None` | 78 | 107 | 30 | inferred_complete_timeline |
| `Action_None` | 109 | 135 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 79 | 11 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 80 | 125 | 46 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 129 | 144 | 16 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 147 | 177 | 31 | inferred_complete_timeline |
| `Action_None` | 178 | 269 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_DownBlock` | 80 | 108 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 117 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_DownBlock` | 80 | 177 | 98 | inferred_complete_timeline |
| `Action_None` | 178 | 269 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_BallSnap` | 78 | 92 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 177 | 85 | inferred_complete_timeline |
| `Action_None` | 178 | 178 | 1 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PullBlock` | 80 | 109 | 30 | inferred_complete_timeline |
| `Action_PullBlock` | 111 | 118 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 121 | 127 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 129 | 177 | 49 | inferred_complete_timeline |
| `Action_None` | 178 | 248 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 108 | 31 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 113 | 36 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 139 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 77 | 20 | inferred_complete_timeline |
| `Action_None` | 78 | 176 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 118 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 179 | 102 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 5–244
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 11 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 77 | 64 | inferred_complete_timeline |
| `Action_None` | 78 | 244 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 117 | 40 | inferred_complete_timeline |
| `Action_None` | 119 | 127 | 9 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 149 | 8 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |
| `Action_None` | 160 | 269 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–219
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 77 | 73 | inferred_complete_timeline |
| `Action_None` | 78 | 219 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 78 | 92 | 15 | inferred_complete_timeline |
| `Action_None` | 93 | 104 | 12 | inferred_complete_timeline |
| `Action_None` | 107 | 107 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 108 | 126 | 19 | inferred_complete_timeline |
| `Action_None` | 127 | 219 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 121 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–52 | 53 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 15–119 | 70 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 76–269 | 182 | 6 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 96–257 | 157 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 124–219 | 96 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 126–177 | 48 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 126–269 | 101 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 144–269 | 126 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 164–268 | 100 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 171–173 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 178–227 | 50 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 181–269 | 57 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 211–217 | 7 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `12` (C): Annotated start 80 != Inferred start 93
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 502: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '4' (RG) duration 98 frames exceeds threshold 90 frames [start=80, end=177].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (LG) duration 98 frames exceeds threshold 90 frames [start=80, end=177].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (C) duration 98 frames exceeds threshold 90 frames [start=80, end=177].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [78–92], lower_priority='Action_DownBlock' annotated_start=80, effective_Action_DownBlock_start=93.
- ⚠️ Action 'Action_None' range [78-113] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-104] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [80-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [111-118] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [121-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-248] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [80-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-176] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 178, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [178-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [127-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [251-253] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [80-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [129-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [147-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-11] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-244] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-119] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-180] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-239] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-219] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-244] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-268] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-227] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-217] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>