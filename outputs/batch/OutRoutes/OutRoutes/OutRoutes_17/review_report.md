# Play-Annotation-Generator Annotation Review — OutRoutes_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_17`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 49
- **Validation Warnings:** 49
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
- **Inferred Coverage Segments (Action_None):** 28
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | TE | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_SecureCatch` | TE | offense | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | TE | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_PassBlock` | RG | `18` | `18` | 26 | START | 26 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 26 | START | 26 | 60 |
| ✅ EXACT | `Action_PassBlock` | LT | `21` | `21` | 26 | START | 26 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `7` | `7` | 26 | START | 26 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `9` | 26 | START | 26 | 63 |
| ✅ EXACT | `Action_RunOutRoute` | TE | `8` | `8` | 33 | START | 33 | 115 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 33 | END | 33 | 33 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 87 | START | 87 | 95 |
| ✅ EXACT | `Action_SecureCatch` | TE | `8` | `8` | 116 | START | 116 | 123 |
| ✅ EXACT | `Action_BallCarry` | TE | `8` | `8` | 124 | START | 124 | 180 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_None` | 34 | 86 | 53 | inferred_complete_timeline |
| `Action_ThrowPass` | 87 | 95 | 9 | inferred_complete_timeline |
| `Action_None` | 96 | 161 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

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
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_RunOutRoute` | 33 | 115 | 83 | inferred_complete_timeline |
| `Action_SecureCatch` | 116 | 123 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 124 | 180 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 143 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 60 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 67 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 130 | 105 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 180 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 84 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 63 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 90 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 117 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 120 | 162 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

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
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 179 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 180 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

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
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 180 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
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
| `22` | `25` | Position_Unknown | Team_Unknown | 75–79 | 5 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 103–176 | 74 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 140–144 | 5 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 151–174 | 24 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 169–176 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 37 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-180] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-130] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [143-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [124-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-117] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [120-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-178] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-180] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-60] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-67] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-161] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-176] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-144] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-174] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-176] for track '26' has 1 frames without a visible bounding box.
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

</details>