# Play-Annotation-Generator Annotation Review — OutRoutes_149

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_149`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 49
- **Validation Warnings:** 47
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
- **Inferred Coverage Segments (Action_None):** 30
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `4` | `4` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 12 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `13` | 8 | START | 8 | 37 |
| ✅ EXACT | `Action_PassBlock` | RT | `15` | `15` | 8 | START | 8 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 8 | START | 8 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 8 | START | 8 | 28 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `4` | `4` | 13 | START | 13 | 81 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 13 | END | 13 | 13 |
| ✅ EXACT | `Action_ThrowPass` | RB | `6` | `6` | 50 | START | 50 | 60 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `4` | `4` | 82 | START | 82 | 95 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `4` | `4` | 96 | START | 96 | 120 |

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
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 13 | 13 | 1 | inferred_complete_timeline |
| `Action_None` | 14 | 31 | 18 | inferred_complete_timeline |
| `Action_None` | 33 | 120 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ThrowPass` | 50 | 60 | 11 | inferred_complete_timeline |
| `Action_None` | 61 | 120 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_RunOutRoute` | 13 | 81 | 69 | inferred_complete_timeline |
| `Action_SecureCatch` | 82 | 95 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 96 | 120 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 16 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 37 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 48 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 120 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 28 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 61 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 120 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 37 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 47 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 120 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 120 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 120 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 120 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 120 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 91 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 120 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
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
| `8` | `8` | Position_Unknown | Team_Unknown | 0–120 | 121 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 60–61 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 68–69 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 3 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 3 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 6 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 154: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [96-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-31] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-120] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-47] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-16] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-37] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-48] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-120] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.

</details>