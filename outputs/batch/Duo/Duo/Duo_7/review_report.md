# Play-Annotation-Generator Annotation Review — Duo_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_7`
- **Frame Range:** 0 to 358 (359 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 358
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 154
- **Validation Warnings:** 172
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 112
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_ComboBlock` | TE1 | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `19` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 267 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 325 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 2 | 355 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 358 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 82 |
| ✅ EXACT | `Action_ComboBlock` | RG | `18` | `18` | 195 | START | 195 | 280 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | `19` | `19` | 195 | START | 195 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | `20` | `20` | 195 | START | 195 | 196 |
| ✅ EXACT | `Action_ComboBlock` | TE1 | `8` | `8` | 195 | START | 195 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `11` | 218 | START | 218 | 325 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `19` | `19` | 243 | START | 243 | 280 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 280 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 2–355
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 355 | 354 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |
| `Action_BallCarry` | 218 | 325 | 108 | inferred_complete_timeline |
| `Action_BallCarry` | 327 | 332 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 335 | 353 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 267 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 110 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 129 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 194 | 64 | inferred_complete_timeline |
| `Action_ComboBlock` | 195 | 198 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–331
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 325 | 326 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 331 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 117 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 125 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 208 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 222 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 291 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 358 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |
| `Action_ComboBlock` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 199 | 217 | 19 | inferred_complete_timeline |
| `Action_ComboBlock` | 219 | 229 | 11 | inferred_complete_timeline |
| `Action_ComboBlock` | 231 | 242 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 243 | 280 | 38 | inferred_complete_timeline |
| `Action_None` | 281 | 358 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 65 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 129 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 194 | 64 | inferred_complete_timeline |
| `Action_ComboBlock` | 195 | 280 | 86 | inferred_complete_timeline |
| `Action_None` | 281 | 358 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 129 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 194 | 64 | inferred_complete_timeline |
| `Action_ComboBlock` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 198 | 237 | 40 | inferred_complete_timeline |
| `Action_ComboBlock` | 246 | 251 | 6 | inferred_complete_timeline |
| `Action_ComboBlock` | 253 | 257 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 73 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 82 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 117 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 126 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 283 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 291 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 302 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 320 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 332 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 358 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 358 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 255 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 243 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 248 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 272 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 291 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 295 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 300 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 314 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 334 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 264 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–345
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 327 | 328 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 345 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–214 | 151 | 5 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–358 | 323 | 11 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–217 | 156 | 7 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 11–12 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 20–38 | 18 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 57–58 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 224–250 | 11 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 226–358 | 113 | 9 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 234–358 | 116 | 4 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 236–344 | 76 | 10 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 272–283 | 10 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 310–358 | 36 | 3 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 314–358 | 40 | 4 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 348–358 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 141 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-267] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-325] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-331] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-358] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-327] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-340] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-345] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-208] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-214] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-245] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-110] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-129] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [195-198] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-73] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-97] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-245] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-251] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-315] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-319] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-358] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-358] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-217] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [218-325] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [327-332] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [335-353] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-231] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-243] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-248] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-272] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-291] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-295] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-300] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-334] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-358] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-73] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-93] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-117] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-126] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-283] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-291] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-302] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-320] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-332] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-217] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-125] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-222] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-291] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '18' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-129] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-358] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [195-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [199-217] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [219-229] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [243-280] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-129] for track '20' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [195-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [198-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [246-251] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [253-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-355] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-38] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-58] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-250] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-273] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-279] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-324] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-328] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-358] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-242] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-279] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-291] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-272] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-279] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-326] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-344] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-279] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-319] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-322] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-358] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-333] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-341] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-358] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>