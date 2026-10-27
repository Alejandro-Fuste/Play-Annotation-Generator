# Play-Annotation-Generator Annotation Review — Counter_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_25`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `10` | `9` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 53 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 54 | START | 54 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `7` | `6` | 68 | START | 73 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `10` | `9` | 68 | START | 68 | 127 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `9` | `8` | 68 | START | 68 | 140 |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 72 | END | 54 | 72 |
| ✅ EXACT | `Action_Handoff` | QB | `22` | `21` | 81 | START | 81 | 113 |
| ✅ EXACT | `Action_BallCarry` | RB | `13` | `12` | 114 | START | 114 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 140 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_SnapReceive` | 54 | 72 | 19 | inferred_complete_timeline |
| `Action_None` | 73 | 80 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 81 | 113 | 33 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_BallCarry` | 114 | 210 | 97 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 137 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 101 | 48 | inferred_complete_timeline |
| `Action_None` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_BallSnap` | 54 | 72 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 97 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 101 | 103 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 140 | 140 | 1 | inferred_complete_timeline |
| `Action_None` | 141 | 210 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 77 | 24 | inferred_complete_timeline |
| `Action_None` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_None` | 91 | 115 | 25 | inferred_complete_timeline |
| `Action_None` | 117 | 181 | 65 | inferred_complete_timeline |
| `Action_None` | 185 | 210 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 185 | 132 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 85 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 97 | 44 | inferred_complete_timeline |
| `Action_None` | 101 | 137 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 115 | 62 | inferred_complete_timeline |
| `Action_None` | 137 | 163 | 27 | inferred_complete_timeline |
| `Action_None` | 168 | 210 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 129 | 76 | inferred_complete_timeline |
| `Action_None` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 131 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 178 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–210 | 209 | 4 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–210 | 209 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–210 | 204 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 93–210 | 118 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 94–210 | 92 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 136–170 | 35 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 136–160 | 25 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 171–210 | 40 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 180–188 | 7 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 193–210 | 14 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 198–208 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 51: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 52: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ Row 52: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [54–72], lower_priority='Action_DownBlock' annotated_start=68, effective_Action_DownBlock_start=73.
- ⚠️ Action 'Action_None' range [54-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-137] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [73-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [101-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [124-125] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [68-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [68-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-115] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-181] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [114-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-178] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-163] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-106] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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