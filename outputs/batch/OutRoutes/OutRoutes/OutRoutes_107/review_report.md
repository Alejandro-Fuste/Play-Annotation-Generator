# Play-Annotation-Generator Annotation Review — OutRoutes_107

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_107`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 57
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 37
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `18` | `18` | 21 | START | 21 | 91 |
| ✅ EXACT | `Action_PassBlock` | RT | `19` | `19` | 21 | START | 21 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 21 | START | 21 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `9` | 21 | START | 21 | 53 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `1` | `1` | 26 | START | 26 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 26 | END | 26 | 26 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 63 | START | 63 | 72 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `1` | `1` | 99 | START | 99 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `1` | `1` | 106 | START | 106 | 154 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 26 | 1 | inferred_complete_timeline |
| `Action_None` | 27 | 62 | 36 | inferred_complete_timeline |
| `Action_ThrowPass` | 63 | 72 | 10 | inferred_complete_timeline |
| `Action_None` | 73 | 101 | 29 | inferred_complete_timeline |
| `Action_None` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_None` | 118 | 168 | 51 | inferred_complete_timeline |
| `Action_None` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_None` | 175 | 178 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
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
- **Visible Frames:** 0–161
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_RunOutRoute` | 26 | 98 | 73 | inferred_complete_timeline |
| `Action_SecureCatch` | 99 | 105 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 154 | 49 | inferred_complete_timeline |
| `Action_BallCarry` | 158 | 161 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 180 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 53 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 82 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 180 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 41 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 91 | 71 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 115 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 120 | 180 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 98 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 72 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 80 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 180 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
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
- **Visible Frames:** 0–174
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 174 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

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
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
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
| `10` | `10` | Position_Unknown | Team_Unknown | 0–180 | 180 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 66–180 | 115 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 121–180 | 60 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 136–180 | 45 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 146–180 | 35 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 166–180 | 15 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 114: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [158-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-174] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [63-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [120-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-27] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>