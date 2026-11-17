# Play-Annotation-Generator Annotation Review — Power_275

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_275`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 116
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
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_DownBlock` | DE1 | defense | `4` | `4` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 16 | START | 16 | 267 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 16 | START | 16 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 16 | START | 16 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 16 | START | 16 | 367 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 16 | START | 16 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 16 | START | 16 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 16 | START | 16 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 16 | START | 16 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 16 | START | 16 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `15` | `15` | 181 | START | 181 | 258 |
| ✅ EXACT | `Action_DownBlock` | LG | `19` | `19` | 181 | START | 181 | 281 |
| ✅ EXACT | `Action_DownBlock` | DE1 | `4` | `4` | 181 | START | 181 | 275 |
| ✅ EXACT | `Action_PullBlock` | RT | `10` | `10` | 181 | START | 181 | 281 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 16–205
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 205 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 267 | 252 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 389 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 180 | 165 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 258 | 78 | inferred_complete_timeline |
| `Action_DownBlock` | 260 | 281 | 22 | inferred_complete_timeline |
| `Action_None` | 282 | 371 | 90 | inferred_complete_timeline |
| `Action_None` | 373 | 389 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 180 | 165 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 281 | 101 | inferred_complete_timeline |
| `Action_None` | 282 | 389 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 183 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 194 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 389 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 16–367
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 367 | 352 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 180 | 165 | inferred_complete_timeline |
| `Action_PullBlock` | 181 | 281 | 101 | inferred_complete_timeline |
| `Action_None` | 282 | 389 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 16–284
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 180 | 165 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 275 | 95 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 16–227
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 203 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 227 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 18–389
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 39 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 209 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 229 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 389 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 16–224
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 192 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 205 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 224 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 262 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 374 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 389 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 264 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 270 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 371 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 389 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 375 | 360 | inferred_complete_timeline |
| `Action_PreSnap` | 378 | 389 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 280 | 265 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 389 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 313 | 298 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 389 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 16–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 258 | 243 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 264 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 16–378
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 378 | 363 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 16–380 | 343 | 4 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 16–336 | 319 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 16–126 | 78 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 30–359 | 191 | 18 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 206–210 | 5 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 208–379 | 172 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 224–389 | 126 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 255–389 | 135 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 259–389 | 131 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 300–301 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 304–389 | 86 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 312–313 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 325–327 | 3 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 348–370 | 22 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 352–354 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 550: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 550: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (DE1) duration 101 frames exceeds threshold 90 frames [start=181, end=281].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '10' (RT) duration 101 frames exceeds threshold 90 frames [start=181, end=281].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (LT) duration 101 frames exceeds threshold 90 frames [start=181, end=281].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 101 frames exceeds threshold 90 frames [start=181, end=281].
- ⚠️ Action 'Action_PreSnap' range [16-267] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-389] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-255] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-380] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-275] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-258] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-264] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-202] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-336] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-378] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-280] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-389] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-375] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-367] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-262] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-374] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-264] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-270] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-371] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-258] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [260-281] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-371] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-227] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-313] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-192] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-219] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-39] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-209] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-229] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-74] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-196] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-238] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-259] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-277] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-316] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-321] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-330] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-339] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-342] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-359] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-379] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-301] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-352] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-370] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-354] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>