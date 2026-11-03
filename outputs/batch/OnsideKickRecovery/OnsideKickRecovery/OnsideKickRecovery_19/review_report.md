# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_19

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_19`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 59
- **Validation Warnings:** 88
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 4
- **Exact Matches:** 1
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ⚠️ START CHANGED | `Action_KickApproach` | Position_Unknown | Team_Unknown | `10` | `10` |
| ✅ EXACT | `Action_KickBall` | Position_Unknown | Team_Unknown | `10` | `10` |
| ⚠️ START CHANGED | `Action_AttemptRecovery` | Position_Unknown | Team_Unknown | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `14` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ⚠️ START CHANGED | `Action_KickApproach` | Position_Unknown | `10` | `10` | 4 | START | 66 | 70 |
| ✅ EXACT | `Action_KickBall` | Position_Unknown | `10` | `10` | 71 | START | 71 | 74 |
| ⚠️ START CHANGED | `Action_AttemptRecovery` | Position_Unknown | `14` | `13` | 133 | START | 135 | 136 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Position_Unknown | `14` | `13` | 147 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

*(No offensive player tracks)*

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 124 | 121 | inferred_complete_timeline |
| `Action_None` | 126 | 150 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 65 | 62 | inferred_complete_timeline |
| `Action_None` | 89 | 96 | 8 | inferred_complete_timeline |
| `Action_None` | 99 | 149 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 89 | 86 | inferred_complete_timeline |
| `Action_None` | 92 | 96 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 112 | 15 | inferred_complete_timeline |
| `Action_None` | 114 | 122 | 9 | inferred_complete_timeline |
| `Action_None` | 124 | 130 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 102 | 99 | inferred_complete_timeline |
| `Action_None` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_None` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 150 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 96 | 93 | inferred_complete_timeline |
| `Action_None` | 98 | 150 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 141 | 138 | inferred_complete_timeline |
| `Action_None` | 145 | 150 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 54–57 | 4 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 62–76 | 15 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 66–74 | 9 | 2 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 69–70 | 2 | 1 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 70–76 | 7 | 1 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 75–136 | 47 | 5 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 109–114 | 6 | 1 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 119–150 | 31 | 2 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 122–150 | 19 | 3 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 125–149 | 18 | 3 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 133–143 | 10 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 136–141 | 6 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 139–150 | 11 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 148–149 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 148–149 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_KickApproach` for actor_track_id `10` (Position_Unknown): Annotated start 4 != Inferred start 66
- ⚠️ `Action_AttemptRecovery` for actor_track_id `14` (Position_Unknown): Annotated start 133 != Inferred start 135
- ❌ Missing segment for action `Action_SecureRecovery` on target `14` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Onside_Recovery_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 40: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SecureRecovery' for track '13' has invalid range: start=147, end=136. Clamping end to start.
- ⚠️ Action 'Action_None' range [4-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-102] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-150] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-141] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-96] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-124] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-65] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-76] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [66-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [71-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-76] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-104] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-129] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [135-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-141] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>