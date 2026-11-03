# Play-Annotation-Generator Annotation Review — OutRoutes_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_73`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 10 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 11 | START | 11 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 11 | START | 11 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 11 | START | 11 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 11 | START | 11 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `9` | 11 | START | 11 | 39 |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | `1` | `1` | 16 | START | 16 | 93 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 16 | END | 16 | 16 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 54 | START | 54 | 68 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `1` | `1` | 94 | START | 94 | 99 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `1` | `1` | 100 | START | 100 | 180 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 16 | 1 | inferred_complete_timeline |
| `Action_None` | 17 | 53 | 37 | inferred_complete_timeline |
| `Action_ThrowPass` | 54 | 68 | 15 | inferred_complete_timeline |
| `Action_None` | 69 | 73 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 180 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

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
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunOutRoute` | 16 | 93 | 78 | inferred_complete_timeline |
| `Action_SecureCatch` | 94 | 99 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 180 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

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
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 49 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 69 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 40 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 65 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 109 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 123 | 131 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 140 | 143 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 38 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 48 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 67 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 94 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 64 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 93 | 94 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 39 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 69 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 143 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 180 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 60 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 119 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

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
<summary>CB3 — actor_track_id `14`</summary>

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
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
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
| `5` | `5` | Position_Unknown | Team_Unknown | 0–118 | 99 | 8 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 105–109 | 4 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 105–180 | 76 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 128–180 | 39 | 5 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 142–165 | 24 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 147–180 | 34 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 154–180 | 18 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 155–180 | 26 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (9 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 80: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-143] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-81] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-114] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-39] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-69] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-180] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-40] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-109] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [123-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [140-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-49] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-69] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-69] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [93-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-38] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-42] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-67] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-139] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-166] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-180] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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