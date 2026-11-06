# Play-Annotation-Generator Annotation Review — OutsideZoneRead_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_46`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 231
- **Validation Warnings:** 299
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 206
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_PressEdge` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 0 | START | 0 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `14` | 77 | START | 77 | 107 |
| ✅ EXACT | `Action_ZoneBlock` | C | `17` | `17` | 77 | START | 77 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `19` | 77 | START | 77 | 103 |
| ❌ MISSING SEGMENT | `Action_PressEdge` | QB | `12` | `12` | 82 | START | N/A | N/A |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `12` | `12` | 82 | START | 82 | 100 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 101 | START | 101 | 111 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 82 | 100 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 101 | 111 | 11 | inferred_complete_timeline |
| `Action_None` | 112 | 329 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 118 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–468
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 118 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 125 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 443 | 303 | inferred_complete_timeline |
| `Action_PreSnap` | 453 | 468 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 290 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 306 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 479 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 107 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 118 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 125 | 6 | inferred_complete_timeline |
| `Action_None` | 126 | 126 | 1 | inferred_complete_timeline |
| `Action_None` | 150 | 288 | 139 | inferred_complete_timeline |
| `Action_None` | 293 | 306 | 14 | inferred_complete_timeline |
| `Action_None` | 310 | 322 | 13 | inferred_complete_timeline |
| `Action_None` | 341 | 413 | 73 | inferred_complete_timeline |
| `Action_None` | 415 | 421 | 7 | inferred_complete_timeline |
| `Action_None` | 423 | 424 | 2 | inferred_complete_timeline |
| `Action_None` | 428 | 433 | 6 | inferred_complete_timeline |
| `Action_None` | 435 | 449 | 15 | inferred_complete_timeline |
| `Action_None` | 451 | 460 | 10 | inferred_complete_timeline |
| `Action_None` | 463 | 479 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 125 | 49 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 205 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 103 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 118 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 125 | 6 | inferred_complete_timeline |
| `Action_None` | 126 | 126 | 1 | inferred_complete_timeline |
| `Action_None` | 132 | 479 | 348 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–450
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 128 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 433 | 304 | inferred_complete_timeline |
| `Action_PreSnap` | 440 | 450 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 118 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 281 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 474 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 477 | 479 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 101 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 251 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 369 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 372 | 409 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 411 | 413 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 415 | 419 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 421 | 427 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 429 | 452 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 458 | 479 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–472
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 244 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 251 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 278 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 283 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 419 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 421 | 472 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 200 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 245 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 279 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 283 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 306 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 479 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 182 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 277 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 161 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–202 | 190 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–476 | 433 | 12 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–268 | 243 | 7 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 52–95 | 23 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 110–479 | 359 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 111–155 | 36 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 124–399 | 264 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 142–479 | 338 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 175–332 | 149 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 176–249 | 68 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 177–178 | 2 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 188–194 | 6 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 198–479 | 270 | 4 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 204–472 | 264 | 5 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 213–218 | 6 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 224–321 | 61 | 4 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 227–229 | 3 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 233–236 | 4 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 244–331 | 43 | 7 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 260–479 | 217 | 2 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 267–479 | 180 | 14 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 268–314 | 18 | 4 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 283–323 | 22 | 5 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 286–479 | 158 | 8 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 301–391 | 26 | 8 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 305–307 | 3 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 311–333 | 21 | 2 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 345–349 | 5 | 1 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 363–427 | 65 | 1 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 399–479 | 70 | 3 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 404–479 | 76 | 1 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 426–428 | 3 | 1 | Undefined position; Undefined team |
| `53` | `76` | Position_Unknown | Team_Unknown | 426–477 | 39 | 4 | Undefined position; Undefined team |
| `54` | `77` | Position_Unknown | Team_Unknown | 435–479 | 45 | 1 | Undefined position; Undefined team |
| `55` | `79` | Position_Unknown | Team_Unknown | 450–452 | 3 | 1 | Undefined position; Undefined team |
| `56` | `81` | Position_Unknown | Team_Unknown | 464–465 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ❌ Missing segment for action `Action_PressEdge` on target `12` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 218 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 94: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 94: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 94: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Overlapping action conflict at frame 82 for track '12': 'Action_PressEdge' vs 'Action_ReadEdgeDefender'. Overriding with 'Action_ReadEdgeDefender'.
- ⚠️ Action 'Action_PreSnap' range [0-238] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-290] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-306] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-479] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-200] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-245] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-279] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-283] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-306] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-479] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-118] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-118] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-134] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-281] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-474] for track '5' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-277] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-125] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-135] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-443] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-468] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-190] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-244] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-251] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-278] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-283] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-419] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-472] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-251] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-369] for track '11' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-409] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-413] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-419] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-427] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-452] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-479] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-329] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-107] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 126, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [126-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-288] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-306] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-322] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-413] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-421] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-433] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-449] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-460] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-197] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-245] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-288] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-291] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-368] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-476] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-128] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-433] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-450] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-205] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-182] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-103] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-118] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 126, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [126-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-479] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-118] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-251] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-268] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-60] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-85] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-125] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-479] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-353] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-368] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-394] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-399] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-219] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-328] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-332] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-241] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-189] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-194] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-337] for track '32' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-356] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-361] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-479] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-288] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-323] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-335] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-341] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-472] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-218] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-288] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-305] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-321] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-229] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-236] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-246] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-254] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-284] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-300] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-306] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-320] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-331] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-466] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-276] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-306] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-321] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-330] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-339] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-343] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-355] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-358] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-361] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-365] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-388] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-479] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-279] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-290] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-306] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-310] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-325] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-331] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-361] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-390] for track '43' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-409] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-441] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-479] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-306] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-313] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-321] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-369] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-375] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-385] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-388] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-391] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-307] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-324] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-333] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-349] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-359] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-427] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-402] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-428] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-428] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-457] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-460] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-468] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [475-477] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-452] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-465] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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