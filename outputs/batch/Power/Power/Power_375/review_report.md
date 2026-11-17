# Play-Annotation-Generator Annotation Review — Power_375

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_375`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 89
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
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 16 | START | 16 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 16 | START | 16 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 16 | START | 16 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 16 | START | 16 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 16 | START | 16 | 226 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 16 | START | 16 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 16 | START | 16 | 242 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 16 | START | 16 | 226 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 16 | START | 16 | 226 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 16 | START | 16 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 16 | START | 16 | 359 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `15` | `15` | 227 | START | 227 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `20` | `20` | 227 | START | 227 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `21` | `21` | 227 | START | 227 | 237 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 16–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 359 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 16–279
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 238 | 223 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 279 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 16–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 359 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 16–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 359 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 16–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 359 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 16–359
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 237 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 263 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 290 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 317 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 359 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 16–359
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 242 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 288 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 352 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 359 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 16–278
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 226 | 211 | inferred_complete_timeline |
| `Action_PullBlock` | 227 | 237 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 240 | 271 | 32 | inferred_complete_timeline |
| `Action_PullBlock` | 273 | 273 | 1 | inferred_complete_timeline |
| `Action_None` | 274 | 278 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 16–265
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 230 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 265 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 16–359
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 226 | 211 | inferred_complete_timeline |
| `Action_DownBlock` | 227 | 237 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 250 | 273 | 24 | inferred_complete_timeline |
| `Action_None` | 274 | 278 | 5 | inferred_complete_timeline |
| `Action_None` | 302 | 306 | 5 | inferred_complete_timeline |
| `Action_None` | 308 | 313 | 6 | inferred_complete_timeline |
| `Action_None` | 316 | 317 | 2 | inferred_complete_timeline |
| `Action_None` | 330 | 334 | 5 | inferred_complete_timeline |
| `Action_None` | 345 | 359 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 16–359
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 226 | 211 | inferred_complete_timeline |
| `Action_DownBlock` | 227 | 237 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 249 | 273 | 25 | inferred_complete_timeline |
| `Action_None` | 274 | 279 | 6 | inferred_complete_timeline |
| `Action_None` | 282 | 287 | 6 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_None` | 302 | 359 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 16–357
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 244 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 284 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 335 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 339 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 352 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 357 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 16–318
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 237 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 279 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 290 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 312 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 318 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 16–261
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 233 | 218 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 237 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 261 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 16–284
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 237 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 280 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 284 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 16–359
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 268 | 253 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 278 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 317 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 333 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 348 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 16–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 359 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 16–359
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 349 | 334 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 359 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 16–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 359 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 16–278
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 264 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 278 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 16–336
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 326 | 311 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 336 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 16–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 348 | 333 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 359 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 249–344 | 96 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 263–280 | 18 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 297–358 | 58 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 298–353 | 56 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 303–359 | 33 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 306–359 | 54 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 309–343 | 35 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 313–335 | 18 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 70 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [16-348] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-244] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-335] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-339] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-352] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-357] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-230] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-237] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-280] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-284] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-268] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-278] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-317] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-333] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-348] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-279] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-290] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-312] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-318] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-264] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-278] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-237] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-237] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-263] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-290] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-317] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [227-237] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-278] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-306] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-313] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-334] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-238] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-279] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-326] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-349] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-288] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-352] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [227-237] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-279] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-359] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [227-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [240-271] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-278] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-344] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-280] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-334] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-348] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-358] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-353] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-343] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-321] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-335] for track '29' has 2 frames without a visible bounding box.
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

</details>