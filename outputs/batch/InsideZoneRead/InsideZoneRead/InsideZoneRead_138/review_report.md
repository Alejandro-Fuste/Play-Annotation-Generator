# Play-Annotation-Generator Annotation Review — InsideZoneRead_138

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_138`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 113
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
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `16` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 171 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 172 | START | 172 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 175 | START | 175 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 175 | START | 184 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 175 | START | 175 | 185 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `22` | `21` | 175 | START | 175 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `6` | 175 | START | 175 | 233 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 183 | END | 172 | 183 |
| ✅ EXACT | `Action_ReadDefender` | QB | `14` | `13` | 196 | START | 196 | 202 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `14` | `13` | 209 | START | 210 | 220 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `21` | `20` | 217 | START | 217 | 221 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `4` | 221 | START | 221 | 361 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 272 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_SnapReceive` | 172 | 183 | 12 | inferred_complete_timeline |
| `Action_None` | 184 | 195 | 12 | inferred_complete_timeline |
| `Action_ReadDefender` | 196 | 202 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 210 | 220 | 11 | inferred_complete_timeline |
| `Action_None` | 221 | 233 | 13 | inferred_complete_timeline |
| `Action_None` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_None` | 305 | 339 | 35 | inferred_complete_timeline |
| `Action_None` | 341 | 347 | 7 | inferred_complete_timeline |
| `Action_None` | 351 | 354 | 4 | inferred_complete_timeline |
| `Action_None` | 357 | 389 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–361
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 220 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 221 | 361 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–373
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 373 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 307 | 136 | inferred_complete_timeline |
| `Action_None` | 311 | 334 | 24 | inferred_complete_timeline |
| `Action_None` | 344 | 354 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 283 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 233 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 245 | 255 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 198 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_BallSnap` | 172 | 183 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 202 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 185 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 217 | 221 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 224 | 227 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 239 | 255 | 17 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_None` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 330 | 11 | inferred_complete_timeline |
| `Action_None` | 335 | 343 | 9 | inferred_complete_timeline |
| `Action_None` | 346 | 389 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 233 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 239 | 272 | 34 | inferred_complete_timeline |
| `Action_None` | 273 | 274 | 2 | inferred_complete_timeline |
| `Action_None` | 291 | 329 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–335
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 236 | 65 | inferred_complete_timeline |
| `Action_None` | 238 | 264 | 27 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 278 | 287 | 10 | inferred_complete_timeline |
| `Action_None` | 291 | 335 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 204 | 33 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 227 | 18 | inferred_complete_timeline |
| `Action_None` | 239 | 241 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 251 | 9 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–381
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 236 | 65 | inferred_complete_timeline |
| `Action_None` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_None` | 247 | 254 | 8 | inferred_complete_timeline |
| `Action_None` | 283 | 285 | 3 | inferred_complete_timeline |
| `Action_None` | 293 | 381 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 227 | 56 | inferred_complete_timeline |
| `Action_None` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_None` | 250 | 255 | 6 | inferred_complete_timeline |
| `Action_None` | 280 | 283 | 4 | inferred_complete_timeline |
| `Action_None` | 285 | 389 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 255 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 235 | 64 | inferred_complete_timeline |
| `Action_None` | 238 | 241 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 267 | 96 | inferred_complete_timeline |
| `Action_None` | 270 | 319 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 332 | 161 | inferred_complete_timeline |
| `Action_None` | 335 | 389 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_None` | 172 | 357 | 186 | inferred_complete_timeline |
| `Action_None` | 361 | 389 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 15–17 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 216–297 | 30 | 7 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 264–266 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 275–327 | 47 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 286–389 | 99 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 294–389 | 96 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 294–302 | 9 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 299–389 | 91 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 309–389 | 73 | 3 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 313–389 | 73 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 359–383 | 25 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 379–385 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `14` (QB): Annotated start 209 != Inferred start 210
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 98 frames exceeds threshold 90 frames [start=175, end=272].
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [172–183], lower_priority='Action_ZoneBlock' annotated_start=175, effective_Action_ZoneBlock_start=184.
- ⚠️ Action 'Action_None' range [172-236] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-287] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-335] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-255] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [221-361] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-227] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-251] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-233] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [239-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [245-255] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-307] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-334] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-354] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-357] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-389] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-332] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-373] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [196-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-339] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-347] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-236] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-381] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-319] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-233] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-329] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' for track '20' starts at frame 217, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BlockSecondLevel' range [217-221] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [224-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [239-255] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [260-262] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-330] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-343] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-198] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-17] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-313] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-323] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-389] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-302] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-371] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-381] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-318] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-389] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-383] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-381] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-385] for track '34' has 1 frames without a visible bounding box.
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

</details>