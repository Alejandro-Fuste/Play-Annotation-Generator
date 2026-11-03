# Play-Annotation-Generator Annotation Review — OutRoutes_143

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_143`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `7` | `Group` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | WR3 | offense | `17` | `17` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `17` | `17` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `17` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `7` | `Group` | 0 | START | 0 | 67 |
| ✅ EXACT | `Action_PassBlock` | LT | `10` | `10` | 3 | START | 3 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 3 | START | 3 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 3 | START | 3 | 148 |
| ✅ EXACT | `Action_PassBlock` | C | `20` | `20` | 3 | START | 3 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 3 | START | 3 | 47 |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | `17` | `17` | 7 | START | 7 | 65 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 7 | END | 7 | 7 |
| ✅ EXACT | `Action_ThrowPass` | WR3 | `17` | `17` | 66 | START | 66 | 74 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `17` | `17` | 92 | START | 92 | 102 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `17` | `17` | 103 | START | 103 | 103 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 7 | 1 | inferred_complete_timeline |
| `Action_None` | 8 | 67 | 60 | inferred_complete_timeline |
| `Action_None` | 119 | 156 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 156 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_RunOutRoute` | 7 | 65 | 59 | inferred_complete_timeline |
| `Action_ThrowPass` | 66 | 74 | 9 | inferred_complete_timeline |
| `Action_None` | 75 | 91 | 17 | inferred_complete_timeline |
| `Action_SecureCatch` | 92 | 102 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 103 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 106 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 87 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 131 | 129 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 163 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 152 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 47 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 148 | 146 | inferred_complete_timeline |
| `Action_PassBlock` | 150 | 180 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 148 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 116 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 78 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 118 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 127 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 146 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 152 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 165 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 180 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
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
| `11` | `11` | Position_Unknown | Team_Unknown | 0–180 | 181 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 39–180 | 142 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 64–180 | 117 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 66–153 | 83 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 82–117 | 35 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 88–154 | 12 | 4 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 104–127 | 5 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 111–123 | 13 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 128–159 | 27 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 142–145 | 4 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 144–175 | 31 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 146–151 | 6 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 148: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-116] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-106] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [7-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '17' starts at frame 103, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [103-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-131] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-163] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [150-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-100] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-125] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-131] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-153] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-103] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-102] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-106] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-123] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-131] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-159] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-145] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-146] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-175] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-151] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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