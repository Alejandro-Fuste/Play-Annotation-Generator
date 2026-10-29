# Play-Annotation-Generator Annotation Review — Duo_90

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_90`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 328
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `28` | `22` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `19` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 319 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `13` | `Group` | 0 | START | 0 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 254 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 266 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 192 |
| ✅ EXACT | `Action_ComboBlock` | C | `15` | `15` | 210 | START | 210 | 287 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | QB | `16` | `16` | 210 | START | 210 | 260 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `18` | `18` | 210 | START | 210 | 328 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | `28` | `22` | 210 | START | 213 | 226 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `19` | `19` | 328 | START | 328 | 328 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 371 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–285
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_ComboBlock` | 210 | 260 | 51 | inferred_complete_timeline |
| `Action_ComboBlock` | 263 | 274 | 12 | inferred_complete_timeline |
| `Action_ComboBlock` | 280 | 285 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 319 | 320 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 323 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 328 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 254 | 255 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 273 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 328 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 266 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 236 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 298 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_ComboBlock` | 210 | 287 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 297 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–316
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 205 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 294 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 316 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–288
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 288 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 101 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 106 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 243 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 16–328 | 305 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 33–328 | 296 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 113–328 | 216 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 167–177 | 8 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 213–309 | 90 | 5 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 213–328 | 106 | 5 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 214–321 | 108 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 221–328 | 108 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 238–242 | 4 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 245–269 | 25 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 257–328 | 72 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 258–260 | 3 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 285–300 | 9 | 3 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 300–328 | 28 | 2 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 301–323 | 16 | 4 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 306–307 | 2 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 313–317 | 5 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 314–328 | 5 | 2 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 325–328 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `22` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 64 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-319] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-323] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-328] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-288] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-266] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-294] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-316] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-235] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-243] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-236] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-241] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-298] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-297] for track '12' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-254] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-273] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-328] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [210-287] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [210-260] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [263-274] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [280-285] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-207] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-328] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [213-226] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [228-259] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [263-302] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [305-306] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [308-309] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-246] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-251] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-281] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-298] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-321] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-260] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-293] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-300] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-319] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-328] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-305] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-313] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-323] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-317] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-316] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-328] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_None' has invalid start frame 371. Video range is [0, 328].

</details>