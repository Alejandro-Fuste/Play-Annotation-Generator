# Play-Annotation-Generator Annotation Review — SplitZone_169

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_169`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 155
- **Validation Warnings:** 171
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 131
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 23 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `3` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 139 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 140 | START | 140 | 155 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `11` | 143 | START | 143 | 245 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `16` | `16` | 143 | START | 143 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `18` | 143 | START | 143 | 184 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `21` | `21` | 143 | START | 156 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `22` | 143 | START | 143 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `3` | `3` | 153 | START | 153 | 184 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 155 | END | 140 | 155 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `20` | 158 | START | 158 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `13` | `13` | 173 | START | 173 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `21` | `21` | 184 | START | 187 | 190 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 245 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_SnapReceive` | 140 | 155 | 16 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 158 | 172 | 15 | inferred_complete_timeline |
| `Action_None` | 173 | 296 | 124 | inferred_complete_timeline |
| `Action_None` | 299 | 326 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–301
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_BallCarry` | 173 | 183 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 187 | 189 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 199 | 203 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 215 | 222 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 225 | 230 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 233 | 247 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 258 | 260 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 262 | 274 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 288 | 290 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 292 | 296 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 300 | 301 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_SplitBlock` | 153 | 184 | 32 | inferred_complete_timeline |
| `Action_SplitBlock` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 228 | 230 | 3 | inferred_complete_timeline |
| `Action_SplitBlock` | 240 | 245 | 6 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 262 | 14 | inferred_complete_timeline |
| `Action_None` | 264 | 273 | 10 | inferred_complete_timeline |
| `Action_None` | 275 | 359 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 353 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 359 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 210 | 71 | inferred_complete_timeline |
| `Action_None` | 213 | 219 | 7 | inferred_complete_timeline |
| `Action_None` | 221 | 225 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–303
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 245 | 103 | inferred_complete_timeline |
| `Action_None` | 246 | 253 | 8 | inferred_complete_timeline |
| `Action_None` | 267 | 271 | 5 | inferred_complete_timeline |
| `Action_None` | 277 | 303 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 23–194
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 91 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 142 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 177 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 189 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 139 | 119 | inferred_complete_timeline |
| `Action_BallSnap` | 140 | 155 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 199 | 204 | 6 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 207 | 222 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 225 | 245 | 21 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_None` | 269 | 270 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 146 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 184 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 209 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 211 | 72 | inferred_complete_timeline |
| `Action_None` | 213 | 246 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 158 | 19 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 222 | 83 | inferred_complete_timeline |
| `Action_None` | 224 | 230 | 7 | inferred_complete_timeline |
| `Action_None` | 233 | 261 | 29 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 193 | 54 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 215 | 17 | inferred_complete_timeline |
| `Action_None` | 225 | 250 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 205 | 66 | inferred_complete_timeline |
| `Action_None` | 215 | 222 | 8 | inferred_complete_timeline |
| `Action_None` | 224 | 247 | 24 | inferred_complete_timeline |
| `Action_None` | 254 | 257 | 4 | inferred_complete_timeline |
| `Action_None` | 268 | 270 | 3 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_None` | 282 | 310 | 29 | inferred_complete_timeline |
| `Action_None` | 314 | 359 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 203 | 64 | inferred_complete_timeline |
| `Action_None` | 266 | 298 | 33 | inferred_complete_timeline |
| `Action_None` | 300 | 302 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 252 | 113 | inferred_complete_timeline |
| `Action_None` | 263 | 270 | 8 | inferred_complete_timeline |
| `Action_None` | 272 | 359 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 359 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 359 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 213 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 330 | 191 | inferred_complete_timeline |
| `Action_None` | 333 | 345 | 13 | inferred_complete_timeline |
| `Action_None` | 352 | 359 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–167 | 156 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 71–109 | 25 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 172–182 | 11 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 188–347 | 126 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 218–248 | 26 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 222–230 | 9 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 236–359 | 117 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 243–247 | 4 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 266–350 | 76 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 269–296 | 21 | 3 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 276–359 | 83 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 294–350 | 57 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 299–351 | 53 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 315–347 | 33 | 1 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 315–322 | 5 | 2 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 317–340 | 24 | 1 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 319–348 | 30 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 321–333 | 12 | 2 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 325–332 | 8 | 1 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 328–334 | 7 | 1 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (5 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `21` (C): Annotated start 143 != Inferred start 156
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `3` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (15 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `21` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 120 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 103 frames exceeds threshold 90 frames [start=143, end=245].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [140–155], lower_priority='Action_ZoneBlock' annotated_start=143, effective_Action_ZoneBlock_start=156.
- ⚠️ Action 'Action_None' range [140-353] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-246] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [153-184] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [216-217] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [221-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [228-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-262] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-273] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-205] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-247] for track '4' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-310] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-330] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-345] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-298] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-270] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-245] for track '11' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-271] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-303] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-159] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [173-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [187-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [199-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [215-222] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [225-230] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [233-247] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [254-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-260] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [262-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [285-286] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [288-290] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [292-296] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [300-301] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-222] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-261] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-184] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-209] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-215] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-250] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-296] for track '20' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-326] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-160] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [187-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [193-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [199-204] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [207-222] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [225-245] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-91] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-177] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-189] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-194] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-93] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-182] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-204] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-273] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-347] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-230] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-286] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-328] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-274] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-350] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-296] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-286] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-359] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-350] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-351] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-347] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-340] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-348] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-333] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-332] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-334] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>