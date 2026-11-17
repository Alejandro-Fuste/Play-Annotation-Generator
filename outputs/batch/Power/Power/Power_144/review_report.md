# Play-Annotation-Generator Annotation Review — Power_144

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_144`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 63
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 43
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 11 | START | 11 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 11 | START | 11 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 11 | START | 11 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 11 | START | 11 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 11 | START | 11 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 11 | START | 11 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 11 | START | 11 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 11 | START | 11 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `0` | `0` | 59 | START | 59 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `9` | `9` | 59 | START | 59 | 74 |
| ✅ EXACT | `Action_PullBlock` | LG | `3` | `3` | 59 | START | 59 | 113 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 11–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 11–182
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 84 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 135 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 156 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 165 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 182 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 11–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 149 | 139 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 11–156
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 136 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 156 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 11–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 58 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 59 | 113 | 55 | inferred_complete_timeline |
| `Action_None` | 114 | 143 | 30 | inferred_complete_timeline |
| `Action_None` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 11–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 58 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 59 | 74 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 80 | 104 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 11–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 84 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 155 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 210 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 11–143
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 58 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 59 | 101 | 43 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 115 | 123 | 9 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 143 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 11–152
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 80 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 125 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 152 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 59 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 210 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 11–63
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 26 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 56 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 63 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 11–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 140 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 11–107
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 107 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 11–202
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 139 | 129 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 160 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 178 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 202 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 11–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 11–77 | 67 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 111–210 | 96 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 115–199 | 74 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 145–210 | 59 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 147–210 | 63 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 155–210 | 54 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 189–210 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 290: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_DownBlock' range [59-101] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-113] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-123] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-143] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-80] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [59-113] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-149] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-87] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-155] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-210] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-84] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-135] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [59-74] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [80-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-139] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-160] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-178] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-202] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-140] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-210] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-63] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-156] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-182] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-155] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-201] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>