# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_29`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 126
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
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage6 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `7` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `17` | `17` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Onside_Recovery_Front3 | defense | `15` | `15` |
| ✅ EXACT | `Action_SecureRecovery` | Left_Coverage6 | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `10` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage6 | `19` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `7` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `17` | `17` | 2 | START | 2 | 15 |
| ✅ EXACT | `Action_KickBall` | Kicker | `17` | `17` | 16 | START | 16 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_AttemptRecovery` | Onside_Recovery_Front3 | `15` | `15` | 70 | START | 70 | 70 |
| ✅ EXACT | `Action_SecureRecovery` | Left_Coverage6 | `19` | `19` | 83 | START | 83 | 94 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 15 | 14 | inferred_complete_timeline |
| `Action_KickBall` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–23
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 2 | 1 | inferred_complete_timeline |
| `Action_None` | 14 | 23 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 16 | 15 | inferred_complete_timeline |
| `Action_None` | 21 | 28 | 8 | inferred_complete_timeline |
| `Action_None` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_None` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_None` | 40 | 45 | 6 | inferred_complete_timeline |
| `Action_None` | 47 | 53 | 7 | inferred_complete_timeline |
| `Action_None` | 55 | 66 | 12 | inferred_complete_timeline |
| `Action_None` | 68 | 169 | 102 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 59 | 58 | inferred_complete_timeline |
| `Action_None` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_None` | 68 | 70 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 63 | 62 | inferred_complete_timeline |
| `Action_None` | 69 | 75 | 7 | inferred_complete_timeline |
| `Action_None` | 77 | 81 | 5 | inferred_complete_timeline |
| `Action_None` | 83 | 127 | 45 | inferred_complete_timeline |
| `Action_None` | 129 | 146 | 18 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 131 | 130 | inferred_complete_timeline |
| `Action_None` | 137 | 210 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage6 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_SecureRecovery` | 83 | 94 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 145 | 144 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 35 | 34 | inferred_complete_timeline |
| `Action_None` | 43 | 161 | 119 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 37 | 36 | inferred_complete_timeline |
| `Action_None` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_None` | 51 | 65 | 15 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 70 | 70 | 1 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 79 | 84 | 6 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 90 | 134 | 45 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 75 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 147 | 146 | inferred_complete_timeline |
| `Action_None` | 150 | 210 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front7 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front8 — actor_track_id `8`</summary>

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
<summary>Onside_Recovery_Support1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
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
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 11–137 | 126 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 81–146 | 56 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 82–210 | 129 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 88–89 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 112–209 | 60 | 6 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 121–122 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 123–210 | 88 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 139–210 | 72 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 140–210 | 71 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 144–151 | 8 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 148–172 | 22 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 152–209 | 28 | 4 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 160–204 | 45 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 175–210 | 34 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 178–184 | 7 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 186–189 | 4 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 201–203 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_AttemptRecovery` and target `15` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Onside_Recovery_Front7` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Onside_Recovery_Front8` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 89 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [2-210] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-145] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-131] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-35] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-161] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-59] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-66] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-37] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-44] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-65] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-147] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' for track '15' starts at frame 70, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_AttemptRecovery' range [70-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [72-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [79-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [90-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [136-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-63] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-146] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [16-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [83-94] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-16] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-28] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-33] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-45] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-66] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-169] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 2, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [2-2] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-23] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-160] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-202] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-210] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-151] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-160] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-172] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-197] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-204] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-196] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '39' has 1 frames without a visible bounding box.
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

</details>