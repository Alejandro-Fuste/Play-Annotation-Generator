# Play-Annotation-Generator Annotation Review — SplitZone_99

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_99`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 141
- **Validation Warnings:** 148
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 120
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `5` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 14 | START | 17 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 14 | START | 17 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 14 | START | 17 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 14 | START | 17 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 14 | START | 17 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 14 | START | 17 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 14 | START | 17 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 14 | START | 17 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 14 | START | 17 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 14 | START | 17 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 14 | START | 17 | 179 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 180 | START | 180 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 183 | START | 194 | 204 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 183 | START | 183 | 213 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `18` | 183 | START | 183 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `19` | 183 | START | 183 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 183 | START | 183 | 217 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 193 | END | 180 | 193 |
| ✅ EXACT | `Action_SplitBlock` | TE | `5` | `5` | 195 | START | 195 | 229 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `16` | 198 | START | 198 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `14` | 215 | START | 215 | 217 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 305 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 17–419
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_SnapReceive` | 180 | 193 | 14 | inferred_complete_timeline |
| `Action_None` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 198 | 214 | 17 | inferred_complete_timeline |
| `Action_None` | 215 | 343 | 129 | inferred_complete_timeline |
| `Action_None` | 345 | 362 | 18 | inferred_complete_timeline |
| `Action_None` | 364 | 369 | 6 | inferred_complete_timeline |
| `Action_None` | 372 | 390 | 19 | inferred_complete_timeline |
| `Action_None` | 400 | 419 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 17–419
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 214 | 198 | inferred_complete_timeline |
| `Action_BallCarry` | 215 | 217 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 419 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 17–242
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 242 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 17–419
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 248 | 69 | inferred_complete_timeline |
| `Action_None` | 256 | 419 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 17–257
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 257 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 17–229
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 194 | 178 | inferred_complete_timeline |
| `Action_SplitBlock` | 195 | 229 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 17–419
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 182 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 206 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 208 | 252 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 256 | 305 | 50 | inferred_complete_timeline |
| `Action_None` | 306 | 419 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 17–419
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 182 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 213 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 220 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 223 | 226 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 229 | 267 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 270 | 279 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 286 | 305 | 20 | inferred_complete_timeline |
| `Action_None` | 306 | 419 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 17–240
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_BallSnap` | 180 | 193 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 204 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 240 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 17–269
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 182 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 217 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 17–253
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 182 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 239 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 249 | 253 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 419 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 419 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 233 | 54 | inferred_complete_timeline |
| `Action_None` | 236 | 240 | 5 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 275 | 24 | inferred_complete_timeline |
| `Action_None` | 277 | 279 | 3 | inferred_complete_timeline |
| `Action_None` | 281 | 419 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 280 | 101 | inferred_complete_timeline |
| `Action_None` | 282 | 419 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 344 | 165 | inferred_complete_timeline |
| `Action_None` | 346 | 419 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 233 | 54 | inferred_complete_timeline |
| `Action_None` | 240 | 273 | 34 | inferred_complete_timeline |
| `Action_None` | 275 | 346 | 72 | inferred_complete_timeline |
| `Action_None` | 353 | 419 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 419 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 229 | 50 | inferred_complete_timeline |
| `Action_None` | 234 | 240 | 7 | inferred_complete_timeline |
| `Action_None` | 242 | 342 | 101 | inferred_complete_timeline |
| `Action_None` | 348 | 360 | 13 | inferred_complete_timeline |
| `Action_None` | 370 | 371 | 2 | inferred_complete_timeline |
| `Action_None` | 373 | 383 | 11 | inferred_complete_timeline |
| `Action_None` | 386 | 392 | 7 | inferred_complete_timeline |
| `Action_None` | 395 | 419 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 419 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 17–419
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 284 | 105 | inferred_complete_timeline |
| `Action_None` | 294 | 365 | 72 | inferred_complete_timeline |
| `Action_None` | 369 | 372 | 4 | inferred_complete_timeline |
| `Action_None` | 376 | 419 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 17–364
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 179 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 364 | 185 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 23–25 | 3 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 24–129 | 15 | 4 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 27–85 | 34 | 6 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 245–246 | 2 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 265–419 | 155 | 1 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 271–412 | 138 | 3 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 273–419 | 137 | 3 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 281–417 | 98 | 5 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 283–419 | 137 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 297–419 | 123 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 315–335 | 20 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 336–341 | 6 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 336–419 | 60 | 6 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 338–419 | 76 | 4 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 352–418 | 61 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 382–402 | 9 | 3 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 383–413 | 10 | 4 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 395–397 | 3 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 398–405 | 8 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 400–403 | 4 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 401–405 | 5 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 414–415 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [180–193], lower_priority='Action_ZoneBlock' annotated_start=183, effective_Action_ZoneBlock_start=194.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 123 frames exceeds threshold 90 frames [start=183, end=305].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 123 frames exceeds threshold 90 frames [start=183, end=305].
- ⚠️ Action 'Action_None' range [180-257] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-365] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-372] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-364] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [195-229] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-419] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-344] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-229] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-240] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-342] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-360] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-383] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-392] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-419] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-419] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-275] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-273] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-346] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-419] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [215-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-240] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-343] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-362] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-369] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-390] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-419] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-213] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [215-220] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [223-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [229-267] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [270-279] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [249-253] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [208-252] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-419] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-280] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [256-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [267-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-25] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-27] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-29] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-38] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-45] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-54] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-63] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-412] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-320] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-369] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-419] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-324] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-335] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-341] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-360] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-367] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-383] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-348] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-383] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-393] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-419] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-371] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-412] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-418] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-402] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-386] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-405] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-403] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-405] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '43' has 1 frames without a visible bounding box.
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

</details>