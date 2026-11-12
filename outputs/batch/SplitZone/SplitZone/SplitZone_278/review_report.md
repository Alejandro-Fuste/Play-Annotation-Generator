# Play-Annotation-Generator Annotation Review — SplitZone_278

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_278`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 208
- **Validation Warnings:** 217
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 182
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | Team_Unknown | `22` | `22` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `22` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 180 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 134 | START | 134 | 147 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 147 | END | 134 | 147 |
| ✅ EXACT | `Action_SplitBlock` | TE | `5` | `5` | 147 | START | 147 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | `22` | `22` | 157 | START | 157 | 175 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 160 | START | 160 | 181 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | LG | `15` | `15` | 174 | START | 202 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `22` | `22` | 179 | START | 179 | 214 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `11` | `11` | 181 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `13` | 181 | START | 181 | 201 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | `15` | `15` | 181 | START | 182 | 201 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `16` | `16` | 181 | START | 181 | 201 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 181 | START | 181 | 201 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_SnapReceive` | 134 | 147 | 14 | inferred_complete_timeline |
| `Action_None` | 148 | 159 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 160 | 181 | 22 | inferred_complete_timeline |
| `Action_None` | 182 | 359 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 359 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 237 | 104 | inferred_complete_timeline |
| `Action_None` | 242 | 258 | 17 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 235 | 102 | inferred_complete_timeline |
| `Action_None` | 238 | 244 | 7 | inferred_complete_timeline |
| `Action_None` | 246 | 250 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_SplitBlock` | 147 | 189 | 43 | inferred_complete_timeline |
| `Action_None` | 190 | 190 | 1 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 201 | 21 | inferred_complete_timeline |
| `Action_None` | 202 | 214 | 13 | inferred_complete_timeline |
| `Action_None` | 221 | 230 | 10 | inferred_complete_timeline |
| `Action_None` | 232 | 270 | 39 | inferred_complete_timeline |
| `Action_None` | 287 | 298 | 12 | inferred_complete_timeline |
| `Action_None` | 301 | 303 | 3 | inferred_complete_timeline |
| `Action_None` | 306 | 359 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 201 | 20 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 202 | 206 | 5 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 265 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_BallSnap` | 134 | 147 | 14 | inferred_complete_timeline |
| `Action_None` | 148 | 153 | 6 | inferred_complete_timeline |
| `Action_None` | 158 | 180 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 201 | 21 | inferred_complete_timeline |
| `Action_None` | 202 | 211 | 10 | inferred_complete_timeline |
| `Action_None` | 213 | 219 | 7 | inferred_complete_timeline |
| `Action_None` | 223 | 239 | 17 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 274 | 18 | inferred_complete_timeline |
| `Action_None` | 278 | 303 | 26 | inferred_complete_timeline |
| `Action_None` | 306 | 307 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 178 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 180 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 201 | 21 | inferred_complete_timeline |
| `Action_None` | 202 | 359 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 168 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 211 | 78 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–356
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 183 | 50 | inferred_complete_timeline |
| `Action_None` | 186 | 190 | 5 | inferred_complete_timeline |
| `Action_None` | 193 | 211 | 19 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 229 | 9 | inferred_complete_timeline |
| `Action_None` | 233 | 240 | 8 | inferred_complete_timeline |
| `Action_None` | 260 | 293 | 34 | inferred_complete_timeline |
| `Action_None` | 296 | 304 | 9 | inferred_complete_timeline |
| `Action_None` | 307 | 310 | 4 | inferred_complete_timeline |
| `Action_None` | 313 | 329 | 17 | inferred_complete_timeline |
| `Action_None` | 335 | 353 | 19 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 190 | 57 | inferred_complete_timeline |
| `Action_None` | 193 | 199 | 7 | inferred_complete_timeline |
| `Action_None` | 206 | 211 | 6 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 219 | 4 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 243 | 246 | 4 | inferred_complete_timeline |
| `Action_None` | 253 | 255 | 3 | inferred_complete_timeline |
| `Action_None` | 258 | 262 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 168 | 35 | inferred_complete_timeline |
| `Action_None` | 171 | 191 | 21 | inferred_complete_timeline |
| `Action_None` | 193 | 211 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 169 | 36 | inferred_complete_timeline |
| `Action_None` | 171 | 191 | 21 | inferred_complete_timeline |
| `Action_None` | 193 | 203 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 193 | 60 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 359 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 269 | 136 | inferred_complete_timeline |
| `Action_None` | 278 | 320 | 43 | inferred_complete_timeline |
| `Action_None` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_None` | 328 | 334 | 7 | inferred_complete_timeline |
| `Action_None` | 340 | 341 | 2 | inferred_complete_timeline |
| `Action_None` | 344 | 358 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 204 | 71 | inferred_complete_timeline |
| `Action_None` | 213 | 217 | 5 | inferred_complete_timeline |
| `Action_None` | 226 | 269 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 256 | 123 | inferred_complete_timeline |
| `Action_None` | 258 | 270 | 13 | inferred_complete_timeline |
| `Action_None` | 281 | 294 | 14 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_None` | 301 | 303 | 3 | inferred_complete_timeline |
| `Action_None` | 308 | 313 | 6 | inferred_complete_timeline |
| `Action_None` | 315 | 335 | 21 | inferred_complete_timeline |
| `Action_None` | 337 | 359 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 266 | 133 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 11–326 | 287 | 12 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 201–232 | 31 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 206–359 | 144 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 225–359 | 47 | 11 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 243–359 | 76 | 9 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 247–252 | 6 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 254–351 | 75 | 10 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 256–306 | 43 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 264–269 | 4 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 281–294 | 14 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 283–359 | 65 | 6 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 283–359 | 73 | 3 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 283–359 | 58 | 7 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 291–359 | 50 | 6 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 301–359 | 48 | 3 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 316–319 | 4 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 317–359 | 43 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 318–359 | 39 | 2 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 328–359 | 32 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 329–359 | 17 | 5 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `22` (2 segments found)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `15` (LG): Annotated start 174 != Inferred start 202
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (9 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `11` (RT)
- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (LG): Annotated start 181 != Inferred start 182

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 173 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '11' has invalid range: start=181, end=168. Clamping end to start.
- ⚠️ Action 'Action_None' range [134-235] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-244] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-359] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-203] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-237] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '5' starts at frame 190, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [190-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-320] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-334] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-358] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-168] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-191] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-211] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-266] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-270] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-298] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-359] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-219] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-168] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-211] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-201] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-211] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-303] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-269] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [182-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [202-206] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-265] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-178] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-211] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-293] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-304] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-329] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-353] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-270] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-294] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-313] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-335] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [157-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [179-214] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-270] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [280-307] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [309-312] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [315-316] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [318-319] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [321-323] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [325-326] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-215] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-232] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-303] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-321] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-359] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-304] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-318] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-286] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-336] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-345] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-359] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-252] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-270] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-289] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-323] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-337] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-306] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-294] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-294] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-304] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-313] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-337] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-304] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-312] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-334] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-359] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-305] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-337] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-359] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-305] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-322] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-359] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-359] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-333] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-340] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '42' has 1 frames without a visible bounding box.
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

</details>