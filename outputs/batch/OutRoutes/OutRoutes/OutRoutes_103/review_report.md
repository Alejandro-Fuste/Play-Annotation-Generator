# Play-Annotation-Generator Annotation Review — OutRoutes_103

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_103`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `22` | `22` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `13` | `13` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `10` | `10` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_PassBlock` | LT | `18` | `18` | 13 | START | 13 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 13 | START | 13 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 13 | START | 13 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `22` | `22` | 13 | START | 13 | 20 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `10` | `10` | 17 | START | 17 | 92 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 17 | END | 17 | 17 |
| ✅ EXACT | `Action_ThrowPass` | RB | `13` | `13` | 60 | START | 60 | 69 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `10` | `10` | 93 | START | 93 | 101 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `10` | `10` | 102 | START | 102 | 180 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 17 | 1 | inferred_complete_timeline |
| `Action_None` | 18 | 26 | 9 | inferred_complete_timeline |
| `Action_None` | 34 | 87 | 54 | inferred_complete_timeline |
| `Action_None` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 102 | 129 | 28 | inferred_complete_timeline |
| `Action_None` | 131 | 180 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_ThrowPass` | 60 | 69 | 10 | inferred_complete_timeline |
| `Action_None` | 70 | 100 | 31 | inferred_complete_timeline |
| `Action_None` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 133 | 180 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_RunOutRoute` | 17 | 92 | 76 | inferred_complete_timeline |
| `Action_SecureCatch` | 93 | 101 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 180 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

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
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 180 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 180 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 20 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 180 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 41 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 58 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 78 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 18 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 49 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 64 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 91 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 180 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 79 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 84 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 160 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

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
| `16` | `16` | Position_Unknown | Team_Unknown | 0–72 | 52 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–45 | 46 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 2–40 | 18 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 15–52 | 6 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 23–180 | 119 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 51–54 | 4 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 69–180 | 112 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 73–77 | 5 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 82–83 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 95–106 | 11 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 98–180 | 83 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 110–180 | 54 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 116–129 | 10 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 121–180 | 59 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 132–135 | 4 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 132–180 | 30 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 161–180 | 18 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 110: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-160] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-180] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-180] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-72] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-26] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-87] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-129] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-18] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-91] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-58] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-20] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-180] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-10] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-28] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-40] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-17] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-52] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-27] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-49] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-57] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-180] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-54] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-77] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-99] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-106] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-123] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-122] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-164] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-135] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-135] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-173] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-180] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-165] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-180] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>