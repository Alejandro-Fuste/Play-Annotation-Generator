# Play-Annotation-Generator Annotation Review — PuntBlock_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_33`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 157
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 124
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_BlockPunt` | Right_Jammer4 | defense | `19` | `19` |
| ✅ EXACT | `Action_SecureRecovery` | Left_Edge_Rusher1 | defense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 0 | START | 0 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `8` | `8` | 16 | START | 16 | 34 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 44 | END | 44 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `6` | `6` | 75 | START | 75 | 92 |
| ✅ EXACT | `Action_BlockPunt` | Right_Jammer4 | `19` | `19` | 85 | START | 85 | 91 |
| ✅ EXACT | `Action_SecureRecovery` | Left_Edge_Rusher1 | `4` | `4` | 142 | START | 142 | 152 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 205 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 149 | 134 | inferred_complete_timeline |
| `Action_None` | 152 | 243 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 16 | 34 | 19 | inferred_complete_timeline |
| `Action_LongSnap` | 37 | 74 | 38 | inferred_complete_timeline |
| `Action_None` | 75 | 235 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 149 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 56 | 41 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_None` | 75 | 82 | 8 | inferred_complete_timeline |
| `Action_None` | 84 | 120 | 37 | inferred_complete_timeline |
| `Action_None` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_None` | 128 | 211 | 84 | inferred_complete_timeline |
| `Action_None` | 213 | 218 | 6 | inferred_complete_timeline |
| `Action_None` | 222 | 229 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 41 | 75 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_None` | 45 | 74 | 30 | inferred_complete_timeline |
| `Action_PuntBall` | 75 | 92 | 18 | inferred_complete_timeline |
| `Action_PuntBall` | 94 | 115 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_PuntBall` | 130 | 139 | 10 | inferred_complete_timeline |
| `Action_PuntBall` | 145 | 202 | 58 | inferred_complete_timeline |
| `Action_PuntBall` | 209 | 269 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 64 | 49 | inferred_complete_timeline |
| `Action_None` | 67 | 189 | 123 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 74 | 59 | inferred_complete_timeline |
| `Action_None` | 123 | 126 | 4 | inferred_complete_timeline |
| `Action_None` | 165 | 205 | 41 | inferred_complete_timeline |
| `Action_None` | 207 | 220 | 14 | inferred_complete_timeline |
| `Action_None` | 222 | 225 | 4 | inferred_complete_timeline |
| `Action_None` | 239 | 249 | 11 | inferred_complete_timeline |
| `Action_None` | 252 | 256 | 5 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 117 | 102 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 153 | 32 | inferred_complete_timeline |
| `Action_None` | 169 | 184 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_SecureRecovery` | 142 | 152 | 11 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 160 | 164 | 5 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 209 | 194 | inferred_complete_timeline |
| `Action_None` | 211 | 223 | 13 | inferred_complete_timeline |
| `Action_None` | 226 | 230 | 5 | inferred_complete_timeline |
| `Action_None` | 236 | 269 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 136 | 121 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 187 | 172 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 50 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 69 | 54 | inferred_complete_timeline |
| `Action_None` | 75 | 128 | 54 | inferred_complete_timeline |
| `Action_None` | 133 | 191 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 84 | 30 | inferred_complete_timeline |
| `Action_BlockPunt` | 85 | 91 | 7 | inferred_complete_timeline |
| `Action_None` | 92 | 111 | 20 | inferred_complete_timeline |
| `Action_None` | 115 | 143 | 29 | inferred_complete_timeline |
| `Action_None` | 145 | 153 | 9 | inferred_complete_timeline |
| `Action_None` | 158 | 231 | 74 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |
| `Action_None` | 244 | 252 | 9 | inferred_complete_timeline |
| `Action_None` | 254 | 258 | 5 | inferred_complete_timeline |
| `Action_None` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–254 | 254 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 57–168 | 112 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 63–142 | 77 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 67–269 | 198 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 72–96 | 19 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 103–263 | 128 | 8 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 110–120 | 8 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 125–127 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 125–127 | 3 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 154–199 | 46 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 168–171 | 4 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 179–269 | 76 | 5 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 189–215 | 27 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 208–215 | 8 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 224–236 | 6 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 241–263 | 22 | 2 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 253–269 | 17 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 255–269 | 15 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 261–269 | 6 | 2 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 264–269 | 6 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `6` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Jammer3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Jammer4` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 104 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 68: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [16-205] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-64] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-209] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-223] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-74] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-205] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-220] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-249] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-256] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-141] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [142-152] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-149] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [75-92] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [94-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [117-118] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [130-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [145-202] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-187] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [16-34] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-235] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-50] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-243] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-211] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-69] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-191] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-254] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-37] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-136] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-75] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-111] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-143] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-231] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-252] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-117] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-86] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-108] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-133] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-204] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-254] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-199] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-219] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-263] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-215] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-215] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-263] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-269] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>