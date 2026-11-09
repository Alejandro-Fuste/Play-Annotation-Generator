# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_73`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 39
- **Ball Tracks:** 1
- **Action Segments:** 115
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `15` | `15` |
| ✅ EXACT | `Action_Handoff` | C | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 279 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 380 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 393 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `17` | 160 | START | 160 | 177 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `18` | 160 | START | 160 | 223 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `19` | `19` | 160 | START | 160 | 223 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `20` | 160 | START | 160 | 223 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 160 | START | 160 | 178 |
| ✅ EXACT | `Action_PressEdge` | RB | `15` | `15` | 167 | START | 167 | 201 |
| ✅ EXACT | `Action_Handoff` | C | `17` | `17` | 178 | START | 178 | 195 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 449 | 450 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–440
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_PressEdge` | 167 | 201 | 35 | inferred_complete_timeline |
| `Action_None` | 202 | 254 | 53 | inferred_complete_timeline |
| `Action_None` | 256 | 410 | 155 | inferred_complete_timeline |
| `Action_None` | 421 | 440 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 380 | 381 | inferred_complete_timeline |
| `Action_PreSnap` | 388 | 398 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 401 | 402 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 404 | 449 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 393 | 394 | inferred_complete_timeline |
| `Action_PreSnap` | 395 | 399 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 401 | 449 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 279 | 280 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 449 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 223 | 64 | inferred_complete_timeline |
| `Action_None` | 224 | 449 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 223 | 64 | inferred_complete_timeline |
| `Action_None` | 224 | 388 | 165 | inferred_complete_timeline |
| `Action_None` | 392 | 398 | 7 | inferred_complete_timeline |
| `Action_None` | 400 | 402 | 3 | inferred_complete_timeline |
| `Action_None` | 413 | 417 | 5 | inferred_complete_timeline |
| `Action_None` | 421 | 439 | 19 | inferred_complete_timeline |
| `Action_None` | 444 | 449 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–443
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 177 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 178 | 195 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 223 | 28 | inferred_complete_timeline |
| `Action_None` | 224 | 317 | 94 | inferred_complete_timeline |
| `Action_None` | 320 | 372 | 53 | inferred_complete_timeline |
| `Action_None` | 375 | 395 | 21 | inferred_complete_timeline |
| `Action_None` | 397 | 412 | 16 | inferred_complete_timeline |
| `Action_None` | 419 | 443 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 178 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 223 | 35 | inferred_complete_timeline |
| `Action_None` | 224 | 260 | 37 | inferred_complete_timeline |
| `Action_None` | 262 | 449 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–375
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 223 | 64 | inferred_complete_timeline |
| `Action_None` | 224 | 375 | 152 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 223 | 224 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 235 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 236 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 264 | 265 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 272 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 449 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 406 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 408 | 418 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 420 | 449 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–446
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 441 | 442 | inferred_complete_timeline |
| `Action_PreSnap` | 443 | 446 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–366
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 287 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 293 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 311 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 318 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 324 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 366 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 449 | 450 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 440 | 441 | inferred_complete_timeline |
| `Action_PreSnap` | 448 | 449 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 196–216 | 21 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 251–252 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 262–449 | 183 | 4 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 267–449 | 178 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 272–449 | 169 | 6 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 277–348 | 46 | 8 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 287–379 | 50 | 11 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 306–307 | 2 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 315–316 | 2 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 322–326 | 5 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 335–336 | 2 | 1 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |
| `35` | `57` | Position_Unknown | Team_Unknown | 397–400 | 4 | 1 | Undefined position; Undefined team |
| `36` | `58` | Position_Unknown | Team_Unknown | 398–403 | 6 | 1 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 400–424 | 12 | 2 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 431–438 | 8 | 1 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 438–439 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `23` | `27` | 203 | 214 | 4 | 33.3% | 205–207, 209–213 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 92 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-279] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-449] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-449] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-380] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-398] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-402] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-223] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-264] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-272] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-246] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-406] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-418] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-449] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-393] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-399] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-449] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-441] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-446] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-200] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-236] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-440] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-254] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-410] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-440] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-287] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-293] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-311] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-318] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-324] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-366] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-317] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-372] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-395] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-412] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-443] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-388] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-398] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-402] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-417] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-439] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-375] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [160-178] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-260] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-449] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-267] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-386] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-389] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-271] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-317] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-322] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-326] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-331] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-343] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-293] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-302] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-306] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-323] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-332] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-341] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-348] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-291] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-301] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-308] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-317] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-335] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-345] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-351] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-362] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-373] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-379] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-316] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-326] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-358] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-400] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-403] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-407] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-424] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-438] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-439] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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