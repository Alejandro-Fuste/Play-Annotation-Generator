# Play-Annotation-Generator Annotation Review — Duo_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_83`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 328
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `26` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BlockSecondLevel` | SAF1 | defense | `5` | `5` |
| ⚠️ START CHANGED | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `27` | `25` |
| ✅ EXACT | `Action_ComboBlock` | SAF2 | defense | `4` | `4` |
| ✅ EXACT | `Action_ComboBlock` | SAF1 | defense | `5` | `5` |
| ✅ EXACT | `Action_ComboBlock` | CB3 | defense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 288 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 277 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `24` | `Group` | 0 | START | 25 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `26` | `Group` | 0 | START | 102 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 328 |
| ✅ EXACT | `Action_BlockSecondLevel` | SAF1 | `5` | `5` | 148 | START | 148 | 195 |
| ⚠️ START CHANGED | `Action_ComboBlock` | Position_Unknown | `27` | `25` | 196 | START | 246 | 247 |
| ✅ EXACT | `Action_ComboBlock` | SAF2 | `4` | `4` | 196 | START | 196 | 254 |
| ✅ EXACT | `Action_ComboBlock` | SAF1 | `5` | `5` | 196 | START | 196 | 254 |
| ✅ EXACT | `Action_ComboBlock` | CB3 | `6` | `6` | 196 | START | 196 | 254 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 254 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 323 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 288 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 312 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 279 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 283 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 327 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 25–327
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 42 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 51 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 71 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 163 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 233 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 277 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 327 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 277 | 278 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 293 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `26`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `26`
- **team_side:** `offense`
- **Visible Frames:** 102–211
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 102 | 211 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 328 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 328 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 241 | 242 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 277 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 328 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 235 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 327 | 328 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 254 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 278 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 328 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_ComboBlock` | 196 | 254 | 59 | inferred_complete_timeline |
| `Action_None` | 255 | 277 | 23 | inferred_complete_timeline |
| `Action_None` | 279 | 328 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 148 | 195 | 48 | inferred_complete_timeline |
| `Action_ComboBlock` | 196 | 254 | 59 | inferred_complete_timeline |
| `Action_None` | 255 | 328 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_ComboBlock` | 196 | 254 | 59 | inferred_complete_timeline |
| `Action_None` | 255 | 271 | 17 | inferred_complete_timeline |
| `Action_None` | 273 | 298 | 26 | inferred_complete_timeline |
| `Action_None` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 321 | 325 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–83 | 84 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–276 | 232 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–232 | 232 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–14 | 4 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 5–6 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 257–276 | 16 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 275–328 | 52 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 287–328 | 42 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 308–328 | 21 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 309–325 | 17 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 320–328 | 9 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 323–327 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ComboBlock` for actor_track_id `27` (Position_Unknown): Annotated start 196 != Inferred start 246

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 61 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-249] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-327] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-271] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-298] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-325] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-277] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-298] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-244] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-224] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-271] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-328] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-279] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-283] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-327] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-288] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-312] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-241] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-277] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-267] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-276] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-277] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-284] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-323] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-232] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-42] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-51] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-71] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-233] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-242] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-277] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-327] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [246-247] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-265] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-276] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-278] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-328] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-325] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-328] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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

</details>