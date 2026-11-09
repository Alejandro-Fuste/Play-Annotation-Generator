# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_70`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 181
- **Validation Warnings:** 225
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 160
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `0` | `0` | 140 | START | 140 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `1` | 140 | START | 140 | 158 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `2` | `2` | 140 | START | 140 | 182 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 140 | START | 140 | 182 |
| ✅ EXACT | `Action_PressEdge` | RB | `3` | `3` | 144 | START | 144 | 203 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 155 | START | 155 | 177 |

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
- **Visible Frames:** 0–224
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 154 | 113 | inferred_complete_timeline |
| `Action_Handoff` | 155 | 177 | 23 | inferred_complete_timeline |
| `Action_None` | 178 | 224 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–360
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PressEdge` | 144 | 203 | 60 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_None` | 212 | 332 | 121 | inferred_complete_timeline |
| `Action_None` | 335 | 354 | 20 | inferred_complete_timeline |
| `Action_None` | 357 | 360 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 199 | 187 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 264 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 139 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 182 | 43 | inferred_complete_timeline |
| `Action_None` | 183 | 228 | 46 | inferred_complete_timeline |
| `Action_None` | 230 | 233 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–412
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 139 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 158 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 182 | 21 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 231 | 45 | inferred_complete_timeline |
| `Action_None` | 233 | 286 | 54 | inferred_complete_timeline |
| `Action_None` | 288 | 412 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–405
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 139 | 106 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 182 | 43 | inferred_complete_timeline |
| `Action_None` | 183 | 195 | 13 | inferred_complete_timeline |
| `Action_None` | 197 | 281 | 85 | inferred_complete_timeline |
| `Action_None` | 297 | 302 | 6 | inferred_complete_timeline |
| `Action_None` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_None` | 315 | 316 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 405 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 139 | 116 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 165 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 182 | 1 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 239 | 53 | inferred_complete_timeline |
| `Action_None` | 246 | 294 | 49 | inferred_complete_timeline |
| `Action_None` | 302 | 363 | 62 | inferred_complete_timeline |
| `Action_None` | 378 | 379 | 2 | inferred_complete_timeline |
| `Action_None` | 381 | 409 | 29 | inferred_complete_timeline |
| `Action_None` | 412 | 479 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 142 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 248 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 257 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 269 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 395 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 397 | 402 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 404 | 415 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 421 | 479 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–425
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 48 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 191 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 425 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–415
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 210 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 311 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 327 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 352 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 383 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 385 | 386 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 394 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 411 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 415 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 234 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 161 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 313 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 431 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 437 | 438 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 446 | 447 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 453 | 479 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 212 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 236 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–1
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 213 | 199 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 242 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 249 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 257 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 285 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 333 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 359 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 382 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 387 | 391 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 415 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 420 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 423 | 479 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 11–230 | 217 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 16–479 | 388 | 14 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 27–201 | 151 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 27–479 | 435 | 8 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 171–479 | 262 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 171–206 | 4 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 177–218 | 37 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 196–384 | 183 | 3 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 228–479 | 240 | 4 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 252–346 | 95 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 252–259 | 8 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 253–479 | 225 | 3 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 264–412 | 149 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 265–268 | 4 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 267–479 | 212 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 270–272 | 3 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 272–280 | 9 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 275–314 | 40 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 320–479 | 160 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 339–357 | 10 | 3 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 366–449 | 84 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 398–410 | 7 | 2 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 402–429 | 28 | 1 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 405–478 | 66 | 4 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 413–467 | 55 | 1 | Undefined position; Undefined team |
| `42` | `63` | Position_Unknown | Team_Unknown | 420–479 | 60 | 1 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 433–458 | 20 | 4 | Undefined position; Undefined team |
| `44` | `68` | Position_Unknown | Team_Unknown | 442–479 | 35 | 2 | Undefined position; Undefined team |
| `45` | `71` | Position_Unknown | Team_Unknown | 452–479 | 28 | 1 | Undefined position; Undefined team |
| `46` | `72` | Position_Unknown | Team_Unknown | 464–479 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 162 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-294] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-363] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-409] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-158] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-231] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-286] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-412] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-281] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-302] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-405] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [144-203] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-332] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-354] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-360] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-311] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-327] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-352] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-383] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-386] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-394] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-411] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-415] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-199] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-264] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-234] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-212] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-228] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-161] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-313] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-431] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-438] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-447] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-213] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-242] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-249] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-285] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-333] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-359] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-382] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-391] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-415] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-420] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-479] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-191] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-425] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-224] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-248] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-257] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-269] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-395] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-402] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-415] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-479] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-179] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-187] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-230] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-45] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-246] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-293] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-305] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-331] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-343] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-356] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-379] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-413] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-416] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-459] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-462] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-210] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-213] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-225] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-249] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-479] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-246] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-320] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-218] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-284] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-297] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-384] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-277] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-338] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-479] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-346] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-259] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-339] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-349] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-479] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-412] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-350] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-479] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-272] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-280] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-314] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-341] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-351] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-357] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-449] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-400] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-410] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-429] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-430] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-469] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-475] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-478] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-467] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-439] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-443] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-448] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-458] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-458] for track '44' has 3 frames without a visible bounding box.
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

</details>