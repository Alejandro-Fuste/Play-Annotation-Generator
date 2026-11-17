# Play-Annotation-Generator Annotation Review — Power_168

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_168`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 149
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | DE1 | defense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 24 | START | 24 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 24 | START | 24 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 24 | START | 24 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 24 | START | 24 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 24 | START | 24 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 24 | START | 24 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 24 | START | 24 | 232 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 24 | START | 24 | 194 |
| ✅ EXACT | `Action_DownBlock` | DE1 | `1` | `1` | 195 | START | 195 | 270 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `12` | `12` | 195 | START | 195 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `8` | `8` | 195 | START | 195 | 215 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 24–359
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 232 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 247 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 281 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 290 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 359 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 24–249
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 72 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 224 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 249 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 24–357
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 299 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 340 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 344 | 354 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 357 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 24–359
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 200 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 240 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 359 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 24–290
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 194 | 171 | inferred_complete_timeline |
| `Action_PullBlock` | 195 | 215 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 225 | 229 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 234 | 260 | 27 | inferred_complete_timeline |
| `Action_PullBlock` | 262 | 268 | 7 | inferred_complete_timeline |
| `Action_None` | 271 | 290 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 24–221
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 202 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 221 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 24–359
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 245 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 284 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 359 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 24–215
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 194 | 171 | inferred_complete_timeline |
| `Action_DownBlock` | 195 | 199 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 214 | 215 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 24–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 194 | 171 | inferred_complete_timeline |
| `Action_DownBlock` | 195 | 270 | 76 | inferred_complete_timeline |
| `Action_None` | 271 | 296 | 26 | inferred_complete_timeline |
| `Action_None` | 298 | 302 | 5 | inferred_complete_timeline |
| `Action_None` | 304 | 306 | 3 | inferred_complete_timeline |
| `Action_None` | 308 | 334 | 27 | inferred_complete_timeline |
| `Action_None` | 336 | 339 | 4 | inferred_complete_timeline |
| `Action_None` | 343 | 359 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 24–359
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 306 | 283 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 318 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 359 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 24–359
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 183 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 254 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 359 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 24–357
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 253 | 230 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 326 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 357 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 24–276
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 233 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 268 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 276 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 24–338
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 311 | 288 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 330 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 334 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 338 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 24–359
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 296 | 273 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 359 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 24–259 | 116 | 10 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 24–196 | 63 | 9 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 228–251 | 23 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 228–344 | 65 | 11 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 229–259 | 8 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 245–359 | 107 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 254–310 | 15 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 258–359 | 99 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 258–359 | 102 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 261–265 | 5 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 272–282 | 6 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 278–344 | 52 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 313–359 | 47 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 316–359 | 33 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 319–359 | 23 | 3 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 333–334 | 2 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 339–359 | 21 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 341–359 | 10 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 348–359 | 12 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 351–359 | 9 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 351–359 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 106 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [24-233] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-241] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-276] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-296] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-302] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-334] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-339] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-253] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-326] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-357] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-72] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-224] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-249] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-306] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-318] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-240] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-245] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-284] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-247] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-281] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-290] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [195-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [221-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [225-229] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [234-260] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [262-268] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-290] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-311] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-330] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-334] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-338] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-170] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-255] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-259] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-299] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-340] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-354] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-357] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [195-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [214-215] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-296] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-196] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-254] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-211] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-251] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-254] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-271] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-284] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-302] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-334] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-339] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-344] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-231] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-259] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-248] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-263] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-310] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-303] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-359] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-282] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-325] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-344] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-330] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-340] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-355] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-334] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-347] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-359] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-334] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-342] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-359] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-359] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>