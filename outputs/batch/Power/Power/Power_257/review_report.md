# Play-Annotation-Generator Annotation Review — Power_257

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_257`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 154
- **Validation Warnings:** 198
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `23` | `21` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 11 | START | 11 | 233 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 11 | START | 11 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 11 | START | 11 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 11 | START | 11 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 11 | START | 11 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 11 | START | 11 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 11 | START | 11 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 11 | START | 11 | 380 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `15` | 186 | START | 186 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `23` | `21` | 186 | START | 186 | 202 |
| ✅ EXACT | `Action_PullBlock` | LG | `17` | `17` | 186 | START | 186 | 218 |

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
- **Visible Frames:** 11–242
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 233 | 223 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 242 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 11–395
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 205 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 307 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 395 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 11–419
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 380 | 370 | inferred_complete_timeline |
| `Action_PreSnap` | 399 | 419 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 11–419
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 245 | 235 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 419 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 11–419
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 245 | 235 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 266 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 325 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 328 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 419 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 11–218
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 185 | 175 | inferred_complete_timeline |
| `Action_PullBlock` | 186 | 218 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 11–215
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 185 | 175 | inferred_complete_timeline |
| `Action_DownBlock` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 214 | 215 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 11–419
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 34 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 95 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 183 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 201 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 214 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 237 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 246 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 266 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 329 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 419 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 11–245
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 199 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 221 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 245 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 19–189
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 31 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 49 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 189 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 11–218
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 21 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 109 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 218 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 11–214
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 214 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 11–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 238 | 228 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 419 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 11–418
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 313 | 303 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 322 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 340 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 348 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 360 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 365 | 366 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 370 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 384 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 405 | 418 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 11–419
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 368 | 358 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 419 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 11–294
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 246 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 273 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 294 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 11–412
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 253 | 243 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 354 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 358 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 361 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 365 | 366 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 376 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 384 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 388 | 390 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 393 | 396 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 405 | 406 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 412 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 11–419
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 286 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 302 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 419 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 11–419 | 407 | 3 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 11–211 | 201 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 11–340 | 330 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 103–417 | 286 | 7 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 241–419 | 173 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 242–248 | 7 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 256–419 | 162 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 258–406 | 142 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 269–328 | 6 | 3 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 277–278 | 2 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 278–419 | 136 | 3 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 282–409 | 128 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 286–419 | 134 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 293–419 | 127 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 305–339 | 27 | 4 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 314–416 | 91 | 6 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 316–418 | 33 | 9 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 316–419 | 35 | 9 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 318–319 | 2 | 1 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 322–419 | 94 | 3 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 348–419 | 71 | 2 | Undefined position; Undefined team |
| `43` | `49` | Position_Unknown | Team_Unknown | 364–396 | 12 | 3 | Undefined position; Undefined team |
| `44` | `50` | Position_Unknown | Team_Unknown | 369–370 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `23` (2 segments found)

### Track Identity Issues

- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 141 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 514: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
- ⚠️ Row 514: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [11-363] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-380] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-286] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-302] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-419] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-205] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-307] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-395] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-273] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-277] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-294] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-313] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-322] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-340] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-348] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-360] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-366] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-370] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-384] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-418] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-380] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-253] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-354] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-358] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-361] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-366] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-376] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-384] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-390] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-396] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-406] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-412] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-242] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-221] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-245] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-245] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-266] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-325] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-340] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [198-201] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [214-215] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-368] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-419] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [186-218] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-34] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-214] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-222] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-237] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-246] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-266] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-109] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-218] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-31] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-49] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-189] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-105] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [204-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-414] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-330] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-397] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-260] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-419] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-262] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-286] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-377] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-406] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-363] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-369] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-409] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-419] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-322] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-329] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-334] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-339] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-329] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-396] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-406] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-410] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-416] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-327] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-347] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-366] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-395] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-406] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-410] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-418] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-324] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-362] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-369] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-375] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-384] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-396] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-410] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-419] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-358] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-413] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-384] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-419] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-369] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-381] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-396] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-370] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>