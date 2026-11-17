# Play-Annotation-Generator Annotation Review — Power_211

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_211`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_DownBlock` | TE | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | Team_Unknown | `25` | `22` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `0` | `Group` | 7 | START | 7 | 233 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 7 | START | 7 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 7 | START | 7 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 7 | START | 7 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 7 | START | 7 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 7 | START | 8 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 7 | START | 43 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 7 | START | 63 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 7 | START | 7 | 319 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 7 | START | 7 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `17` | 195 | START | 195 | 200 |
| ✅ EXACT | `Action_DownBlock` | TE | `19` | `19` | 195 | START | 195 | 271 |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | `25` | `22` | 195 | START | 217 | 271 |
| ✅ EXACT | `Action_PullBlock` | LG | `18` | `18` | 195 | START | 195 | 271 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 7–279
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 15 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 235 | 219 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 279 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 7–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 233 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 299 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 319 | 313 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 359 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 275 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 359 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 8–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 194 | 187 | inferred_complete_timeline |
| `Action_DownBlock` | 195 | 271 | 77 | inferred_complete_timeline |
| `Action_None` | 272 | 359 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 43–221
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 214 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 221 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 7–291
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 194 | 188 | inferred_complete_timeline |
| `Action_PullBlock` | 195 | 271 | 77 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_None` | 277 | 291 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 194 | 188 | inferred_complete_timeline |
| `Action_DownBlock` | 195 | 200 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 220 | 258 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 263 | 267 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 269 | 271 | 3 | inferred_complete_timeline |
| `Action_None` | 272 | 280 | 9 | inferred_complete_timeline |
| `Action_None` | 282 | 288 | 7 | inferred_complete_timeline |
| `Action_None` | 290 | 293 | 4 | inferred_complete_timeline |
| `Action_None` | 303 | 359 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 63–260
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 193 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 253 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 260 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 7–195
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 195 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 218 | 212 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 239 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 257 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 359 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 225 | 219 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 359 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 221 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 359 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 221 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 307 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 359 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 7–288
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 288 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 7–342
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 320 | 314 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 342 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 359 | 353 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 359 | 353 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 359 | 353 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 359 | 353 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 7–359 | 353 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 7–273 | 266 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 217–359 | 140 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 227–359 | 71 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 227–229 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 236–359 | 124 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 262–359 | 95 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 268–276 | 9 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 275–317 | 28 | 6 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 302–359 | 58 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 307–359 | 53 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 328–359 | 32 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (4 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `25` (Position_Unknown): Annotated start 195 != Inferred start 217

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 424: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [7-233] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-299] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-275] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-319] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-15] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-235] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-279] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-320] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-342] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-218] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-257] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-225] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-288] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-221] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-221] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-307] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-263] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-273] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [195-200] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [220-258] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [263-267] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-280] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-288] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-291] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-359] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-193] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-253] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-260] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-339] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-297] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-303] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-319] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-288] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-276] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-278] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-288] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-292] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-310] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-317] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-359] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>