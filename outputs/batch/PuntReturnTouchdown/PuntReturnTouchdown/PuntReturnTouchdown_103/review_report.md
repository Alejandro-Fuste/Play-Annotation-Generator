# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_103

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_103`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 359
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 154
- **Validation Warnings:** 181
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 140
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Position_Unknown | Team_Unknown | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `11` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `16` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `18` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `3` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `8` | `Group` | 0 | START | 0 | 44 |
| ✅ EXACT | `Action_LongSnap` | Position_Unknown | `1` | `1` | 45 | START | 45 | 84 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 76 | END | 76 | 76 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 101 | START | 101 | 114 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `21` | `21` | 343 | START | 343 | 352 |

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
- **Visible Frames:** 0–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 106 | 62 | inferred_complete_timeline |
| `Action_None` | 111 | 166 | 56 | inferred_complete_timeline |
| `Action_None` | 192 | 359 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 258 | 214 | inferred_complete_timeline |
| `Action_None` | 281 | 359 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 138 | 94 | inferred_complete_timeline |
| `Action_None` | 140 | 152 | 13 | inferred_complete_timeline |
| `Action_None` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_None` | 161 | 207 | 47 | inferred_complete_timeline |
| `Action_None` | 210 | 340 | 131 | inferred_complete_timeline |
| `Action_None` | 346 | 359 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 99 | 55 | inferred_complete_timeline |
| `Action_None` | 102 | 160 | 59 | inferred_complete_timeline |
| `Action_None` | 162 | 176 | 15 | inferred_complete_timeline |
| `Action_None` | 202 | 307 | 106 | inferred_complete_timeline |
| `Action_None` | 310 | 316 | 7 | inferred_complete_timeline |
| `Action_None` | 318 | 359 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 98 | 54 | inferred_complete_timeline |
| `Action_None` | 110 | 163 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 149 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_None` | 77 | 100 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 101 | 114 | 14 | inferred_complete_timeline |
| `Action_None` | 115 | 132 | 18 | inferred_complete_timeline |
| `Action_None` | 137 | 151 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 149 | 105 | inferred_complete_timeline |
| `Action_None` | 151 | 308 | 158 | inferred_complete_timeline |
| `Action_None` | 310 | 315 | 6 | inferred_complete_timeline |
| `Action_None` | 318 | 320 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 136 | 92 | inferred_complete_timeline |
| `Action_None` | 138 | 141 | 4 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 88 | 44 | inferred_complete_timeline |
| `Action_None` | 91 | 133 | 43 | inferred_complete_timeline |
| `Action_None` | 135 | 359 | 225 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 107 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 68 | 24 | inferred_complete_timeline |
| `Action_None` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 84 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 92 | 48 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 58 | 14 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 98 | 54 | inferred_complete_timeline |
| `Action_None` | 101 | 133 | 33 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 157 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 162 | 118 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 195 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 128 | 84 | inferred_complete_timeline |
| `Action_None` | 146 | 152 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 190 | 146 | inferred_complete_timeline |
| `Action_None` | 192 | 286 | 95 | inferred_complete_timeline |
| `Action_None` | 290 | 292 | 3 | inferred_complete_timeline |
| `Action_None` | 301 | 307 | 7 | inferred_complete_timeline |
| `Action_None` | 310 | 323 | 14 | inferred_complete_timeline |
| `Action_None` | 325 | 359 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 136 | 92 | inferred_complete_timeline |
| `Action_None` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_None` | 146 | 153 | 8 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 167 | 5 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_None` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_None` | 185 | 189 | 5 | inferred_complete_timeline |
| `Action_None` | 191 | 198 | 8 | inferred_complete_timeline |
| `Action_None` | 200 | 216 | 17 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 338 | 116 | inferred_complete_timeline |
| `Action_None` | 342 | 359 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–84 | 85 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 63–359 | 287 | 6 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 104–111 | 8 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 119–151 | 18 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 128–132 | 5 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 130–131 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 150–342 | 160 | 3 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 173–174 | 2 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 179–359 | 181 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 181–211 | 23 | 5 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 191–237 | 47 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 192–359 | 155 | 4 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 194–359 | 162 | 2 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 220–359 | 137 | 3 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 224–359 | 131 | 3 | Undefined position; Undefined team |
| `36` | `58` | Position_Unknown | Team_Unknown | 227–349 | 118 | 4 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 243–244 | 2 | 1 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 245–278 | 32 | 3 | Undefined position; Undefined team |
| `40` | `62` | Position_Unknown | Team_Unknown | 250–252 | 3 | 1 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 259–345 | 76 | 3 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 262–359 | 35 | 2 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 266–359 | 94 | 1 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 279–287 | 4 | 2 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 293–294 | 2 | 1 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 298–359 | 62 | 1 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 314–316 | 3 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 321–322 | 2 | 1 | Undefined position; Undefined team |
| `49` | `72` | Position_Unknown | Team_Unknown | 347–359 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 117 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 208: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [45-136] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [45-84] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-136] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-153] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-198] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-216] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-338] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-307] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-316] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-162] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-128] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-151] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-149] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-286] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-307] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-323] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-258] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-359] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-88] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-106] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-166] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-138] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-207] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-340] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-149] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-308] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-98] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-133] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-98] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-163] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-157] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-252] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-302] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-342] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-132] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-257] for track '27' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-336] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-237] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-294] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-302] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-316] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-359] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-295] for track '34' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-307] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-359] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-238] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-342] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-349] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-260] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-278] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-275] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-287] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-345] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>