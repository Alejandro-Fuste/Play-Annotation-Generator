# Play-Annotation-Generator Annotation Review — OutRoutes_93

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_93`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `14` | `14` |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `3` | `3` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `11` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `13` | 1 | START | 1 | 1 |
| ✅ EXACT | `Action_PassBlock` | LT | `14` | `14` | 1 | START | 1 | 1 |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | `3` | `3` | 7 | START | 7 | 76 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 7 | END | 7 | 7 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 46 | START | 46 | 56 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `3` | `3` | 77 | START | 77 | 86 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `3` | `3` | 87 | START | 87 | 108 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 7 | 1 | inferred_complete_timeline |
| `Action_None` | 8 | 45 | 38 | inferred_complete_timeline |
| `Action_ThrowPass` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_None` | 57 | 180 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

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
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_RunOutRoute` | 7 | 76 | 70 | inferred_complete_timeline |
| `Action_SecureCatch` | 77 | 86 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 87 | 108 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–1
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 1 | 1 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 1 | 1 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 107 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 145 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 147 | 154 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 160 | 176 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

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
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 131 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 154 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 179 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 17–125 | 104 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 19–20 | 2 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 22–180 | 70 | 6 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 24–180 | 149 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 29–30 | 2 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 42–180 | 139 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 45–180 | 56 | 10 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 66–180 | 114 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 76–78 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 77–98 | 17 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 112–180 | 21 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 118–180 | 50 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 134–180 | 47 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 139–144 | 6 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 140–161 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 71 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-123] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-131] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [87-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '13' starts at frame 1, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [1-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [121-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [147-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [160-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [179-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '14' starts at frame 1, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [1-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-86] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-125] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-72] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-56] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-67] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-75] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-154] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-88] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-78] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-80] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-98] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-180] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-129] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-155] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-180] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-161] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>