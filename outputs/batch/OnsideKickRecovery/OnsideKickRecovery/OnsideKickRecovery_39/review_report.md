# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_39`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `20` | `20` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Kicker | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Kicker | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `0` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `1` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `11` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `15` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `16` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `20` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `3` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `4` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `5` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `8` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `9` | `Group` | 0 | START | 0 | 8 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `20` | `20` | 9 | START | 9 | 52 |
| ✅ EXACT | `Action_KickBall` | Kicker | `20` | `20` | 53 | START | 53 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Kicker | `20` | `20` | 90 | START | 90 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Kicker | `20` | `20` | 130 | START | 130 | 135 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_KickApproach` | 9 | 52 | 44 | inferred_complete_timeline |
| `Action_KickBall` | 53 | 89 | 37 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 90 | 97 | 8 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 113 | 129 | 17 | inferred_complete_timeline |
| `Action_SecureRecovery` | 130 | 135 | 6 | inferred_complete_timeline |
| `Action_SecureRecovery` | 138 | 144 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 123 | 115 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 135 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 146 | 138 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 90 | 82 | inferred_complete_timeline |
| `Action_None` | 93 | 97 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 129 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 138 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 92 | 84 | inferred_complete_timeline |
| `Action_None` | 97 | 150 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front7 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front8 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 150 | 142 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–150 | 132 | 7 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 0–149 | 113 | 9 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 39–40 | 2 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 54–103 | 28 | 7 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 93–148 | 40 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 106–109 | 4 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 111–138 | 9 | 4 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 117–125 | 9 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 145–149 | 5 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 147–149 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_AttemptRecovery` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SecureRecovery` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Onside_Recovery_Front7` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Onside_Recovery_Front8` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 65 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [9-123] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-135] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-138] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-146] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [90-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [130-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [138-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-92] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-137] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-100] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-40] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-60] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-87] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-121] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-125] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '32' has 1 frames without a visible bounding box.
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

</details>