# Play-Annotation-Generator Annotation Review — JetSweep_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_24`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 8
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `9` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | offense | `5` | `4` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `11` | `10` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `11` | `10` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `8` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 121 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `9` | `8` | 10 | START | 10 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 120 | START | 120 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `15` | `14` | 122 | START | 125 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `9` | 122 | START | 122 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `10` | 122 | START | 122 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `11` | 122 | START | 122 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 122 | START | 129 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `7` | 122 | START | 122 | 151 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 128 | END | 120 | 128 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `9` | `8` | 133 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `11` | `10` | 134 | START | 134 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | `5` | `4` | 140 | START | 140 | 151 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `11` | `10` | 175 | BOUNDARY | 158 | 175 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `11` | `10` | 175 | BOUNDARY | 158 | 175 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `12` | `11` | 175 | BOUNDARY | 171 | 175 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `14` | `13` | 175 | BOUNDARY | 147 | 175 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `8` | `7` | 175 | BOUNDARY | N/A | 175 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_SnapReceive` | 120 | 128 | 9 | inferred_complete_timeline |
| `Action_None` | 129 | 139 | 11 | inferred_complete_timeline |
| `Action_Toss` | 140 | 151 | 12 | inferred_complete_timeline |
| `Action_Toss` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_LeadBlock` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 131 | 175 | 45 | inferred_complete_timeline |
| `Action_None` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 151 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 158 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 174 | 53 | inferred_complete_timeline |
| `Action_None` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 133 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 158 | 175 | 18 | inferred_complete_timeline |
| `Action_None` | 176 | 278 | 103 | inferred_complete_timeline |
| `Action_None` | 280 | 299 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_BallSnap` | 120 | 128 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 143 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 175 | 29 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 299 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 165 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 175 | 5 | inferred_complete_timeline |
| `Action_None` | 176 | 227 | 52 | inferred_complete_timeline |
| `Action_None` | 229 | 299 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 189 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 299 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 119 | 97 | inferred_complete_timeline |
| `Action_None` | 120 | 159 | 40 | inferred_complete_timeline |
| `Action_None` | 161 | 299 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 299 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 148 | 29 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 153 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–299 | 295 | 4 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–23 | 24 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 110–266 | 151 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 126–299 | 174 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 147–299 | 153 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 180–298 | 116 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 191–227 | 37 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 194–240 | 47 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 194–299 | 106 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 204–208 | 5 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 209–216 | 8 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 211–269 | 58 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 226–230 | 5 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 239–288 | 41 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 257–299 | 22 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 260–262 | 3 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 275–276 | 2 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `9` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 50: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Invalid track ID '9,17' in Player Track ID sheet. Must be an integer.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '8' has invalid range: start=133, end=23. Clamping end to start.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [120–128], lower_priority='Action_ZoneBlock' annotated_start=122, effective_Action_ZoneBlock_start=129.
- ⚠️ Action 'Action_None' range [120-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-270] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [140-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-151] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [10-23] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-174] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-299] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [134-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [158-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-278] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-159] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [125-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-266] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-289] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-240] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-228] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-288] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-269] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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