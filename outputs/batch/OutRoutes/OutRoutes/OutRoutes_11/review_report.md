# Play-Annotation-Generator Annotation Review — OutRoutes_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_11`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `13` | `13` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `18` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 5 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 6 | START | 6 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `19` | `19` | 6 | START | 6 | 94 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 6 | START | 6 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 6 | START | 6 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `7` | `7` | 6 | START | 6 | 82 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `0` | `0` | 10 | START | 10 | 97 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `13` | `13` | 10 | END | 10 | 10 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `13` | `13` | 64 | START | 64 | 72 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `0` | `0` | 98 | START | 98 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `0` | `0` | 107 | START | 107 | 149 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 112 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 125 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 151 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_RunOutRoute` | 10 | 97 | 88 | inferred_complete_timeline |
| `Action_SecureCatch` | 98 | 106 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 149 | 43 | inferred_complete_timeline |
| `Action_BallCarry` | 156 | 161 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 47 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 180 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 94 | 89 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 108 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 128 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 141 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 147 | 148 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 43 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 70 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 86 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 112 | 119 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 138 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–30
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 21 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 30 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 53 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 82 | 77 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 94 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 109 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 112 | 120 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 141 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 149 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 141 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 149 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 157 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 180 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 76 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 176 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 164 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 180 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 151 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 165 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 43 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 58 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 70 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 89 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 104 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 180 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–180 | 181 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 61–180 | 116 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 66–68 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 76–135 | 47 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 76–77 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 86–180 | 95 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 88–179 | 68 | 8 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 92–149 | 53 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 117–176 | 34 | 4 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 120–180 | 61 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 149–180 | 31 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 174–180 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (7 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 104 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 18: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_BallCarry' range [107-149] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [156-161] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-112] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-125] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-151] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-62] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-70] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-104] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-165] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-94] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-109] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [112-120] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [126-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-141] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [143-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-47] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-43] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-180] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-141] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-157] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-21] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-30] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-94] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-128] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [143-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [147-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-70] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-86] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [112-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [123-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-94] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-180] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-99] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-92] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-104] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-113] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-121] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-139] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-158] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-179] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-125] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-141] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-123] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-130] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-156] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-176] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-180] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-180] for track '33' has 1 frames without a visible bounding box.
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