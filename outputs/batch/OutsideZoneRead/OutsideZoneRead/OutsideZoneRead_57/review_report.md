# Play-Annotation-Generator Annotation Review — OutsideZoneRead_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_57`
- **Frame Range:** 0 to 929 (930 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 929
- **Player Tracks:** 81
- **Ball Tracks:** 0
- **Action Segments:** 171
- **Validation Warnings:** 264
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 149
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `13` | `13` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 296 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 427 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 316 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `12` | 143 | START | 143 | 189 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `15` | 143 | START | 143 | 189 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `18` | `18` | 143 | START | 143 | 189 |
| ✅ EXACT | `Action_ZoneBlock` | C | `19` | `19` | 143 | START | 143 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 143 | START | 143 | 168 |
| ✅ EXACT | `Action_PressEdge` | RB | `13` | `13` | 147 | START | 147 | 194 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `17` | `17` | 150 | START | 150 | 168 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `17` | 169 | START | 169 | 173 |

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
- **Visible Frames:** 0–320
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 150 | 168 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 320 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PressEdge` | 147 | 194 | 48 | inferred_complete_timeline |
| `Action_None` | 195 | 275 | 81 | inferred_complete_timeline |
| `Action_None` | 280 | 282 | 3 | inferred_complete_timeline |
| `Action_None` | 287 | 297 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 296 | 297 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–427
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 427 | 428 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–427
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 316 | 317 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 427 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–427
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 222 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 427 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–427
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 189 | 47 | inferred_complete_timeline |
| `Action_None` | 190 | 427 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–427
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 189 | 47 | inferred_complete_timeline |
| `Action_None` | 190 | 427 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–427
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 189 | 47 | inferred_complete_timeline |
| `Action_None` | 190 | 233 | 44 | inferred_complete_timeline |
| `Action_None` | 237 | 282 | 46 | inferred_complete_timeline |
| `Action_None` | 298 | 303 | 6 | inferred_complete_timeline |
| `Action_None` | 306 | 427 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 168 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 189 | 17 | inferred_complete_timeline |
| `Action_None` | 190 | 195 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–427
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 189 | 47 | inferred_complete_timeline |
| `Action_None` | 190 | 427 | 238 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–429
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 429 | 430 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 190 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 358 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 280 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–427
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 427 | 428 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–427
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 427 | 428 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 207 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–350
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 293 | 294 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 299 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 331 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 339 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 350 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–379
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 342 | 343 | inferred_complete_timeline |
| `Action_PreSnap` | 352 | 368 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 379 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–427
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 370 | 371 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 427 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 173–414 | 242 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 190–427 | 230 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 223–427 | 205 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 260–284 | 13 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 272–427 | 151 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 312–429 | 111 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 328–334 | 7 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 361–427 | 67 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 376–427 | 52 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 405–427 | 23 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 424–429 | 6 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `37` | `40` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `38` | `41` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `39` | `42` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `40` | `43` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `41` | `44` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `42` | `45` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `43` | `46` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `44` | `47` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `45` | `48` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `46` | `49` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `47` | `50` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `48` | `51` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `49` | `52` | Position_Unknown | Team_Unknown | 476–929 | 392 | 4 | Undefined position; Undefined team |
| `50` | `53` | Position_Unknown | Team_Unknown | 476–929 | 451 | 2 | Undefined position; Undefined team |
| `51` | `54` | Position_Unknown | Team_Unknown | 476–929 | 445 | 3 | Undefined position; Undefined team |
| `52` | `55` | Position_Unknown | Team_Unknown | 476–928 | 429 | 6 | Undefined position; Undefined team |
| `53` | `56` | Position_Unknown | Team_Unknown | 476–929 | 453 | 2 | Undefined position; Undefined team |
| `54` | `57` | Position_Unknown | Team_Unknown | 476–876 | 371 | 3 | Undefined position; Undefined team |
| `55` | `58` | Position_Unknown | Team_Unknown | 476–874 | 386 | 3 | Undefined position; Undefined team |
| `56` | `59` | Position_Unknown | Team_Unknown | 476–929 | 428 | 4 | Undefined position; Undefined team |
| `57` | `60` | Position_Unknown | Team_Unknown | 476–920 | 444 | 2 | Undefined position; Undefined team |
| `58` | `61` | Position_Unknown | Team_Unknown | 476–929 | 449 | 3 | Undefined position; Undefined team |
| `59` | `62` | Position_Unknown | Team_Unknown | 476–929 | 434 | 4 | Undefined position; Undefined team |
| `60` | `63` | Position_Unknown | Team_Unknown | 476–929 | 431 | 3 | Undefined position; Undefined team |
| `61` | `64` | Position_Unknown | Team_Unknown | 476–789 | 314 | 1 | Undefined position; Undefined team |
| `62` | `65` | Position_Unknown | Team_Unknown | 476–650 | 118 | 4 | Undefined position; Undefined team |
| `63` | `66` | Position_Unknown | Team_Unknown | 476–555 | 80 | 1 | Undefined position; Undefined team |
| `64` | `67` | Position_Unknown | Team_Unknown | 476–851 | 355 | 5 | Undefined position; Undefined team |
| `65` | `69` | Position_Unknown | Team_Unknown | 760–804 | 29 | 2 | Undefined position; Undefined team |
| `66` | `70` | Position_Unknown | Team_Unknown | 778–788 | 11 | 1 | Undefined position; Undefined team |
| `67` | `72` | Position_Unknown | Team_Unknown | 785–928 | 93 | 8 | Undefined position; Undefined team |
| `68` | `74` | Position_Unknown | Team_Unknown | 819–929 | 96 | 3 | Undefined position; Undefined team |
| `69` | `75` | Position_Unknown | Team_Unknown | 828–929 | 94 | 2 | Undefined position; Undefined team |
| `70` | `76` | Position_Unknown | Team_Unknown | 832–929 | 98 | 1 | Undefined position; Undefined team |
| `71` | `77` | Position_Unknown | Team_Unknown | 833–929 | 96 | 2 | Undefined position; Undefined team |
| `72` | `79` | Position_Unknown | Team_Unknown | 837–839 | 3 | 1 | Undefined position; Undefined team |
| `73` | `81` | Position_Unknown | Team_Unknown | 840–929 | 90 | 1 | Undefined position; Undefined team |
| `74` | `84` | Position_Unknown | Team_Unknown | 852–855 | 4 | 1 | Undefined position; Undefined team |
| `75` | `85` | Position_Unknown | Team_Unknown | 862–923 | 62 | 1 | Undefined position; Undefined team |
| `76` | `86` | Position_Unknown | Team_Unknown | 863–929 | 50 | 4 | Undefined position; Undefined team |
| `77` | `87` | Position_Unknown | Team_Unknown | 867–929 | 63 | 1 | Undefined position; Undefined team |
| `78` | `88` | Position_Unknown | Team_Unknown | 891–910 | 20 | 1 | Undefined position; Undefined team |
| `79` | `89` | Position_Unknown | Team_Unknown | 906–929 | 24 | 1 | Undefined position; Undefined team |
| `80` | `91` | Position_Unknown | Team_Unknown | 913–915 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 59 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 59 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 118 |
| Missing visible bounding boxes during action | 145 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 929 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-427] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-296] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-427] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-427] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-316] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-427] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-342] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-368] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-379] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-280] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-358] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-370] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-427] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-202] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-190] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-427] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-275] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-297] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-293] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-331] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-339] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-350] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-427] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-429] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-320] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-189] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-427] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-282] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-303] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-427] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-427] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [170-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-414] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-427] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-427] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-264] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-284] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-277] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-427] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-322] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-429] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-334] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-427] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-427] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-427] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-429] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-779] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [809-814] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [841-868] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-817] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-782] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [785-800] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-528] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [533-538] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [546-790] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [795-855] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [858-915] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [923-928] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-840] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [842-929] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-789] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [791-839] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [869-876] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-500] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [508-819] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [826-874] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-505] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [512-643] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [650-786] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-797] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [799-920] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-757] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [761-904] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-617] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [624-675] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [689-732] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [734-929] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-613] for track '60' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [617-644] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [665-929] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-789] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-558] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [602-613] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [620-633] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [642-650] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-555] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-499] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [502-755] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [765-780] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [786-796] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [802-851] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [760-763] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [780-804] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [778-788] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [785-788] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [826-829] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [831-833] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [836-872] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [880-884] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [887-904] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [906-913] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [915-928] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [819-882] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [887-888] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [828-895] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [833-839] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [837-839] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [840-929] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [852-855] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [862-923] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [863-871] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [879-915] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [923-924] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [891-910] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [913-915] for track '80' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.

</details>