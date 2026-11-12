# Play-Annotation-Generator Annotation Review — SplitZone_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_17`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 509
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 148
- **Validation Warnings:** 158
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 4
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 117
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `29` | `27` |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `1` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 336 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 378 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 336 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 251 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 0 | START | 0 | 345 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `19` | `19` | 337 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `15` | 338 | START | 341 | 353 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `18` | `18` | 338 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `9` | `9` | 346 | START | 346 | 391 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `4` | `4` | 347 | END | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `29` | `27` | 350 | START | 371 | 395 |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | `4` | `4` | 365 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `1` | `1` | 379 | START | 379 | 408 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 422 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 251 | 252 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 288 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 295 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–474
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 378 | 379 | inferred_complete_timeline |
| `Action_BallCarry` | 379 | 408 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 413 | 474 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 507

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 336 | 337 | inferred_complete_timeline |
| `Action_None` | 337 | 436 | 100 | inferred_complete_timeline |
| `Action_None` | 440 | 509 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 336 | 337 | inferred_complete_timeline |
| `Action_None` | 337 | 509 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 482

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 194 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 336 | 117 | inferred_complete_timeline |
| `Action_None` | 337 | 363 | 27 | inferred_complete_timeline |
| `Action_None` | 365 | 367 | 3 | inferred_complete_timeline |
| `Action_None` | 370 | 402 | 33 | inferred_complete_timeline |
| `Action_None` | 409 | 509 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–406
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 345 | 346 | inferred_complete_timeline |
| `Action_SplitBlock` | 346 | 391 | 46 | inferred_complete_timeline |
| `Action_SplitBlock` | 395 | 396 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 398 | 406 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–465
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 19 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 105 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 123 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 166 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 341 | 353 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 376 | 422 | 47 | inferred_complete_timeline |
| `Action_None` | 423 | 465 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 159 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 72 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 205 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 262 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 291 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 298 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 336 | 30 | inferred_complete_timeline |
| `Action_None` | 337 | 509 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 37 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 166 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 253 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 282 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 336 | 7 | inferred_complete_timeline |
| `Action_None` | 337 | 385 | 49 | inferred_complete_timeline |
| `Action_None` | 387 | 509 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 23 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 45 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 171 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 193 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 209 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 257 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 287 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 310 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 321 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 336 | 12 | inferred_complete_timeline |
| `Action_None` | 337 | 377 | 41 | inferred_complete_timeline |
| `Action_None` | 386 | 509 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 503

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 336 | 337 | inferred_complete_timeline |
| `Action_None` | 337 | 388 | 52 | inferred_complete_timeline |
| `Action_None` | 394 | 414 | 21 | inferred_complete_timeline |
| `Action_None` | 417 | 509 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 336 | 337 | inferred_complete_timeline |
| `Action_None` | 337 | 481 | 145 | inferred_complete_timeline |
| `Action_None` | 483 | 488 | 6 | inferred_complete_timeline |
| `Action_None` | 491 | 497 | 7 | inferred_complete_timeline |
| `Action_None` | 500 | 509 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 336 | 309 | inferred_complete_timeline |
| `Action_None` | 337 | 445 | 109 | inferred_complete_timeline |
| `Action_None` | 449 | 509 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 336 | 337 | inferred_complete_timeline |
| `Action_None` | 337 | 426 | 90 | inferred_complete_timeline |
| `Action_None` | 431 | 432 | 2 | inferred_complete_timeline |
| `Action_None` | 434 | 509 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 336 | 337 | inferred_complete_timeline |
| `Action_None` | 337 | 509 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–428
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 336 | 337 | inferred_complete_timeline |
| `Action_None` | 337 | 428 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 336 | 337 | inferred_complete_timeline |
| `Action_None` | 337 | 509 | 173 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 5–31 | 18 | 5 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 28–125 | 98 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 89–430 | 190 | 9 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 89–509 | 251 | 6 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 151–161 | 11 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 308–507 | 188 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 342–509 | 168 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 343–373 | 27 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 371–509 | 131 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 389–401 | 4 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 414–509 | 92 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 417–505 | 83 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 433–509 | 77 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 449–509 | 60 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 483–509 | 23 | 4 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 503–504 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `19` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `18` (RT)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `9` (3 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `4` (QB)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `29` (2 segments found)
- ❌ Missing segment for action `Action_Handoff` on target `4` (QB)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 121 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '4' has invalid range: start=337, end=295. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '4' has invalid range: start=365, end=295. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '18' has invalid range: start=338, end=159. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '19' has invalid range: start=337, end=31. Clamping end to start.
- ⚠️ Action 'Action_BallCarry' range [379-408] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [413-474] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-426] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-509] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-254] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-288] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-388] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-414] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-481] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-488] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-497] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-509] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-428] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [346-391] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [395-396] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [398-406] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-211] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-336] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-363] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-402] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-509] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-445] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-72] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-205] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-262] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-291] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-336] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-509] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-436] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-23] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-45] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-209] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-257] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-287] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-310] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-321] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-336] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-377] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-19] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-105] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-166] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [341-353] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-465] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-253] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-282] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-385] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-509] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-7] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-19] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-23] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-31] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-106] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-140] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-168] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-256] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-282] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-336] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-430] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-166] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-380] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-424] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-310] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-373] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-507] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-509] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [371-395] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-509] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-431] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-497] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-505] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-455] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-489] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-494] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-499] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-509] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>