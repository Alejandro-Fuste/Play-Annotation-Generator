# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_1`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 62
- **Validation Warnings:** 48
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Onside_Recovery_Support1 | defense | `1` | `1` |
| ✅ EXACT | `Action_SecureRecovery` | Left_Coverage2 | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `0` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `14` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `15` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `17` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `18` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `3` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `4` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `5` | `5` | 6 | START | 6 | 29 |
| ✅ EXACT | `Action_KickBall` | Kicker | `5` | `5` | 30 | START | 30 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Onside_Recovery_Support1 | `1` | `1` | 97 | START | 97 | 102 |
| ✅ EXACT | `Action_SecureRecovery` | Left_Coverage2 | `4` | `4` | 136 | START | 136 | 144 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_KickApproach` | 6 | 29 | 24 | inferred_complete_timeline |
| `Action_KickBall` | 30 | 150 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_SecureRecovery` | 136 | 144 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 89 | 84 | inferred_complete_timeline |
| `Action_None` | 97 | 150 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 149 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 73 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 94 | 89 | inferred_complete_timeline |
| `Action_None` | 99 | 104 | 6 | inferred_complete_timeline |
| `Action_None` | 107 | 116 | 10 | inferred_complete_timeline |
| `Action_None` | 119 | 129 | 11 | inferred_complete_timeline |
| `Action_None` | 133 | 141 | 9 | inferred_complete_timeline |
| `Action_None` | 143 | 150 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front7 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front8 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front9 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 104 | 123 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 150 | 145 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 82–146 | 25 | 7 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 87–112 | 26 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 87–88 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 141–150 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_AttemptRecovery` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Onside_Recovery_Front7` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Onside_Recovery_Front8` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Onside_Recovery_Front9` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 39 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [6-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [97-102] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [104-123] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [136-144] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [30-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-73] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-129] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-141] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-112] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>