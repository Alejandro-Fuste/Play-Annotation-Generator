# Play-Annotation-Generator Annotation Review — Power_183

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_183`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 123
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 0
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `24` | `24` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 23 | START | 23 | 362 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 23 | START | 23 | 357 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 23 | START | 23 | 248 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 23 | START | 23 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 23 | START | 23 | 229 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 23 | START | 23 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `2` | `Group` | 23 | START | 23 | 259 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 23 | START | 23 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 23 | START | 23 | 266 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 23 | START | 23 | 242 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 23 | START | 23 | 336 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `21` | `21` | 229 | START | 229 | 243 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `24` | `24` | 229 | START | 229 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `13` | `13` | 229 | START | 229 | 264 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 23–266
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 266 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 23–336
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 336 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 23–419
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 259 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 288 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 320 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 419 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 23–362
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 362 | 340 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 23–387
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 357 | 335 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 387 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 23–419
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 248 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 274 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 419 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 23–266
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 37 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 228 | 174 | inferred_complete_timeline |
| `Action_DownBlock` | 229 | 243 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 249 | 266 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 23–413
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 186 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 195 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 249 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 288 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 413 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 23–255
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 229 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 255 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 23–401
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 228 | 206 | inferred_complete_timeline |
| `Action_PullBlock` | 229 | 264 | 36 | inferred_complete_timeline |
| `Action_PullBlock` | 266 | 269 | 4 | inferred_complete_timeline |
| `Action_None` | 270 | 401 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 23–419
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 242 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 247 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 419 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 23–372
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 234 | 212 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 372 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 23–398
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 261 | 239 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 304 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 398 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 23–308
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 237 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 262 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 308 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 23–351
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 240 | 218 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 264 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 276 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 312 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 351 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 23–419
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 243 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 23–276
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 255 | 233 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 276 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 23–387
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 274 | 252 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 387 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 23–419
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 419 | 397 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 23–316
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 316 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 23–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 402 | 380 | inferred_complete_timeline |
| `Action_PreSnap` | 404 | 408 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 419 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 23–261 | 237 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 34–156 | 32 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 165–168 | 4 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 175–404 | 215 | 8 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 219–236 | 7 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 268–408 | 139 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 295–301 | 6 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 309–332 | 23 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 315–387 | 73 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 317–378 | 54 | 4 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 319–360 | 41 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 323–381 | 34 | 3 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 335–341 | 4 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 345–375 | 31 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 356–400 | 45 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 403–412 | 10 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 409–419 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `24` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 88 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [23-362] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-357] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-387] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-259] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-288] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-320] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-419] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-266] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-252] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-419] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-261] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-304] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-398] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-336] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-316] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-255] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-276] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-248] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-274] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [229-264] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-401] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-402] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-408] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-240] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-264] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-276] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-312] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-351] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-274] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-387] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-255] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-242] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-262] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-308] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-195] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-249] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-288] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-413] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-234] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-372] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-37] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [229-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [245-246] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [249-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-61] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-228] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [229-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [240-243] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [248-254] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [259-261] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-404] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-276] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-408] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-301] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-332] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-387] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-324] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-357] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-378] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-355] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-360] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-340] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-351] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-381] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-375] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-400] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-412] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-419] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>