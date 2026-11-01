# Play-Annotation-Generator Annotation Review — InsideZoneRead_200

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_200`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 125
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 241 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 0 | START | 0 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 241 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 241 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 241 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 239 | START | 239 | 250 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `10` | 242 | START | 242 | 317 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `16` | 242 | START | 242 | 264 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 242 | START | 251 | 290 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 242 | START | 242 | 263 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 242 | START | 242 | 317 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 250 | END | 239 | 250 |
| ✅ EXACT | `Action_ReadDefender` | QB | `19` | `18` | 254 | START | 254 | 267 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `18` | 268 | START | 268 | 278 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `11` | 279 | START | 279 | 373 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 317 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–304
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_SnapReceive` | 239 | 250 | 12 | inferred_complete_timeline |
| `Action_None` | 251 | 253 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 254 | 267 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 268 | 278 | 11 | inferred_complete_timeline |
| `Action_None` | 279 | 304 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 278 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 279 | 373 | 95 | inferred_complete_timeline |
| `Action_BallCarry` | 375 | 389 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 296 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 389 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 389 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 378 | 140 | inferred_complete_timeline |
| `Action_None` | 382 | 389 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 241 | 242 | inferred_complete_timeline |
| `Action_ZoneBlock` | 242 | 317 | 76 | inferred_complete_timeline |
| `Action_None` | 318 | 339 | 22 | inferred_complete_timeline |
| `Action_None` | 341 | 352 | 12 | inferred_complete_timeline |
| `Action_None` | 362 | 389 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 241 | 242 | inferred_complete_timeline |
| `Action_ZoneBlock` | 242 | 264 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 276 | 280 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_BallSnap` | 239 | 250 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 290 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 308 | 317 | 10 | inferred_complete_timeline |
| `Action_None` | 318 | 328 | 11 | inferred_complete_timeline |
| `Action_None` | 330 | 333 | 4 | inferred_complete_timeline |
| `Action_None` | 336 | 389 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 241 | 242 | inferred_complete_timeline |
| `Action_ZoneBlock` | 242 | 263 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 266 | 277 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 279 | 284 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 290 | 317 | 28 | inferred_complete_timeline |
| `Action_None` | 318 | 339 | 22 | inferred_complete_timeline |
| `Action_None` | 341 | 354 | 14 | inferred_complete_timeline |
| `Action_None` | 356 | 378 | 23 | inferred_complete_timeline |
| `Action_None` | 380 | 389 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 241 | 242 | inferred_complete_timeline |
| `Action_ZoneBlock` | 242 | 317 | 76 | inferred_complete_timeline |
| `Action_None` | 318 | 389 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–339
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 339 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 282 | 44 | inferred_complete_timeline |
| `Action_None` | 285 | 318 | 34 | inferred_complete_timeline |
| `Action_None` | 323 | 326 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 266 | 28 | inferred_complete_timeline |
| `Action_None` | 268 | 296 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 268 | 30 | inferred_complete_timeline |
| `Action_None` | 270 | 389 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 389 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 389 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 366 | 128 | inferred_complete_timeline |
| `Action_None` | 368 | 369 | 2 | inferred_complete_timeline |
| `Action_None` | 374 | 377 | 4 | inferred_complete_timeline |
| `Action_None` | 379 | 380 | 2 | inferred_complete_timeline |
| `Action_None` | 382 | 389 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 319 | 81 | inferred_complete_timeline |
| `Action_None` | 321 | 389 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 348 | 110 | inferred_complete_timeline |
| `Action_None` | 365 | 389 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 389 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–345
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_None` | 239 | 345 | 107 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 35–133 | 92 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 36–48 | 12 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 161–237 | 46 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 194–244 | 15 | 5 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 261–264 | 4 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 285–304 | 9 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 311–315 | 5 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 314–377 | 32 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 316–321 | 6 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 319–389 | 60 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 319–325 | 5 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 322–389 | 65 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 346–384 | 28 | 3 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 349–389 | 22 | 6 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 351–389 | 39 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 354–376 | 15 | 4 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 358–389 | 32 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 362–371 | 10 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 364–372 | 9 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 366–367 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [239–250], lower_priority='Action_ZoneBlock' annotated_start=242, effective_Action_ZoneBlock_start=251.
- ⚠️ Action 'Action_None' range [239-378] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-296] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-339] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-282] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-318] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-389] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-345] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-268] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-389] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-348] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [242-317] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-339] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-352] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [279-373] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-319] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-389] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-296] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [242-264] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [276-280] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-304] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-366] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [251-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-328] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-333] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [242-263] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [266-277] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [279-284] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-339] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-354] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-378] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-75] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-126] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-40] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-48] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-187] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-191] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-199] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-315] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-371] for track '29' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-377] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-321] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-325] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-332] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-389] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-377] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-366] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-384] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-354] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-377] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-369] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-389] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-371] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-372] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '41' has 1 frames without a visible bounding box.
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