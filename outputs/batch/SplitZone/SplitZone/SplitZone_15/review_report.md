# Play-Annotation-Generator Annotation Review — SplitZone_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_15`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | defense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `7` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 163 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 161 | START | 161 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `10` | 164 | START | 164 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 164 | START | 181 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 164 | START | 164 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `3` | 164 | START | 164 | 242 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `9` | 164 | START | 164 | 196 |
| ✅ EXACT | `Action_SplitBlock` | HB | `7` | `7` | 174 | START | 174 | 251 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 180 | END | 161 | 180 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 189 | START | 189 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | `14` | `14` | 208 | START | 208 | 244 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `21` | `21` | 212 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 256 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–377
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_SnapReceive` | 161 | 180 | 20 | inferred_complete_timeline |
| `Action_None` | 181 | 188 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 189 | 211 | 23 | inferred_complete_timeline |
| `Action_None` | 212 | 377 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_SplitBlock` | 174 | 251 | 78 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 262 | 289 | 28 | inferred_complete_timeline |
| `Action_None` | 299 | 301 | 3 | inferred_complete_timeline |
| `Action_None` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_None` | 310 | 330 | 21 | inferred_complete_timeline |
| `Action_None` | 334 | 338 | 5 | inferred_complete_timeline |
| `Action_None` | 352 | 389 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–386
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 374 | 214 | inferred_complete_timeline |
| `Action_None` | 377 | 386 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 389 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 253 | 93 | inferred_complete_timeline |
| `Action_None` | 255 | 289 | 35 | inferred_complete_timeline |
| `Action_None` | 291 | 389 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 196 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 244 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 251 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 253 | 255 | 3 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 358 | 99 | inferred_complete_timeline |
| `Action_None` | 361 | 362 | 2 | inferred_complete_timeline |
| `Action_None` | 364 | 366 | 3 | inferred_complete_timeline |
| `Action_None` | 369 | 371 | 3 | inferred_complete_timeline |
| `Action_None` | 375 | 389 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 242 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 251 | 5 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 283 | 23 | inferred_complete_timeline |
| `Action_None` | 286 | 289 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_BallSnap` | 161 | 180 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 200 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 211 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 217 | 220 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 234 | 241 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 356 | 61 | inferred_complete_timeline |
| `Action_None` | 363 | 371 | 9 | inferred_complete_timeline |
| `Action_None` | 381 | 389 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 200 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 202 | 211 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 243 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 249 | 251 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 199 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 243 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 208 | 48 | inferred_complete_timeline |
| `Action_None` | 216 | 236 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 200 | 40 | inferred_complete_timeline |
| `Action_None` | 203 | 389 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 208 | 244 | 37 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 249 | 251 | 3 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 274 | 10 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 200 | 40 | inferred_complete_timeline |
| `Action_None` | 202 | 243 | 42 | inferred_complete_timeline |
| `Action_None` | 259 | 316 | 58 | inferred_complete_timeline |
| `Action_None` | 319 | 330 | 12 | inferred_complete_timeline |
| `Action_None` | 334 | 335 | 2 | inferred_complete_timeline |
| `Action_None` | 337 | 348 | 12 | inferred_complete_timeline |
| `Action_None` | 353 | 356 | 4 | inferred_complete_timeline |
| `Action_None` | 362 | 363 | 2 | inferred_complete_timeline |
| `Action_None` | 365 | 372 | 8 | inferred_complete_timeline |
| `Action_None` | 375 | 377 | 3 | inferred_complete_timeline |
| `Action_None` | 381 | 389 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 200 | 40 | inferred_complete_timeline |
| `Action_None` | 202 | 389 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 200 | 40 | inferred_complete_timeline |
| `Action_None` | 202 | 240 | 39 | inferred_complete_timeline |
| `Action_None` | 249 | 251 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 389 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 301 | 141 | inferred_complete_timeline |
| `Action_None` | 310 | 389 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 241 | 81 | inferred_complete_timeline |
| `Action_None` | 251 | 255 | 5 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 264 | 4 | inferred_complete_timeline |
| `Action_None` | 269 | 389 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 389 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 243 | 83 | inferred_complete_timeline |
| `Action_None` | 249 | 251 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 208–282 | 48 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 234–278 | 34 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 248–249 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 258–389 | 132 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 261–389 | 127 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 261–389 | 129 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 262–389 | 128 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 294–326 | 26 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 303–382 | 75 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 303–383 | 20 | 3 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 313–316 | 4 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 320–324 | 5 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 352–359 | 8 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 368–386 | 12 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `14` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `21` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 93 frames exceeds threshold 90 frames [start=164, end=256].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 93 frames exceeds threshold 90 frames [start=164, end=256].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 93 frames exceeds threshold 90 frames [start=164, end=256].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [161–180], lower_priority='Action_ZoneBlock' annotated_start=164, effective_Action_ZoneBlock_start=181.
- ⚠️ Segment 'Action_BallCarry' for track '21' has invalid range: start=212, end=196. Clamping end to start.
- ⚠️ Action 'Action_None' range [161-253] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-289] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-389] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-374] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-386] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-243] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-242] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [247-251] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-283] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-241] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [174-251] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-289] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-330] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-338] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-389] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [206-208] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-244] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [248-251] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [253-255] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-358] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-366] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-371] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-199] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-243] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-208] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-389] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [202-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [205-211] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-215] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [217-220] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [234-241] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [250-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-356] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-371] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [208-244] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [249-251] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-240] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-243] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-316] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-330] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-348] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-372] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-377] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-301] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-389] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-377] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [164-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [202-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [218-243] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [249-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-282] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-278] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-389] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-365] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-306] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-315] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-326] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-382] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-314] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-383] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-324] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-359] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-373] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-386] for track '35' has 1 frames without a visible bounding box.
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

</details>