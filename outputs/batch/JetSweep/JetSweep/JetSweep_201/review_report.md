# Play-Annotation-Generator Annotation Review — JetSweep_201

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_201`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | WR1 | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `20` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 156 |
| ✅ EXACT | `Action_JetMotion` | WR3 | `2` | `1` | 140 | START | 140 | 187 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 157 | START | 157 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | WR1 | `7` | `6` | 159 | START | 159 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 159 | START | 159 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `18` | 159 | START | 159 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 159 | START | 173 | 286 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `22` | `21` | 159 | START | 165 | 286 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 172 | END | 157 | 172 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 182 | START | 182 | 187 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `2` | `1` | 188 | START | 188 | 312 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 286 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_SnapReceive` | 157 | 172 | 16 | inferred_complete_timeline |
| `Action_None` | 173 | 181 | 9 | inferred_complete_timeline |
| `Action_Toss` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_None` | 188 | 359 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 321 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_LeadBlock` | 159 | 203 | 45 | inferred_complete_timeline |
| `Action_LeadBlock` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 211 | 220 | 10 | inferred_complete_timeline |
| `Action_LeadBlock` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 196 | 40 | inferred_complete_timeline |
| `Action_None` | 219 | 226 | 8 | inferred_complete_timeline |
| `Action_None` | 236 | 359 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_JetMotion` | 140 | 187 | 48 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 312 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 359 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 165 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 177 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 188 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_BallSnap` | 157 | 172 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 286 | 114 | inferred_complete_timeline |
| `Action_None` | 287 | 359 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 45 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 81 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 143 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 286 | 122 | inferred_complete_timeline |
| `Action_None` | 287 | 359 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 238 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 241 | 258 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 264 | 269 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_None` | 287 | 359 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 174 | 18 | inferred_complete_timeline |
| `Action_None` | 196 | 359 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 173 | 17 | inferred_complete_timeline |
| `Action_None` | 176 | 359 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 250 | 94 | inferred_complete_timeline |
| `Action_None` | 254 | 359 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 359 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 359 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 273 | 117 | inferred_complete_timeline |
| `Action_None` | 275 | 359 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–354
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 351 | 195 | inferred_complete_timeline |
| `Action_None` | 353 | 354 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 275 | 119 | inferred_complete_timeline |
| `Action_None` | 278 | 280 | 3 | inferred_complete_timeline |
| `Action_None` | 298 | 323 | 26 | inferred_complete_timeline |
| `Action_None` | 331 | 333 | 3 | inferred_complete_timeline |
| `Action_None` | 336 | 342 | 7 | inferred_complete_timeline |
| `Action_None` | 348 | 359 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 182 | 26 | inferred_complete_timeline |
| `Action_None` | 189 | 193 | 5 | inferred_complete_timeline |
| `Action_None` | 195 | 359 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 234 | 78 | inferred_complete_timeline |
| `Action_None` | 246 | 359 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–345
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 345 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–359 | 360 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 179–187 | 8 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 208–214 | 7 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 251–266 | 16 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 271–359 | 73 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 278–359 | 82 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `22` (RG): Annotated start 159 != Inferred start 165

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 404: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 404: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 128 frames exceeds threshold 90 frames [start=159, end=286].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 128 frames exceeds threshold 90 frames [start=159, end=286].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [157–172], lower_priority='Action_ZoneBlock' annotated_start=159, effective_Action_ZoneBlock_start=173.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 128 frames exceeds threshold 90 frames [start=159, end=286].
- ⚠️ Action 'Action_None' range [157-359] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-312] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [159-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [206-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [211-220] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [222-223] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-321] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-238] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [241-258] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [264-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [277-278] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-234] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-345] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-182] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-273] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-275] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-323] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-342] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-359] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-351] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-250] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [170-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-196] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-49] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-81] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-143] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [165-286] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-214] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-266] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-290] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-308] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>