# Play-Annotation-Generator Annotation Review — Counter_164

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_164`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 1
- **Action Segments:** 71
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB2 | defense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB3 | defense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF1 | defense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB2 | defense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `15` | `13` |
| ✅ EXACT | `Action_PullLeadBlock` | CB1 | defense | `12` | `11` |
| ✅ EXACT | `Action_SnapReceive` | WR1 | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | WR1 | offense | `8` | `7` |
| ⚠️ START CHANGED | `Action_BallCarry` | TE | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `22` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `25` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 108 |
| ✅ EXACT | `Action_BallSnap` | CB2 | `6` | `5` | 71 | START | 71 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB3 | `2` | `1` | 73 | START | 73 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF1 | `5` | `4` | 73 | START | 73 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | CB2 | `6` | `5` | 73 | START | 73 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `15` | `13` | 73 | START | 78 | 90 |
| ✅ EXACT | `Action_PullLeadBlock` | CB1 | `12` | `11` | 73 | START | 73 | 153 |
| ✅ EXACT | `Action_SnapReceive` | WR1 | `8` | `7` | 83 | END | 71 | 83 |
| ✅ EXACT | `Action_Handoff` | WR1 | `8` | `7` | 91 | START | 91 | 113 |
| ⚠️ START CHANGED | `Action_BallCarry` | TE | `9` | `8` | 114 | START | 115 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 153 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 109 | 39 | inferred_complete_timeline |
| `Action_None` | 138 | 210 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_SnapReceive` | 71 | 83 | 13 | inferred_complete_timeline |
| `Action_None` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 91 | 113 | 23 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 115 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 210 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_BallCarry` | 115 | 210 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 78–210
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PullBlock` | 78 | 90 | 13 | inferred_complete_timeline |
| `Action_PullBlock` | 97 | 153 | 57 | inferred_complete_timeline |
| `Action_None` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 110–157
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 110 | 125 | 16 | inferred_complete_timeline |
| `Action_None` | 149 | 157 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `25`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 129–210
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 129 | 142 | 14 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 120–210
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 120 | 137 | 18 | inferred_complete_timeline |
| `Action_None` | 139 | 151 | 13 | inferred_complete_timeline |
| `Action_None` | 163 | 210 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `24`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 128–209
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 128 | 157 | 30 | inferred_complete_timeline |
| `Action_None` | 172 | 209 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 82–210
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 82 | 210 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 106 | 36 | inferred_complete_timeline |
| `Action_None` | 110 | 116 | 7 | inferred_complete_timeline |
| `Action_None` | 118 | 129 | 12 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 73 | 153 | 81 | inferred_complete_timeline |
| `Action_None` | 154 | 197 | 44 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_BallSnap` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 85 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 87 | 104 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 102 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 106 | 153 | 48 | inferred_complete_timeline |
| `Action_None` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 106 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 210 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `18` | Position_Unknown | Team_Unknown | 105–209 | 94 | 5 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 115–125 | 9 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 131–165 | 18 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 136–149 | 13 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 138–161 | 24 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 146–210 | 60 | 4 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 159–210 | 38 | 3 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 196–209 | 14 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 197–210 | 14 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 198–203 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `12` | `14` | 33 | 53 | 2 | 9.5% | 34–52 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `15` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `9` (TE): Annotated start 114 != Inferred start 115

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 329: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Track ID '23' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [71-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [73-102] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [106-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-115] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [73-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [73-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [87-104] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-109] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [115-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-129] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [78-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-165] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-209] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-154] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-179] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>