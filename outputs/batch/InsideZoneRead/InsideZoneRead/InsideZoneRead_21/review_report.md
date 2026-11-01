# Play-Annotation-Generator Annotation Review — InsideZoneRead_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_21`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `12` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 20 | START | 20 | 39 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `14` | 22 | START | 40 | 42 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 39 | END | 20 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `6` | `5` | 44 | START | 44 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `6` | `5` | 51 | START | 51 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `9` | 59 | START | 59 | 79 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 118 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 39 | 20 | inferred_complete_timeline |
| `Action_None` | 40 | 43 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 44 | 48 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 50 | 50 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 51 | 55 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_None` | 59 | 244 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 58 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 59 | 79 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 136 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 146 | 154 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 163 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 230 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 144 | 125 | inferred_complete_timeline |
| `Action_None` | 146 | 269 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_BallSnap` | 20 | 39 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 42 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 22 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 238 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 269 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 197 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 257 | 238 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–269 | 264 | 5 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 2–103 | 62 | 7 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 2–77 | 69 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 58–269 | 149 | 7 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 63–79 | 13 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 64–269 | 139 | 9 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 64–137 | 23 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 65–269 | 148 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 75–269 | 127 | 7 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 124–220 | 85 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 125–269 | 116 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 155–269 | 112 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 157–238 | 78 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 161–269 | 109 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 163–269 | 105 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 180–269 | 46 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 209–233 | 21 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 249–269 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 22 != Inferred start 40
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF3` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 44: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 44: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [20–39], lower_priority='Action_ZoneBlock' annotated_start=22, effective_Action_ZoneBlock_start=40.
- ⚠️ Action 'Action_None' range [20-230] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-197] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-217] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [44-48] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [51-55] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-257] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-238] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-58] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [59-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-136] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [146-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-22] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [20-39] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-19] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-70] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-86] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-68] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-68] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-135] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-212] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-130] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-137] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-220] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-192] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-225] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-195] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-233] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-269] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>