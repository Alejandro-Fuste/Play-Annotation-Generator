# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_36`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 98
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Onside_Recovery_Front6 | defense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Right_Coverage5 | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `10` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `9` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `19` | `19` | 2 | START | 2 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickBall` | Kicker | `19` | `19` | 78 | START | 78 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Onside_Recovery_Front6 | `7` | `7` | 140 | START | 140 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Right_Coverage5 | `10` | `10` | 183 | START | 183 | 195 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 77 | 76 | inferred_complete_timeline |
| `Action_KickBall` | 78 | 141 | 64 | inferred_complete_timeline |
| `Action_KickBall` | 143 | 239 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 61 | 60 | inferred_complete_timeline |
| `Action_None` | 63 | 80 | 18 | inferred_complete_timeline |
| `Action_None` | 87 | 177 | 91 | inferred_complete_timeline |
| `Action_None` | 180 | 219 | 40 | inferred_complete_timeline |
| `Action_None` | 222 | 225 | 4 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 67 | 66 | inferred_complete_timeline |
| `Action_None` | 69 | 74 | 6 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 88 | 94 | 7 | inferred_complete_timeline |
| `Action_None` | 104 | 145 | 42 | inferred_complete_timeline |
| `Action_None` | 153 | 163 | 11 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 239 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 67 | 66 | inferred_complete_timeline |
| `Action_None` | 69 | 185 | 117 | inferred_complete_timeline |
| `Action_None` | 191 | 239 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 159 | 158 | inferred_complete_timeline |
| `Action_None` | 175 | 239 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 67 | 66 | inferred_complete_timeline |
| `Action_None` | 69 | 101 | 33 | inferred_complete_timeline |
| `Action_None` | 104 | 219 | 116 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 103 | 102 | inferred_complete_timeline |
| `Action_None` | 106 | 239 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_SecureRecovery` | 183 | 195 | 13 | inferred_complete_timeline |
| `Action_SecureRecovery` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_SecureRecovery` | 208 | 214 | 7 | inferred_complete_timeline |
| `Action_SecureRecovery` | 217 | 224 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 212 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 202 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 174 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 140 | 179 | 40 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 208 | 207 | inferred_complete_timeline |
| `Action_None` | 215 | 239 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 191 | 190 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 2–57 | 9 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 52–239 | 167 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 131–212 | 23 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 132–138 | 7 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 194–220 | 22 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 195–202 | 8 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 207–213 | 6 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 214–237 | 17 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 216–239 | 21 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 219–239 | 6 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 225–239 | 15 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickBall` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_AttemptRecovery` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SecureRecovery` and target `10` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 69 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [2-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-212] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-239] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [140-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [198-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-202] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-103] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [183-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [199-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [208-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [217-224] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-80] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-177] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-219] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-174] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-67] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-185] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-159] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-239] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-67] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-219] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [2-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [78-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-5] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-79] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-239] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-137] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-167] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-138] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '34' has 1 frames without a visible bounding box.
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

</details>