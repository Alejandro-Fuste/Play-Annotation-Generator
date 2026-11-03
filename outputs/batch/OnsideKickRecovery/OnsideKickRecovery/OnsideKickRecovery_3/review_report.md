# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_3`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Onside_Recovery_Front1 | defense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Left_Coverage1 | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `0` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `13` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `14` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `3` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `4` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `8` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `9` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `13` | `13` | 20 | START | 20 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | `13` | `13` | 112 | START | 112 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Onside_Recovery_Front1 | `7` | `7` | 150 | START | 150 | 160 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Left_Coverage1 | `14` | `14` | 212 | START | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_KickApproach` | 20 | 111 | 92 | inferred_complete_timeline |
| `Action_KickBall` | 112 | 135 | 24 | inferred_complete_timeline |
| `Action_KickBall` | 137 | 299 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 196 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 202 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 136 | 117 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 149 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 182 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 128 | 109 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 184 | 15 | inferred_complete_timeline |
| `Action_None` | 189 | 257 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 130 | 111 | inferred_complete_timeline |
| `Action_None` | 139 | 170 | 32 | inferred_complete_timeline |
| `Action_None` | 173 | 286 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 252 | 233 | inferred_complete_timeline |
| `Action_None` | 255 | 299 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 177 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 262 | 83 | inferred_complete_timeline |
| `Action_None` | 264 | 275 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 196 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 299 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 299 | 280 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 150 | 160 | 11 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 176 | 181 | 6 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 187 | 232 | 46 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 235 | 236 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 283 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 185 | 166 | inferred_complete_timeline |
| `Action_None` | 187 | 237 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 171 | 152 | inferred_complete_timeline |
| `Action_None` | 173 | 178 | 6 | inferred_complete_timeline |
| `Action_None` | 181 | 193 | 13 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 278 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 200 | 181 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 299 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–169 | 170 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 142–299 | 158 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 152–299 | 148 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 163–299 | 136 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 164–299 | 136 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 188–299 | 105 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 201–299 | 99 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 205–299 | 91 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 260–299 | 40 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 290–296 | 7 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 292–293 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickBall` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_AttemptRecovery` and target `7` (6 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `14` (Left_Coverage1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 7: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_SecureRecovery' for track '14' has invalid range: start=212, end=202. Clamping end to start.
- ⚠️ Action 'Action_None' range [20-171] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-193] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-278] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-177] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-262] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-275] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-196] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-283] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [150-160] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [170-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [173-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [176-181] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [187-232] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [235-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-252] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-136] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-182] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-185] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-237] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-170] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-286] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-169] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [112-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [137-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-196] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-202] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-257] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-235] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-272] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-244] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>