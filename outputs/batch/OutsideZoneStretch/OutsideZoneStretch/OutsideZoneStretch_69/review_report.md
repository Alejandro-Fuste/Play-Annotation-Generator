# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_69

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_69`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 240
- **Validation Warnings:** 306
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 1
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 211
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `16` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 260 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 137 | START | 137 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `3` | `3` | 153 | START | 153 | 175 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `16` | `14` | 171 | START | 171 | 180 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_PressEdge` | 153 | 175 | 23 | inferred_complete_timeline |
| `Action_PressEdge` | 177 | 191 | 15 | inferred_complete_timeline |
| `Action_PressEdge` | 194 | 201 | 8 | inferred_complete_timeline |
| `Action_PressEdge` | 205 | 205 | 1 | inferred_complete_timeline |
| `Action_None` | 206 | 259 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–447
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 273 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 304 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 423 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 425 | 442 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 446 | 447 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–437
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 260 | 261 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 405 | 143 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 410 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 415 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 420 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 427 | 429 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 436 | 437 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 187 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 217 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 231 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 250 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 136 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 143 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 168 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 192 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 201 | 6 | inferred_complete_timeline |
| `Action_None` | 203 | 243 | 41 | inferred_complete_timeline |
| `Action_None` | 245 | 248 | 4 | inferred_complete_timeline |
| `Action_None` | 250 | 288 | 39 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–5
- **Visible Samples:** 6

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 192 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 195 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–428
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 187 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 237 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 249 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 260 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 303 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 307 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 312 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 328 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 401 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 418 | 419 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 427 | 428 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 166 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 201 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 204 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–381
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 381 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 452 | 453 | inferred_complete_timeline |
| `Action_PreSnap` | 467 | 479 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 280 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 286 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 304 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 311 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 323 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 365 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 380 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 389 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 391 | 398 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 424 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–380
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 349 | 350 | inferred_complete_timeline |
| `Action_PreSnap` | 352 | 360 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 362 | 364 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 376 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 380 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `15` | Position_Unknown | Team_Unknown | 104–443 | 262 | 11 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 144–479 | 326 | 6 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 155–479 | 310 | 8 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 163–459 | 228 | 13 | Undefined position; Undefined team |
| `17` | `24` | Position_Unknown | Team_Unknown | 176–479 | 298 | 4 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 178–331 | 150 | 3 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 178–479 | 261 | 10 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 178–479 | 266 | 9 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 178–479 | 294 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 179–479 | 286 | 6 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 204–212 | 9 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 211–225 | 10 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 225–288 | 52 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 230–414 | 169 | 9 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 235–257 | 11 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 249–479 | 218 | 5 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 263–308 | 44 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 314–315 | 2 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 322–477 | 99 | 10 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 326–420 | 71 | 3 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 329–479 | 134 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 344–345 | 2 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 353–354 | 2 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 360–479 | 117 | 2 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 369–479 | 51 | 10 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 389–392 | 4 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 390–433 | 14 | 3 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 411–413 | 3 | 1 | Undefined position; Undefined team |
| `42` | `63` | Position_Unknown | Team_Unknown | 412–415 | 4 | 1 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 417–418 | 2 | 1 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 424–479 | 49 | 3 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 428–479 | 49 | 2 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 431–479 | 30 | 6 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 448–462 | 15 | 1 | Undefined position; Undefined team |
| `48` | `72` | Position_Unknown | Team_Unknown | 472–473 | 2 | 1 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 474–479 | 6 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 475–479 | 5 | 1 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 479–479 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `3` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 227 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-235] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-273] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-304] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-423] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-442] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-447] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-260] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-405] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-410] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-415] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-420] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-429] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-437] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-452] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-479] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [153-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [177-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [194-201] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-259] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-187] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-192] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-231] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-236] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-187] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-237] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-240] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-249] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-260] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-303] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-307] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-312] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-328] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-401] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-419] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-428] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-349] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-360] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-364] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-376] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-280] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-304] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-311] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-323] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-365] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-380] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-389] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-398] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-424] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-381] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [171-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [176-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-243] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-288] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-166] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-201] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-192] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-197] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-313] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-323] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-389] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-398] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-419] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-430] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-443] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-374] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-409] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-461] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-479] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-192] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-209] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-392] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-417] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-326] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-368] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-373] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-402] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-408] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-413] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-435] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-440] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-452] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-455] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-459] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-218] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-472] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [475-479] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-187] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-331] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-288] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-330] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-348] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-389] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-412] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-418] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-421] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-192] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-312] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-324] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-479] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-383] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-431] for track '22' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-449] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-479] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-216] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-225] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-288] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-251] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-288] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-318] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-326] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-403] for track '26' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-408] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-414] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-243] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-257] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-257] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-288] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-311] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-303] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-308] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-324] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-384] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-404] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-414] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-432] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-436] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-449] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-458] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-468] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-477] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-401] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-420] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-446] for track '34' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-345] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-354] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-365] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-479] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-379] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-397] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-410] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-422] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-425] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-435] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-439] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-453] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-457] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-392] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-399] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-417] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-433] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-413] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-415] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-418] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-437] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-444] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-479] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-431] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-479] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-435] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-448] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-457] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-460] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-464] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-479] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-462] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-473] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-479] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [475-479] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>