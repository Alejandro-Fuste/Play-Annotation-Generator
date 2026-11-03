# Play-Annotation-Generator Annotation Review — Slants0to10_79

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_79`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | DT1 | defense | `18` | `18` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 15 | START | 15 | 30 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `17` | `17` | 18 | START | 31 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 18 | START | 18 | 67 |
| ✅ EXACT | `Action_PassBlock` | LT | `20` | `20` | 18 | START | 18 | 225 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 18 | START | 18 | 52 |
| ✅ EXACT | `Action_PassBlock` | RT | `5` | `5` | 18 | START | 18 | 201 |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | `0` | `0` | 27 | START | 27 | 99 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `18` | `18` | 30 | END | 15 | 30 |
| ✅ EXACT | `Action_ThrowPass` | DT1 | `18` | `18` | 66 | START | 66 | 75 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `0` | `0` | 107 | START | 107 | 299 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 132 | 118 | inferred_complete_timeline |
| `Action_None` | 134 | 139 | 6 | inferred_complete_timeline |
| `Action_None` | 143 | 299 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 27 | 99 | 73 | inferred_complete_timeline |
| `Action_None` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 299 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 225 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 52 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 65 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 15 | 30 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 43 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 67 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 93 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 102 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 208 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 201 | 184 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 274 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 30 | 16 | inferred_complete_timeline |
| `Action_None` | 31 | 65 | 35 | inferred_complete_timeline |
| `Action_ThrowPass` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_None` | 76 | 111 | 36 | inferred_complete_timeline |
| `Action_None` | 113 | 197 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 233 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 78 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 126 | 112 | inferred_complete_timeline |
| `Action_None` | 132 | 299 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 299 | 285 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–154 | 79 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 49–51 | 3 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 77–78 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 84–229 | 126 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 93–249 | 157 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 96–97 | 2 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 97–218 | 117 | 3 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 106–112 | 7 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 131–135 | 5 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 144–212 | 69 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 187–225 | 33 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 245–248 | 4 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 276–278 | 3 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `17` (C): Annotated start 18 != Inferred start 31
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 80: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [15–30], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=31.
- ⚠️ Action 'Action_None' range [15-132] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-299] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-299] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-43] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-197] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-67] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-93] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-102] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-109] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-225] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-107] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-109] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-130] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-218] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-212] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '31' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>