# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_33`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 359
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 191
- **Validation Warnings:** 225
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 177
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `13` | `13` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `1` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `13` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `15` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `16` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `3` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `7` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `9` | `Group` | 0 | START | 0 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `11` | `11` | 66 | START | 66 | 105 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `13` | `13` | 92 | END | 92 | 92 |
| ✅ EXACT | `Action_PuntBall` | Punter | `13` | `13` | 122 | START | 122 | 135 |

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
- **Visible Frames:** 0–359
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 222 | 157 | inferred_complete_timeline |
| `Action_None` | 225 | 267 | 43 | inferred_complete_timeline |
| `Action_None` | 278 | 282 | 5 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_None` | 291 | 321 | 31 | inferred_complete_timeline |
| `Action_None` | 338 | 359 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 243 | 178 | inferred_complete_timeline |
| `Action_None` | 250 | 256 | 7 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 285 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 266 | 201 | inferred_complete_timeline |
| `Action_None` | 269 | 272 | 4 | inferred_complete_timeline |
| `Action_None` | 276 | 280 | 5 | inferred_complete_timeline |
| `Action_None` | 312 | 313 | 2 | inferred_complete_timeline |
| `Action_None` | 321 | 324 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 162 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_LongSnap` | 66 | 105 | 40 | inferred_complete_timeline |
| `Action_LongSnap` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_LongSnap` | 121 | 121 | 1 | inferred_complete_timeline |
| `Action_None` | 122 | 130 | 9 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 162 | 97 | inferred_complete_timeline |
| `Action_None` | 167 | 359 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 359 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_SnapReceive` | 92 | 92 | 1 | inferred_complete_timeline |
| `Action_None` | 93 | 121 | 29 | inferred_complete_timeline |
| `Action_PuntBall` | 122 | 135 | 14 | inferred_complete_timeline |
| `Action_None` | 136 | 359 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 130 | 65 | inferred_complete_timeline |
| `Action_None` | 132 | 175 | 44 | inferred_complete_timeline |
| `Action_None` | 178 | 183 | 6 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 169 | 104 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 106 | 41 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 116 | 134 | 19 | inferred_complete_timeline |
| `Action_None` | 138 | 168 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 359 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 154 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 100 | 35 | inferred_complete_timeline |
| `Action_None` | 102 | 105 | 4 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 130 | 10 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 217 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 100 | 35 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 110 | 114 | 5 | inferred_complete_timeline |
| `Action_None` | 116 | 130 | 15 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 148 | 11 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–354
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 134 | 69 | inferred_complete_timeline |
| `Action_None` | 145 | 173 | 29 | inferred_complete_timeline |
| `Action_None` | 179 | 188 | 10 | inferred_complete_timeline |
| `Action_None` | 226 | 244 | 19 | inferred_complete_timeline |
| `Action_None` | 249 | 252 | 4 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 275 | 15 | inferred_complete_timeline |
| `Action_None` | 277 | 291 | 15 | inferred_complete_timeline |
| `Action_None` | 293 | 310 | 18 | inferred_complete_timeline |
| `Action_None` | 325 | 328 | 4 | inferred_complete_timeline |
| `Action_None` | 332 | 337 | 6 | inferred_complete_timeline |
| `Action_None` | 352 | 354 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 236 | 171 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 355 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 197 | 132 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 244 | 37 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 283 | 29 | inferred_complete_timeline |
| `Action_None` | 287 | 291 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 158 | 93 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 239 | 66 | inferred_complete_timeline |
| `Action_None` | 241 | 243 | 3 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 359 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 168 | 103 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 103–104 | 2 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 132–176 | 7 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 140–168 | 10 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 146–152 | 7 | 1 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 189–273 | 63 | 6 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 190–359 | 166 | 2 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 190–278 | 79 | 5 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 194–305 | 108 | 3 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 197–359 | 162 | 2 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 205–207 | 3 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 207–219 | 12 | 2 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 207–220 | 14 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 210–232 | 4 | 2 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 235–237 | 3 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 237–359 | 123 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 252–340 | 83 | 4 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 257–359 | 103 | 1 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 258–359 | 56 | 8 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 279–359 | 73 | 3 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 282–359 | 76 | 3 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 297–359 | 52 | 7 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 299–351 | 29 | 6 | Undefined position; Undefined team |
| `43` | `70` | Position_Unknown | Team_Unknown | 314–327 | 6 | 3 | Undefined position; Undefined team |
| `44` | `71` | Position_Unknown | Team_Unknown | 316–359 | 40 | 2 | Undefined position; Undefined team |
| `45` | `73` | Position_Unknown | Team_Unknown | 317–359 | 36 | 4 | Undefined position; Undefined team |
| `46` | `74` | Position_Unknown | Team_Unknown | 318–342 | 25 | 1 | Undefined position; Undefined team |
| `47` | `75` | Position_Unknown | Team_Unknown | 321–332 | 12 | 1 | Undefined position; Undefined team |
| `48` | `77` | Position_Unknown | Team_Unknown | 323–326 | 4 | 1 | Undefined position; Undefined team |
| `49` | `80` | Position_Unknown | Team_Unknown | 325–331 | 5 | 2 | Undefined position; Undefined team |
| `50` | `81` | Position_Unknown | Team_Unknown | 327–355 | 20 | 2 | Undefined position; Undefined team |
| `51` | `82` | Position_Unknown | Team_Unknown | 329–359 | 24 | 2 | Undefined position; Undefined team |
| `52` | `84` | Position_Unknown | Team_Unknown | 339–359 | 20 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 158 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [66-243] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-285] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-130] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-175] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-197] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-244] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-283] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-134] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-173] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-188] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-244] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-275] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-291] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-310] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-337] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-354] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-158] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-239] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-106] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-134] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [66-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [111-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-154] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-217] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-162] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-236] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-355] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-222] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-267] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-282] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-321] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-221] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-237] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-359] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-237] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-263] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-293] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-302] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-340] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-359] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-220] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-266] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-282] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-340] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-359] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-265] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-292] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-304] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-341] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-359] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-308] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-305] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-322] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-335] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-359] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-303] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-337] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-341] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-345] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-359] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-336] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-359] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-342] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-332] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-337] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-355] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-333] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-348] for track '52' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>