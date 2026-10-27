# Play-Annotation-Generator Annotation Review — Counter_389

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_389`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | WR3 | offense | `12` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `12` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `14` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 140 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 141 | START | 141 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `9` | 144 | START | 157 | 159 |
| ✅ EXACT | `Action_DownBlock` | LG | `19` | `18` | 144 | START | 144 | 252 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `21` | `20` | 144 | START | 144 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | WR3 | `12` | `11` | 144 | START | 144 | 226 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 156 | END | 141 | 156 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `16` | 161 | START | 161 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `22` | `21` | 188 | START | 188 | 243 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 252 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_SnapReceive` | 141 | 156 | 16 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 161 | 187 | 27 | inferred_complete_timeline |
| `Action_None` | 188 | 389 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 243 | 56 | inferred_complete_timeline |
| `Action_BallCarry` | 245 | 377 | 133 | inferred_complete_timeline |
| `Action_BallCarry` | 382 | 389 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 144 | 226 | 83 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 236 | 252 | 17 | inferred_complete_timeline |
| `Action_None` | 253 | 268 | 16 | inferred_complete_timeline |
| `Action_None` | 271 | 274 | 4 | inferred_complete_timeline |
| `Action_None` | 279 | 389 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 252 | 109 | inferred_complete_timeline |
| `Action_None` | 253 | 389 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_BallSnap` | 141 | 156 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 166 | 252 | 87 | inferred_complete_timeline |
| `Action_None` | 253 | 348 | 96 | inferred_complete_timeline |
| `Action_None` | 353 | 354 | 2 | inferred_complete_timeline |
| `Action_None` | 361 | 389 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PullBlock` | 144 | 203 | 60 | inferred_complete_timeline |
| `Action_PullBlock` | 206 | 209 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 233 | 93 | inferred_complete_timeline |
| `Action_None` | 295 | 297 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 310 | 170 | inferred_complete_timeline |
| `Action_None` | 313 | 389 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 272 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–389 | 390 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–389 | 390 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 154–166 | 11 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 182–185 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 209–389 | 181 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 248–274 | 22 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 249–380 | 108 | 6 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 272–389 | 118 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 279–389 | 105 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 305–372 | 28 | 6 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 352–353 | 2 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 367–368 | 2 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 389–389 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 780: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 780: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (C) duration 109 frames exceeds threshold 90 frames [start=144, end=252].
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [141–156], lower_priority='Action_DownBlock' annotated_start=144, effective_Action_DownBlock_start=157.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (LG) duration 109 frames exceeds threshold 90 frames [start=144, end=252].
- ⚠️ Action 'Action_None' range [141-389] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-310] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-348] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [144-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-389] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [144-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [206-209] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [245-377] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [382-389] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-389] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-266] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-261] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-330] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-364] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-376] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-294] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-389] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-330] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>