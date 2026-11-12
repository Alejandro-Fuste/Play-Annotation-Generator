# Play-Annotation-Generator Annotation Review — SplitZone_280

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_280`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 43
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_SplitBlock` | WR2 | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `19` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 262 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 229 | START | 229 | 244 |
| ✅ EXACT | `Action_SplitBlock` | WR2 | `4` | `4` | 236 | START | 236 | 302 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 244 | END | 229 | 244 |
| ✅ EXACT | `Action_ZoneBlock` | C | `10` | `10` | 246 | START | 246 | 311 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `13` | 246 | START | 246 | 255 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 246 | START | 246 | 311 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `7` | 246 | START | 246 | 259 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `16` | `16` | 255 | START | 255 | 275 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `7` | `7` | 260 | START | 260 | 272 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `9` | `9` | 263 | START | 263 | 269 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `16` | 276 | START | 276 | 285 |
| ✅ EXACT | `Action_BallCarry` | RB | `9` | `9` | 283 | START | 283 | 449 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_SnapReceive` | 229 | 244 | 16 | inferred_complete_timeline |
| `Action_None` | 245 | 254 | 10 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 255 | 275 | 21 | inferred_complete_timeline |
| `Action_Handoff` | 276 | 285 | 10 | inferred_complete_timeline |
| `Action_None` | 286 | 449 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_PressEdge` | 263 | 269 | 7 | inferred_complete_timeline |
| `Action_PressEdge` | 272 | 282 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 283 | 449 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 449 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_SplitBlock` | 236 | 302 | 67 | inferred_complete_timeline |
| `Action_None` | 303 | 449 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 449 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 449 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 311 | 66 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 255 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 264 | 311 | 48 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_BallSnap` | 229 | 244 | 16 | inferred_complete_timeline |
| `Action_None` | 245 | 245 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 311 | 66 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 259 | 14 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 260 | 272 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 273 | 305 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 307 | 311 | 5 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 264 | 36 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 272 | 277 | 6 | inferred_complete_timeline |
| `Action_None` | 294 | 311 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 449 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 302 | 74 | inferred_complete_timeline |
| `Action_None` | 309 | 449 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 449 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 449 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 449 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 360 | 132 | inferred_complete_timeline |
| `Action_None` | 362 | 371 | 10 | inferred_complete_timeline |
| `Action_None` | 383 | 449 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 310 | 82 | inferred_complete_timeline |
| `Action_None` | 318 | 449 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 449 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 449 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_None` | 229 | 380 | 152 | inferred_complete_timeline |
| `Action_None` | 383 | 449 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–449 | 448 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 255–265 | 11 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 277–280 | 4 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 326–449 | 122 | 2 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 425–426 | 2 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 434–437 | 4 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 438–439 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 27 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 562: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_None' range [229-295] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-311] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-360] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-371] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-449] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [273-305] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [263-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [283-449] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-302] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [246-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [258-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-449] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-449] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-449] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-380] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-449] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-310] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-265] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-449] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-437] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>