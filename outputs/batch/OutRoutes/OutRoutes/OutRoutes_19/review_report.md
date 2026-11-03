# Play-Annotation-Generator Annotation Review — OutRoutes_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_19`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `3` | `3` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `0` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `14` | 1 | START | 1 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 1 | START | 1 | 66 |
| ✅ EXACT | `Action_PassBlock` | RT | `2` | `2` | 1 | START | 1 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 1 | START | 1 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 1 | START | 1 | 95 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `3` | `3` | 3 | START | 3 | 72 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 3 | END | 3 | 3 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 46 | START | 46 | 51 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `3` | `3` | 73 | START | 73 | 77 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `3` | `3` | 78 | START | 78 | 120 |

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
- **Visible Frames:** 0–100
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 3 | 1 | inferred_complete_timeline |
| `Action_None` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_ThrowPass` | 46 | 51 | 6 | inferred_complete_timeline |
| `Action_None` | 52 | 81 | 30 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 100 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_RunOutRoute` | 3 | 72 | 70 | inferred_complete_timeline |
| `Action_SecureCatch` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 78 | 120 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 120 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 1 | 48 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 79 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 102 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 106 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 1 | 38 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 54 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 1 | 95 | 95 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 120 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 1 | 66 | 66 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 82 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 120 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 1 | 106 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 120 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 107 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 120 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 108 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 93 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 120 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 80 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 91 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 120 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 32–33 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 38–120 | 6 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 64–83 | 8 | 3 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 64–99 | 16 | 3 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 65–66 | 2 | 1 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 71–77 | 6 | 2 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 73–74 | 2 | 1 | Undefined position; Undefined team |
| `29` | `29` | Position_Unknown | Team_Unknown | 73–74 | 2 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 86–98 | 11 | 3 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 89–120 | 27 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 93–112 | 14 | 3 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 95–107 | 4 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 97–107 | 11 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 102–120 | 17 | 2 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 26: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [1-106] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [78-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-120] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-54] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-108] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-66] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [1-48] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-102] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-81] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-100] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-120] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-107] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [1-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-120] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [1-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [1-95] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-120] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-83] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-94] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-99] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-77] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-87] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-91] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-98] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-112] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-120] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-97] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-103] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-112] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-107] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-107] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-110] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-120] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>