# Play-Annotation-Generator Annotation Review — SplitZone_239

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_239`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 25 | START | 26 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 25 | START | 26 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 25 | START | 26 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 25 | START | 26 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 25 | START | 26 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 25 | START | 26 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 25 | START | 26 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 25 | START | 26 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 25 | START | 26 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 25 | START | 26 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 25 | START | 26 | 193 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 191 | START | 191 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `18` | 194 | START | 206 | 208 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 194 | START | 194 | 225 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `20` | 194 | START | 194 | 242 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 194 | START | 194 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `6` | 194 | START | 194 | 217 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `14` | `14` | 198 | START | 198 | 235 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 205 | END | 191 | 205 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `17` | 211 | START | 211 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 222 | START | 222 | 257 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 251 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 26–479
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_SnapReceive` | 191 | 205 | 15 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 211 | 221 | 11 | inferred_complete_timeline |
| `Action_None` | 222 | 226 | 5 | inferred_complete_timeline |
| `Action_None` | 228 | 479 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 26–479
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 221 | 196 | inferred_complete_timeline |
| `Action_BallCarry` | 222 | 257 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 264 | 267 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 270 | 273 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 276 | 326 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 329 | 409 | 81 | inferred_complete_timeline |
| `Action_BallCarry` | 423 | 479 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 26–479
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 479 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 26–479
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 479 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 26–479
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 479 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 26–283
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 197 | 172 | inferred_complete_timeline |
| `Action_SplitBlock` | 198 | 235 | 38 | inferred_complete_timeline |
| `Action_SplitBlock` | 248 | 251 | 4 | inferred_complete_timeline |
| `Action_None` | 252 | 283 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 26–378
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 193 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 242 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 248 | 3 | inferred_complete_timeline |
| `Action_None` | 271 | 275 | 5 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |
| `Action_None` | 287 | 355 | 69 | inferred_complete_timeline |
| `Action_None` | 377 | 378 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 26–364
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 193 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 199 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 210 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 248 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 251 | 1 | inferred_complete_timeline |
| `Action_None` | 252 | 364 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 26–300
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_BallSnap` | 191 | 205 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 251 | 37 | inferred_complete_timeline |
| `Action_None` | 252 | 264 | 13 | inferred_complete_timeline |
| `Action_None` | 269 | 300 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 26–312
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 193 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 225 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 242 | 246 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 251 | 1 | inferred_complete_timeline |
| `Action_None` | 252 | 312 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 26–312
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 193 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 217 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 251 | 6 | inferred_complete_timeline |
| `Action_None` | 252 | 252 | 1 | inferred_complete_timeline |
| `Action_None` | 307 | 309 | 3 | inferred_complete_timeline |
| `Action_None` | 311 | 312 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 26–244
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 230 | 40 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 26–476
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 252 | 62 | inferred_complete_timeline |
| `Action_None` | 256 | 310 | 55 | inferred_complete_timeline |
| `Action_None` | 312 | 454 | 143 | inferred_complete_timeline |
| `Action_None` | 457 | 476 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 26–235
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 235 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 26–318
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 273 | 83 | inferred_complete_timeline |
| `Action_None` | 275 | 318 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 26–285
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 285 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 26–479
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 341 | 151 | inferred_complete_timeline |
| `Action_None` | 346 | 369 | 24 | inferred_complete_timeline |
| `Action_None` | 448 | 479 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 26–332
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 328 | 138 | inferred_complete_timeline |
| `Action_None` | 330 | 332 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 26–479
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 479 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 26–413
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 324 | 134 | inferred_complete_timeline |
| `Action_None` | 345 | 368 | 24 | inferred_complete_timeline |
| `Action_None` | 406 | 413 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 26–290
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 290 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 26–479
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 405 | 215 | inferred_complete_timeline |
| `Action_None` | 409 | 411 | 3 | inferred_complete_timeline |
| `Action_None` | 413 | 439 | 27 | inferred_complete_timeline |
| `Action_None` | 455 | 460 | 6 | inferred_complete_timeline |
| `Action_None` | 478 | 479 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 217–479 | 193 | 6 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 258–375 | 118 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 281–446 | 160 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 289–386 | 95 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 307–479 | 172 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 309–328 | 20 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 330–451 | 77 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 336–479 | 64 | 5 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 358–456 | 32 | 5 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 362–392 | 15 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 387–393 | 6 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 426–472 | 31 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 434–479 | 46 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 435–475 | 31 | 3 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 446–479 | 34 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 451–472 | 17 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 462–479 | 18 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 462–479 | 18 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 476–479 | 4 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 477–479 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 91 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [191–205], lower_priority='Action_ZoneBlock' annotated_start=194, effective_Action_ZoneBlock_start=206.
- ⚠️ Action 'Action_None' range [191-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [222-257] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [264-267] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [270-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [276-326] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [329-409] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [423-479] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-217] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 252, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [252-252] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-252] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-310] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-454] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-476] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-273] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-318] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-341] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-369] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-479] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-328] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-290] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-285] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-235] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [198-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-283] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-405] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-411] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-439] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-460] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-324] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-368] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-413] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '18' starts at frame 206, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [206-208] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-264] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-300] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-225] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [242-246] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-312] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-242] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [246-248] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-355] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [205-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [219-248] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-364] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-277] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-357] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-362] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-457] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-465] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-375] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-369] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-446] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-334] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-386] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-328] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-328] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-335] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-398] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-443] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-451] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-360] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-447] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-462] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-362] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-399] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-413] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-444] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-456] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-370] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-392] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-390] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-393] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-452] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-472] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-442] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-454] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-475] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-456] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-472] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-479] for track '40' has 1 frames without a visible bounding box.
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

</details>