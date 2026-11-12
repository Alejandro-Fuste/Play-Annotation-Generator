# Play-Annotation-Generator Annotation Review — SplitZone_282

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_282`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_PressEdge` | DE1 | defense | `6` | `6` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_ReadEdgeDefender` | DT2 | defense | `18` | `18` |
| ✅ EXACT | `Action_Handoff` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 146 | START | 176 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 146 | START | 146 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `21` | 146 | START | 146 | 207 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 146 | START | 146 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `8` | 146 | START | 146 | 190 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 159 | START | 159 | 175 |
| ✅ EXACT | `Action_PressEdge` | DE1 | `6` | `6` | 174 | START | 174 | 206 |
| ✅ EXACT | `Action_SplitBlock` | TE | `1` | `1` | 174 | START | 174 | 215 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 175 | END | 159 | 175 |
| ✅ EXACT | `Action_ReadEdgeDefender` | DT2 | `18` | `18` | 182 | START | 182 | 190 |
| ✅ EXACT | `Action_Handoff` | LG | `8` | `8` | 191 | START | 191 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `10` | 206 | START | 206 | 365 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–396
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_SnapReceive` | 159 | 175 | 17 | inferred_complete_timeline |
| `Action_None` | 176 | 205 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 206 | 365 | 160 | inferred_complete_timeline |
| `Action_BallCarry` | 367 | 368 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 372 | 390 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 393 | 396 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 449 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 449 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 449 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 449 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–446
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_SplitBlock` | 174 | 215 | 42 | inferred_complete_timeline |
| `Action_None` | 216 | 446 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 207 | 62 | inferred_complete_timeline |
| `Action_None` | 208 | 449 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 190 | 45 | inferred_complete_timeline |
| `Action_Handoff` | 191 | 206 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 207 | 1 | inferred_complete_timeline |
| `Action_None` | 208 | 374 | 167 | inferred_complete_timeline |
| `Action_None` | 376 | 449 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_None` | 146 | 158 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 159 | 175 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 190 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 207 | 12 | inferred_complete_timeline |
| `Action_None` | 208 | 449 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 169 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 207 | 37 | inferred_complete_timeline |
| `Action_None` | 208 | 273 | 66 | inferred_complete_timeline |
| `Action_None` | 277 | 291 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 207 | 62 | inferred_complete_timeline |
| `Action_None` | 208 | 449 | 242 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PressEdge` | 174 | 206 | 33 | inferred_complete_timeline |
| `Action_None` | 207 | 274 | 68 | inferred_complete_timeline |
| `Action_None` | 284 | 449 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 449 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 251 | 93 | inferred_complete_timeline |
| `Action_None` | 265 | 449 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 182 | 190 | 9 | inferred_complete_timeline |
| `Action_None` | 191 | 449 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–444
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 444 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 283 | 125 | inferred_complete_timeline |
| `Action_None` | 288 | 298 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 449 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 449 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 449 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 449 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–432
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 432 | 274 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 214–217 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 214–216 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 250–257 | 8 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 297–449 | 153 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 300–449 | 150 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 339–340 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 345–351 | 7 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 379–449 | 51 | 6 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 416–418 | 3 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 438–442 | 5 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 440–441 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [159–175], lower_priority='Action_ZoneBlock' annotated_start=146, effective_Action_ZoneBlock_start=176.
- ⚠️ Action 'Action_None' range [159-449] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-446] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-251] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-449] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-274] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-449] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-374] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-432] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [206-365] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [367-368] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [372-390] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [393-396] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-449] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-444] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [176-190] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-283] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-298] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-273] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-291] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-449] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-351] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-383] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-399] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-428] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-449] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-418] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-442] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '33' has 1 frames without a visible bounding box.
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

</details>