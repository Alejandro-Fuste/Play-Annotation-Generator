# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_38`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `16` | `16` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `16` | `16` |
| ✅ EXACT | `Action_AttemptRecovery` | Kicker | offense | `16` | `16` |
| ✅ EXACT | `Action_SecureRecovery` | Kicker | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `0` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `3` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `4` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `5` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `6` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `7` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `16` | `16` | 10 | START | 10 | 80 |
| ✅ EXACT | `Action_KickBall` | Kicker | `16` | `16` | 81 | START | 81 | 129 |
| ✅ EXACT | `Action_AttemptRecovery` | Kicker | `16` | `16` | 130 | START | 130 | 139 |
| ✅ EXACT | `Action_SecureRecovery` | Kicker | `16` | `16` | 140 | START | 140 | 145 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_KickApproach` | 10 | 80 | 71 | inferred_complete_timeline |
| `Action_KickBall` | 81 | 129 | 49 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 130 | 139 | 10 | inferred_complete_timeline |
| `Action_SecureRecovery` | 140 | 145 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 179 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 155 | 146 | inferred_complete_timeline |
| `Action_None` | 157 | 210 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 182 | 173 | inferred_complete_timeline |
| `Action_None` | 189 | 195 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 167 | 158 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 202 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 188 | 179 | inferred_complete_timeline |
| `Action_None` | 193 | 210 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 126 | 117 | inferred_complete_timeline |
| `Action_None` | 130 | 151 | 22 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 139 | 130 | inferred_complete_timeline |
| `Action_None` | 144 | 160 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 61 | 52 | inferred_complete_timeline |
| `Action_None` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_None` | 75 | 149 | 75 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 210 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 178 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 116 | 107 | inferred_complete_timeline |
| `Action_None` | 119 | 141 | 23 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 169 | 21 | inferred_complete_timeline |
| `Action_None` | 172 | 210 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 5–185 | 111 | 7 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 11–125 | 54 | 10 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 39–200 | 139 | 7 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 135–207 | 54 | 7 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 153–210 | 45 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 178–198 | 14 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 182–210 | 29 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 184–206 | 14 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 185–210 | 26 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 199–210 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Onside_Recovery_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kicker` position mapped to `offense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 74 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [10-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-182] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-179] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-141] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-169] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-178] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [130-139] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [140-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-71] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-164] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-12] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-23] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-45] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-72] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-200] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-160] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-203] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '26' has 1 frames without a visible bounding box.
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