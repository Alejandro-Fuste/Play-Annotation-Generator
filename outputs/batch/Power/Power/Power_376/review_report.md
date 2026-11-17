# Play-Annotation-Generator Annotation Review — Power_376

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_376`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 5 | START | 5 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 5 | START | 5 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 5 | START | 5 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 5 | START | 5 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 5 | START | 5 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 5 | START | 5 | 333 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 5 | START | 5 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 5 | START | 5 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `13` | 239 | START | 239 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `8` | `8` | 239 | START | 239 | 250 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `2` | `2` | 239 | START | 239 | 247 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 5–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 134 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 270 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 389 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–328
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 275 | 271 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 294 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 328 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 5–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 333 | 329 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 348 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 389 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 5–389
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 246 | 242 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 261 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 292 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 304 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 342 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 346 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 389 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 5–257
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 238 | 234 | inferred_complete_timeline |
| `Action_PullBlock` | 239 | 247 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 253 | 257 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 5–380
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 155 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 238 | 80 | inferred_complete_timeline |
| `Action_DownBlock` | 239 | 245 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 254 | 256 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 271 | 289 | 19 | inferred_complete_timeline |
| `Action_None` | 290 | 333 | 44 | inferred_complete_timeline |
| `Action_None` | 337 | 348 | 12 | inferred_complete_timeline |
| `Action_None` | 357 | 360 | 4 | inferred_complete_timeline |
| `Action_None` | 367 | 368 | 2 | inferred_complete_timeline |
| `Action_None` | 378 | 380 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 5–272
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 135 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 246 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 272 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 5–389
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 238 | 234 | inferred_complete_timeline |
| `Action_DownBlock` | 239 | 250 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 254 | 285 | 32 | inferred_complete_timeline |
| `Action_None` | 297 | 333 | 37 | inferred_complete_timeline |
| `Action_None` | 337 | 348 | 12 | inferred_complete_timeline |
| `Action_None` | 351 | 389 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 5–389
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 246 | 242 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 336 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 389 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 5–295
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 138 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 295 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 5–284
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 246 | 242 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 284 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 5–389
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 243 | 239 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 303 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 389 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 5–301
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 158 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 301 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 5–184
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 184 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 5–333
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 333 | 329 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 97–389 | 291 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 108–389 | 250 | 9 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 263–389 | 104 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 277–389 | 113 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 283–346 | 64 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 285–389 | 93 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 313–346 | 25 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 314–389 | 76 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 317–333 | 16 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 344–389 | 36 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 345–346 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 375–389 | 15 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 383–389 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 67 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [5-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-138] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-295] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [239-247] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [253-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-333] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-348] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-336] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-333] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-243] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-303] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-135] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-246] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-272] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [239-250] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [254-285] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-333] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-348] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-284] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-301] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-246] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-292] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-304] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-342] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-346] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-270] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-238] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [239-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [254-256] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-333] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-348] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-360] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-275] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-294] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-337] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-389] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-288] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-294] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-322] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-333] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-346] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-362] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-368] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-371] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-304] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-355] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-346] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-345] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-333] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-340] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-346] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-323] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-333] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-346] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-346] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>