# Play-Annotation-Generator Annotation Review — SplitZone_286

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_286`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 161
- **Validation Warnings:** 153
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 138
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | WR1 | offense | `11` | `11` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `2` |
| ✅ EXACT | `Action_Handoff` | WR1 | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 80 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 81 | START | 81 | 93 |
| ✅ EXACT | `Action_SplitBlock` | TE | `3` | `3` | 86 | START | 86 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `14` | 90 | START | 90 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `17` | 90 | START | 90 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 90 | START | 94 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 90 | START | 90 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `21` | 90 | START | 90 | 113 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 93 | END | 81 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | WR1 | `11` | `11` | 97 | START | 97 | 125 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `10` | `10` | 97 | START | 97 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `2` | 121 | START | 121 | 244 |
| ✅ EXACT | `Action_Handoff` | WR1 | `11` | `11` | 126 | START | 126 | 137 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_SnapReceive` | 81 | 93 | 13 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 97 | 107 | 11 | inferred_complete_timeline |
| `Action_None` | 108 | 407 | 300 | inferred_complete_timeline |
| `Action_None` | 410 | 413 | 4 | inferred_complete_timeline |
| `Action_None` | 415 | 419 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_BallCarry` | 121 | 244 | 124 | inferred_complete_timeline |
| `Action_BallCarry` | 246 | 352 | 107 | inferred_complete_timeline |
| `Action_BallCarry` | 355 | 419 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–391
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PressEdge` | 97 | 125 | 29 | inferred_complete_timeline |
| `Action_Handoff` | 126 | 137 | 12 | inferred_complete_timeline |
| `Action_PressEdge` | 138 | 152 | 15 | inferred_complete_timeline |
| `Action_None` | 153 | 325 | 173 | inferred_complete_timeline |
| `Action_None` | 327 | 366 | 40 | inferred_complete_timeline |
| `Action_None` | 369 | 376 | 8 | inferred_complete_timeline |
| `Action_None` | 378 | 379 | 2 | inferred_complete_timeline |
| `Action_None` | 381 | 382 | 2 | inferred_complete_timeline |
| `Action_None` | 390 | 391 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 174 | 94 | inferred_complete_timeline |
| `Action_None` | 185 | 297 | 113 | inferred_complete_timeline |
| `Action_None` | 300 | 308 | 9 | inferred_complete_timeline |
| `Action_None` | 311 | 315 | 5 | inferred_complete_timeline |
| `Action_None` | 318 | 419 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 136 | 56 | inferred_complete_timeline |
| `Action_None` | 140 | 419 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_SplitBlock` | 86 | 121 | 36 | inferred_complete_timeline |
| `Action_None` | 122 | 208 | 87 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 113 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 141 | 26 | inferred_complete_timeline |
| `Action_None` | 142 | 406 | 265 | inferred_complete_timeline |
| `Action_None` | 408 | 414 | 7 | inferred_complete_timeline |
| `Action_None` | 416 | 419 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–415
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 141 | 52 | inferred_complete_timeline |
| `Action_None` | 142 | 350 | 209 | inferred_complete_timeline |
| `Action_None` | 366 | 369 | 4 | inferred_complete_timeline |
| `Action_None` | 374 | 375 | 2 | inferred_complete_timeline |
| `Action_None` | 382 | 386 | 5 | inferred_complete_timeline |
| `Action_None` | 388 | 394 | 7 | inferred_complete_timeline |
| `Action_None` | 398 | 415 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_BallSnap` | 81 | 93 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 141 | 26 | inferred_complete_timeline |
| `Action_None` | 142 | 419 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 113 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 120 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 141 | 52 | inferred_complete_timeline |
| `Action_None` | 142 | 419 | 278 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 107 | 27 | inferred_complete_timeline |
| `Action_None` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_None` | 115 | 419 | 305 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 113 | 33 | inferred_complete_timeline |
| `Action_None` | 115 | 419 | 305 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 419 | 339 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 156 | 76 | inferred_complete_timeline |
| `Action_None` | 159 | 164 | 6 | inferred_complete_timeline |
| `Action_None` | 167 | 419 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–417
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 316 | 236 | inferred_complete_timeline |
| `Action_None` | 328 | 343 | 16 | inferred_complete_timeline |
| `Action_None` | 345 | 375 | 31 | inferred_complete_timeline |
| `Action_None` | 378 | 379 | 2 | inferred_complete_timeline |
| `Action_None` | 381 | 392 | 12 | inferred_complete_timeline |
| `Action_None` | 397 | 398 | 2 | inferred_complete_timeline |
| `Action_None` | 402 | 403 | 2 | inferred_complete_timeline |
| `Action_None` | 416 | 417 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 110 | 30 | inferred_complete_timeline |
| `Action_None` | 118 | 294 | 177 | inferred_complete_timeline |
| `Action_None` | 296 | 298 | 3 | inferred_complete_timeline |
| `Action_None` | 302 | 310 | 9 | inferred_complete_timeline |
| `Action_None` | 313 | 314 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 419 | 339 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 211 | 131 | inferred_complete_timeline |
| `Action_None` | 213 | 353 | 141 | inferred_complete_timeline |
| `Action_None` | 355 | 376 | 22 | inferred_complete_timeline |
| `Action_None` | 378 | 393 | 16 | inferred_complete_timeline |
| `Action_None` | 395 | 398 | 4 | inferred_complete_timeline |
| `Action_None` | 416 | 419 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 282 | 202 | inferred_complete_timeline |
| `Action_None` | 285 | 419 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 266 | 186 | inferred_complete_timeline |
| `Action_None` | 270 | 274 | 5 | inferred_complete_timeline |
| `Action_None` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_None` | 283 | 290 | 8 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_None` | 298 | 304 | 7 | inferred_complete_timeline |
| `Action_None` | 306 | 311 | 6 | inferred_complete_timeline |
| `Action_None` | 313 | 317 | 5 | inferred_complete_timeline |
| `Action_None` | 321 | 323 | 3 | inferred_complete_timeline |
| `Action_None` | 329 | 332 | 4 | inferred_complete_timeline |
| `Action_None` | 336 | 342 | 7 | inferred_complete_timeline |
| `Action_None` | 345 | 346 | 2 | inferred_complete_timeline |
| `Action_None` | 349 | 350 | 2 | inferred_complete_timeline |
| `Action_None` | 356 | 357 | 2 | inferred_complete_timeline |
| `Action_None` | 361 | 367 | 7 | inferred_complete_timeline |
| `Action_None` | 369 | 405 | 37 | inferred_complete_timeline |
| `Action_None` | 407 | 419 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 419 | 339 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 123–419 | 279 | 9 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 159–161 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 173–185 | 13 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 205–217 | 11 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 227–260 | 28 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 253–303 | 25 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 284–376 | 28 | 5 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 328–419 | 52 | 10 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 370–371 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 401–404 | 4 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 407–408 | 2 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 411–413 | 3 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 417–419 | 3 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 419–419 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 119 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [81–93], lower_priority='Action_ZoneBlock' annotated_start=90, effective_Action_ZoneBlock_start=94.
- ⚠️ Action 'Action_None' range [81-136] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [246-352] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [355-419] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-208] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-419] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-110] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-294] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-310] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-419] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-297] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-308] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-315] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-419] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-353] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-376] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-393] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-398] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-419] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-407] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-413] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-325] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-366] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-376] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-419] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-419] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-316] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-343] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-375] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-392] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-266] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-290] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-311] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-317] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-342] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-367] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-405] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-120] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-282] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-419] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [116-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-419] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-350] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-386] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-394] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-415] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-113] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-406] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-414] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-133] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-272] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-339] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-378] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-395] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-260] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-261] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-303] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-292] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-350] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-372] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-342] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-352] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-362] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-368] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-404] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-413] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-419] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-404] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-413] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-419] for track '36' has 1 frames without a visible bounding box.
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

</details>