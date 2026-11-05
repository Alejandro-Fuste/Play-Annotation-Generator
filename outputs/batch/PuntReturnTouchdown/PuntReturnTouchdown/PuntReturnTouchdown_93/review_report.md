# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_93

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_93`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 73
- **Ball Tracks:** 0
- **Action Segments:** 221
- **Validation Warnings:** 295
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 205
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `27` | `24` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `27` | `24` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Personal_Protector1 | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `11` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `20` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | `5` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `7` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | `9` | `Group` | 0 | START | 0 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `20` | `20` | 98 | START | 98 | 115 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 126 | END | 126 | 126 |
| ✅ EXACT | `Action_PuntBall` | Punter | `6` | `6` | 155 | START | 155 | 164 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `27` | `24` | 247 | START | 247 | 274 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `27` | `24` | 284 | START | 284 | 358 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Personal_Protector1 | `7` | `7` | 564 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 144 | 47 | inferred_complete_timeline |
| `Action_None` | 155 | 162 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 245 | 148 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 257 | 3 | inferred_complete_timeline |
| `Action_None` | 259 | 261 | 3 | inferred_complete_timeline |
| `Action_None` | 273 | 413 | 141 | inferred_complete_timeline |
| `Action_None` | 415 | 479 | 65 | inferred_complete_timeline |
| `Action_None` | 492 | 569 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_LongSnap` | 98 | 115 | 18 | inferred_complete_timeline |
| `Action_LongSnap` | 120 | 140 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 206 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–313
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 171 | 74 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 215 | 37 | inferred_complete_timeline |
| `Action_None` | 218 | 313 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_SnapReceive` | 126 | 126 | 1 | inferred_complete_timeline |
| `Action_None` | 127 | 154 | 28 | inferred_complete_timeline |
| `Action_PuntBall` | 155 | 164 | 10 | inferred_complete_timeline |
| `Action_None` | 165 | 202 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 177 | 80 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 184 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 192 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 171 | 74 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 203 | 214 | 12 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |
| `Action_None` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_None` | 236 | 238 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 136 | 39 | inferred_complete_timeline |
| `Action_None` | 139 | 141 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 143 | 46 | inferred_complete_timeline |
| `Action_None` | 147 | 155 | 9 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 145 | 48 | inferred_complete_timeline |
| `Action_None` | 149 | 154 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 183 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 122 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 145 | 48 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 151 | 163 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 169 | 72 | inferred_complete_timeline |
| `Action_None` | 171 | 245 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 118 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 184 | 87 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 236 | 39 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |
| `Action_None` | 247 | 308 | 62 | inferred_complete_timeline |
| `Action_None` | 310 | 322 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 189 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–154 | 138 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 184–209 | 8 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 196–199 | 4 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 199–264 | 44 | 8 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 200–358 | 159 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 201–231 | 31 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 203–454 | 230 | 7 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 203–205 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 203–216 | 11 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 210–270 | 49 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 213–367 | 127 | 10 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 230–231 | 2 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 237–569 | 330 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 240–242 | 3 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 244–363 | 117 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 252–256 | 5 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 252–255 | 4 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 261–274 | 14 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 280–569 | 282 | 4 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 282–334 | 41 | 4 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 282–569 | 282 | 3 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 288–291 | 4 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 290–397 | 24 | 3 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 290–293 | 4 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 293–569 | 276 | 2 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 298–569 | 257 | 5 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 298–402 | 77 | 3 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 302–356 | 41 | 4 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 313–569 | 215 | 11 | Undefined position; Undefined team |
| `50` | `65` | Position_Unknown | Team_Unknown | 315–372 | 58 | 1 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 322–395 | 74 | 1 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |
| `53` | `71` | Position_Unknown | Team_Unknown | 322–396 | 67 | 3 | Undefined position; Undefined team |
| `54` | `72` | Position_Unknown | Team_Unknown | 323–346 | 22 | 2 | Undefined position; Undefined team |
| `55` | `73` | Position_Unknown | Team_Unknown | 325–326 | 2 | 1 | Undefined position; Undefined team |
| `56` | `75` | Position_Unknown | Team_Unknown | 332–569 | 238 | 1 | Undefined position; Undefined team |
| `57` | `77` | Position_Unknown | Team_Unknown | 335–569 | 235 | 1 | Undefined position; Undefined team |
| `58` | `78` | Position_Unknown | Team_Unknown | 335–455 | 104 | 4 | Undefined position; Undefined team |
| `59` | `80` | Position_Unknown | Team_Unknown | 337–345 | 8 | 2 | Undefined position; Undefined team |
| `60` | `82` | Position_Unknown | Team_Unknown | 345–569 | 205 | 2 | Undefined position; Undefined team |
| `61` | `84` | Position_Unknown | Team_Unknown | 356–569 | 194 | 3 | Undefined position; Undefined team |
| `62` | `85` | Position_Unknown | Team_Unknown | 366–394 | 29 | 1 | Undefined position; Undefined team |
| `63` | `86` | Position_Unknown | Team_Unknown | 366–569 | 187 | 4 | Undefined position; Undefined team |
| `64` | `87` | Position_Unknown | Team_Unknown | 366–569 | 197 | 3 | Undefined position; Undefined team |
| `65` | `88` | Position_Unknown | Team_Unknown | 367–502 | 132 | 3 | Undefined position; Undefined team |
| `66` | `89` | Position_Unknown | Team_Unknown | 383–569 | 178 | 3 | Undefined position; Undefined team |
| `67` | `90` | Position_Unknown | Team_Unknown | 384–569 | 178 | 2 | Undefined position; Undefined team |
| `68` | `91` | Position_Unknown | Team_Unknown | 384–455 | 71 | 2 | Undefined position; Undefined team |
| `69` | `94` | Position_Unknown | Team_Unknown | 404–568 | 165 | 1 | Undefined position; Undefined team |
| `70` | `95` | Position_Unknown | Team_Unknown | 405–569 | 130 | 5 | Undefined position; Undefined team |
| `71` | `98` | Position_Unknown | Team_Unknown | 412–569 | 150 | 3 | Undefined position; Undefined team |
| `72` | `101` | Position_Unknown | Team_Unknown | 473–567 | 93 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `20` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `7` (Personal_Protector1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 53 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 53 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 106 |
| Missing visible bounding boxes during action | 184 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 188: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CrossGoalLine' for track '7' has invalid range: start=564, end=206. Clamping end to start.
- ⚠️ Action 'Action_None' range [98-245] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-413] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-479] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-569] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-245] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-189] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-184] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-236] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-308] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-322] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-313] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-202] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-206] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-214] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-177] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [98-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [120-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-213] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-235] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-246] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [284-358] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-231] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-262] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-283] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-361] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-454] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-211] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-250] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-270] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-247] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-334] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-348] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-355] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-393] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-411] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-313] for track '34' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-363] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-256] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-274] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-292] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-307] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-442] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-295] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-315] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-331] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-569] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-303] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-314] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-400] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-337] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-367] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-382] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-412] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-333] for track '47' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-356] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-402] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-319] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-325] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-356] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-342] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-357] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-384] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-396] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-468] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-473] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-483] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-372] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-395] for track '51' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-342] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-391] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-396] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-346] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-569] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-339] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-405] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-455] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-342] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-374] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-363] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-393] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-569] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-394] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-377] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-437] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-371] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-452] for track '64' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-497] for track '65' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-502] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-396] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-542] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-390] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-400] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-455] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-568] for track '69' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-407] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-428] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-446] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-503] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-555] for track '71' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-566] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-549] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-559] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-567] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>