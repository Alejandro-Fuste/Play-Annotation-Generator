# Play-Annotation-Generator Annotation Review — Duo_199

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_199`
- **Frame Range:** 0 to 349 (350 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 349
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 144
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ComboBlock` | DT1 | defense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `27` | `24` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `12` | `Group` | 0 | START | 0 | 243 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 349 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 52 |
| ✅ EXACT | `Action_ComboBlock` | C | `10` | `10` | 257 | START | 257 | 263 |
| ✅ EXACT | `Action_ComboBlock` | DT1 | `17` | `17` | 257 | START | 257 | 275 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | `27` | `24` | 257 | START | 257 | 283 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LT | `9` | `9` | 257 | START | 257 | 278 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `10` | `10` | 264 | START | 264 | 290 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 294 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 271 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 278 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–315
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 290 | 257 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 315 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 349 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 349 | 350 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–304
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 209 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 256 | 46 | inferred_complete_timeline |
| `Action_ComboBlock` | 257 | 278 | 22 | inferred_complete_timeline |
| `Action_ComboBlock` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 288 | 294 | 7 | inferred_complete_timeline |
| `Action_None` | 295 | 295 | 1 | inferred_complete_timeline |
| `Action_None` | 300 | 301 | 2 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 262 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 298 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 349 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 54 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 63 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 97 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 256 | 150 | inferred_complete_timeline |
| `Action_ComboBlock` | 257 | 263 | 7 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 264 | 290 | 27 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 25 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 349 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–29
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 29 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 237 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 342 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 349 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–25
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 25 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 202 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 256 | 52 | inferred_complete_timeline |
| `Action_ComboBlock` | 257 | 275 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 24 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 249 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 323 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 349 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 328 | 261 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 344 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 349 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 270 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 349 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 70 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 252 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–68 | 69 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 6–121 | 55 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 32–220 | 158 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 70–319 | 231 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 73–348 | 274 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 76–349 | 221 | 7 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 86–204 | 119 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 207–300 | 85 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 211–349 | 118 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 237–250 | 14 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 271–285 | 15 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 284–285 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 301–310 | 10 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 309–343 | 23 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 316–327 | 10 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 326–346 | 9 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 341–349 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `27` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 109 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 349 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-67] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-270] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-349] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-29] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-290] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-42] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-252] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-349] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-328] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-344] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-25] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-237] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-342] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [257-278] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [280-281] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [288-294] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 295, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [295-295] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-63] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-256] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [257-263] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [264-290] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [292-293] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-271] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-278] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-243] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-262] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-298] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-349] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-323] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-349] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-25] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [257-275] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-96] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-220] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-265] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-291] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-315] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-340] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-348] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-230] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-245] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-287] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-305] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-204] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [257-283] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-300] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-214] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-349] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-250] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-285] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-310] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-329] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-343] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-320] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-327] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-331] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-346] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>