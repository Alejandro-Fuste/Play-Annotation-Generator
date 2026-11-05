# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_4`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 77
- **Ball Tracks:** 0
- **Action Segments:** 179
- **Validation Warnings:** 277
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 163
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `10` | `10` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `36` | `29` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `36` | `29` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `36` | `29` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `0` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `10` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `15` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `2` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `3` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `9` | `Group` | 0 | START | 0 | 43 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `14` | `14` | 44 | START | 44 | 90 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `10` | `10` | 69 | END | 69 | 69 |
| ✅ EXACT | `Action_PuntBall` | Punter | `10` | `10` | 91 | START | 91 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchPunt` | Position_Unknown | `36` | `29` | 216 | START | 216 | 217 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `36` | `29` | 231 | START | 231 | 553 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | `36` | `29` | 554 | START | 554 | 561 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 84 | 41 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_None` | 99 | 138 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_LongSnap` | 44 | 90 | 47 | inferred_complete_timeline |
| `Action_None` | 91 | 137 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 131 | 88 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 206 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 197 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 230 | 187 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 300 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_SnapReceive` | 69 | 69 | 1 | inferred_complete_timeline |
| `Action_None` | 70 | 90 | 21 | inferred_complete_timeline |
| `Action_PuntBall` | 91 | 103 | 13 | inferred_complete_timeline |
| `Action_None` | 104 | 130 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 68 | 25 | inferred_complete_timeline |
| `Action_None` | 71 | 216 | 146 | inferred_complete_timeline |
| `Action_None` | 219 | 221 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 43 | 12 | inferred_complete_timeline |
| `Action_None` | 44 | 55 | 12 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 215 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 206 | 163 | inferred_complete_timeline |
| `Action_None` | 208 | 215 | 8 | inferred_complete_timeline |
| `Action_None` | 225 | 293 | 69 | inferred_complete_timeline |
| `Action_None` | 296 | 320 | 25 | inferred_complete_timeline |
| `Action_None` | 325 | 343 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 205 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 209 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 110 | 67 | inferred_complete_timeline |
| `Action_None` | 113 | 115 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 127 | 84 | inferred_complete_timeline |
| `Action_None` | 129 | 201 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 181 | 138 | inferred_complete_timeline |
| `Action_None` | 183 | 208 | 26 | inferred_complete_timeline |
| `Action_None` | 210 | 215 | 6 | inferred_complete_timeline |
| `Action_None` | 218 | 224 | 7 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_None` | 247 | 304 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 110 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 15–216 | 169 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 19–213 | 188 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 81–263 | 183 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 101–371 | 271 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 115–195 | 79 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 126–174 | 38 | 4 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 144–348 | 205 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 145–294 | 97 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 147–206 | 59 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 160–174 | 11 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 161–195 | 29 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 161–164 | 4 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 162–569 | 400 | 8 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 191–293 | 103 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 191–192 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 223–313 | 91 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 231–234 | 4 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 245–309 | 65 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 246–281 | 36 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 249–293 | 45 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 255–359 | 105 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 279–292 | 9 | 2 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 280–364 | 85 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 285–569 | 208 | 5 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 290–316 | 27 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 302–308 | 7 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 318–355 | 38 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 327–518 | 183 | 5 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 327–479 | 153 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 329–331 | 3 | 1 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 335–400 | 66 | 1 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 351–484 | 132 | 2 | Undefined position; Undefined team |
| `49` | `68` | Position_Unknown | Team_Unknown | 355–382 | 28 | 1 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 415–569 | 154 | 2 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 415–455 | 14 | 3 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 420–421 | 2 | 1 | Undefined position; Undefined team |
| `53` | `77` | Position_Unknown | Team_Unknown | 420–436 | 13 | 3 | Undefined position; Undefined team |
| `54` | `81` | Position_Unknown | Team_Unknown | 432–569 | 134 | 3 | Undefined position; Undefined team |
| `55` | `83` | Position_Unknown | Team_Unknown | 434–569 | 135 | 2 | Undefined position; Undefined team |
| `56` | `84` | Position_Unknown | Team_Unknown | 434–556 | 121 | 2 | Undefined position; Undefined team |
| `57` | `86` | Position_Unknown | Team_Unknown | 438–439 | 2 | 1 | Undefined position; Undefined team |
| `58` | `88` | Position_Unknown | Team_Unknown | 441–565 | 100 | 6 | Undefined position; Undefined team |
| `59` | `89` | Position_Unknown | Team_Unknown | 445–494 | 46 | 2 | Undefined position; Undefined team |
| `60` | `90` | Position_Unknown | Team_Unknown | 445–451 | 7 | 1 | Undefined position; Undefined team |
| `61` | `91` | Position_Unknown | Team_Unknown | 450–542 | 93 | 1 | Undefined position; Undefined team |
| `62` | `92` | Position_Unknown | Team_Unknown | 453–520 | 68 | 1 | Undefined position; Undefined team |
| `63` | `93` | Position_Unknown | Team_Unknown | 458–460 | 3 | 1 | Undefined position; Undefined team |
| `64` | `94` | Position_Unknown | Team_Unknown | 460–569 | 101 | 4 | Undefined position; Undefined team |
| `65` | `95` | Position_Unknown | Team_Unknown | 467–543 | 76 | 2 | Undefined position; Undefined team |
| `66` | `96` | Position_Unknown | Team_Unknown | 468–522 | 43 | 2 | Undefined position; Undefined team |
| `67` | `97` | Position_Unknown | Team_Unknown | 477–534 | 23 | 3 | Undefined position; Undefined team |
| `68` | `98` | Position_Unknown | Team_Unknown | 478–481 | 4 | 1 | Undefined position; Undefined team |
| `69` | `103` | Position_Unknown | Team_Unknown | 512–534 | 12 | 4 | Undefined position; Undefined team |
| `70` | `104` | Position_Unknown | Team_Unknown | 520–521 | 2 | 1 | Undefined position; Undefined team |
| `71` | `105` | Position_Unknown | Team_Unknown | 531–569 | 36 | 2 | Undefined position; Undefined team |
| `72` | `108` | Position_Unknown | Team_Unknown | 545–555 | 5 | 2 | Undefined position; Undefined team |
| `73` | `109` | Position_Unknown | Team_Unknown | 547–561 | 15 | 1 | Undefined position; Undefined team |
| `74` | `110` | Position_Unknown | Team_Unknown | 549–550 | 2 | 1 | Undefined position; Undefined team |
| `75` | `111` | Position_Unknown | Team_Unknown | 566–569 | 4 | 1 | Undefined position; Undefined team |
| `76` | `112` | Position_Unknown | Team_Unknown | 566–567 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CatchPunt` and target `36` (2 segments found)
- ⚠️ Ambiguous match for action `Action_CrossGoalLine` and target `36` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 61 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 61 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 122 |
| Missing visible bounding boxes during action | 152 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [44-197] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-127] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-131] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-84] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-304] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-205] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-110] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-216] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-206] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-293] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-320] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-343] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-230] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-300] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-209] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-215] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-26] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-213] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-371] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-195] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-145] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-168] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-348] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-220] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-294] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-181] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-170] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-215] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchPunt' range [216-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '29' starts at frame 224, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [224-230] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-553] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [554-561] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-293] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-313] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-309] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-281] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-293] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-359] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-285] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-364] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-293] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-389] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-561] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-316] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-308] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-355] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-381] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-389] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-395] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-514] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-479] for track '45' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-400] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-452] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-484] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-382] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-561] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-423] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-449] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-426] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-431] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-561] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-566] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-561] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-569] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-544] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-556] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-484] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-501] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-507] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-514] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-561] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-482] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-494] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-451] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-542] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-520] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-460] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-539] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-551] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-561] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-528] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-543] for track '65' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-506] for track '66' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-522] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-493] for track '67' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-498] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-534] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-481] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-514] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-524] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-531] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-561] for track '71' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-547] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-561] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>