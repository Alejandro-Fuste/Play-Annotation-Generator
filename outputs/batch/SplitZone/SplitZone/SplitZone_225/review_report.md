# Play-Annotation-Generator Annotation Review — SplitZone_225

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_225`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 108
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 21 | START | 22 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 21 | START | 22 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 21 | START | 22 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 21 | START | 22 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 21 | START | 22 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 21 | START | 22 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 21 | START | 22 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 21 | START | 25 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 21 | START | 22 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 21 | START | 22 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 21 | START | 22 | 207 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 180 | START | 180 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `13` | 183 | START | 183 | 226 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `19` | 183 | START | 183 | 240 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 183 | START | 183 | 253 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `22` | `21` | 183 | START | 194 | 209 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 183 | START | 183 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `3` | `3` | 186 | START | 186 | 290 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 193 | END | 180 | 193 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 199 | START | 199 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `8` | 215 | START | 215 | 249 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | `7` | `7` | 230 | START | 230 | 245 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 297 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 22–312
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_SnapReceive` | 180 | 193 | 14 | inferred_complete_timeline |
| `Action_None` | 194 | 198 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 199 | 214 | 16 | inferred_complete_timeline |
| `Action_None` | 215 | 312 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 22–449
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 207 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 214 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 215 | 249 | 35 | inferred_complete_timeline |
| `Action_BallCarry` | 255 | 449 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 22–334
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 334 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 22–362
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 339 | 160 | inferred_complete_timeline |
| `Action_None` | 341 | 346 | 6 | inferred_complete_timeline |
| `Action_None` | 361 | 362 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 22–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 449 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 22–307
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 185 | 164 | inferred_complete_timeline |
| `Action_SplitBlock` | 186 | 290 | 105 | inferred_complete_timeline |
| `Action_SplitBlock` | 292 | 297 | 6 | inferred_complete_timeline |
| `Action_None` | 298 | 307 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 22–357
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 182 | 161 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 240 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 258 | 297 | 40 | inferred_complete_timeline |
| `Action_None` | 298 | 357 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 22–383
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 182 | 161 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 226 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 228 | 290 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 294 | 297 | 4 | inferred_complete_timeline |
| `Action_None` | 298 | 304 | 7 | inferred_complete_timeline |
| `Action_None` | 321 | 325 | 5 | inferred_complete_timeline |
| `Action_None` | 331 | 342 | 12 | inferred_complete_timeline |
| `Action_None` | 344 | 363 | 20 | inferred_complete_timeline |
| `Action_None` | 367 | 383 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 25–449
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 43 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 179 | 131 | inferred_complete_timeline |
| `Action_BallSnap` | 180 | 193 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 209 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 227 | 234 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 280 | 297 | 18 | inferred_complete_timeline |
| `Action_None` | 298 | 449 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 22–353
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 182 | 161 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 253 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 270 | 297 | 28 | inferred_complete_timeline |
| `Action_None` | 298 | 353 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 22–361
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 182 | 161 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 229 | 47 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 230 | 245 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 247 | 297 | 51 | inferred_complete_timeline |
| `Action_None` | 298 | 361 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 22–225
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 225 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 22–361
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 224 | 45 | inferred_complete_timeline |
| `Action_None` | 235 | 266 | 32 | inferred_complete_timeline |
| `Action_None` | 268 | 289 | 22 | inferred_complete_timeline |
| `Action_None` | 295 | 361 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 22–289
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 210 | 31 | inferred_complete_timeline |
| `Action_None` | 232 | 238 | 7 | inferred_complete_timeline |
| `Action_None` | 240 | 247 | 8 | inferred_complete_timeline |
| `Action_None` | 256 | 258 | 3 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 289 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 22–383
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 290 | 111 | inferred_complete_timeline |
| `Action_None` | 297 | 334 | 38 | inferred_complete_timeline |
| `Action_None` | 337 | 383 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 22–449
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 213 | 34 | inferred_complete_timeline |
| `Action_None` | 215 | 449 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 22–399
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 290 | 111 | inferred_complete_timeline |
| `Action_None` | 294 | 324 | 31 | inferred_complete_timeline |
| `Action_None` | 329 | 333 | 5 | inferred_complete_timeline |
| `Action_None` | 335 | 375 | 41 | inferred_complete_timeline |
| `Action_None` | 377 | 399 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 22–274
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 274 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 359 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 22–282
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 282 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 22–270
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 270 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 22–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 179 | 158 | inferred_complete_timeline |
| `Action_None` | 180 | 449 | 270 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 152–154 | 3 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 228–364 | 132 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 233–261 | 15 | 4 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 233–248 | 16 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 273–285 | 11 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 281–449 | 169 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 293–357 | 53 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 302–322 | 21 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 336–389 | 53 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 343–392 | 50 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 409–410 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 412–449 | 38 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LG) duration 115 frames exceeds threshold 90 frames [start=183, end=297].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 115 frames exceeds threshold 90 frames [start=183, end=297].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 115 frames exceeds threshold 90 frames [start=183, end=297].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 115 frames exceeds threshold 90 frames [start=183, end=297].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [180–193], lower_priority='Action_ZoneBlock' annotated_start=183, effective_Action_ZoneBlock_start=194.
- ⚠️ Action 'Action_None' range [180-449] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-339] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-346] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-289] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-361] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [186-290] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [292-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-307] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-270] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-290] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-334] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-383] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-274] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [230-245] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-361] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [215-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-290] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-324] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-333] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-375] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-399] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-334] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-226] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [228-290] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-325] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-342] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-363] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-383] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-282] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-312] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-213] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-449] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-247] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-289] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [249-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-357] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [258-259] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-353] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-209] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [219-222] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [227-234] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-312] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-337] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-364] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-248] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-285] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-300] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-342] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-357] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-322] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-342] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-389] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-392] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-449] for track '33' has 1 frames without a visible bounding box.
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

</details>