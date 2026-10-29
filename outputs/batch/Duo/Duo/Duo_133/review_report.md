# Play-Annotation-Generator Annotation Review — Duo_133

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_133`
- **Frame Range:** 0 to 358 (359 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 358
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | WR2 | offense | `17` | `17` |
| ✅ EXACT | `Action_ComboBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 297 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `15` | `Group` | 0 | START | 0 | 358 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 260 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 334 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 208 |
| ✅ EXACT | `Action_ComboBlock` | WR2 | `17` | `17` | 197 | START | 197 | 257 |
| ✅ EXACT | `Action_ComboBlock` | LT | `18` | `18` | 197 | START | 197 | 204 |
| ✅ EXACT | `Action_ComboBlock` | C | `20` | `20` | 197 | START | 197 | 254 |
| ✅ EXACT | `Action_ComboBlock` | RG | `21` | `21` | 197 | START | 197 | 257 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `18` | `18` | 211 | START | 211 | 257 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 257 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 260 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 297 | 298 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 321 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 326 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 358 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_ComboBlock` | 197 | 257 | 61 | inferred_complete_timeline |
| `Action_None` | 258 | 358 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 318 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_ComboBlock` | 197 | 204 | 8 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 211 | 257 | 47 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |
| `Action_None` | 262 | 265 | 4 | inferred_complete_timeline |
| `Action_None` | 268 | 298 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 230 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 234 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_ComboBlock` | 197 | 254 | 58 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_ComboBlock` | 197 | 257 | 61 | inferred_complete_timeline |
| `Action_None` | 258 | 272 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–334
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 334 | 335 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 312 | 313 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 328 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 358 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 212 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–307
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 292 | 293 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 307 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–347
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 315 | 316 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 334 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 339 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 347 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 330 | 331 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 358 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

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
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 259 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 288 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 293 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 315 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 358 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 215–358 | 144 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 223–358 | 123 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 238–250 | 6 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 242–338 | 97 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 251–252 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 257–260 | 4 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 262–288 | 14 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 267–358 | 87 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 273–358 | 86 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 285–331 | 39 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 295–358 | 62 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 305–306 | 2 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 328–347 | 18 | 2 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 333–345 | 13 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 338–358 | 21 | 1 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 340–344 | 5 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 344–358 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 66 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-211] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-315] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-334] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-339] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-347] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-330] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-358] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-292] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-307] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-334] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-318] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-312] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-328] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-358] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-231] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-358] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-288] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-293] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-315] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-297] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-321] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-326] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-260] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [197-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-217] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-230] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [197-254] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-272] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-339] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-358] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-241] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-338] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-268] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-288] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-282] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-332] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-358] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-318] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-331] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-310] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-347] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-345] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-344] for track '37' has 2 frames without a visible bounding box.
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

</details>