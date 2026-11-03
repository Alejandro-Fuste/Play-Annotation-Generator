# Play-Annotation-Generator Annotation Review — SlantAndGo_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_13`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_SellRoute` | SAF1 | defense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | SAF1 | defense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 10 | START | 10 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 13 | START | 25 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 13 | START | 13 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 13 | START | 13 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `7` | `7` | 13 | START | 13 | 80 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `4` | 24 | END | 10 | 24 |
| ✅ EXACT | `Action_SellRoute` | SAF1 | `1` | `1` | 30 | START | 30 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | SAF1 | `1` | `1` | 64 | START | 64 | 197 |
| ✅ EXACT | `Action_ThrowPass` | QB | `4` | `4` | 84 | START | 84 | 94 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 24 | 15 | inferred_complete_timeline |
| `Action_None` | 25 | 83 | 59 | inferred_complete_timeline |
| `Action_ThrowPass` | 84 | 94 | 11 | inferred_complete_timeline |
| `Action_None` | 95 | 110 | 16 | inferred_complete_timeline |
| `Action_None` | 112 | 117 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 57 | 48 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 152 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 102 | 93 | inferred_complete_timeline |
| `Action_None` | 104 | 183 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 28 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 46 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 70 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 24 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 41 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 55 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 37 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 48 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 131 | 77 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 137 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 80 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 107 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 109 | 115 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 166 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 109 | 100 | inferred_complete_timeline |
| `Action_None` | 113 | 115 | 3 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 54 | 45 | inferred_complete_timeline |
| `Action_None` | 56 | 123 | 68 | inferred_complete_timeline |
| `Action_None` | 127 | 139 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 81 | 72 | inferred_complete_timeline |
| `Action_None` | 83 | 87 | 5 | inferred_complete_timeline |
| `Action_None` | 89 | 100 | 12 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 111 | 135 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 122 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 149 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_SellRoute` | 30 | 63 | 34 | inferred_complete_timeline |
| `Action_VerticalStem` | 64 | 197 | 134 | inferred_complete_timeline |
| `Action_VerticalStem` | 199 | 291 | 93 | inferred_complete_timeline |
| `Action_VerticalStem` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 149 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–149 | 145 | 3 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–159 | 160 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–299 | 297 | 4 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–299 | 268 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–116 | 115 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 3–131 | 106 | 9 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 62–146 | 85 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 91–132 | 41 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 107–133 | 22 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 183–185 | 3 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 203–299 | 97 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 214–299 | 86 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 283–299 | 10 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 286–299 | 14 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 291–299 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (6 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 23: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 24: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ Track ID '22' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [10–24], lower_priority='Action_PassBlock' annotated_start=13, effective_Action_PassBlock_start=25.
- ⚠️ Action 'Action_None' range [10-113] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [64-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [199-291] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-75] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-57] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-92] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [109-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-149] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-152] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-109] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-139] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-100] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-135] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-97] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-113] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-55] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-37] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-28] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-70] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-7] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-40] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-83] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-100] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-132] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-124] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.

</details>