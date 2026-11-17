# Play-Annotation-Generator Annotation Review — Power_167

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_167`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 88
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
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 22 | START | 22 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 22 | START | 22 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 22 | START | 22 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 22 | START | 22 | 277 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 22 | START | 22 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 22 | START | 22 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 22 | START | 22 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 22 | START | 22 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 22 | START | 22 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 22 | START | 22 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 22 | START | 22 | 359 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `13` | `13` | 218 | START | 218 | 266 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `16` | `16` | 218 | START | 218 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `21` | `21` | 218 | START | 218 | 243 |

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
- **Visible Frames:** 22–277
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 277 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 22–78
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 78 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 22–333
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 234 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 285 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 296 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 320 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 333 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 359 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 298 | 277 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 359 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 359 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 230 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 257 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 276 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 322 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 359 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 22–284
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 222 | 201 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 284 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 22–259
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 217 | 196 | inferred_complete_timeline |
| `Action_PullBlock` | 218 | 243 | 26 | inferred_complete_timeline |
| `Action_PullBlock` | 245 | 259 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 217 | 196 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 239 | 253 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 255 | 277 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_None` | 288 | 359 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 22–279
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 217 | 196 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 266 | 49 | inferred_complete_timeline |
| `Action_DownBlock` | 275 | 279 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 359 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 22–323
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 140 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 323 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 22–354
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 277 | 256 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 304 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 346 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 354 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 22–288
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 232 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 241 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 267 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 288 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 22–285
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 242 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 285 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 359 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 359 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 22–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 345 | 324 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 359 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 359 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 22–359
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 300 | 279 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 352 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 359 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 22–359 | 338 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 87–359 | 265 | 5 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 224–232 | 9 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 295–359 | 55 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 311–359 | 48 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 312–315 | 4 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 313–359 | 45 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 328–359 | 32 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 330–359 | 30 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 334–358 | 19 | 4 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 359–359 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 336: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [22-234] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-285] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-296] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-320] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-333] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-298] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-242] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-359] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-241] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-267] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-288] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-140] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-323] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-345] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-300] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-352] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-359] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-277] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-281] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-304] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-346] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-354] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-266] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [275-279] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-277] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-219] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [239-253] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [255-277] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [285-287] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-284] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-230] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-257] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-276] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-322] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [218-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [245-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-292] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-308] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-315] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-340] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-301] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-315] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-354] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-315] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-315] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-359] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-345] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-353] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-358] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>