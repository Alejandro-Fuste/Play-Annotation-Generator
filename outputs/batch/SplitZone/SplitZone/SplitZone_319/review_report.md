# Play-Annotation-Generator Annotation Review — SplitZone_319

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_319`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 27
- **Ball Tracks:** 3
- **Action Segments:** 65
- **Validation Warnings:** 52
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 10
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `4` | `4` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 242 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 242 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 251 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 242 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 242 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 232 | START | 232 | 246 |
| ✅ EXACT | `Action_SplitBlock` | TE | `7` | `7` | 240 | START | 240 | 292 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `1` | 243 | START | 243 | 297 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 243 | START | 247 | 288 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `11` | 243 | START | 243 | 297 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 243 | START | 243 | 297 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `9` | 243 | START | 243 | 297 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 246 | END | 232 | 246 |
| ✅ EXACT | `Action_PressEdge` | RB | `4` | `4` | 252 | START | 252 | 274 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `8` | `8` | 252 | START | 252 | 260 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 261 | START | 261 | 276 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 275 | START | 275 | 453 |

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
- **Visible Frames:** 0–392
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_SnapReceive` | 232 | 246 | 15 | inferred_complete_timeline |
| `Action_None` | 247 | 251 | 5 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 252 | 260 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 261 | 276 | 16 | inferred_complete_timeline |
| `Action_None` | 277 | 392 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 251 | 252 | inferred_complete_timeline |
| `Action_PressEdge` | 252 | 274 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 275 | 453 | 179 | inferred_complete_timeline |
| `Action_BallCarry` | 456 | 457 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 462 | 479 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |
| `Action_SplitBlock` | 240 | 292 | 53 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 306 | 479 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–452
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 242 | 243 | inferred_complete_timeline |
| `Action_ZoneBlock` | 243 | 297 | 55 | inferred_complete_timeline |
| `Action_None` | 298 | 452 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 242 | 243 | inferred_complete_timeline |
| `Action_ZoneBlock` | 243 | 297 | 55 | inferred_complete_timeline |
| `Action_None` | 298 | 479 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_BallSnap` | 232 | 246 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 288 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 290 | 297 | 8 | inferred_complete_timeline |
| `Action_None` | 298 | 479 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 242 | 243 | inferred_complete_timeline |
| `Action_ZoneBlock` | 243 | 297 | 55 | inferred_complete_timeline |
| `Action_None` | 298 | 479 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 242 | 243 | inferred_complete_timeline |
| `Action_ZoneBlock` | 243 | 297 | 55 | inferred_complete_timeline |
| `Action_None` | 298 | 479 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 479 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 479 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 323 | 92 | inferred_complete_timeline |
| `Action_None` | 325 | 408 | 84 | inferred_complete_timeline |
| `Action_None` | 412 | 479 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 479 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 479 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_None` | 232 | 479 | 248 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 27–479 | 441 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 281–479 | 199 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 289–479 | 191 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 292–293 | 2 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 302–336 | 22 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 322–472 | 151 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 358–479 | 122 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 359–464 | 106 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 362–479 | 118 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 368–380 | 13 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 426–434 | 9 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 461–479 | 19 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 478–479 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | 0 | 87 | 60 | 68.2% | 3–10, 13, 22, 27, 57–61, 64–65, 67–69, 72–75, 78, 81–82 |
| `15` | `15` | 21 | 21 | 1 | 100.0% | None |
| `17` | `17` | 197 | 232 | 33 | 91.7% | 204–205, 223 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 24 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [232–246], lower_priority='Action_ZoneBlock' annotated_start=243, effective_Action_ZoneBlock_start=247.
- ⚠️ Action 'Action_PreSnap' range [0-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [275-453] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [456-457] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [462-479] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-452] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-479] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-392] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [243-297] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [247-288] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-323] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-408] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-479] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-195] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-307] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-336] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-472] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-464] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-380] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-434] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>