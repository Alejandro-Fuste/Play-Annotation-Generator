# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_4`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 54
- **Ball Tracks:** 0
- **Action Segments:** 150
- **Validation Warnings:** 199
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 133
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Onside_Recovery_Support2 | defense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Onside_Recovery_Support2 | defense | `16` | `16` |
| ✅ EXACT | `Action_AttemptRecovery` | Onside_Recovery_Front1 | defense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Left_Coverage1 | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_KickApproach` | Onside_Recovery_Support2 | `16` | `16` | 2 | START | 2 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Onside_Recovery_Support2 | `16` | `16` | 54 | START | 54 | 99 |
| ✅ EXACT | `Action_AttemptRecovery` | Onside_Recovery_Front1 | `0` | `0` | 97 | START | 97 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Left_Coverage1 | `17` | `17` | 152 | START | 152 | 157 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Coverage1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 24 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 85 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 140 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 151 | 9 | inferred_complete_timeline |
| `Action_SecureRecovery` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_SecureRecovery` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_SecureRecovery` | 170 | 175 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 184 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 6 | 5 | inferred_complete_timeline |
| `Action_None` | 14 | 16 | 3 | inferred_complete_timeline |
| `Action_None` | 26 | 94 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 30 | 29 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 176 | 175 | inferred_complete_timeline |
| `Action_None` | 195 | 197 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 197 | 196 | inferred_complete_timeline |
| `Action_None` | 208 | 214 | 7 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_None` | 51 | 68 | 18 | inferred_complete_timeline |
| `Action_None` | 71 | 195 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 183 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 226 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 97 | 100 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 71 | 70 | inferred_complete_timeline |
| `Action_None` | 73 | 109 | 37 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 149 | 10 | inferred_complete_timeline |
| `Action_None` | 156 | 166 | 11 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 183 | 11 | inferred_complete_timeline |
| `Action_None` | 185 | 198 | 14 | inferred_complete_timeline |
| `Action_None` | 204 | 239 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 100 | 99 | inferred_complete_timeline |
| `Action_None` | 102 | 140 | 39 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 177 | 11 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 234 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 53 | 52 | inferred_complete_timeline |
| `Action_KickBall` | 54 | 99 | 46 | inferred_complete_timeline |
| `Action_KickBall` | 105 | 109 | 5 | inferred_complete_timeline |
| `Action_KickBall` | 115 | 182 | 68 | inferred_complete_timeline |
| `Action_KickBall` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_KickBall` | 193 | 202 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 85 | 84 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 126 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–239 | 238 | 4 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–149 | 145 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 14–200 | 167 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 41–164 | 106 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 67–71 | 5 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 71–228 | 152 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 92–197 | 80 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 114–194 | 49 | 6 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 116–119 | 4 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 125–197 | 73 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 129–197 | 16 | 5 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 152–163 | 12 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 176–239 | 64 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 186–200 | 15 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 192–209 | 18 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 195–239 | 27 | 4 | Undefined position; Undefined team |
| `33` | `80` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |
| `34` | `81` | Position_Unknown | Team_Unknown | 206–239 | 32 | 3 | Undefined position; Undefined team |
| `35` | `82` | Position_Unknown | Team_Unknown | 206–234 | 17 | 5 | Undefined position; Undefined team |
| `36` | `91` | Position_Unknown | Team_Unknown | 208–239 | 32 | 1 | Undefined position; Undefined team |
| `37` | `92` | Position_Unknown | Team_Unknown | 208–239 | 32 | 1 | Undefined position; Undefined team |
| `38` | `94` | Position_Unknown | Team_Unknown | 208–212 | 5 | 1 | Undefined position; Undefined team |
| `39` | `95` | Position_Unknown | Team_Unknown | 209–239 | 31 | 1 | Undefined position; Undefined team |
| `40` | `100` | Position_Unknown | Team_Unknown | 210–226 | 17 | 1 | Undefined position; Undefined team |
| `41` | `101` | Position_Unknown | Team_Unknown | 211–231 | 14 | 3 | Undefined position; Undefined team |
| `42` | `104` | Position_Unknown | Team_Unknown | 212–216 | 5 | 1 | Undefined position; Undefined team |
| `43` | `105` | Position_Unknown | Team_Unknown | 212–217 | 6 | 1 | Undefined position; Undefined team |
| `44` | `106` | Position_Unknown | Team_Unknown | 212–239 | 27 | 2 | Undefined position; Undefined team |
| `45` | `109` | Position_Unknown | Team_Unknown | 217–219 | 3 | 1 | Undefined position; Undefined team |
| `46` | `113` | Position_Unknown | Team_Unknown | 221–239 | 10 | 3 | Undefined position; Undefined team |
| `47` | `115` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `48` | `116` | Position_Unknown | Team_Unknown | 225–228 | 4 | 1 | Undefined position; Undefined team |
| `49` | `120` | Position_Unknown | Team_Unknown | 230–239 | 5 | 2 | Undefined position; Undefined team |
| `50` | `122` | Position_Unknown | Team_Unknown | 230–238 | 7 | 2 | Undefined position; Undefined team |
| `51` | `123` | Position_Unknown | Team_Unknown | 231–237 | 6 | 2 | Undefined position; Undefined team |
| `52` | `129` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `53` | `132` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickBall` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_SecureRecovery` and target `17` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ 37 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 37 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 74 |
| Missing visible bounding boxes during action | 122 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 10: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 10: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_AttemptRecovery' for track '0' starts at frame 97, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_AttemptRecovery' range [97-100] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-140] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-177] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-234] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-109] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-149] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-166] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-198] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-214] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-176] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-97] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-239] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-195] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-183] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-184] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-239] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' for track '16' starts at frame 2, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_KickApproach' range [2-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [54-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [105-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [115-182] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [185-190] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [193-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-24] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-85] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-140] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [152-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [159-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [170-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-6] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-174] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-200] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-88] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-164] for track '20' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-171] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-228] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-169] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-197] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-172] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-239] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-200] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-209] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-215] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-232] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-226] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.

</details>