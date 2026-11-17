# Play-Annotation-Generator Annotation Review — Power_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_67`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 0
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 23 | START | 23 | 339 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 23 | START | 23 | 324 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 23 | START | 23 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 23 | START | 23 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 23 | START | 23 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 23 | START | 23 | 240 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 23 | START | 23 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 23 | START | 23 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 23 | START | 23 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 23 | START | 23 | 250 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 23 | START | 23 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `12` | `12` | 220 | START | 220 | 248 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `17` | `17` | 220 | START | 220 | 250 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `21` | 220 | START | 220 | 250 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `8` | `8` | 220 | START | 220 | 248 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 23–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 359 | 337 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 23–332
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 291 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 300 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 303 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 332 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 23–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 359 | 337 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 23–359
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 339 | 317 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 348 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 23–359
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 324 | 302 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 359 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 23–240
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 240 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 23–358
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 219 | 197 | inferred_complete_timeline |
| `Action_DownBlock` | 220 | 248 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 259 | 277 | 19 | inferred_complete_timeline |
| `Action_None` | 278 | 299 | 22 | inferred_complete_timeline |
| `Action_None` | 315 | 358 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 23–359
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 250 | 228 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 282 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 300 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 359 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 23–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 219 | 197 | inferred_complete_timeline |
| `Action_DownBlock` | 220 | 250 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 255 | 276 | 22 | inferred_complete_timeline |
| `Action_None` | 279 | 359 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 23–322
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 219 | 197 | inferred_complete_timeline |
| `Action_PullBlock` | 220 | 248 | 29 | inferred_complete_timeline |
| `Action_PullBlock` | 255 | 277 | 23 | inferred_complete_timeline |
| `Action_None` | 278 | 300 | 23 | inferred_complete_timeline |
| `Action_None` | 317 | 322 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 23–359
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 219 | 197 | inferred_complete_timeline |
| `Action_DownBlock` | 220 | 250 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 255 | 277 | 23 | inferred_complete_timeline |
| `Action_None` | 278 | 304 | 27 | inferred_complete_timeline |
| `Action_None` | 310 | 312 | 3 | inferred_complete_timeline |
| `Action_None` | 314 | 359 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 23–345
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 250 | 228 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 300 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 320 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 345 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 23–359
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 248 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 300 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 359 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 23–359
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 242 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 302 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 359 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 23–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 302 | 280 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 359 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 23–245
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 245 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 23–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 359 | 337 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 23–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 269 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 23–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 359 | 337 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 23–354
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 284 | 262 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 304 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 307 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 330 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 340 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 345 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 354 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 23–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 327 | 305 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 341 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 344 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 359 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 23–358 | 336 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 51–54 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 256–357 | 90 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 262–359 | 59 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 318–359 | 42 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 331–358 | 28 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 350–359 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 136: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [23-339] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-348] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-324] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-359] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-240] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-358] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-302] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-311] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-250] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-300] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-320] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-345] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-250] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-282] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-300] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-310] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [220-248] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-300] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-322] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-248] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-300] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-284] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-304] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-330] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-340] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-345] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-354] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [220-248] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [256-257] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-358] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-302] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-359] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-291] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-300] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-332] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-327] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-341] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-344] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [220-250] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-304] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-359] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [220-250] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [255-276] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-54] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-301] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-357] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-264] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-300] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-358] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-354] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-359] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>