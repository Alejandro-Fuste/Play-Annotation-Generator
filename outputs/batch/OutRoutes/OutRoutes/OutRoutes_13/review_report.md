# Play-Annotation-Generator Annotation Review — OutRoutes_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_13`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 12 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `13` | `13` | 13 | START | 13 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 13 | START | 13 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 13 | START | 13 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 13 | START | 13 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `9` | 13 | START | 13 | 41 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `3` | `3` | 20 | START | 20 | 82 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 20 | END | 20 | 20 |
| ✅ EXACT | `Action_ThrowPass` | QB | `7` | `7` | 55 | START | 55 | 64 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `3` | `3` | 83 | START | 83 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `3` | `3` | 91 | START | 91 | 93 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_None` | 21 | 54 | 34 | inferred_complete_timeline |
| `Action_ThrowPass` | 55 | 64 | 10 | inferred_complete_timeline |
| `Action_None` | 65 | 210 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 52 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunOutRoute` | 20 | 82 | 63 | inferred_complete_timeline |
| `Action_SecureCatch` | 83 | 90 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 93 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 95 | 109 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 114 | 117 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 163 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 210 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 41 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 49 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 87 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 210 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 125 | 113 | inferred_complete_timeline |
| `Action_PassBlock` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 127 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 65 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 114 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 181 | 188 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 201 | 208 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 133 | 121 | inferred_complete_timeline |
| `Action_PassBlock` | 138 | 199 | 62 | inferred_complete_timeline |
| `Action_PassBlock` | 202 | 210 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 210 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 164 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 172 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

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
<summary>CB1 — actor_track_id `6`</summary>

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
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 119 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `27` | Position_Unknown | Team_Unknown | 85–205 | 99 | 7 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 88–210 | 54 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 107–109 | 3 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 116–118 | 3 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 143–178 | 36 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 147–210 | 64 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 162–208 | 41 | 4 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 177–178 | 2 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 192–196 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (7 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 20: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-144] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-163] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-119] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [95-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [114-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-41] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-49] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-58] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-125] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [146-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-127] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-65] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [116-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [181-188] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [201-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-133] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [138-199] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [202-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-136] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-205] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-173] for track '23' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-210] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-118] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-178] for track '26' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-171] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-196] for track '30' has 1 frames without a visible bounding box.
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

</details>