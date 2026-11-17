# Play-Annotation-Generator Annotation Review — Power_225

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_225`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `14` | `14` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `1` | `Group` | 11 | START | 11 | 341 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 11 | START | 11 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 11 | START | 11 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 11 | START | 11 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 11 | START | 11 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 11 | START | 11 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 11 | START | 11 | 296 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 11 | START | 11 | 331 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 11 | START | 11 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 11 | START | 11 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 11 | START | 11 | 398 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `11` | `11` | 270 | START | 270 | 278 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `12` | `12` | 270 | START | 270 | 289 |
| ✅ EXACT | `Action_DownBlock` | LG | `14` | `14` | 270 | START | 270 | 315 |
| ✅ EXACT | `Action_PullBlock` | RG | `21` | `21` | 270 | START | 270 | 314 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 11–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 449 | 439 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 11–331
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 331 | 321 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 11–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 449 | 439 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 11–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 449 | 439 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 11–449
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 341 | 331 | inferred_complete_timeline |
| `Action_PreSnap` | 387 | 449 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 11–449
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 398 | 388 | inferred_complete_timeline |
| `Action_PreSnap` | 404 | 430 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 440 | 449 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 11–449
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 269 | 259 | inferred_complete_timeline |
| `Action_DownBlock` | 270 | 289 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 291 | 293 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 302 | 315 | 14 | inferred_complete_timeline |
| `Action_None` | 316 | 390 | 75 | inferred_complete_timeline |
| `Action_None` | 404 | 449 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 11–386
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 269 | 259 | inferred_complete_timeline |
| `Action_DownBlock` | 270 | 315 | 46 | inferred_complete_timeline |
| `Action_None` | 316 | 347 | 32 | inferred_complete_timeline |
| `Action_None` | 353 | 373 | 21 | inferred_complete_timeline |
| `Action_None` | 375 | 386 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 11–449
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 269 | 259 | inferred_complete_timeline |
| `Action_DownBlock` | 270 | 278 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 280 | 284 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 289 | 303 | 15 | inferred_complete_timeline |
| `Action_None` | 318 | 449 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 11–338
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 269 | 259 | inferred_complete_timeline |
| `Action_PullBlock` | 270 | 314 | 45 | inferred_complete_timeline |
| `Action_None` | 318 | 322 | 5 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 11–369
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 296 | 286 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 305 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 351 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 369 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–353
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 294 | 284 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 304 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 353 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 11–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 347 | 337 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 449 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 11–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 299 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 11–311
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 311 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 11–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 314 | 304 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 323 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 341 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 449 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 11–379
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 379 | 369 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 11–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 449 | 439 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 11–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 449 | 439 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 11–428
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 413 | 403 | inferred_complete_timeline |
| `Action_PreSnap` | 426 | 428 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 11–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 449 | 439 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 11–449
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 96 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 407 | 310 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 449 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 292–340 | 49 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 313–449 | 131 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 321–325 | 5 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 329–436 | 81 | 8 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 345–449 | 95 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 346–430 | 73 | 4 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 361–400 | 33 | 3 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 370–449 | 56 | 5 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 391–449 | 59 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 405–406 | 2 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 444–449 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)

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
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [11-341] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-331] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-398] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-430] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-311] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-294] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-304] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-353] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-314] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-323] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-341] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-407] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-379] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [270-278] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [280-284] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [289-303] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [270-289] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [291-293] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-390] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-449] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-413] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-428] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-347] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-373] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-386] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-347] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-296] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-305] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-351] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-369] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [270-314] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-322] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-340] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-360] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-325] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-332] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-337] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-348] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-402] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-413] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-420] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-436] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-375] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-449] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-366] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-411] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-421] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-430] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-385] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-393] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-400] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-396] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-408] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-420] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-435] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-449] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-449] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-406] for track '31' has 1 frames without a visible bounding box.
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