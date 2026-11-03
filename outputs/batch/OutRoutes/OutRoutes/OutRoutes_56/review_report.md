# Play-Annotation-Generator Annotation Review — OutRoutes_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_56`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 52
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 36
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | LB2 | defense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | DE1 | defense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | LB2 | defense | `0` | `0` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LB2 | defense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_PassBlock` | C | `12` | `12` | 15 | START | 15 | 84 |
| ✅ EXACT | `Action_PassBlock` | RT | `5` | `5` | 15 | START | 15 | 80 |
| ✅ EXACT | `Action_PassBlock` | LG | `6` | `6` | 15 | START | 15 | 68 |
| ✅ EXACT | `Action_PassBlock` | RG | `7` | `7` | 15 | START | 15 | 77 |
| ✅ EXACT | `Action_PassBlock` | LT | `9` | `9` | 15 | START | 15 | 72 |
| ✅ EXACT | `Action_RunOutRoute` | LB2 | `0` | `0` | 20 | START | 20 | 57 |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `11` | `11` | 20 | END | 20 | 20 |
| ✅ EXACT | `Action_ThrowPass` | DE1 | `11` | `11` | 54 | START | 54 | 65 |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | LB2 | `0` | `0` | 86 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LB2 | `0` | `0` | 90 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 72 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 68 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 84 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 77 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 80 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_None` | 21 | 53 | 33 | inferred_complete_timeline |
| `Action_ThrowPass` | 54 | 65 | 12 | inferred_complete_timeline |
| `Action_None` | 66 | 76 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 150 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunOutRoute` | 20 | 57 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–65 | 66 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–68 | 63 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 67–141 | 75 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 69–79 | 11 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 69–79 | 11 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 69–83 | 15 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 69–70 | 2 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 69–76 | 8 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 72–86 | 15 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 73–85 | 13 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 74–141 | 65 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 78–150 | 73 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 78–150 | 73 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 86–93 | 7 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 90–92 | 3 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 109–150 | 42 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 120–150 | 31 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 120–150 | 31 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 122–150 | 29 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 135–150 | 16 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 135–138 | 4 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 145–147 | 3 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 145–150 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SecureCatch` on target `0` (LB2)
- ❌ Missing segment for action `Action_BallCarry` on target `0` (LB2)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 64: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureCatch' for track '0' has invalid range: start=86, end=57. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '0' has invalid range: start=90, end=57. Clamping end to start.
- ⚠️ Action 'Action_RunOutRoute' range [20-57] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-80] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-68] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-77] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-64] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-76] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-141] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-90] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-92] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-150] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-150] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-138] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-150] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>