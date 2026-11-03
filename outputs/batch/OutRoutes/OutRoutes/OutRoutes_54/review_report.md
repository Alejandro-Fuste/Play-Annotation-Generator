# Play-Annotation-Generator Annotation Review — OutRoutes_54

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_54`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 48
- **Validation Warnings:** 59
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 31
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | DT1 | defense | `0` | `0` |
| ✅ EXACT | `Action_RunOutRoute` | DE2 | defense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_SecureCatch` | DE2 | defense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE2 | defense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `2` | `2` | 17 | START | 17 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `3` | `3` | 17 | START | 17 | 35 |
| ✅ EXACT | `Action_PassBlock` | LG | `4` | `4` | 17 | START | 17 | 76 |
| ✅ EXACT | `Action_PassBlock` | LT | `8` | `8` | 17 | START | 17 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `9` | `9` | 17 | START | 17 | 72 |
| ✅ EXACT | `Action_RunOutRoute` | DT1 | `0` | `0` | 20 | START | 20 | 72 |
| ✅ EXACT | `Action_RunOutRoute` | DE2 | `6` | `6` | 20 | START | 20 | 82 |
| ✅ EXACT | `Action_SnapReceive` | LT | `8` | `8` | 20 | END | 20 | 20 |
| ✅ EXACT | `Action_ThrowPass` | LT | `8` | `8` | 51 | START | 51 | 60 |
| ✅ EXACT | `Action_SecureCatch` | DE2 | `6` | `6` | 83 | START | 83 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE2 | `6` | `6` | 92 | START | 92 | 145 |

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
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 19 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_None` | 21 | 50 | 30 | inferred_complete_timeline |
| `Action_ThrowPass` | 51 | 60 | 10 | inferred_complete_timeline |
| `Action_None` | 61 | 75 | 15 | inferred_complete_timeline |
| `Action_None` | 77 | 81 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 76 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 48 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 69 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 82 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 72 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 87 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 35 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 93 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunOutRoute` | 20 | 82 | 63 | inferred_complete_timeline |
| `Action_SecureCatch` | 83 | 91 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 92 | 145 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunOutRoute` | 20 | 72 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 19–58 | 35 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 24–67 | 44 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 32–149 | 114 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 78–146 | 69 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 80–150 | 71 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 89–150 | 62 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 90–150 | 61 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 104–134 | 31 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 125–133 | 9 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 136–145 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 35 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_RunOutRoute' range [20-72] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-48] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-69] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-82] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-35] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [92-145] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [149-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-75] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-26] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-42] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-143] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-150] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-145] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>