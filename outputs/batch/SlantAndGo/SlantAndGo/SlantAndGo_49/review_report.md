# Play-Annotation-Generator Annotation Review — SlantAndGo_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_49`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `22` | `22` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_SellRoute` | WR1 | offense | `10` | `10` |
| ✅ EXACT | `Action_VerticalStem` | WR1 | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 2 | START | 2 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `15` | `15` | 5 | START | 5 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 5 | START | 5 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 5 | START | 20 | 21 |
| ✅ EXACT | `Action_PassBlock` | LG | `21` | `21` | 5 | START | 5 | 13 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `22` | `22` | 5 | START | 5 | 13 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 16 | END | 2 | 16 |
| ✅ EXACT | `Action_SellRoute` | WR1 | `10` | `10` | 33 | START | 33 | 64 |
| ✅ EXACT | `Action_VerticalStem` | WR1 | `10` | `10` | 65 | START | 65 | 150 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 85 | START | 85 | 93 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 16 | 15 | inferred_complete_timeline |
| `Action_None` | 17 | 84 | 68 | inferred_complete_timeline |
| `Action_ThrowPass` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_None` | 94 | 136 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 136 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SellRoute` | 33 | 64 | 32 | inferred_complete_timeline |
| `Action_VerticalStem` | 65 | 150 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 132 | 131 | inferred_complete_timeline |
| `Action_None` | 134 | 136 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 164 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 13 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 118 | 88 | inferred_complete_timeline |
| `Action_PassBlock` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 149 | 151 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–13
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 13 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 15 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 147 | 123 | inferred_complete_timeline |
| `Action_PassBlock` | 149 | 160 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 15 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 118 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 16 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 58 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 77 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 123 | 122 | inferred_complete_timeline |
| `Action_None` | 125 | 130 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 16 | 15 | inferred_complete_timeline |
| `Action_None` | 20 | 70 | 51 | inferred_complete_timeline |
| `Action_None` | 75 | 121 | 47 | inferred_complete_timeline |
| `Action_None` | 125 | 130 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 18 | 17 | inferred_complete_timeline |
| `Action_None` | 20 | 145 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 166 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 75 | 74 | inferred_complete_timeline |
| `Action_None` | 77 | 113 | 37 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 18 | 17 | inferred_complete_timeline |
| `Action_None` | 20 | 33 | 14 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_None` | 43 | 49 | 7 | inferred_complete_timeline |
| `Action_None` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_None` | 88 | 95 | 8 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 168 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 180 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 131 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 141 | 140 | inferred_complete_timeline |
| `Action_None` | 146 | 154 | 9 | inferred_complete_timeline |
| `Action_None` | 160 | 180 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 180 | 179 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–45 | 33 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–140 | 140 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 35–99 | 19 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 45–46 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 74–144 | 63 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 102–132 | 31 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 108–122 | 10 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 112–122 | 11 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 129–152 | 20 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 150–156 | 6 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 176–180 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [2–16], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=17.
- ⚠️ Action 'Action_None' range [2-164] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-168] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-15] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-34] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-45] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-166] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-18] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-33] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-49] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-83] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-131] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [65-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-70] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-121] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-16] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-58] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-119] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-15] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-118] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [2-15] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-21] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-147] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [149-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-13] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-13] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-118] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [126-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [149-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-38] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-134] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-132] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-122] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-134] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-152] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>