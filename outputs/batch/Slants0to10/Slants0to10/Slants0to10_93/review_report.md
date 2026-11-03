# Play-Annotation-Generator Annotation Review — Slants0to10_93

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_93`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `18` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 1 | START | 1 | 11 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `13` | 4 | START | 4 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 4 | START | 4 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `19` | `19` | 4 | START | 4 | 175 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `20` | `20` | 4 | START | 12 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 4 | START | 4 | 154 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `8` | `8` | 11 | START | 11 | 85 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 11 | END | 1 | 11 |
| ✅ EXACT | `Action_ThrowPass` | QB | `5` | `5` | 59 | START | 59 | 68 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `8` | `8` | 89 | START | 89 | 156 |

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
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 11 | 11 | inferred_complete_timeline |
| `Action_None` | 12 | 58 | 47 | inferred_complete_timeline |
| `Action_ThrowPass` | 59 | 68 | 10 | inferred_complete_timeline |
| `Action_None` | 69 | 140 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 11 | 85 | 75 | inferred_complete_timeline |
| `Action_None` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 89 | 156 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 183 | 183 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 175 | 172 | inferred_complete_timeline |
| `Action_PassBlock` | 177 | 188 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 29 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 121 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 134 | 139 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 174 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 11 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 136 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 154 | 151 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 160 | 176 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 183 | 190 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 112 | 109 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 136 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 138 | 206 | 69 | inferred_complete_timeline |
| `Action_PassBlock` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 47 | 47 | inferred_complete_timeline |
| `Action_None` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_None` | 59 | 210 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 39 | 39 | inferred_complete_timeline |
| `Action_None` | 51 | 126 | 76 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 142 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 71 | 71 | inferred_complete_timeline |
| `Action_None` | 77 | 82 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 84 | 84 | inferred_complete_timeline |
| `Action_None` | 87 | 210 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 168 | 168 | inferred_complete_timeline |
| `Action_None` | 175 | 210 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 53 | 53 | inferred_complete_timeline |
| `Action_None` | 58 | 61 | 4 | inferred_complete_timeline |
| `Action_None` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_None` | 69 | 130 | 62 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 204 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 155 | 155 | inferred_complete_timeline |
| `Action_None` | 157 | 173 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 91–92 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 115–138 | 16 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 148–210 | 62 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 172–210 | 37 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 180–210 | 31 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 198–210 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `20` (C): Annotated start 4 != Inferred start 12
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [1–11], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=12.
- ⚠️ Action 'Action_None' range [1-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-183] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-204] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-47] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-71] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [89-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-39] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-130] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-136] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [138-206] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [209-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-121] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [134-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [142-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [146-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [152-174] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [176-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [177-188] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-154] for track '21' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [160-176] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [183-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-127] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '27' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>