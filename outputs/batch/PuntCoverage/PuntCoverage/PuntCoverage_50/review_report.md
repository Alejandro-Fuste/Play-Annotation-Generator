# Play-Annotation-Generator Annotation Review — PuntCoverage_50

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_50`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 359
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 131
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 112
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `26` | `25` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `26` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Left_Guard | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `6` | `Group` | 0 | START | 0 | 264 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `5` | `5` | 1 | START | 1 | 50 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 32 | END | 32 | 32 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 51 | START | 51 | 72 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `26` | `25` | 159 | START | 159 | 171 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `26` | `25` | 181 | START | 181 | 220 |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Left_Guard | `6` | `6` | 287 | START | 287 | 295 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 264 | 265 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 272 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 286 | 12 | inferred_complete_timeline |
| `Action_Tackle` | 287 | 295 | 9 | inferred_complete_timeline |
| `Action_Tackle` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_Tackle` | 308 | 325 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 126 | 126 | inferred_complete_timeline |
| `Action_None` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_None` | 137 | 142 | 6 | inferred_complete_timeline |
| `Action_None` | 147 | 157 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 1 | 50 | 50 | inferred_complete_timeline |
| `Action_None` | 51 | 83 | 33 | inferred_complete_timeline |
| `Action_None` | 88 | 192 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 137 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 10 | 10 | inferred_complete_timeline |
| `Action_None` | 12 | 20 | 9 | inferred_complete_timeline |
| `Action_None` | 24 | 28 | 5 | inferred_complete_timeline |
| `Action_None` | 31 | 47 | 17 | inferred_complete_timeline |
| `Action_None` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_None` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_None` | 71 | 141 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 129 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 32 | 1 | inferred_complete_timeline |
| `Action_None` | 33 | 50 | 18 | inferred_complete_timeline |
| `Action_PuntBall` | 51 | 72 | 22 | inferred_complete_timeline |
| `Action_None` | 73 | 101 | 29 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–342
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 34 | 34 | inferred_complete_timeline |
| `Action_None` | 36 | 100 | 65 | inferred_complete_timeline |
| `Action_None` | 106 | 127 | 22 | inferred_complete_timeline |
| `Action_None` | 130 | 172 | 43 | inferred_complete_timeline |
| `Action_None` | 238 | 342 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–345
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 156 | 156 | inferred_complete_timeline |
| `Action_None` | 158 | 345 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 31 | 31 | inferred_complete_timeline |
| `Action_None` | 41 | 48 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–344
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 54 | 54 | inferred_complete_timeline |
| `Action_None` | 56 | 103 | 48 | inferred_complete_timeline |
| `Action_None` | 109 | 178 | 70 | inferred_complete_timeline |
| `Action_None` | 182 | 196 | 15 | inferred_complete_timeline |
| `Action_None` | 198 | 328 | 131 | inferred_complete_timeline |
| `Action_None` | 343 | 344 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 67 | 67 | inferred_complete_timeline |
| `Action_None` | 69 | 87 | 19 | inferred_complete_timeline |
| `Action_None` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 141 | 37 | inferred_complete_timeline |
| `Action_None` | 145 | 156 | 12 | inferred_complete_timeline |
| `Action_None` | 168 | 172 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 179 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 60 | 60 | inferred_complete_timeline |
| `Action_None` | 108 | 120 | 13 | inferred_complete_timeline |
| `Action_None` | 123 | 194 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 131 | 131 | inferred_complete_timeline |
| `Action_None` | 136 | 268 | 133 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 280 | 359 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 90 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 204 | 204 | inferred_complete_timeline |
| `Action_None` | 211 | 359 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 21 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 34 | 34 | inferred_complete_timeline |
| `Action_None` | 36 | 39 | 4 | inferred_complete_timeline |
| `Action_None` | 42 | 47 | 6 | inferred_complete_timeline |
| `Action_None` | 52 | 325 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 142 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 72 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 131 | 131 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 40–176 | 112 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 75–359 | 285 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 96–147 | 52 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 103–240 | 125 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 140–220 | 81 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 191–359 | 157 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 193–195 | 3 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 206–359 | 146 | 5 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 212–359 | 148 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 228–359 | 113 | 4 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 231–232 | 2 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 249–359 | 110 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 249–359 | 111 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 253–359 | 86 | 2 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 264–359 | 96 | 1 | Undefined position; Undefined team |
| `37` | `40` | Position_Unknown | Team_Unknown | 267–338 | 72 | 1 | Undefined position; Undefined team |
| `38` | `41` | Position_Unknown | Team_Unknown | 291–359 | 69 | 1 | Undefined position; Undefined team |
| `39` | `42` | Position_Unknown | Team_Unknown | 298–344 | 46 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_Tackle` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 94 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [1-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-345] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-72] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-359] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-83] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-264] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-272] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [287-295] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [301-302] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [308-325] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-39] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-325] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-21] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-31] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-54] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-178] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-328] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-268] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-359] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-126] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-157] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-156] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-60] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-194] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-100] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-127] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-172] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-342] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-10] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-20] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-28] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-141] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-54] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-134] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-147] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-141] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-193] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-240] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [181-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-273] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-339] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-316] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-331] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-314] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-264] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-338] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-359] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-302] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-344] for track '39' has 1 frames without a visible bounding box.
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

</details>