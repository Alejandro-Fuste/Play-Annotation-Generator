# Play-Annotation-Generator Annotation Review — OutRoutes_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_77`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | Position_Unknown | Team_Unknown | `1` | `1` |
| ✅ EXACT | `Action_RunOutRoute` | WR4 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_SecureCatch` | WR4 | offense | `2` | `2` |
| ✅ EXACT | `Action_BallCarry` | WR4 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `0` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 25 | START | 25 | 34 |
| ✅ EXACT | `Action_PassBlock` | RG | `18` | `18` | 25 | START | 25 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 25 | START | 25 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 25 | START | 25 | 54 |
| ✅ EXACT | `Action_RunOutRoute` | Position_Unknown | `1` | `1` | 30 | START | 30 | 210 |
| ✅ EXACT | `Action_RunOutRoute` | WR4 | `2` | `2` | 30 | START | 30 | 111 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 30 | END | 30 | 30 |
| ✅ EXACT | `Action_ThrowPass` | QB | `10` | `10` | 70 | START | 70 | 79 |
| ✅ EXACT | `Action_SecureCatch` | WR4 | `2` | `2` | 112 | START | 112 | 122 |
| ✅ EXACT | `Action_BallCarry` | WR4 | `2` | `2` | 123 | START | 123 | 200 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_SnapReceive` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_None` | 31 | 69 | 39 | inferred_complete_timeline |
| `Action_ThrowPass` | 70 | 79 | 10 | inferred_complete_timeline |
| `Action_None` | 80 | 109 | 30 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 210 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_RunOutRoute` | 30 | 111 | 82 | inferred_complete_timeline |
| `Action_SecureCatch` | 112 | 122 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 123 | 200 | 78 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 48 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 62 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 54 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 99 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 34 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 72 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 210 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 210 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 112 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 66 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 74 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 210 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 110 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 207 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 168 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 182 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 210 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 153 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 210 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 200 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–210 | 186 | 4 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–135 | 122 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 60–61 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 60–210 | 145 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 98–210 | 104 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 99–135 | 12 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 114–120 | 7 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 117–205 | 86 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 117–122 | 6 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 141–208 | 63 | 4 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 148–164 | 10 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 167–209 | 29 | 6 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 180–197 | 10 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 194–201 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 84: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 84: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 84: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [30-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-200] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-207] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-181] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-91] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-111] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-110] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-109] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-135] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-168] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-66] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-48] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-51] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-54] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-67] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-99] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-96] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-108] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-110] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-135] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-164] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-122] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-180] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-185] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-208] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-164] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-191] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-195] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-209] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-181] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-189] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-197] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-197] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-201] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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