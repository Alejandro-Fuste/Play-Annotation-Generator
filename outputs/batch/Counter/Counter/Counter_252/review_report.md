# Play-Annotation-Generator Annotation Review — Counter_252

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_252`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 45 | START | 45 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `10` | `9` | 48 | START | 48 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 48 | START | 68 | 72 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `2` | `1` | 48 | START | 48 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `7` | `6` | 48 | START | 48 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `3` | `2` | 48 | START | 48 | 85 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 60 | END | 45 | 60 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 70 | START | 70 | 93 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `4` | 94 | START | 94 | 187 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 120 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 60 | 16 | inferred_complete_timeline |
| `Action_None` | 61 | 69 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 70 | 93 | 24 | inferred_complete_timeline |
| `Action_None` | 94 | 192 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 187 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 56 | 12 | inferred_complete_timeline |
| `Action_None` | 61 | 113 | 53 | inferred_complete_timeline |
| `Action_None` | 121 | 129 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 48 | 67 | 20 | inferred_complete_timeline |
| `Action_PullBlock` | 75 | 100 | 26 | inferred_complete_timeline |
| `Action_PullBlock` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 117 | 120 | 4 | inferred_complete_timeline |
| `Action_None` | 121 | 149 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_BallSnap` | 45 | 59 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 68 | 72 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 120 | 22 | inferred_complete_timeline |
| `Action_None` | 121 | 210 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 48 | 69 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 77 | 106 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 139 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 86 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 51 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 55 | 11 | inferred_complete_timeline |
| `Action_None` | 106 | 110 | 5 | inferred_complete_timeline |
| `Action_None` | 120 | 210 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 44 | 39 | inferred_complete_timeline |
| `Action_None` | 45 | 61 | 17 | inferred_complete_timeline |
| `Action_None` | 64 | 88 | 25 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 204 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 63 | 19 | inferred_complete_timeline |
| `Action_None` | 67 | 82 | 16 | inferred_complete_timeline |
| `Action_None` | 85 | 136 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

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
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–77 | 78 | 2 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–210 | 199 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 51–192 | 85 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 55–157 | 97 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 64–86 | 16 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 65–97 | 33 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 114–161 | 48 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 122–210 | 89 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 125–150 | 26 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 129–205 | 71 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 176–183 | 8 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 206–210 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [45–60], lower_priority='Action_DownBlock' annotated_start=48, effective_Action_DownBlock_start=61.
- ⚠️ Action 'Action_None' range [45-56] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-113] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [48-77] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [48-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-187] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-86] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [48-67] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [75-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [113-114] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-63] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-82] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-136] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [48-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [74-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [77-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [45-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [68-72] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [84-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [89-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-192] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-55] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-88] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-150] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-199] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.

</details>