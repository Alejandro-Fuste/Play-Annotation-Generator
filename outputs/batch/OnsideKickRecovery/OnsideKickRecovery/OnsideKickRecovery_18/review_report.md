# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_18

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_18`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | offense | `14` | `14` |
| ✅ EXACT | `Action_AttemptRecovery` | Kicker | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Kicker | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `10` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `6` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `9` | `Group` | 0 | START | 0 | 1 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `14` | `14` | 2 | START | 2 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | `14` | `14` | 48 | START | 48 | 54 |
| ✅ EXACT | `Action_AttemptRecovery` | Kicker | `14` | `14` | 106 | START | 106 | 109 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Kicker | `14` | `14` | 115 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 18 | 17 | inferred_complete_timeline |
| `Action_KickApproach` | 20 | 30 | 11 | inferred_complete_timeline |
| `Action_KickApproach` | 38 | 47 | 10 | inferred_complete_timeline |
| `Action_KickBall` | 48 | 54 | 7 | inferred_complete_timeline |
| `Action_KickBall` | 57 | 65 | 9 | inferred_complete_timeline |
| `Action_KickBall` | 70 | 76 | 7 | inferred_complete_timeline |
| `Action_KickBall` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_KickBall` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_KickBall` | 105 | 105 | 1 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 106 | 109 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 20 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 56 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 84 | 27 | inferred_complete_timeline |
| `Action_None` | 87 | 95 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 65 | 64 | inferred_complete_timeline |
| `Action_None` | 69 | 73 | 5 | inferred_complete_timeline |
| `Action_None` | 76 | 90 | 15 | inferred_complete_timeline |
| `Action_None` | 92 | 105 | 14 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 133 | 12 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 34 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_None` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_None` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_None` | 71 | 102 | 32 | inferred_complete_timeline |
| `Action_None` | 109 | 123 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 36 | 35 | inferred_complete_timeline |
| `Action_None` | 40 | 43 | 4 | inferred_complete_timeline |
| `Action_None` | 71 | 123 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 50 | 49 | inferred_complete_timeline |
| `Action_None` | 52 | 56 | 5 | inferred_complete_timeline |
| `Action_None` | 60 | 67 | 8 | inferred_complete_timeline |
| `Action_None` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_None` | 82 | 100 | 19 | inferred_complete_timeline |
| `Action_None` | 107 | 148 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 148 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 114 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 56 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 150 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 71 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 3–9 | 4 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 31–32 | 2 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 46–47 | 2 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 53–122 | 66 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 55–150 | 69 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 59–150 | 88 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 59–123 | 51 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 63–65 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 70–71 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 72–148 | 77 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 72–150 | 58 | 4 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 74–150 | 49 | 4 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 76–150 | 75 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 85–118 | 26 | 4 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 91–141 | 34 | 4 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 96–99 | 4 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 113–120 | 8 | 1 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 140–149 | 7 | 2 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 143–150 | 8 | 1 | Undefined position; Undefined team |
| `35` | `37` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_KickBall` and target `14` (6 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `14` (Kicker)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 90 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 37: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SecureRecovery' for track '14' has invalid range: start=115, end=109. Clamping end to start.
- ⚠️ Action 'Action_None' range [2-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-36] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-43] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-123] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-148] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-56] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-84] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-95] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-34] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-41] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-50] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-102] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-123] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-67] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-100] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-65] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-150] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [2-18] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [20-30] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [48-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [57-65] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [70-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [86-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [100-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [106-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-20] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-4] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-9] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-81] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-81] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-106] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-112] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-116] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-94] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-108] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-98] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-120] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-138] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-120] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '35' has 1 frames without a visible bounding box.
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

</details>