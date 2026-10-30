# Play-Annotation-Generator Annotation Review — FieldGoalBlock_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_51`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 160
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `11` | `11` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `9` | `9` |
| ✅ EXACT | `Action_BlockKick` | Right_Edge_Rusher | defense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `10` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `11` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `15` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `16` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `20` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `5` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `6` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `9` | `Group` | 0 | START | 0 | 60 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `11` | `11` | 38 | START | 38 | 53 |
| ✅ EXACT | `Action_KickBall` | Kicker | `9` | `9` | 61 | START | 61 | 68 |
| ✅ EXACT | `Action_BlockKick` | Right_Edge_Rusher | `3` | `3` | 68 | START | 68 | 79 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PlaceBall` | 38 | 53 | 16 | inferred_complete_timeline |
| `Action_None` | 54 | 269 | 216 | inferred_complete_timeline |
| `Action_None` | 273 | 279 | 7 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 310 | 23 | inferred_complete_timeline |
| `Action_None` | 321 | 323 | 3 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_KickBall` | 61 | 68 | 8 | inferred_complete_timeline |
| `Action_None` | 69 | 311 | 243 | inferred_complete_timeline |
| `Action_None` | 313 | 329 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 150 | 90 | inferred_complete_timeline |
| `Action_None` | 152 | 290 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_None` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 111 | 51 | inferred_complete_timeline |
| `Action_None` | 113 | 131 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 329 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_None` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_None` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_None` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 329 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 49 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 60 | 10 | inferred_complete_timeline |
| `Action_None` | 61 | 143 | 83 | inferred_complete_timeline |
| `Action_None` | 145 | 270 | 126 | inferred_complete_timeline |
| `Action_None` | 313 | 329 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_None` | 97 | 301 | 205 | inferred_complete_timeline |
| `Action_None` | 303 | 329 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 329 | 269 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 187 | 127 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 231 | 23 | inferred_complete_timeline |
| `Action_None` | 234 | 326 | 93 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 209 | 149 | inferred_complete_timeline |
| `Action_None` | 211 | 283 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 213 | 153 | inferred_complete_timeline |
| `Action_None` | 219 | 225 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 215 | 155 | inferred_complete_timeline |
| `Action_None` | 218 | 329 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 51 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 60 | 1 | inferred_complete_timeline |
| `Action_None` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_None` | 63 | 97 | 35 | inferred_complete_timeline |
| `Action_None` | 99 | 131 | 33 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 60 | 25 | inferred_complete_timeline |
| `Action_None` | 61 | 91 | 31 | inferred_complete_timeline |
| `Action_None` | 93 | 98 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 60 | 8 | inferred_complete_timeline |
| `Action_None` | 63 | 73 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–310
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 310 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_BlockKick` | 68 | 79 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 21–66 | 10 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 54–89 | 34 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 66–329 | 258 | 4 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 75–76 | 2 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 78–329 | 201 | 2 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 88–329 | 228 | 6 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 94–329 | 236 | 1 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 99–329 | 231 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 107–329 | 222 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 124–150 | 14 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 155–310 | 154 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 171–174 | 4 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 172–329 | 156 | 2 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 190–194 | 4 | 2 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 200–203 | 4 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 214–218 | 5 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 216–220 | 5 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 222–329 | 108 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 252–321 | 50 | 5 | Undefined position; Undefined team |
| `42` | `50` | Position_Unknown | Team_Unknown | 284–329 | 42 | 2 | Undefined position; Undefined team |
| `43` | `51` | Position_Unknown | Team_Unknown | 285–329 | 19 | 4 | Undefined position; Undefined team |
| `44` | `52` | Position_Unknown | Team_Unknown | 288–310 | 23 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 322–328 | 5 | 2 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 107 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-51] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-310] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [68-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-213] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-187] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-231] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-326] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-56] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '8' starts at frame 61, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [61-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-97] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-131] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-311] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-290] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-269] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-279] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-310] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-209] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-283] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-73] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-301] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-111] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-131] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-49] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-270] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-23] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-58] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-83] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-145] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-157] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-193] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-286] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-295] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-125] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-171] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-310] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-326] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-329] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-291] for track '41' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-301] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-290] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-304] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-310] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '45' has 1 frames without a visible bounding box.
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

</details>