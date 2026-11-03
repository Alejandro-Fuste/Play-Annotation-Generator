# Play-Annotation-Generator Annotation Review — OutRoutes_121

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_121`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 64
- **Validation Warnings:** 61
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
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | TE | offense | `16` | `16` |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `17` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `11` | `11` | 16 | START | 16 | 97 |
| ✅ EXACT | `Action_PassBlock` | C | `13` | `13` | 16 | START | 16 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 16 | START | 16 | 97 |
| ✅ EXACT | `Action_PassBlock` | RT | `21` | `21` | 16 | START | 16 | 210 |
| ✅ EXACT | `Action_RunOutRoute` | TE | `16` | `16` | 21 | START | 21 | 210 |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | `3` | `3` | 21 | START | 21 | 91 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 21 | END | 21 | 21 |
| ✅ EXACT | `Action_ThrowPass` | QB | `10` | `10` | 59 | START | 59 | 71 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `3` | `3` | 92 | START | 92 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `3` | `3` | 102 | START | 102 | 125 |

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
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_None` | 22 | 58 | 37 | inferred_complete_timeline |
| `Action_ThrowPass` | 59 | 71 | 13 | inferred_complete_timeline |
| `Action_None` | 72 | 98 | 27 | inferred_complete_timeline |
| `Action_None` | 100 | 210 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

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
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunOutRoute` | 21 | 91 | 71 | inferred_complete_timeline |
| `Action_SecureCatch` | 92 | 101 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 125 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 134 | 169 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 185 | 192 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 200 | 202 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunOutRoute` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 97 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 124 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 134 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 139 | 210 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 46 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 97 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 203 | 104 | inferred_complete_timeline |
| `Action_PassBlock` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 210 | 195 | inferred_complete_timeline |

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
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 98 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 210 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 99 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 210 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 64 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 64 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 98 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 203 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 209 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

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
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 210 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 210 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 82 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 210 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–210 | 206 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 87–210 | 123 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 102–209 | 101 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 3 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 3 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 6 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 128: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-99] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [134-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [185-192] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [200-202] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-82] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-98] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-97] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-124] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [128-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [139-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-98] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [21-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-64] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [205-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.

</details>