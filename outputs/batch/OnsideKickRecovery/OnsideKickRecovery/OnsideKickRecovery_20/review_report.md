# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_20

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_20`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | offense | `6` | `6` |
| ✅ EXACT | `Action_AttemptRecovery` | Right_Coverage6 | offense | `14` | `14` |
| ✅ EXACT | `Action_SecureRecovery` | Right_Coverage6 | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `14` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `6` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `7` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `9` | `Group` | 0 | START | 0 | 1 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `6` | `6` | 2 | START | 2 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | `6` | `6` | 84 | START | 84 | 147 |
| ✅ EXACT | `Action_AttemptRecovery` | Right_Coverage6 | `14` | `14` | 150 | START | 150 | 152 |
| ✅ EXACT | `Action_SecureRecovery` | Right_Coverage6 | `14` | `14` | 160 | START | 160 | 162 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 28 | 27 | inferred_complete_timeline |
| `Action_KickApproach` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 36 | 42 | 7 | inferred_complete_timeline |
| `Action_KickApproach` | 46 | 52 | 7 | inferred_complete_timeline |
| `Action_KickApproach` | 54 | 72 | 19 | inferred_complete_timeline |
| `Action_KickApproach` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_KickBall` | 84 | 147 | 64 | inferred_complete_timeline |
| `Action_KickBall` | 149 | 155 | 7 | inferred_complete_timeline |
| `Action_KickBall` | 157 | 173 | 17 | inferred_complete_timeline |
| `Action_KickBall` | 175 | 193 | 19 | inferred_complete_timeline |
| `Action_KickBall` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 89 | 88 | inferred_complete_timeline |
| `Action_None` | 93 | 152 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 157 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 60 | 59 | inferred_complete_timeline |
| `Action_None` | 66 | 80 | 15 | inferred_complete_timeline |
| `Action_None` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 110 | 5 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 98 | 97 | inferred_complete_timeline |
| `Action_None` | 100 | 149 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 168 | 167 | inferred_complete_timeline |
| `Action_None` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 197 | 18 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 87 | 86 | inferred_complete_timeline |
| `Action_None` | 102 | 120 | 19 | inferred_complete_timeline |
| `Action_None` | 126 | 142 | 17 | inferred_complete_timeline |
| `Action_None` | 144 | 170 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 136 | 135 | inferred_complete_timeline |
| `Action_None` | 139 | 162 | 24 | inferred_complete_timeline |
| `Action_None` | 165 | 201 | 37 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 193 | 192 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 150 | 152 | 3 | inferred_complete_timeline |
| `Action_SecureRecovery` | 160 | 162 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 80 | 79 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 149 | 46 | inferred_complete_timeline |
| `Action_None` | 151 | 161 | 11 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 174 | 173 | inferred_complete_timeline |
| `Action_None` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 195 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 201 | 200 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 11–210 | 161 | 6 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 29–210 | 154 | 10 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 61–210 | 144 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 148–205 | 47 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 152–157 | 4 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 169–210 | 42 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 184–210 | 27 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 198–209 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `6` (6 segments found)
- ⚠️ Ambiguous match for action `Action_KickBall` and target `6` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 82 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [2-168] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-197] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-136] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-162] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-174] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [2-28] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [30-31] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [36-42] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [46-52] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [54-72] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [84-147] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [149-155] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [157-173] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [175-193] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [199-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-120] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-170] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [150-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [160-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-193] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-60] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-80] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-152] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-80] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-149] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-14] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-20] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-45] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-139] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-69] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-104] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-181] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-205] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-209] for track '26' has 2 frames without a visible bounding box.
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