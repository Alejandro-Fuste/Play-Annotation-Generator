# Play-Annotation-Generator Annotation Review — OutsideZoneRead_79

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_79`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 629
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `4` | `4` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 629 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 257 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 259 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 629 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 237 |
| ✅ EXACT | `Action_PressEdge` | RB | `4` | `4` | 225 | START | 225 | 283 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `8` | `8` | 231 | START | 231 | 243 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `13` | `13` | 238 | START | 238 | 275 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `20` | 238 | START | 238 | 275 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 238 | START | 238 | 275 |
| ✅ EXACT | `Action_ZoneBlock` | C | `5` | `5` | 238 | START | 238 | 275 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `9` | 238 | START | 238 | 244 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 244 | START | 244 | 257 |

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
- **Visible Frames:** 0–629
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 231 | 243 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 244 | 257 | 14 | inferred_complete_timeline |
| `Action_None` | 258 | 617 | 360 | inferred_complete_timeline |
| `Action_None` | 623 | 629 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_PressEdge` | 225 | 283 | 59 | inferred_complete_timeline |
| `Action_None` | 284 | 298 | 15 | inferred_complete_timeline |
| `Action_None` | 327 | 328 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 629 | 630 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 629 | 630 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 615

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 257 | 258 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 290 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 324 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 609 | 280 | inferred_complete_timeline |
| `Action_PreSnap` | 611 | 629 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–415
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 318 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 331 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 337 | 363 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 367 | 375 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 398 | 415 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 275 | 38 | inferred_complete_timeline |
| `Action_None` | 276 | 629 | 354 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 275 | 38 | inferred_complete_timeline |
| `Action_None` | 276 | 629 | 354 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 275 | 38 | inferred_complete_timeline |
| `Action_None` | 276 | 629 | 354 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 275 | 38 | inferred_complete_timeline |
| `Action_None` | 276 | 434 | 159 | inferred_complete_timeline |
| `Action_None` | 437 | 476 | 40 | inferred_complete_timeline |
| `Action_None` | 478 | 629 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 244 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 252 | 275 | 24 | inferred_complete_timeline |
| `Action_None` | 276 | 354 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 629 | 630 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 629 | 630 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 629 | 365 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 628

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 288 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 629 | 339 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–516
- **Visible Samples:** 515

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_PreSnap` | 435 | 516 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 276 | 277 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 629 | 347 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–603
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 583 | 584 | inferred_complete_timeline |
| `Action_PreSnap` | 585 | 587 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 592 | 597 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 602 | 603 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 622

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 339 | 318 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 629 | 284 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 629 | 630 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 435 | 436 | inferred_complete_timeline |
| `Action_PreSnap` | 437 | 629 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 314 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 238–284 | 9 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 289–629 | 339 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 333–629 | 274 | 6 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 335–339 | 5 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 349–401 | 29 | 6 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 350–360 | 8 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 372–385 | 11 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 384–629 | 246 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 515–516 | 2 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 530–629 | 100 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 536–537 | 2 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 599–602 | 4 | 1 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 608–613 | 6 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 610–629 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 58 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-288] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-629] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-259] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-318] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-331] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-363] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-375] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-415] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-298] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-306] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-314] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-435] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-617] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-354] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-339] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-257] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-290] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-324] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-609] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-434] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-476] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-276] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-583] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [585-587] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [592-597] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [602-603] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-432] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-516] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-275] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-284] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-402] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-335] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-347] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-393] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-409] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-467] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-339] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-354] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-363] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-369] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-390] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-401] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-355] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-360] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-375] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-385] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-516] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-537] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [599-602] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [608-613] for track '34' has 1 frames without a visible bounding box.
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