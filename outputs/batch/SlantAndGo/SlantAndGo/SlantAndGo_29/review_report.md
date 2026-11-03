# Play-Annotation-Generator Annotation Review — SlantAndGo_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_29`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_SellRoute` | WR3 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 19 | START | 19 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `12` | `12` | 22 | START | 22 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 22 | START | 36 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 22 | START | 22 | 115 |
| ✅ EXACT | `Action_PassBlock` | RG | `9` | `9` | 22 | START | 22 | 197 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 35 | END | 19 | 35 |
| ✅ EXACT | `Action_SellRoute` | WR3 | `1` | `1` | 48 | START | 48 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR3 | `1` | `1` | 77 | START | 77 | 161 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 96 | START | 96 | 102 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 35 | 17 | inferred_complete_timeline |
| `Action_None` | 36 | 95 | 60 | inferred_complete_timeline |
| `Action_ThrowPass` | 96 | 102 | 7 | inferred_complete_timeline |
| `Action_None` | 103 | 179 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 91 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SellRoute` | 48 | 76 | 29 | inferred_complete_timeline |
| `Action_VerticalStem` | 77 | 161 | 85 | inferred_complete_timeline |
| `Action_VerticalStem` | 163 | 166 | 4 | inferred_complete_timeline |
| `Action_VerticalStem` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_VerticalStem` | 173 | 194 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 101 | 80 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 122 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 115 | 94 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 204 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 35 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 36 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 47 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 97 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 105 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 114 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 197 | 176 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 42 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 66 | 48 | inferred_complete_timeline |
| `Action_None` | 69 | 114 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 49 | 31 | inferred_complete_timeline |
| `Action_None` | 51 | 166 | 116 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 190 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 81 | 63 | inferred_complete_timeline |
| `Action_None` | 83 | 90 | 8 | inferred_complete_timeline |
| `Action_None` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 62–210 | 147 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 105–144 | 27 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 125–210 | 86 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 127–210 | 83 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 127–201 | 75 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 155–206 | 47 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `1` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 42: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 42: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ Row 42: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 42: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ Row 42: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [19–35], lower_priority='Action_PassBlock' annotated_start=22, effective_Action_PassBlock_start=36.
- ⚠️ Action 'Action_None' range [19-190] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [77-161] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [163-166] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [169-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [173-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-49] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-81] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-90] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-66] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-114] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-122] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-42] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '20' starts at frame 36, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [36-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-47] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-66] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-97] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-105] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-115] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-152] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-201] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-206] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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