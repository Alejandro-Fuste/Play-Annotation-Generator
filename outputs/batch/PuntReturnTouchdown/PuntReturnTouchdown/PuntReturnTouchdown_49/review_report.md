# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_49`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 68
- **Ball Tracks:** 0
- **Action Segments:** 172
- **Validation Warnings:** 246
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 157
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `40` | `32` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `40` | `32` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `77` | `65` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `10` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `14` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `20` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `6` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `8` | `Group` | 0 | START | 0 | 84 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `13` | `13` | 85 | START | 85 | 140 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 117 | END | 117 | 117 |
| ✅ EXACT | `Action_PuntBall` | Punter | `12` | `12` | 141 | START | 141 | 154 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `40` | `32` | 256 | START | 256 | 262 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `40` | `32` | 275 | START | 275 | 290 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `77` | `65` | 588 | START | 588 | 599 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 125 | 41 | inferred_complete_timeline |
| `Action_None` | 127 | 180 | 54 | inferred_complete_timeline |
| `Action_None` | 182 | 274 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 170 | 86 | inferred_complete_timeline |
| `Action_None` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_None` | 190 | 233 | 44 | inferred_complete_timeline |
| `Action_None` | 240 | 248 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 217 | 133 | inferred_complete_timeline |
| `Action_None` | 226 | 237 | 12 | inferred_complete_timeline |
| `Action_None` | 239 | 243 | 5 | inferred_complete_timeline |
| `Action_None` | 248 | 255 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_LongSnap` | 85 | 140 | 56 | inferred_complete_timeline |
| `Action_None` | 141 | 182 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 95 | 11 | inferred_complete_timeline |
| `Action_None` | 99 | 135 | 37 | inferred_complete_timeline |
| `Action_None` | 139 | 205 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 177 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_SnapReceive` | 117 | 117 | 1 | inferred_complete_timeline |
| `Action_None` | 118 | 140 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 141 | 154 | 14 | inferred_complete_timeline |
| `Action_None` | 155 | 192 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 127 | 43 | inferred_complete_timeline |
| `Action_None` | 144 | 193 | 50 | inferred_complete_timeline |
| `Action_None` | 195 | 245 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 115 | 31 | inferred_complete_timeline |
| `Action_None` | 117 | 201 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 218 | 134 | inferred_complete_timeline |
| `Action_None` | 224 | 266 | 43 | inferred_complete_timeline |
| `Action_None` | 269 | 275 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 197 | 113 | inferred_complete_timeline |
| `Action_None` | 199 | 219 | 21 | inferred_complete_timeline |
| `Action_None` | 222 | 246 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–406
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 406 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 182 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 129 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 84 | 68 | inferred_complete_timeline |
| `Action_None` | 85 | 133 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 105 | 21 | inferred_complete_timeline |
| `Action_None` | 108 | 172 | 65 | inferred_complete_timeline |
| `Action_None` | 174 | 197 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 115 | 31 | inferred_complete_timeline |
| `Action_None` | 158 | 182 | 25 | inferred_complete_timeline |
| `Action_None` | 185 | 222 | 38 | inferred_complete_timeline |
| `Action_None` | 226 | 231 | 6 | inferred_complete_timeline |
| `Action_None` | 239 | 251 | 13 | inferred_complete_timeline |
| `Action_None` | 253 | 258 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 175 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–582 | 577 | 4 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–349 | 348 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–214 | 215 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 111–122 | 10 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 145–156 | 12 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 168–346 | 179 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 168–217 | 34 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 187–195 | 8 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 200–202 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 200–248 | 47 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 203–231 | 29 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 205–208 | 4 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 206–220 | 10 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 228–294 | 66 | 5 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 233–343 | 72 | 3 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 242–263 | 15 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 244–251 | 8 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 256–372 | 112 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 260–492 | 233 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 264–266 | 3 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 284–464 | 170 | 4 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 301–528 | 207 | 6 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 310–486 | 177 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 332–589 | 211 | 4 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 363–586 | 131 | 3 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 375–542 | 165 | 2 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 377–592 | 168 | 4 | Undefined position; Undefined team |
| `46` | `56` | Position_Unknown | Team_Unknown | 379–407 | 25 | 2 | Undefined position; Undefined team |
| `47` | `57` | Position_Unknown | Team_Unknown | 380–599 | 220 | 1 | Undefined position; Undefined team |
| `48` | `58` | Position_Unknown | Team_Unknown | 389–542 | 128 | 8 | Undefined position; Undefined team |
| `49` | `59` | Position_Unknown | Team_Unknown | 394–599 | 206 | 1 | Undefined position; Undefined team |
| `50` | `60` | Position_Unknown | Team_Unknown | 396–599 | 204 | 1 | Undefined position; Undefined team |
| `51` | `61` | Position_Unknown | Team_Unknown | 401–488 | 82 | 4 | Undefined position; Undefined team |
| `52` | `63` | Position_Unknown | Team_Unknown | 402–555 | 153 | 2 | Undefined position; Undefined team |
| `53` | `64` | Position_Unknown | Team_Unknown | 408–451 | 40 | 3 | Undefined position; Undefined team |
| `54` | `65` | Position_Unknown | Team_Unknown | 419–485 | 66 | 2 | Undefined position; Undefined team |
| `55` | `66` | Position_Unknown | Team_Unknown | 423–474 | 52 | 1 | Undefined position; Undefined team |
| `56` | `67` | Position_Unknown | Team_Unknown | 432–490 | 59 | 1 | Undefined position; Undefined team |
| `57` | `68` | Position_Unknown | Team_Unknown | 433–595 | 163 | 1 | Undefined position; Undefined team |
| `58` | `69` | Position_Unknown | Team_Unknown | 434–586 | 153 | 1 | Undefined position; Undefined team |
| `59` | `70` | Position_Unknown | Team_Unknown | 450–492 | 29 | 2 | Undefined position; Undefined team |
| `60` | `71` | Position_Unknown | Team_Unknown | 472–500 | 29 | 1 | Undefined position; Undefined team |
| `61` | `72` | Position_Unknown | Team_Unknown | 485–502 | 18 | 1 | Undefined position; Undefined team |
| `62` | `73` | Position_Unknown | Team_Unknown | 511–528 | 18 | 1 | Undefined position; Undefined team |
| `63` | `74` | Position_Unknown | Team_Unknown | 522–535 | 14 | 1 | Undefined position; Undefined team |
| `64` | `76` | Position_Unknown | Team_Unknown | 548–599 | 52 | 1 | Undefined position; Undefined team |
| `65` | `77` | Position_Unknown | Team_Unknown | 551–599 | 46 | 4 | Undefined position; Undefined team |
| `66` | `78` | Position_Unknown | Team_Unknown | 563–567 | 5 | 1 | Undefined position; Undefined team |
| `67` | `79` | Position_Unknown | Team_Unknown | 576–579 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `40` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ 50 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 50 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 100 |
| Missing visible bounding boxes during action | 140 |
| Track-related warning | 3 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 100: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 100: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 100: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [85-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-129] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-115] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-182] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-222] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-251] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-182] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-406] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-197] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-246] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-245] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-105] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-172] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-197] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-582] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-260] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-349] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [85-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-217] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-237] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-214] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-266] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-233] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-248] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-274] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-95] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-205] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-156] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-346] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-217] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-248] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-231] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [275-290] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [292-294] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-324] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-343] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-253] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-251] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-266] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-367] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-372] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-492] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-369] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-408] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-464] for track '39' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-354] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-391] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-403] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-454] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-505] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-528] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-486] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-415] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-489] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-589] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-437] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-499] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-586] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-484] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-542] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-458] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-508] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-513] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-592] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-385] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-407] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-478] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-482] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-489] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-495] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-503] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-507] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-530] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-542] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-420] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-431] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-442] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-488] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-546] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-555] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-422] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-430] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-451] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-472] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-485] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-474] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-490] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-595] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-586] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-452] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-492] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-500] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-502] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-528] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-535] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-599] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [551-555] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [558-559] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-567] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-579] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>