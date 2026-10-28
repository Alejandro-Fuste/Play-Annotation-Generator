# Play-Annotation-Generator Annotation Review — Draw_94

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_94`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 206
- **Validation Warnings:** 216
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 181
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `19` | `18` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | RB | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 31 | START | 31 | 44 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `16` | `15` | 34 | START | 45 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `17` | 34 | START | 34 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `20` | 34 | START | 34 | 108 |
| ✅ EXACT | `Action_PassBlock` | LT | `22` | `21` | 34 | START | 34 | 108 |
| ✅ EXACT | `Action_PassBlock` | RT | `9` | `8` | 34 | START | 34 | 108 |
| ✅ EXACT | `Action_SnapReceive` | RB | `19` | `18` | 44 | END | 31 | 44 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | RB | `19` | `18` | 49 | START | 49 | 80 |
| ✅ EXACT | `Action_BallCarry` | RB | `19` | `18` | 81 | START | 81 | 111 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 108 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 118 | 88 | inferred_complete_timeline |
| `Action_None` | 126 | 218 | 93 | inferred_complete_timeline |
| `Action_None` | 221 | 248 | 28 | inferred_complete_timeline |
| `Action_None` | 251 | 419 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 44 | 14 | inferred_complete_timeline |
| `Action_None` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 49 | 80 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 111 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 419 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 419 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 122 | 92 | inferred_complete_timeline |
| `Action_None` | 124 | 142 | 19 | inferred_complete_timeline |
| `Action_None` | 146 | 216 | 71 | inferred_complete_timeline |
| `Action_None` | 218 | 227 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 208 | 178 | inferred_complete_timeline |
| `Action_None` | 210 | 251 | 42 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 266 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 275 | 4 | inferred_complete_timeline |
| `Action_None` | 279 | 284 | 6 | inferred_complete_timeline |
| `Action_None` | 290 | 292 | 3 | inferred_complete_timeline |
| `Action_None` | 296 | 297 | 2 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 311 | 312 | 2 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 319 | 321 | 3 | inferred_complete_timeline |
| `Action_None` | 326 | 330 | 5 | inferred_complete_timeline |
| `Action_None` | 333 | 337 | 5 | inferred_complete_timeline |
| `Action_None` | 341 | 342 | 2 | inferred_complete_timeline |
| `Action_None` | 350 | 352 | 3 | inferred_complete_timeline |
| `Action_None` | 356 | 361 | 6 | inferred_complete_timeline |
| `Action_None` | 363 | 368 | 6 | inferred_complete_timeline |
| `Action_None` | 381 | 390 | 10 | inferred_complete_timeline |
| `Action_None` | 395 | 419 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 108 | 75 | inferred_complete_timeline |
| `Action_None` | 111 | 116 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 74 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 79 | 108 | 30 | inferred_complete_timeline |
| `Action_None` | 109 | 124 | 16 | inferred_complete_timeline |
| `Action_None` | 129 | 246 | 118 | inferred_complete_timeline |
| `Action_None` | 251 | 263 | 13 | inferred_complete_timeline |
| `Action_None` | 273 | 274 | 2 | inferred_complete_timeline |
| `Action_None` | 291 | 292 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 44 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 61 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 108 | 75 | inferred_complete_timeline |
| `Action_None` | 109 | 124 | 16 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 363 | 229 | inferred_complete_timeline |
| `Action_None` | 365 | 370 | 6 | inferred_complete_timeline |
| `Action_None` | 395 | 419 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 108 | 75 | inferred_complete_timeline |
| `Action_None` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 144 | 114 | inferred_complete_timeline |
| `Action_None` | 153 | 250 | 98 | inferred_complete_timeline |
| `Action_None` | 253 | 266 | 14 | inferred_complete_timeline |
| `Action_None` | 269 | 274 | 6 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 283 | 5 | inferred_complete_timeline |
| `Action_None` | 290 | 300 | 11 | inferred_complete_timeline |
| `Action_None` | 320 | 322 | 3 | inferred_complete_timeline |
| `Action_None` | 335 | 337 | 3 | inferred_complete_timeline |
| `Action_None` | 350 | 352 | 3 | inferred_complete_timeline |
| `Action_None` | 363 | 366 | 4 | inferred_complete_timeline |
| `Action_None` | 398 | 419 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–402
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 402 | 372 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 96 | 66 | inferred_complete_timeline |
| `Action_None` | 101 | 108 | 8 | inferred_complete_timeline |
| `Action_None` | 113 | 419 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 83 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 113 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 79 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–406
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 266 | 236 | inferred_complete_timeline |
| `Action_None` | 271 | 275 | 5 | inferred_complete_timeline |
| `Action_None` | 283 | 300 | 18 | inferred_complete_timeline |
| `Action_None` | 303 | 306 | 4 | inferred_complete_timeline |
| `Action_None` | 323 | 376 | 54 | inferred_complete_timeline |
| `Action_None` | 378 | 388 | 11 | inferred_complete_timeline |
| `Action_None` | 402 | 406 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 419 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 239 | 209 | inferred_complete_timeline |
| `Action_None` | 242 | 246 | 5 | inferred_complete_timeline |
| `Action_None` | 261 | 266 | 6 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 276 | 283 | 8 | inferred_complete_timeline |
| `Action_None` | 291 | 300 | 10 | inferred_complete_timeline |
| `Action_None` | 302 | 358 | 57 | inferred_complete_timeline |
| `Action_None` | 362 | 390 | 29 | inferred_complete_timeline |
| `Action_None` | 395 | 396 | 2 | inferred_complete_timeline |
| `Action_None` | 403 | 406 | 4 | inferred_complete_timeline |
| `Action_None` | 411 | 418 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 202 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 140 | 110 | inferred_complete_timeline |
| `Action_None` | 145 | 246 | 102 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 259 | 261 | 3 | inferred_complete_timeline |
| `Action_None` | 265 | 297 | 33 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |
| `Action_None` | 302 | 419 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 60–292 | 192 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 96–97 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 103–292 | 162 | 10 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 106–417 | 292 | 8 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 127–386 | 260 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 130–419 | 267 | 6 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 154–419 | 207 | 7 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 161–352 | 175 | 4 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 264–266 | 3 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 275–276 | 2 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 278–418 | 131 | 5 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 282–419 | 119 | 6 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 307–308 | 2 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 310–312 | 3 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 312–419 | 39 | 4 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 312–321 | 10 | 1 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 328–417 | 21 | 6 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 356–419 | 63 | 2 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 372–419 | 41 | 4 | Undefined position; Undefined team |
| `42` | `63` | Position_Unknown | Team_Unknown | 389–390 | 2 | 1 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 402–416 | 13 | 3 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 409–416 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `16` (C): Annotated start 34 != Inferred start 45
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 168 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [31–44], lower_priority='Action_PassBlock' annotated_start=34, effective_Action_PassBlock_start=45.
- ⚠️ Action 'Action_None' range [31-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-251] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-284] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-330] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-337] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-361] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-368] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-390] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-419] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-419] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-402] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-216] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-227] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-144] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-250] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-266] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-274] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-283] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-300] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-366] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-283] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-300] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-358] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-390] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-406] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-418] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-266] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-300] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-376] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-388] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-406] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-140] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-246] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-297] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-419] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-120] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-419] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-202] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-124] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-246] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-118] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-218] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-363] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-370] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-209] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-234] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-284] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-221] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-275] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-300] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-306] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-312] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-367] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-417] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-386] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-136] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-247] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-393] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-373] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-410] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-246] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-265] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-288] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-352] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-286] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-396] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-418] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-297] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-302] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-419] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-395] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-413] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-321] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-336] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-371] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-416] for track '40' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-386] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-393] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-419] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-410] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-416] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-416] for track '44' has 1 frames without a visible bounding box.
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

</details>