# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_164

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_164`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 129
- **Validation Warnings:** 149
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `7` | `7` |
| ⚠️ START CHANGED | `Action_Handoff` | RB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 3 | START | 0 | 301 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 3 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 3 | START | 0 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 3 | START | 0 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 3 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 3 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 3 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 3 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 3 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 3 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 3 | START | 0 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `11` | 172 | START | 172 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 172 | START | 172 | 184 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 172 | START | 172 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 172 | START | 172 | 189 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `21` | 172 | START | 172 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `7` | `7` | 176 | START | 176 | 196 |
| ⚠️ START CHANGED | `Action_Handoff` | RB | `7` | `7` | 199 | START | 202 | 204 |

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
- **Visible Frames:** 0–312
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 312 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PressEdge` | 176 | 196 | 21 | inferred_complete_timeline |
| `Action_Handoff` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_PressEdge` | 205 | 226 | 22 | inferred_complete_timeline |
| `Action_None` | 227 | 233 | 7 | inferred_complete_timeline |
| `Action_None` | 245 | 299 | 55 | inferred_complete_timeline |
| `Action_None` | 301 | 424 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 301 | 302 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 321 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 340 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 449 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–438
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 323 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 338 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 417 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 424 | 428 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 434 | 435 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 437 | 438 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–377
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 355 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 358 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 366 | 370 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 377 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 202 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_None` | 220 | 223 | 4 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 187 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 184 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 211 | 25 | inferred_complete_timeline |
| `Action_None` | 230 | 257 | 28 | inferred_complete_timeline |
| `Action_None` | 265 | 424 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 189 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 219 | 24 | inferred_complete_timeline |
| `Action_None` | 220 | 280 | 61 | inferred_complete_timeline |
| `Action_None` | 282 | 296 | 15 | inferred_complete_timeline |
| `Action_None` | 299 | 325 | 27 | inferred_complete_timeline |
| `Action_None` | 327 | 333 | 7 | inferred_complete_timeline |
| `Action_None` | 336 | 372 | 37 | inferred_complete_timeline |
| `Action_None` | 374 | 449 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–408
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 219 | 48 | inferred_complete_timeline |
| `Action_None` | 220 | 238 | 19 | inferred_complete_timeline |
| `Action_None` | 265 | 308 | 44 | inferred_complete_timeline |
| `Action_None` | 312 | 408 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 308 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 449 | 450 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 220 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 265 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 296 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 397 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 399 | 400 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 405 | 408 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 415 | 417 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 424 | 425 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 449 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–402
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 402 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 449 | 450 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–392
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 256 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 392 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 319 | 320 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 401 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 403 | 405 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 408 | 449 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–366
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 366 | 367 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 283 | 284 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–278 | 147 | 8 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 2–360 | 327 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 209–356 | 132 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 226–327 | 96 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 235–449 | 200 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 239–240 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 244–449 | 205 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 268–389 | 112 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 295–319 | 25 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 309–316 | 6 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 330–390 | 30 | 4 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 334–449 | 105 | 5 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 349–362 | 14 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 400–449 | 50 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 401–406 | 6 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 406–417 | 11 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 408–426 | 19 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 446–449 | 4 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 448–449 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `7` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `7` (RB): Annotated start 199 != Inferred start 202

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 110 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-301] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-321] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-340] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-366] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-319] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-401] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-405] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-402] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-323] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-338] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-417] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-428] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-435] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-438] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [176-196] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-424] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-283] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-256] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-392] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-256] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-278] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-202] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-312] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-308] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-221] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-211] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-257] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-424] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-355] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-358] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-370] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-377] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-220] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-296] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-397] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-400] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-408] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-417] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-425] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-449] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-189] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-280] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-296] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-325] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-333] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-372] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-449] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-238] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-308] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-408] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-9] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-28] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-206] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-335] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-360] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-224] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-324] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-356] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-273] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-296] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-327] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-304] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-368] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-274] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-389] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-319] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-310] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-316] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-331] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-335] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-352] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-390] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-377] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-412] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-420] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-430] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-362] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-406] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-413] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-417] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-426] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-449] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>