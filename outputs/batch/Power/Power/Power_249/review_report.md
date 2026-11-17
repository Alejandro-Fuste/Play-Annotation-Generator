# Play-Annotation-Generator Annotation Review — Power_249

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_249`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 139
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_DownBlock` | LB2 | defense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 16 | START | 16 | 303 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 16 | START | 16 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 16 | START | 16 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 16 | START | 16 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 16 | START | 16 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 16 | START | 16 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 16 | START | 16 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 16 | START | 16 | 297 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 16 | START | 16 | 178 |
| ✅ EXACT | `Action_DownBlock` | RT | `14` | `14` | 179 | START | 179 | 201 |
| ✅ EXACT | `Action_DownBlock` | LB2 | `17` | `17` | 179 | START | 179 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `9` | `9` | 179 | START | 179 | 225 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `21` | `21` | 179 | START | 179 | 246 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 16–302
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 297 | 282 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 302 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 16–347
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 303 | 288 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 347 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 16–225
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 208 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 16–376
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 204 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 248 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 336 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 349 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 352 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 366 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 371 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 376 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 178 | 163 | inferred_complete_timeline |
| `Action_DownBlock` | 179 | 225 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 231 | 246 | 16 | inferred_complete_timeline |
| `Action_None` | 247 | 281 | 35 | inferred_complete_timeline |
| `Action_None` | 285 | 389 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 237 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 254 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 258 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 389 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 178 | 163 | inferred_complete_timeline |
| `Action_DownBlock` | 179 | 201 | 23 | inferred_complete_timeline |
| `Action_None` | 262 | 389 | 128 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 204 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 316 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 335 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 389 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 16–247
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 239 | 224 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 247 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 234 | 219 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 239 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 255 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 372 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 389 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 248 | 233 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 389 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 178 | 163 | inferred_complete_timeline |
| `Action_DownBlock` | 179 | 246 | 68 | inferred_complete_timeline |
| `Action_None` | 247 | 301 | 55 | inferred_complete_timeline |
| `Action_None` | 314 | 340 | 27 | inferred_complete_timeline |
| `Action_None` | 342 | 389 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 16–357
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 274 | 259 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 291 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 301 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 308 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 351 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 357 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 16–238
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 122 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 227 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 233 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 238 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 16–368
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 368 | 353 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 16–325
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 325 | 310 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 307 | 292 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 313 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 317 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 325 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 330 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 334 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 344 | 345 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 377 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 389 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 16–297 | 230 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 16–389 | 374 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 16–36 | 13 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 226–389 | 164 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 254–389 | 133 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 254–389 | 117 | 9 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 260–269 | 6 | 3 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 268–389 | 122 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 271–389 | 109 | 3 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 288–389 | 78 | 6 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 289–291 | 3 | 1 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 290–292 | 3 | 1 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 309–348 | 15 | 4 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 315–319 | 5 | 1 | Undefined position; Undefined team |
| `35` | `57` | Position_Unknown | Team_Unknown | 333–336 | 4 | 1 | Undefined position; Undefined team |
| `36` | `61` | Position_Unknown | Team_Unknown | 360–389 | 15 | 3 | Undefined position; Undefined team |
| `37` | `62` | Position_Unknown | Team_Unknown | 366–389 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 499: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 499: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [16-303] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-347] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-316] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-335] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-389] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-248] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-336] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-349] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-352] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-366] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-371] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-234] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-255] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-372] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-389] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-218] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-368] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-297] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [179-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [231-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-281] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-307] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-313] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-317] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-325] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-330] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-334] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-345] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-377] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-325] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-274] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-291] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-301] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-308] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-351] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-357] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-247] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [179-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-389] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-237] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-240] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-254] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-258] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-389] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-301] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-340] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-227] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-252] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-24] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-36] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-306] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-317] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-327] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-348] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-365] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-374] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-386] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-261] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-322] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-389] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-290] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-324] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-366] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-389] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-291] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-312] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-320] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-344] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-348] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-319] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-336] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-365] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-372] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>