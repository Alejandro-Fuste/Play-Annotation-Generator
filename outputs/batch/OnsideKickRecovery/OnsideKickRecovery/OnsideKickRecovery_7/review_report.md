# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_7`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Left_Coverage3 | offense | `13` | `13` |
| ✅ EXACT | `Action_KickBall` | Left_Coverage3 | offense | `13` | `13` |
| ✅ EXACT | `Action_AttemptRecovery` | Right_Coverage6 | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Coverage6 | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `11` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `13` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `15` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `17` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `21` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `7` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_KickApproach` | Left_Coverage3 | `13` | `13` | 10 | START | 10 | 30 |
| ✅ EXACT | `Action_KickBall` | Left_Coverage3 | `13` | `13` | 31 | START | 31 | 150 |
| ✅ EXACT | `Action_AttemptRecovery` | Right_Coverage6 | `15` | `15` | 87 | START | 87 | 96 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Coverage6 | `15` | `15` | 114 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Coverage1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 35 | 26 | inferred_complete_timeline |
| `Action_None` | 41 | 150 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_KickApproach` | 10 | 30 | 21 | inferred_complete_timeline |
| `Action_KickBall` | 31 | 150 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 122 | 113 | inferred_complete_timeline |
| `Action_None` | 126 | 150 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 112 | 103 | inferred_complete_timeline |
| `Action_None` | 116 | 135 | 20 | inferred_complete_timeline |
| `Action_None` | 142 | 150 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 20 | 11 | inferred_complete_timeline |
| `Action_None` | 25 | 92 | 68 | inferred_complete_timeline |
| `Action_None` | 94 | 115 | 22 | inferred_complete_timeline |
| `Action_None` | 120 | 140 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 20 | 11 | inferred_complete_timeline |
| `Action_None` | 25 | 107 | 83 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 127 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 87 | 96 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 94 | 85 | inferred_complete_timeline |
| `Action_None` | 97 | 106 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 107 | 98 | inferred_complete_timeline |
| `Action_None` | 109 | 150 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 123 | 114 | inferred_complete_timeline |
| `Action_None` | 125 | 141 | 17 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 116 | 107 | inferred_complete_timeline |
| `Action_None` | 122 | 132 | 11 | inferred_complete_timeline |
| `Action_None` | 135 | 138 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–150 | 151 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 100–150 | 36 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 117–150 | 34 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 119–148 | 17 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 123–150 | 28 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SecureRecovery` on target `15` (Right_Coverage6)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Support5` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 15: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SecureRecovery' for track '15' has invalid range: start=114, end=96. Clamping end to start.
- ⚠️ Action 'Action_None' range [10-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-94] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-132] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-141] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [31-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [87-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-35] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-135] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-20] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-107] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-20] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-92] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-116] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>