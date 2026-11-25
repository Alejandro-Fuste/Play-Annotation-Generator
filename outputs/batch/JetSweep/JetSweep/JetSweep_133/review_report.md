# Play-Annotation-Generator Annotation Review — JetSweep_133

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_133`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | DE1 | defense | `13` | `12` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | DE1 | defense | `13` | `12` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_JetMotion` | DE1 | `13` | `12` | 14 | START | 14 | 74 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 47 | START | 47 | 60 |
| ✅ EXACT | `Action_LeadBlock` | RB | `1` | `0` | 48 | START | 48 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE | `2` | `1` | 48 | START | 48 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 48 | START | 77 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 48 | START | 48 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 48 | START | 48 | 150 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 48 | START | 48 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 65 | END | 47 | 65 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 68 | START | 68 | 74 |
| ✅ EXACT | `Action_BallCarry` | DE1 | `13` | `12` | 75 | START | 75 | 75 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `18` | `17` | 75 | START | 75 | 150 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 150 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 65 | 19 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_Toss` | 68 | 74 | 7 | inferred_complete_timeline |
| `Action_None` | 75 | 307 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_LeadBlock` | 48 | 150 | 103 | inferred_complete_timeline |
| `Action_None` | 151 | 359 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 359 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–308
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 260 | 214 | inferred_complete_timeline |
| `Action_None` | 270 | 275 | 6 | inferred_complete_timeline |
| `Action_None` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_None` | 284 | 298 | 15 | inferred_complete_timeline |
| `Action_None` | 300 | 308 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 359 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SealBlock` | 48 | 171 | 124 | inferred_complete_timeline |
| `Action_SealBlock` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_SealBlock` | 187 | 193 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 76 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 150 | 67 | inferred_complete_timeline |
| `Action_None` | 151 | 359 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 60 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 150 | 69 | inferred_complete_timeline |
| `Action_None` | 151 | 354 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 150 | 103 | inferred_complete_timeline |
| `Action_None` | 151 | 245 | 95 | inferred_complete_timeline |
| `Action_None` | 247 | 359 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 150 | 103 | inferred_complete_timeline |
| `Action_None` | 151 | 333 | 183 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_JetMotion` | 14 | 74 | 61 | inferred_complete_timeline |
| `Action_BallCarry` | 75 | 75 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 115 | 69 | inferred_complete_timeline |
| `Action_None` | 117 | 359 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 211 | 165 | inferred_complete_timeline |
| `Action_None` | 213 | 359 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 359 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 101 | 55 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 142 | 29 | inferred_complete_timeline |
| `Action_None` | 154 | 359 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 359 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 359 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–339
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 339 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 359 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 296 | 250 | inferred_complete_timeline |
| `Action_None` | 305 | 359 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 204 | 158 | inferred_complete_timeline |
| `Action_None` | 206 | 359 | 154 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–359 | 360 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 93–359 | 267 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 131–132 | 2 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 192–319 | 89 | 8 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 203–357 | 155 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 216–236 | 18 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 243–245 | 3 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 263–297 | 12 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 278–279 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 300–349 | 28 | 5 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 322–356 | 18 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 325–326 | 2 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 344–359 | 12 | 2 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 348–359 | 12 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 355–356 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SealBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 267: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '0' (RB) duration 103 frames exceeds threshold 90 frames [start=48, end=150].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 103 frames exceeds threshold 90 frames [start=48, end=150].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [47–65], lower_priority='Action_ZoneBlock' annotated_start=48, effective_Action_ZoneBlock_start=66.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 103 frames exceeds threshold 90 frames [start=48, end=150].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 103 frames exceeds threshold 90 frames [start=48, end=150].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 103 frames exceeds threshold 90 frames [start=48, end=150].
- ⚠️ Action 'Action_SealBlock' range [48-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [177-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [187-193] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-339] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-101] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-142] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-359] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-260] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-298] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-308] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-359] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '12' starts at frame 75, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [75-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-307] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-296] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-211] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [47-60] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-354] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-333] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-150] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-245] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-268] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-288] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-309] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-357] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-227] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-272] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-318] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-331] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-349] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-336] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-354] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-359] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>