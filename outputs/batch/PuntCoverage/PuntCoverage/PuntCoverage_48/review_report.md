# Play-Annotation-Generator Annotation Review — PuntCoverage_48

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_48`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 359
- **Player Tracks:** 64
- **Ball Tracks:** 0
- **Action Segments:** 214
- **Validation Warnings:** 269
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 196
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | Left_Edge_Rusher | defense | `3` | `3` |
| ✅ EXACT | `Action_PuntBall` | Left_Edge_Rusher | defense | `3` | `3` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `42` | `32` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `42` | `32` |
| ✅ EXACT | `Action_Tackle` | Right_Gunner | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 11 | START | 11 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `14` | `Group` | 11 | START | 11 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `16` | `Group` | 11 | START | 11 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 11 | START | 11 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 11 | START | 11 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `19` | `Group` | 11 | START | 11 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `2` | `Group` | 11 | START | 11 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `20` | `Group` | 11 | START | 11 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `6` | `Group` | 11 | START | 11 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `7` | `Group` | 11 | START | 11 | 19 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `19` | `19` | 20 | START | 20 | 32 |
| ✅ EXACT | `Action_SnapReceive` | Left_Edge_Rusher | `3` | `3` | 44 | END | 44 | 44 |
| ✅ EXACT | `Action_PuntBall` | Left_Edge_Rusher | `3` | `3` | 71 | START | 71 | 85 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `42` | `32` | 198 | START | 198 | 208 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `42` | `32` | 233 | START | 233 | 249 |
| ✅ EXACT | `Action_Tackle` | Right_Gunner | `2` | `2` | 266 | START | 266 | 269 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 11–81
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 55 | 36 | inferred_complete_timeline |
| `Action_None` | 60 | 81 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 11–70
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 70 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 11–258
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 81 | 62 | inferred_complete_timeline |
| `Action_None` | 85 | 258 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_LongSnap` | 20 | 32 | 13 | inferred_complete_timeline |
| `Action_None` | 91 | 93 | 3 | inferred_complete_timeline |
| `Action_None` | 95 | 341 | 247 | inferred_complete_timeline |
| `Action_None` | 343 | 359 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 11–98
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 98 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 11–79
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 79 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 11–114
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 46 | 27 | inferred_complete_timeline |
| `Action_None` | 49 | 58 | 10 | inferred_complete_timeline |
| `Action_None` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_None` | 91 | 96 | 6 | inferred_complete_timeline |
| `Action_None` | 98 | 105 | 8 | inferred_complete_timeline |
| `Action_None` | 107 | 114 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 11–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 140 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 162 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 265 | 102 | inferred_complete_timeline |
| `Action_Tackle` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 11–59
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 52 | 33 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 11–350
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 84 | 65 | inferred_complete_timeline |
| `Action_None` | 91 | 151 | 61 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 161 | 219 | 59 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 233 | 4 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 266 | 13 | inferred_complete_timeline |
| `Action_None` | 269 | 299 | 31 | inferred_complete_timeline |
| `Action_None` | 302 | 350 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 11–81
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 64 | 45 | inferred_complete_timeline |
| `Action_None` | 67 | 81 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 11–80
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_None` | 41 | 49 | 9 | inferred_complete_timeline |
| `Action_None` | 71 | 74 | 4 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 11–358
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 224 | 205 | inferred_complete_timeline |
| `Action_None` | 228 | 232 | 5 | inferred_complete_timeline |
| `Action_None` | 235 | 245 | 11 | inferred_complete_timeline |
| `Action_None` | 252 | 258 | 7 | inferred_complete_timeline |
| `Action_None` | 260 | 265 | 6 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |
| `Action_None` | 271 | 358 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 11–123
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 60 | 41 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 123 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 11–343
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 81 | 62 | inferred_complete_timeline |
| `Action_None` | 104 | 201 | 98 | inferred_complete_timeline |
| `Action_None` | 203 | 329 | 127 | inferred_complete_timeline |
| `Action_None` | 331 | 343 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 11–352
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 154 | 135 | inferred_complete_timeline |
| `Action_None` | 157 | 161 | 5 | inferred_complete_timeline |
| `Action_None` | 163 | 170 | 8 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_None` | 186 | 214 | 29 | inferred_complete_timeline |
| `Action_None` | 219 | 231 | 13 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 249 | 6 | inferred_complete_timeline |
| `Action_None` | 262 | 264 | 3 | inferred_complete_timeline |
| `Action_None` | 270 | 284 | 15 | inferred_complete_timeline |
| `Action_None` | 292 | 320 | 29 | inferred_complete_timeline |
| `Action_None` | 323 | 352 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 11–180
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 43 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_None` | 45 | 70 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 71 | 85 | 15 | inferred_complete_timeline |
| `Action_None` | 86 | 116 | 31 | inferred_complete_timeline |
| `Action_None` | 120 | 125 | 6 | inferred_complete_timeline |
| `Action_None` | 129 | 135 | 7 | inferred_complete_timeline |
| `Action_None` | 137 | 147 | 11 | inferred_complete_timeline |
| `Action_None` | 149 | 155 | 7 | inferred_complete_timeline |
| `Action_None` | 157 | 163 | 7 | inferred_complete_timeline |
| `Action_None` | 171 | 180 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 11–137
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 79 | 60 | inferred_complete_timeline |
| `Action_None` | 81 | 101 | 21 | inferred_complete_timeline |
| `Action_None` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 114 | 4 | inferred_complete_timeline |
| `Action_None` | 119 | 128 | 10 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 11–168
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 144 | 125 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 11–97
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 19 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 91 | 72 | inferred_complete_timeline |
| `Action_None` | 93 | 97 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 11–359 | 349 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 69–84 | 15 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 106–130 | 23 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 125–128 | 4 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 126–352 | 222 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 138–359 | 222 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 146–147 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 149–359 | 199 | 7 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 153–338 | 121 | 9 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 157–359 | 181 | 8 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 166–168 | 3 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 166–339 | 155 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 172–359 | 176 | 8 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 173–174 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 180–359 | 177 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 184–359 | 175 | 2 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 186–200 | 7 | 3 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 191–359 | 157 | 3 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 200–359 | 160 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 200–213 | 14 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 204–236 | 4 | 2 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 210–213 | 4 | 1 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 213–359 | 123 | 2 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 215–349 | 135 | 1 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 223–350 | 128 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 249–359 | 106 | 3 | Undefined position; Undefined team |
| `47` | `67` | Position_Unknown | Team_Unknown | 263–266 | 4 | 1 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 269–353 | 84 | 2 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 275–356 | 17 | 4 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 279–290 | 9 | 2 | Undefined position; Undefined team |
| `51` | `78` | Position_Unknown | Team_Unknown | 298–350 | 16 | 4 | Undefined position; Undefined team |
| `52` | `79` | Position_Unknown | Team_Unknown | 300–333 | 12 | 4 | Undefined position; Undefined team |
| `53` | `81` | Position_Unknown | Team_Unknown | 311–323 | 13 | 1 | Undefined position; Undefined team |
| `54` | `84` | Position_Unknown | Team_Unknown | 330–331 | 2 | 1 | Undefined position; Undefined team |
| `55` | `85` | Position_Unknown | Team_Unknown | 332–353 | 11 | 2 | Undefined position; Undefined team |
| `56` | `86` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `57` | `87` | Position_Unknown | Team_Unknown | 333–335 | 3 | 1 | Undefined position; Undefined team |
| `58` | `93` | Position_Unknown | Team_Unknown | 351–359 | 9 | 1 | Undefined position; Undefined team |
| `59` | `96` | Position_Unknown | Team_Unknown | 352–359 | 6 | 2 | Undefined position; Undefined team |
| `60` | `103` | Position_Unknown | Team_Unknown | 354–359 | 6 | 1 | Undefined position; Undefined team |
| `61` | `104` | Position_Unknown | Team_Unknown | 354–359 | 6 | 1 | Undefined position; Undefined team |
| `62` | `105` | Position_Unknown | Team_Unknown | 354–359 | 6 | 1 | Undefined position; Undefined team |
| `63` | `106` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `42` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punt_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 44 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 44 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 88 |
| Missing visible bounding boxes during action | 178 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 98: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [20-70] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-79] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-101] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-128] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-162] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-265] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [266-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-116] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-135] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-147] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-224] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-358] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-214] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-231] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-284] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-320] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-352] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-79] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-98] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-81] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-201] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-329] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-343] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-60] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-91] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-38] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-49] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-151] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-219] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-299] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-350] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-64] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-81] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-258] for track '16' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-55] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-46] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-105] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [20-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-341] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-84] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-121] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-320] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-352] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-170] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-200] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-240] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-257] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-264] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-266] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-281] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-338] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-190] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-282] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-359] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-186] for track '31' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-309] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-339] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-232] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [233-249] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [252-253] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-294] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [299-355] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-267] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-301] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-209] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-359] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-213] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-327] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-349] for track '44' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-350] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-255] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-353] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-280] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-305] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-323] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-339] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-353] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-359] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-354] for track '59' has 1 frames without a visible bounding box.
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

</details>