# Play-Annotation-Generator Annotation Review — SplitZone_242

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_242`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 28
- **Ball Tracks:** 1
- **Action Segments:** 94
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `12` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 24 | START | 22 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 24 | START | 22 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 24 | START | 22 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 24 | START | 22 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 24 | START | 22 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 24 | START | 22 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 24 | START | 22 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 24 | START | 22 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 24 | START | 22 | 189 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 187 | START | 187 | 200 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 190 | START | 190 | 290 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 190 | START | 201 | 231 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `15` | 190 | START | 190 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `4` | 190 | START | 190 | 241 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `9` | 190 | START | 190 | 213 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `16` | `16` | 194 | START | 194 | 231 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 200 | END | 187 | 200 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 205 | START | 205 | 220 |
| ✅ EXACT | `Action_BallCarry` | RB | `12` | `12` | 221 | START | 221 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 290 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 22–306
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 186 | 165 | inferred_complete_timeline |
| `Action_SnapReceive` | 187 | 200 | 14 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 205 | 220 | 16 | inferred_complete_timeline |
| `Action_None` | 221 | 227 | 7 | inferred_complete_timeline |
| `Action_None` | 231 | 306 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 220 | 199 | inferred_complete_timeline |
| `Action_BallCarry` | 221 | 359 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 22–231
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 193 | 172 | inferred_complete_timeline |
| `Action_SplitBlock` | 194 | 231 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 22–324
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 186 | 165 | inferred_complete_timeline |
| `Action_None` | 187 | 324 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 22–319
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 189 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 241 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 280 | 282 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 287 | 290 | 4 | inferred_complete_timeline |
| `Action_None` | 291 | 319 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 189 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 205 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 248 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 254 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 262 | 290 | 29 | inferred_complete_timeline |
| `Action_None` | 291 | 359 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 22–355
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 186 | 165 | inferred_complete_timeline |
| `Action_BallSnap` | 187 | 200 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 231 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 259 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 261 | 290 | 30 | inferred_complete_timeline |
| `Action_None` | 291 | 355 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 189 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 213 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 229 | 233 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 239 | 248 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 261 | 290 | 30 | inferred_complete_timeline |
| `Action_None` | 291 | 343 | 53 | inferred_complete_timeline |
| `Action_None` | 348 | 359 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 189 | 168 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 290 | 101 | inferred_complete_timeline |
| `Action_None` | 291 | 359 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 22–321
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 186 | 165 | inferred_complete_timeline |
| `Action_None` | 187 | 249 | 63 | inferred_complete_timeline |
| `Action_None` | 254 | 256 | 3 | inferred_complete_timeline |
| `Action_None` | 259 | 265 | 7 | inferred_complete_timeline |
| `Action_None` | 271 | 290 | 20 | inferred_complete_timeline |
| `Action_None` | 294 | 321 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 22–249
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 186 | 165 | inferred_complete_timeline |
| `Action_None` | 187 | 224 | 38 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 249 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 22–228
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 186 | 165 | inferred_complete_timeline |
| `Action_None` | 187 | 225 | 39 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 22–353
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 186 | 165 | inferred_complete_timeline |
| `Action_None` | 187 | 341 | 155 | inferred_complete_timeline |
| `Action_None` | 350 | 353 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 22–359
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 186 | 165 | inferred_complete_timeline |
| `Action_None` | 187 | 263 | 77 | inferred_complete_timeline |
| `Action_None` | 283 | 285 | 3 | inferred_complete_timeline |
| `Action_None` | 290 | 345 | 56 | inferred_complete_timeline |
| `Action_None` | 347 | 359 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 22–268
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 186 | 165 | inferred_complete_timeline |
| `Action_None` | 187 | 268 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 186 | 165 | inferred_complete_timeline |
| `Action_None` | 187 | 359 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 22–346
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 186 | 165 | inferred_complete_timeline |
| `Action_None` | 187 | 333 | 147 | inferred_complete_timeline |
| `Action_None` | 335 | 346 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 35–55 | 21 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 202–320 | 86 | 4 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 250–290 | 27 | 4 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 263–319 | 55 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 270–359 | 90 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 285–323 | 17 | 4 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 294–359 | 66 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 297–301 | 4 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 308–359 | 52 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 308–357 | 46 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 324–342 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | 95 | 186 | 92 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (6 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 101 frames exceeds threshold 90 frames [start=190, end=290].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RG) duration 101 frames exceeds threshold 90 frames [start=190, end=290].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 101 frames exceeds threshold 90 frames [start=190, end=290].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 101 frames exceeds threshold 90 frames [start=190, end=290].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [187–200], lower_priority='Action_ZoneBlock' annotated_start=190, effective_Action_ZoneBlock_start=201.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LG) duration 101 frames exceeds threshold 90 frames [start=190, end=290].
- ⚠️ Action 'Action_None' range [187-249] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-290] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-321] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-225] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-341] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-241] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [280-282] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-319] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-324] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-224] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-263] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-345] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-227] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-306] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-213] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [218-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [229-233] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [239-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [258-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-343] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [221-359] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-333] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-346] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [201-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [248-259] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-355] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-248] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [251-254] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [194-231] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-320] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-274] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-286] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-319] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-289] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-317] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-340] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-357] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-342] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>