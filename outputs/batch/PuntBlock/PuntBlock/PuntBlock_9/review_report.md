# Play-Annotation-Generator Annotation Review — PuntBlock_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_9`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 56
- **Ball Tracks:** 0
- **Action Segments:** 166
- **Validation Warnings:** 203
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 150
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Right_Guard | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `16` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `9` | `Group` | 0 | START | 0 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Right_Guard | `6` | `6` | 16 | START | 16 | 33 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 47 | END | 47 | 47 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 70 | START | 70 | 89 |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | `21` | `21` | 86 | START | 86 | 94 |
| ✅ EXACT | `Action_SecureRecovery` | Position_Unknown | `21` | `21` | 151 | START | 151 | 171 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 79 | 64 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 125 | 110 | inferred_complete_timeline |
| `Action_None` | 128 | 271 | 144 | inferred_complete_timeline |
| `Action_None` | 274 | 329 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 329 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 70 | 55 | inferred_complete_timeline |
| `Action_None` | 72 | 329 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 72 | 57 | inferred_complete_timeline |
| `Action_None` | 74 | 107 | 34 | inferred_complete_timeline |
| `Action_None` | 109 | 118 | 10 | inferred_complete_timeline |
| `Action_None` | 120 | 172 | 53 | inferred_complete_timeline |
| `Action_None` | 175 | 184 | 10 | inferred_complete_timeline |
| `Action_None` | 186 | 193 | 8 | inferred_complete_timeline |
| `Action_None` | 199 | 202 | 4 | inferred_complete_timeline |
| `Action_None` | 204 | 329 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 76 | 61 | inferred_complete_timeline |
| `Action_None` | 81 | 92 | 12 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_None` | 142 | 151 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 70 | 55 | inferred_complete_timeline |
| `Action_None` | 81 | 105 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 70 | 55 | inferred_complete_timeline |
| `Action_None` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 140 | 329 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 47 | 1 | inferred_complete_timeline |
| `Action_None` | 48 | 69 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 70 | 89 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 16 | 33 | 18 | inferred_complete_timeline |
| `Action_LongSnap` | 35 | 69 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 73 | 58 | inferred_complete_timeline |
| `Action_None` | 76 | 329 | 254 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 137 | 122 | inferred_complete_timeline |
| `Action_None` | 139 | 329 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 329 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 56 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 76 | 61 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 205 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 33 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–303
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 303 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 190 | 175 | inferred_complete_timeline |
| `Action_None` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_None` | 200 | 204 | 5 | inferred_complete_timeline |
| `Action_None` | 217 | 252 | 36 | inferred_complete_timeline |
| `Action_None` | 263 | 266 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 329 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 329 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 307 | 292 | inferred_complete_timeline |
| `Action_None` | 311 | 329 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 36–171 | 104 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 62–99 | 35 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 90–124 | 21 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 104–135 | 16 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 112–115 | 4 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 121–151 | 19 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 124–329 | 206 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 126–130 | 4 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 127–209 | 81 | 3 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 132–133 | 2 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 135–191 | 52 | 3 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 135–139 | 5 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 138–328 | 185 | 4 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 159–329 | 160 | 4 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 168–329 | 153 | 3 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 174–270 | 65 | 6 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 179–259 | 53 | 6 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 197–303 | 104 | 3 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 222–257 | 10 | 4 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 237–329 | 87 | 4 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 245–329 | 76 | 3 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 251–307 | 57 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 253–329 | 71 | 4 | Undefined position; Undefined team |
| `47` | `69` | Position_Unknown | Team_Unknown | 278–327 | 29 | 4 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 280–303 | 15 | 4 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 284–303 | 16 | 2 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 284–286 | 3 | 1 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 309–318 | 6 | 2 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 310–311 | 2 | 1 | Undefined position; Undefined team |
| `53` | `76` | Position_Unknown | Team_Unknown | 311–319 | 5 | 2 | Undefined position; Undefined team |
| `54` | `79` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |
| `55` | `80` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 35 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 35 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 70 |
| Missing visible bounding boxes during action | 131 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [16-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-271] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-307] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-56] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-329] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-303] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [16-33] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [35-69] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [70-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-33] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-72] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-172] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-184] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-329] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-329] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-70] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-105] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-329] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-190] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-252] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-76] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-92] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [151-171] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-72] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-99] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-109] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-129] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-329] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-196] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-209] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-175] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-185] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-166] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-306] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-320] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-290] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-304] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-186] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-329] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-181] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-219] for track '38' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-248] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-221] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-247] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-253] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-268] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-303] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-248] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-261] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-276] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-307] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-264] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-306] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-321] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-286] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-309] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-327] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-303] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '53' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.

</details>