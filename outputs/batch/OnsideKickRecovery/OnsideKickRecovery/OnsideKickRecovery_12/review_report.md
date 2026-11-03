# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_12`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `13` | `13` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `13` | `13` |
| ✅ EXACT | `Action_AttemptRecovery` | Right_Coverage5 | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Coverage5 | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `6` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `8` | `Group` | 0 | START | 0 | 29 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `13` | `13` | 2 | START | 2 | 55 |
| ✅ EXACT | `Action_KickBall` | Kicker | `13` | `13` | 56 | START | 56 | 150 |
| ✅ EXACT | `Action_AttemptRecovery` | Right_Coverage5 | `8` | `8` | 134 | START | 134 | 139 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Coverage5 | `8` | `8` | 141 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 55 | 54 | inferred_complete_timeline |
| `Action_KickBall` | 56 | 150 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 77 | 76 | inferred_complete_timeline |
| `Action_None` | 81 | 147 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 128 | 127 | inferred_complete_timeline |
| `Action_None` | 135 | 150 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 44 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 93 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 133 | 39 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 134 | 139 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 3 | 2 | inferred_complete_timeline |
| `Action_None` | 6 | 8 | 3 | inferred_complete_timeline |
| `Action_None` | 11 | 16 | 6 | inferred_complete_timeline |
| `Action_None` | 19 | 22 | 4 | inferred_complete_timeline |
| `Action_None` | 33 | 71 | 39 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_None` | 92 | 97 | 6 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 110 | 122 | 13 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 145 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 135 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `7`</summary>

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
<summary>Onside_Recovery_Front3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 121 | 120 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 138 | 137 | inferred_complete_timeline |
| `Action_None` | 140 | 145 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `5`</summary>

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

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 8 | 83 | 76 | inferred_complete_timeline |
| `Action_None` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 135 | 25 | inferred_complete_timeline |
| `Action_None` | 137 | 150 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 80 | 79 | inferred_complete_timeline |
| `Action_None` | 84 | 88 | 5 | inferred_complete_timeline |
| `Action_None` | 90 | 142 | 53 | inferred_complete_timeline |
| `Action_None` | 147 | 150 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–1
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–149 | 149 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 2–150 | 149 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 13–150 | 138 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 16–104 | 57 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 46–149 | 96 | 6 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 52–150 | 98 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 79–137 | 8 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 113–127 | 12 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 118–133 | 14 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 144–150 | 7 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SecureRecovery` on target `8` (Right_Coverage5)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 26: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SecureRecovery' for track '8' has invalid range: start=141, end=139. Clamping end to start.
- ⚠️ Action 'Action_None' range [2-121] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-128] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-77] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-147] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-44] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [134-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-3] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-8] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-16] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-22] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-71] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-122] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-135] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [2-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [56-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-135] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-61] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-89] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-51] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-97] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-129] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-84] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-119] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-133] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>