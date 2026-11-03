# Play-Annotation-Generator Annotation Review — Slants0to10_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_61`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `17` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `21` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_PassBlock` | LT | `16` | `16` | 7 | START | 7 | 210 |
| ✅ EXACT | `Action_PassBlock` | RG | `18` | `18` | 7 | START | 7 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 7 | START | 7 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 7 | START | 7 | 25 |
| ✅ EXACT | `Action_PassBlock` | RT | `8` | `8` | 7 | START | 7 | 207 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 7 | END | 7 | 7 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `2` | `2` | 8 | START | 8 | 58 |
| ✅ EXACT | `Action_ThrowPass` | QB | `10` | `10` | 42 | START | 42 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `2` | `2` | 75 | START | 75 | 136 |

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
- **Visible Frames:** 0–206
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 7 | 1 | inferred_complete_timeline |
| `Action_None` | 8 | 41 | 34 | inferred_complete_timeline |
| `Action_ThrowPass` | 42 | 53 | 12 | inferred_complete_timeline |
| `Action_None` | 54 | 126 | 73 | inferred_complete_timeline |
| `Action_None` | 128 | 206 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 93 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 60 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 126 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 144 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

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
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 8 | 58 | 51 | inferred_complete_timeline |
| `Action_None` | 59 | 74 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 75 | 136 | 62 | inferred_complete_timeline |
| `Action_BallCarry` | 152 | 168 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 193 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 202 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 77 | 71 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 93 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 204 | 108 | inferred_complete_timeline |
| `Action_PassBlock` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 25 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 207 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 207 | 201 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 206 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 150 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 166 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 210 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 203 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 209 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 78–210 | 133 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 114–210 | 85 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 127–128 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 145–197 | 48 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 164–174 | 6 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 168–170 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 60 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [75-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [152-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-193] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-202] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-126] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-206] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-207] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-204] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [206-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-25] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-210] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-161] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-187] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-197] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-170] for track '27' has 1 frames without a visible bounding box.
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