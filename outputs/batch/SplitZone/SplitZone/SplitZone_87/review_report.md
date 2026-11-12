# Play-Annotation-Generator Annotation Review — SplitZone_87

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_87`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 174
- **Validation Warnings:** 184
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 139
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `24` | `21` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `1` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 30 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `23` | `Group` | 0 | START | 46 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `24` | `Group` | 0 | START | 49 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 186 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `17` | 187 | START | 187 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `12` | 190 | START | 190 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `13` | 190 | START | 190 | 234 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `16` | `16` | 190 | START | 190 | 262 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `17` | 190 | START | 202 | 204 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `24` | `21` | 190 | START | 190 | 206 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `3` | `3` | 195 | START | 195 | 262 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `1` | 201 | END | 187 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `1` | `1` | 223 | START | 223 | 366 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 262 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_SnapReceive` | 187 | 201 | 15 | inferred_complete_timeline |
| `Action_None` | 202 | 222 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 366 | 144 | inferred_complete_timeline |
| `Action_BallCarry` | 369 | 374 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_None` | 187 | 249 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_None` | 187 | 246 | 60 | inferred_complete_timeline |
| `Action_None` | 248 | 389 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `23`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 46–389
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 46 | 186 | 141 | inferred_complete_timeline |
| `Action_None` | 187 | 286 | 100 | inferred_complete_timeline |
| `Action_None` | 292 | 381 | 90 | inferred_complete_timeline |
| `Action_None` | 383 | 389 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |
| `Action_SplitBlock` | 195 | 262 | 68 | inferred_complete_timeline |
| `Action_None` | 263 | 380 | 118 | inferred_complete_timeline |
| `Action_None` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 25 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 50 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 189 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 234 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 243 | 262 | 20 | inferred_complete_timeline |
| `Action_None` | 263 | 272 | 10 | inferred_complete_timeline |
| `Action_None` | 296 | 389 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `24`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 49–264
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 189 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 206 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 209 | 221 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 30–243
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 43 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 68 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 186 | 102 | inferred_complete_timeline |
| `Action_BallSnap` | 187 | 201 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 234 | 243 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 64 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 72 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 133 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 189 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 262 | 73 | inferred_complete_timeline |
| `Action_None` | 263 | 282 | 20 | inferred_complete_timeline |
| `Action_None` | 290 | 325 | 36 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 189 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 237 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 239 | 241 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `25`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `25`
- **team_side:** `defense`
- **Visible Frames:** 106–226
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 106 | 186 | 81 | inferred_complete_timeline |
| `Action_None` | 187 | 226 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 31–389
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 60 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 186 | 88 | inferred_complete_timeline |
| `Action_None` | 187 | 221 | 35 | inferred_complete_timeline |
| `Action_None` | 238 | 244 | 7 | inferred_complete_timeline |
| `Action_None` | 249 | 252 | 4 | inferred_complete_timeline |
| `Action_None` | 292 | 366 | 75 | inferred_complete_timeline |
| `Action_None` | 371 | 381 | 11 | inferred_complete_timeline |
| `Action_None` | 383 | 389 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 39–282
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 39 | 50 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 186 | 92 | inferred_complete_timeline |
| `Action_None` | 187 | 272 | 86 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_None` | 187 | 358 | 172 | inferred_complete_timeline |
| `Action_None` | 361 | 366 | 6 | inferred_complete_timeline |
| `Action_None` | 369 | 389 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_None` | 187 | 389 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 186 | 157 | inferred_complete_timeline |
| `Action_None` | 187 | 389 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_None` | 187 | 219 | 33 | inferred_complete_timeline |
| `Action_None` | 223 | 228 | 6 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 269 | 36 | inferred_complete_timeline |
| `Action_None` | 280 | 284 | 5 | inferred_complete_timeline |
| `Action_None` | 296 | 303 | 8 | inferred_complete_timeline |
| `Action_None` | 310 | 321 | 12 | inferred_complete_timeline |
| `Action_None` | 323 | 327 | 5 | inferred_complete_timeline |
| `Action_None` | 334 | 336 | 3 | inferred_complete_timeline |
| `Action_None` | 340 | 358 | 19 | inferred_complete_timeline |
| `Action_None` | 361 | 366 | 6 | inferred_complete_timeline |
| `Action_None` | 372 | 389 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_None` | 187 | 382 | 196 | inferred_complete_timeline |
| `Action_None` | 384 | 386 | 3 | inferred_complete_timeline |
| `Action_None` | 388 | 389 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_None` | 187 | 288 | 102 | inferred_complete_timeline |
| `Action_None` | 292 | 389 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_None` | 187 | 244 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_None` | 187 | 389 | 203 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–230 | 225 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–46 | 15 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 231–257 | 25 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 261–389 | 126 | 4 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 265–389 | 125 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 280–389 | 87 | 9 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 297–389 | 56 | 9 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 301–304 | 4 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 316–326 | 5 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 321–364 | 34 | 4 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 325–326 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 332–386 | 27 | 7 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 333–334 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 339–340 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 345–389 | 40 | 4 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 345–389 | 24 | 4 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 350–387 | 13 | 4 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 350–389 | 15 | 5 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 363–365 | 3 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 375–383 | 8 | 2 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 378–389 | 4 | 2 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 379–381 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `24` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 137 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 176: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [187–201], lower_priority='Action_ZoneBlock' annotated_start=190, effective_Action_ZoneBlock_start=202.
- ⚠️ Action 'Action_None' range [187-249] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-366] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [369-374] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [195-262] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-380] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-288] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-246] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-389] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-358] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-366] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-382] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-386] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-219] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-303] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-321] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-327] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-358] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-366] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-244] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-237] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [239-241] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-25] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-50] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-234] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-272] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-389] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-46] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-64] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-133] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-282] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-325] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-43] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [202-204] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [234-243] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-60] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-186] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-366] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-381] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-272] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-286] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-381] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-189] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [209-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [227-228] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [236-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-186] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-257] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-272] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-327] for track '24' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-323] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-336] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-355] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-365] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-383] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-324] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-351] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-366] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-381] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-386] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-339] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-352] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-340] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-383] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-359] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-366] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-382] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-373] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-386] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-387] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-380] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-379] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-383] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-381] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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