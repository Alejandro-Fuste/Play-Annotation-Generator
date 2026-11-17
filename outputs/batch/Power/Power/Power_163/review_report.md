# Play-Annotation-Generator Annotation Review — Power_163

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_163`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 10 | START | 10 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 10 | START | 10 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 10 | START | 10 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 10 | START | 10 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 10 | START | 10 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 10 | START | 10 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 10 | START | 10 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 10 | START | 10 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 10 | START | 10 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 10 | START | 10 | 230 |
| ✅ EXACT | `Action_DownBlock` | C | `20` | `20` | 213 | START | 213 | 215 |
| ✅ EXACT | `Action_DownBlock` | RG | `21` | `21` | 213 | START | 213 | 216 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `13` | `13` | 213 | START | 213 | 216 |

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
- **Visible Frames:** 10–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 359 | 350 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 10–230
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 230 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 10–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 359 | 350 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 10–359
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 287 | 278 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 295 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 339 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 343 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 359 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 10–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 359 | 350 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 10–359
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 222 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 246 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 253 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 267 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 278 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 359 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 10–359
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 215 | 206 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 243 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 285 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 308 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 359 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 10–215
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 212 | 203 | inferred_complete_timeline |
| `Action_DownBlock` | 213 | 215 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 10–216
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 212 | 203 | inferred_complete_timeline |
| `Action_DownBlock` | 213 | 216 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 10–300
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 216 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 246 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 282 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 300 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 10–249
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 217 | 208 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 249 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 10–216
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 216 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 10–216
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 216 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 10–359
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 216 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 253 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 316 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 359 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 10–347
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 255 | 246 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 274 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 283 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 301 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 316 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 347 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 10–278
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 278 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 10–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 359 | 350 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 10–359
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 317 | 308 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 359 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 10–356
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 278 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 337 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 341 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 346 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 356 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 10–350
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 350 | 341 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 10–357
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 357 | 348 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 10–359 | 313 | 11 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 10–42 | 17 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 242–326 | 56 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 242–252 | 7 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 242–277 | 32 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 265–359 | 84 | 5 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 274–359 | 78 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 277–359 | 75 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 290–359 | 70 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 292–293 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 293–359 | 58 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 308–309 | 2 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 312–359 | 41 | 4 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 322–359 | 36 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 327–359 | 32 | 2 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 338–339 | 2 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 350–359 | 3 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `13` (7 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 327: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [10-216] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-217] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-317] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-243] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-285] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-308] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-287] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-295] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-339] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-343] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-359] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-230] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-216] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-255] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-262] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-274] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-283] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-301] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-316] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-347] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-278] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-357] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [213-216] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [241-244] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [248-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [251-253] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [256-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [260-278] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 285, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [285-285] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-307] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-350] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-222] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-246] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-262] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-267] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-278] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-246] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-262] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-282] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-300] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-216] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-253] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-316] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-278] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-281] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-337] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-341] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-346] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-356] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [213-215] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [213-216] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-19] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-42] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-246] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-250] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-278] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-283] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-295] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-326] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-244] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-249] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-257] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-262] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-277] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-278] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-337] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-278] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-359] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-314] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-331] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-351] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-355] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-348] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-339] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-351] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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