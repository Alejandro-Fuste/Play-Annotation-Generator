# Play-Annotation-Generator Annotation Review — InsideZoneRead_117

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_117`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `15` | `14` |
| ✅ EXACT | `Action_ReadDefender` | RB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 270 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 270 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 270 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 270 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 270 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 4 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 270 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `6` | `Group` | 0 | START | 0 | 270 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 271 | START | 271 | 284 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 274 | START | 298 | 299 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `15` | 274 | START | 274 | 371 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `18` | 274 | START | 274 | 308 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 274 | START | 274 | 289 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 274 | START | 274 | 289 |
| ✅ EXACT | `Action_SnapReceive` | RB | `15` | `14` | 290 | END | 271 | 290 |
| ✅ EXACT | `Action_ReadDefender` | RB | `15` | `14` | 293 | START | 293 | 316 |
| ✅ EXACT | `Action_BallCarry` | RB | `15` | `14` | 317 | START | 317 | 479 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 371 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 473

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_None` | 271 | 445 | 175 | inferred_complete_timeline |
| `Action_None` | 450 | 475 | 26 | inferred_complete_timeline |
| `Action_None` | 479 | 479 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_SnapReceive` | 271 | 290 | 20 | inferred_complete_timeline |
| `Action_None` | 291 | 292 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 293 | 316 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 317 | 479 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_None` | 271 | 479 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_None` | 271 | 479 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_None` | 271 | 479 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_None` | 271 | 336 | 66 | inferred_complete_timeline |
| `Action_None` | 338 | 346 | 9 | inferred_complete_timeline |
| `Action_None` | 349 | 368 | 20 | inferred_complete_timeline |
| `Action_None` | 373 | 374 | 2 | inferred_complete_timeline |
| `Action_None` | 377 | 381 | 5 | inferred_complete_timeline |
| `Action_None` | 384 | 390 | 7 | inferred_complete_timeline |
| `Action_None` | 393 | 479 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 27 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 195 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 4–479
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 27 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 37 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 195 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 273 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 274 | 289 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 323 | 371 | 49 | inferred_complete_timeline |
| `Action_None` | 372 | 445 | 74 | inferred_complete_timeline |
| `Action_None` | 448 | 479 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–347
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_BallSnap` | 271 | 284 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 305 | 347 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 203 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 273 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 274 | 308 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 362 | 371 | 10 | inferred_complete_timeline |
| `Action_None` | 372 | 444 | 73 | inferred_complete_timeline |
| `Action_None` | 447 | 473 | 27 | inferred_complete_timeline |
| `Action_None` | 476 | 477 | 2 | inferred_complete_timeline |
| `Action_None` | 479 | 479 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 51 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 203 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 219 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 273 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 274 | 371 | 98 | inferred_complete_timeline |
| `Action_None` | 372 | 479 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 195 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 270 | 42 | inferred_complete_timeline |
| `Action_None` | 271 | 479 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 191 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 270 | 35 | inferred_complete_timeline |
| `Action_None` | 271 | 445 | 175 | inferred_complete_timeline |
| `Action_None` | 448 | 479 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 25 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 71 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 191 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 270 | 37 | inferred_complete_timeline |
| `Action_None` | 271 | 479 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_None` | 271 | 454 | 184 | inferred_complete_timeline |
| `Action_None` | 456 | 479 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–444
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_None` | 271 | 420 | 150 | inferred_complete_timeline |
| `Action_None` | 440 | 444 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_None` | 271 | 445 | 175 | inferred_complete_timeline |
| `Action_None` | 447 | 479 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–446
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_None` | 271 | 446 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_None` | 271 | 405 | 135 | inferred_complete_timeline |
| `Action_None` | 407 | 479 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_None` | 271 | 479 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–459
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 270 | 271 | inferred_complete_timeline |
| `Action_None` | 271 | 392 | 122 | inferred_complete_timeline |
| `Action_None` | 395 | 396 | 2 | inferred_complete_timeline |
| `Action_None` | 399 | 400 | 2 | inferred_complete_timeline |
| `Action_None` | 423 | 428 | 6 | inferred_complete_timeline |
| `Action_None` | 450 | 459 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–318 | 236 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 231–479 | 213 | 8 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 338–479 | 139 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 340–479 | 139 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 355–361 | 7 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 383–443 | 48 | 5 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 405–479 | 74 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 461–479 | 12 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 465–479 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 92 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [271–290], lower_priority='Action_ZoneBlock' annotated_start=274, effective_Action_ZoneBlock_start=291.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RT) duration 98 frames exceeds threshold 90 frames [start=274, end=371].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RG) duration 98 frames exceeds threshold 90 frames [start=274, end=371].
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=274, end=195. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 98 frames exceeds threshold 90 frames [start=274, end=371].
- ⚠️ Action 'Action_None' range [271-445] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-405] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-479] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-336] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-346] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-368] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-381] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-390] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-454] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-479] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-392] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-428] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-459] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-446] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-420] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-444] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-195] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-445] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-475] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [271-284] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [298-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [305-347] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-203] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-213] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-219] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-191] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-445] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-24] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-71] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-199] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-232] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-318] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-203] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [274-308] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [314-315] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [328-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-444] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-473] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-25] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-71] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-191] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-195] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-479] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-27] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-195] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-27] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-37] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-195] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [274-289] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [320-321] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-445] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-270] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-326] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-344] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-364] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-445] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-471] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-366] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-381] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-459] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-361] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-412] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-437] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-477] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-468] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-479] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-479] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>