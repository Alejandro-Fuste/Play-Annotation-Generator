# Play-Annotation-Generator Annotation Review — Counter_280

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_280`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `3` | `2` |
| ⚠️ START CHANGED | `Action_PullBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | LG | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 66 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 64 | START | 64 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `10` | `9` | 67 | START | 67 | 88 |
| ✅ EXACT | `Action_DownBlock` | RT | `3` | `2` | 67 | START | 67 | 115 |
| ⚠️ START CHANGED | `Action_PullBlock` | C | `12` | `11` | 67 | START | 84 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `9` | `8` | 67 | START | 67 | 108 |
| ✅ EXACT | `Action_SnapReceive` | LG | `15` | `14` | 83 | END | 64 | 83 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 97 | START | 97 | 109 |
| ✅ EXACT | `Action_BallCarry` | RB | `8` | `7` | 114 | START | 114 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 169 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_Handoff` | 97 | 109 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_BallCarry` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 67 | 108 | 42 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 111 | 169 | 59 | inferred_complete_timeline |
| `Action_None` | 170 | 239 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 83 | 20 | inferred_complete_timeline |
| `Action_None` | 84 | 239 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 64 | 83 | 20 | inferred_complete_timeline |
| `Action_PullBlock` | 84 | 169 | 86 | inferred_complete_timeline |
| `Action_None` | 170 | 233 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_DownBlock` | 67 | 88 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 169 | 77 | inferred_complete_timeline |
| `Action_None` | 170 | 239 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_DownBlock` | 67 | 115 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 63 | 36 | inferred_complete_timeline |
| `Action_None` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 123 | 29 | inferred_complete_timeline |
| `Action_None` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_None` | 154 | 239 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 85 | 22 | inferred_complete_timeline |
| `Action_None` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_None` | 101 | 119 | 19 | inferred_complete_timeline |
| `Action_None` | 127 | 236 | 110 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 111 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 63 | 8 | inferred_complete_timeline |
| `Action_None` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 227 | 164 | inferred_complete_timeline |
| `Action_None` | 229 | 236 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 99 | 36 | inferred_complete_timeline |
| `Action_None` | 111 | 153 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–239 | 211 | 6 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 10–85 | 74 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 97–229 | 127 | 4 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 113–239 | 127 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 115–165 | 51 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 123–239 | 112 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 140–239 | 100 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 148–193 | 12 | 3 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 155–212 | 58 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 158–239 | 82 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 160–239 | 80 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 169–207 | 4 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 169–179 | 11 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 182–239 | 58 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 209–239 | 31 | 1 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 217–239 | 23 | 1 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 224–235 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `12` (C): Annotated start 67 != Inferred start 84
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 562: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (RG) duration 103 frames exceeds threshold 90 frames [start=67, end=169].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '11' (C) duration 103 frames exceeds threshold 90 frames [start=67, end=169].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [64–83], lower_priority='Action_PullBlock' annotated_start=67, effective_Action_PullBlock_start=84.
- ⚠️ Action 'Action_None' range [64-68] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-135] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-227] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [67-115] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [97-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-111] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-227] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-236] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [114-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [67-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [67-88] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [84-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-119] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-236] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-123] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-35] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-51] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-63] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-135] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-179] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>