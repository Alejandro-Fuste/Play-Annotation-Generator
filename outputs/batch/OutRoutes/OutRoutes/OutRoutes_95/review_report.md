# Play-Annotation-Generator Annotation Review — OutRoutes_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_95`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 59
- **Validation Warnings:** 63
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 39
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `4` | `4` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 134 |
| ✅ EXACT | `Action_PassBlock` | LT | `14` | `14` | 23 | START | 23 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `16` | `16` | 23 | START | 23 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 23 | START | 23 | 81 |
| ✅ EXACT | `Action_PassBlock` | RG | `18` | `18` | 23 | START | 23 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 23 | START | 23 | 31 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `4` | `4` | 29 | START | 29 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 29 | END | 29 | 29 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 64 | START | 64 | 73 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `4` | `4` | 99 | START | 99 | 106 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `4` | `4` | 107 | START | 107 | 167 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 29 | 1 | inferred_complete_timeline |
| `Action_None` | 30 | 63 | 34 | inferred_complete_timeline |
| `Action_ThrowPass` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_None` | 74 | 142 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_RunOutRoute` | 29 | 98 | 70 | inferred_complete_timeline |
| `Action_SecureCatch` | 99 | 106 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 167 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 165 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 31 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 41 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 88 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 102 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 134 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 81 | 59 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 94 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 103 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 171 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 88 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 74 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 137 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 88 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 111 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 137 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 24–146 | 123 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 44–84 | 26 | 7 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 81–139 | 59 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 88–167 | 80 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 102–112 | 6 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 103–159 | 57 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 145–147 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 47 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-167] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-88] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-74] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-81] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-94] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-88] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-31] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-88] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-134] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-46] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-50] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-63] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-72] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-78] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-84] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-139] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-105] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-159] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '27' has 1 frames without a visible bounding box.
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

</details>