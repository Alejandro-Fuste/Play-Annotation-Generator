# Play-Annotation-Generator Annotation Review — PuntCoverage_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_11`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 227
- **Validation Warnings:** 271
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 213
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `37` | `33` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `37` | `33` |
| ❌ MISSING SEGMENT | `Action_Tackle` | Position_Unknown | Team_Unknown | `58` | `43` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `16` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `2` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `4` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `7` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `17` | `17` | 5 | START | 5 | 65 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 34 | END | 34 | 34 |
| ✅ EXACT | `Action_PuntBall` | Punter | `6` | `6` | 66 | START | 66 | 77 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `37` | `33` | 203 | START | 203 | 209 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `37` | `33` | 222 | START | 222 | 248 |
| ❌ MISSING SEGMENT | `Action_Tackle` | Position_Unknown | `58` | `43` | 318 | START | N/A | N/A |

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
- **Visible Frames:** 0–107
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 62 | 58 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_None` | 92 | 107 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 185 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 248 | 62 | inferred_complete_timeline |
| `Action_None` | 253 | 259 | 7 | inferred_complete_timeline |
| `Action_None` | 262 | 267 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_LongSnap` | 5 | 65 | 61 | inferred_complete_timeline |
| `Action_None` | 66 | 175 | 110 | inferred_complete_timeline |
| `Action_None` | 177 | 187 | 11 | inferred_complete_timeline |
| `Action_None` | 195 | 205 | 11 | inferred_complete_timeline |
| `Action_None` | 209 | 221 | 13 | inferred_complete_timeline |
| `Action_None` | 225 | 389 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 162 | 158 | inferred_complete_timeline |
| `Action_None` | 166 | 176 | 11 | inferred_complete_timeline |
| `Action_None` | 180 | 184 | 5 | inferred_complete_timeline |
| `Action_None` | 187 | 189 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_None` | 35 | 65 | 31 | inferred_complete_timeline |
| `Action_PuntBall` | 66 | 77 | 12 | inferred_complete_timeline |
| `Action_None` | 78 | 86 | 9 | inferred_complete_timeline |
| `Action_None` | 93 | 187 | 95 | inferred_complete_timeline |
| `Action_None` | 190 | 198 | 9 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 231 | 235 | 5 | inferred_complete_timeline |
| `Action_None` | 242 | 244 | 3 | inferred_complete_timeline |
| `Action_None` | 251 | 253 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 114 | 110 | inferred_complete_timeline |
| `Action_None` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_None` | 123 | 128 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 136 | 6 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 56 | 52 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 67 | 71 | 5 | inferred_complete_timeline |
| `Action_None` | 73 | 116 | 44 | inferred_complete_timeline |
| `Action_None` | 118 | 124 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 60 | 56 | inferred_complete_timeline |
| `Action_None` | 63 | 75 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 115 | 111 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 128 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 112 | 108 | inferred_complete_timeline |
| `Action_None` | 117 | 253 | 137 | inferred_complete_timeline |
| `Action_None` | 255 | 350 | 96 | inferred_complete_timeline |
| `Action_None` | 354 | 389 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 91 | 87 | inferred_complete_timeline |
| `Action_None` | 93 | 111 | 19 | inferred_complete_timeline |
| `Action_None` | 117 | 128 | 12 | inferred_complete_timeline |
| `Action_None` | 130 | 149 | 20 | inferred_complete_timeline |
| `Action_None` | 151 | 163 | 13 | inferred_complete_timeline |
| `Action_None` | 168 | 177 | 10 | inferred_complete_timeline |
| `Action_None` | 179 | 189 | 11 | inferred_complete_timeline |
| `Action_None` | 194 | 208 | 15 | inferred_complete_timeline |
| `Action_None` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_None` | 222 | 295 | 74 | inferred_complete_timeline |
| `Action_None` | 298 | 389 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 186 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 47 | 43 | inferred_complete_timeline |
| `Action_None` | 52 | 97 | 46 | inferred_complete_timeline |
| `Action_None` | 99 | 172 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–17
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 17 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 118 | 114 | inferred_complete_timeline |
| `Action_None` | 121 | 132 | 12 | inferred_complete_timeline |
| `Action_None` | 134 | 163 | 30 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 206 | 36 | inferred_complete_timeline |
| `Action_None` | 208 | 248 | 41 | inferred_complete_timeline |
| `Action_None` | 251 | 307 | 57 | inferred_complete_timeline |
| `Action_None` | 310 | 372 | 63 | inferred_complete_timeline |
| `Action_None` | 380 | 389 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 48 | 44 | inferred_complete_timeline |
| `Action_None` | 50 | 106 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–340
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 242 | 238 | inferred_complete_timeline |
| `Action_None` | 245 | 300 | 56 | inferred_complete_timeline |
| `Action_None` | 306 | 309 | 4 | inferred_complete_timeline |
| `Action_None` | 313 | 340 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–363
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 72 | 68 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 82 | 99 | 18 | inferred_complete_timeline |
| `Action_None` | 101 | 190 | 90 | inferred_complete_timeline |
| `Action_None` | 192 | 245 | 54 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 268 | 12 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_None` | 287 | 320 | 34 | inferred_complete_timeline |
| `Action_None` | 327 | 363 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 122 | 118 | inferred_complete_timeline |
| `Action_None` | 124 | 156 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–220 | 141 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–169 | 161 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 22–370 | 343 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 37–38 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 82–93 | 11 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 87–110 | 13 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 111–113 | 3 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 119–386 | 260 | 5 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 119–389 | 242 | 6 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 124–231 | 101 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 131–137 | 5 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 132–183 | 49 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 138–248 | 87 | 7 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 167–224 | 56 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 175–389 | 194 | 8 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 185–376 | 166 | 5 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 191–196 | 6 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 196–323 | 74 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 204–389 | 181 | 4 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 206–389 | 184 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 214–389 | 151 | 5 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 232–299 | 39 | 5 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 239–243 | 5 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 244–389 | 144 | 2 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 248–303 | 56 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 260–389 | 130 | 1 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 263–389 | 115 | 5 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 263–309 | 5 | 2 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 281–284 | 4 | 1 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 285–314 | 30 | 1 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 286–335 | 50 | 1 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 289–389 | 98 | 2 | Undefined position; Undefined team |
| `52` | `72` | Position_Unknown | Team_Unknown | 289–389 | 75 | 6 | Undefined position; Undefined team |
| `53` | `75` | Position_Unknown | Team_Unknown | 319–336 | 18 | 1 | Undefined position; Undefined team |
| `54` | `76` | Position_Unknown | Team_Unknown | 324–325 | 2 | 1 | Undefined position; Undefined team |
| `55` | `79` | Position_Unknown | Team_Unknown | 338–389 | 33 | 2 | Undefined position; Undefined team |
| `56` | `81` | Position_Unknown | Team_Unknown | 343–385 | 18 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `37` (5 segments found)
- ❌ Missing segment for action `Action_Tackle` on target `58` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 192 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_Tackle' for track '43' has invalid range: start=318, end=303. Clamping end to start.
- ⚠️ Action 'Action_None' range [5-56] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-71] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-176] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-114] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-128] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-48] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-106] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-60] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [66-77] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-187] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-128] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-62] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-107] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-118] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-163] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-206] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-248] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-307] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-372] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-111] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-128] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-149] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-163] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-177] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-208] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-295] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-17] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-242] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-300] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-340] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-253] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-350] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-248] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-259] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [5-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-175] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-187] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-205] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-159] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-99] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-190] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-245] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-268] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-320] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-363] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-266] for track '21' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-365] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-93] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-209] for track '26' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-374] for track '26' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-382] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-345] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-218] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-231] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-248] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-183] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-224] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-202] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-221] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [222-248] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [253-321] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [334-372] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [376-383] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-273] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-281] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-293] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-360] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-376] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-248] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-272] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-275] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-351] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-389] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-247] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-268] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-256] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-303] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-389] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-314] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-335] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-294] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-389] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-300] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-331] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-371] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-336] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-348] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-360] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-370] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>