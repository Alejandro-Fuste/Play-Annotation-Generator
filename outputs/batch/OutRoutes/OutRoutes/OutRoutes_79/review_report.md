# Play-Annotation-Generator Annotation Review — OutRoutes_79

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_79`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 139
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 22 | START | 22 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR2 | `1` | `1` | 27 | START | 27 | 48 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 27 | END | 27 | 27 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 60 | START | 60 | 67 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `1` | `1` | 91 | START | 91 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `1` | `1` | 97 | START | 97 | 162 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_None` | 28 | 59 | 32 | inferred_complete_timeline |
| `Action_ThrowPass` | 60 | 67 | 8 | inferred_complete_timeline |
| `Action_None` | 68 | 76 | 9 | inferred_complete_timeline |
| `Action_None` | 90 | 101 | 12 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 119 | 140 | 22 | inferred_complete_timeline |
| `Action_None` | 146 | 167 | 22 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 179 | 7 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 54 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 202 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 208 | 2 | inferred_complete_timeline |

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
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunOutRoute` | 27 | 48 | 22 | inferred_complete_timeline |
| `Action_RunOutRoute` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_RunOutRoute` | 59 | 90 | 32 | inferred_complete_timeline |
| `Action_SecureCatch` | 91 | 96 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 162 | 66 | inferred_complete_timeline |
| `Action_BallCarry` | 165 | 195 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 197 | 209 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 79 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 104 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 112 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 27 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 36 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 210 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 102 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 42 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 77 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 102 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 197 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 210 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

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
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–210 | 211 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 3–210 | 172 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 33–40 | 8 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 47–201 | 123 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 53–209 | 130 | 6 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 56–209 | 146 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 57–98 | 24 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 69–74 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 73–100 | 12 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 91–210 | 97 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 93–99 | 6 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 120–122 | 3 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 120–201 | 75 | 5 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 133–210 | 78 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 145–210 | 66 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 148–210 | 63 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 159–210 | 52 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 174–181 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunOutRoute` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 86: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [27-48] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [52-54] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [59-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [165-195] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [197-209] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-79] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-104] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-42] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-56] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-77] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-197] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-167] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-54] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-113] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-202] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-210] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-40] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-108] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-201] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-59] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-203] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-209] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-76] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-74] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-100] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-100] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-96] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-122] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-123] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-163] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-174] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-201] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-210] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-210] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-181] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>