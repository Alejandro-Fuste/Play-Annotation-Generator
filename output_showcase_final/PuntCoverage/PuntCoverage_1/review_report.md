# Play-Annotation-Generator Annotation Review — PuntCoverage_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_1`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 143
- **Validation Warnings:** 145
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 126
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `27` | `22` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `27` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Position_Unknown | Team_Unknown | `43` | `29` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `6` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `8` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `9` | `Group` | 0 | START | 0 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `19` | `19` | 2 | START | 2 | 20 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `9` | `9` | 28 | END | 28 | 28 |
| ✅ EXACT | `Action_PuntBall` | Punter | `9` | `9` | 64 | START | 64 | 73 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `27` | `22` | 167 | START | 167 | 177 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `27` | `22` | 193 | START | 194 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Position_Unknown | `43` | `29` | 196 | START | 209 | 210 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 22 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 166 | 142 | inferred_complete_timeline |
| `Action_None` | 168 | 182 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 204 | 203 | inferred_complete_timeline |
| `Action_None` | 206 | 211 | 6 | inferred_complete_timeline |
| `Action_None` | 218 | 226 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_LongSnap` | 2 | 20 | 19 | inferred_complete_timeline |
| `Action_LongSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_LongSnap` | 34 | 49 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 51 | 63 | 13 | inferred_complete_timeline |
| `Action_None` | 64 | 120 | 57 | inferred_complete_timeline |
| `Action_None` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_None` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 205 | 19 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 254 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 70 | 69 | inferred_complete_timeline |
| `Action_None` | 72 | 81 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 98 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 28 | 1 | inferred_complete_timeline |
| `Action_None` | 29 | 63 | 35 | inferred_complete_timeline |
| `Action_PuntBall` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_None` | 74 | 114 | 41 | inferred_complete_timeline |
| `Action_None` | 122 | 142 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 110 | 109 | inferred_complete_timeline |
| `Action_None` | 123 | 144 | 22 | inferred_complete_timeline |
| `Action_None` | 147 | 156 | 10 | inferred_complete_timeline |
| `Action_None` | 158 | 181 | 24 | inferred_complete_timeline |
| `Action_None` | 188 | 197 | 10 | inferred_complete_timeline |
| `Action_None` | 208 | 299 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 32 | 31 | inferred_complete_timeline |
| `Action_None` | 35 | 139 | 105 | inferred_complete_timeline |
| `Action_None` | 141 | 153 | 13 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 170 | 4 | inferred_complete_timeline |
| `Action_None` | 181 | 230 | 50 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 22 | 21 | inferred_complete_timeline |
| `Action_None` | 25 | 28 | 4 | inferred_complete_timeline |
| `Action_None` | 30 | 85 | 56 | inferred_complete_timeline |
| `Action_None` | 88 | 171 | 84 | inferred_complete_timeline |
| `Action_None` | 173 | 203 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 137 | 136 | inferred_complete_timeline |
| `Action_None` | 139 | 168 | 30 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 299 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 46 | 45 | inferred_complete_timeline |
| `Action_None` | 50 | 89 | 40 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 285 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 26 | 25 | inferred_complete_timeline |
| `Action_None` | 35 | 157 | 123 | inferred_complete_timeline |
| `Action_None` | 160 | 202 | 43 | inferred_complete_timeline |
| `Action_None` | 215 | 285 | 71 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 123 | 122 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 139 | 10 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–299 | 289 | 5 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–129 | 112 | 7 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 128–299 | 169 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 131–199 | 62 | 4 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 149–166 | 8 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 164–249 | 86 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 175–248 | 61 | 5 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 200–299 | 78 | 3 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 201–215 | 11 | 2 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 203–213 | 10 | 2 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 209–299 | 86 | 3 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 228–299 | 72 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 243–299 | 57 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 247–294 | 41 | 4 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 259–299 | 41 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 263–299 | 24 | 4 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 272–299 | 28 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 277–299 | 22 | 2 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 288–299 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `19` (4 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `27` (Position_Unknown): Annotated start 193 != Inferred start 194
- ⚠️ Ambiguous match for action `Action_Tackle` and target `43` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 104 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '25' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [2-204] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-226] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-178] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-46] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-285] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-299] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-28] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-45] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-52] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-26] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-157] for track '7' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-202] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-285] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-110] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-144] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-181] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-114] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-142] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-22] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-166] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-137] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-168] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-70] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-81] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-139] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-22] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-153] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-230] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [2-20] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [24-25] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [34-49] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-120] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-254] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-299] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-177] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-262] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [194-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-245] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-215] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [209-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-285] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-281] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-299] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-285] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-299] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>