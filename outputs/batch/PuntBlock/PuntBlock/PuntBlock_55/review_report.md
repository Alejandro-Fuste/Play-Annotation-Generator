# Play-Annotation-Generator Annotation Review — PuntBlock_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_55`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 152
- **Validation Warnings:** 162
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 135
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | defense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Personal_Protector2 | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `11` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `13` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `17` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `19` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `20` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `4` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `18` | `18` | 8 | START | 8 | 98 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `11` | `11` | 37 | END | 37 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `11` | `11` | 99 | START | 99 | 103 |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | `2` | `2` | 109 | START | 109 | 114 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Personal_Protector2 | `13` | `13` | 211 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 96 | 89 | inferred_complete_timeline |
| `Action_None` | 98 | 299 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 77 | 70 | inferred_complete_timeline |
| `Action_None` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 136 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 92 | 85 | inferred_complete_timeline |
| `Action_None` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_None` | 111 | 116 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 289 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 169 | 71 | inferred_complete_timeline |
| `Action_None` | 186 | 203 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 299 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 92 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 200 | 99 | inferred_complete_timeline |
| `Action_None` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |
| `Action_None` | 241 | 284 | 44 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_None` | 38 | 98 | 61 | inferred_complete_timeline |
| `Action_PuntBall` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_PuntBall` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_PuntBall` | 108 | 122 | 15 | inferred_complete_timeline |
| `Action_PuntBall` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_PuntBall` | 131 | 133 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 205 | 198 | inferred_complete_timeline |
| `Action_None` | 225 | 228 | 4 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 102 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 124 | 299 | 176 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 70 | 63 | inferred_complete_timeline |
| `Action_None` | 73 | 119 | 47 | inferred_complete_timeline |
| `Action_None` | 126 | 153 | 28 | inferred_complete_timeline |
| `Action_None` | 157 | 176 | 20 | inferred_complete_timeline |
| `Action_None` | 183 | 210 | 28 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 92 | 85 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 133 | 137 | 5 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 180 | 21 | inferred_complete_timeline |
| `Action_None` | 182 | 223 | 42 | inferred_complete_timeline |
| `Action_None` | 225 | 265 | 41 | inferred_complete_timeline |
| `Action_None` | 268 | 270 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 80 | 73 | inferred_complete_timeline |
| `Action_None` | 85 | 217 | 133 | inferred_complete_timeline |
| `Action_None` | 222 | 265 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 88 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 37 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 98 | 115 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 108 | 9 | inferred_complete_timeline |
| `Action_BlockPunt` | 109 | 114 | 6 | inferred_complete_timeline |
| `Action_None` | 115 | 141 | 27 | inferred_complete_timeline |
| `Action_None` | 144 | 155 | 12 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 186 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 47 | 40 | inferred_complete_timeline |
| `Action_None` | 49 | 195 | 147 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 299 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 222 | 215 | inferred_complete_timeline |
| `Action_None` | 224 | 299 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–129 | 130 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 37–299 | 244 | 9 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 99–138 | 28 | 5 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 110–137 | 24 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 132–141 | 10 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 142–220 | 67 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 145–205 | 55 | 4 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 146–198 | 53 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 162–207 | 37 | 5 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 171–299 | 117 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 179–299 | 76 | 5 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 180–252 | 67 | 3 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 184–299 | 111 | 4 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 213–214 | 2 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 222–224 | 3 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 223–299 | 67 | 5 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 227–235 | 5 | 2 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 230–299 | 70 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 289–299 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `11` (5 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `13` (Personal_Protector2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Jammer3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Guard` position mapped to `offense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 121 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 112: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [8-205] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-37] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-141] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-88] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-289] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-222] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-80] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-217] for track '7' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-265] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-195] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-136] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [99-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [105-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [108-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [124-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [131-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-92] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-223] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-265] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-92] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-200] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-284] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-115] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-70] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-119] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-153] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-176] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-92] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-299] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-92] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-104] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-133] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-154] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-203] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-121] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-132] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-195] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-190] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-198] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-171] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-187] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-197] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-299] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-186] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-242] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-213] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-252] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-263] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-297] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>