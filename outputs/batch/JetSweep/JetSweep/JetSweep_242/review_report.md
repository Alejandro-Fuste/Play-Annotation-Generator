# Play-Annotation-Generator Annotation Review — JetSweep_242

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_242`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 54
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 34
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_LeadBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 107 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `15` | `14` | 105 | START | 106 | 137 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 108 | START | 108 | 124 |
| ✅ EXACT | `Action_LeadBlock` | LT | `3` | `2` | 114 | START | 114 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 114 | START | 114 | 166 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `3` | `2` | 114 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 114 | START | 114 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `5` | 114 | START | 114 | 160 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `7` | `6` | 114 | START | 125 | 165 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 124 | END | 108 | 124 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 132 | START | 132 | 137 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `15` | `14` | 138 | START | 138 | 172 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 189 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_SnapReceive` | 108 | 124 | 17 | inferred_complete_timeline |
| `Action_None` | 125 | 131 | 7 | inferred_complete_timeline |
| `Action_Toss` | 132 | 137 | 6 | inferred_complete_timeline |
| `Action_None` | 138 | 289 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 181 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_LeadBlock` | 114 | 169 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 166 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_BallSnap` | 108 | 124 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 165 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 160 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 159 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 226 | 119 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 156 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 149 | 42 | inferred_complete_timeline |
| `Action_None` | 152 | 196 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 163 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 299 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_None` | 108 | 163 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 106–172 | 67 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 133–296 | 162 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 188–299 | 112 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 195–299 | 82 | 2 | Undefined position; Undefined team |
| `18` | `27` | Position_Unknown | Team_Unknown | 250–299 | 50 | 1 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 255–299 | 45 | 1 | Undefined position; Undefined team |
| `20` | `30` | Position_Unknown | Team_Unknown | 261–267 | 7 | 1 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 264–270 | 7 | 1 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 268–270 | 3 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 269–295 | 12 | 3 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 275–285 | 11 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 284–299 | 16 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 286–299 | 14 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 289–294 | 6 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 291–292 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `15` (Position_Unknown): Annotated start 105 != Inferred start 106
- ❌ Missing segment for action `Action_ZoneBlock` on target `3` (LT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `7` (C): Annotated start 114 != Inferred start 125

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 32 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Overlapping action conflict at frame 114 for track '2': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [108–124], lower_priority='Action_ZoneBlock' annotated_start=114, effective_Action_ZoneBlock_start=125.
- ⚠️ Action 'Action_None' range [108-226] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-181] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [114-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-159] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-160] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-156] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-299] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-289] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-163] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-196] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-172] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-291] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-205] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-299] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-270] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-295] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-285] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-294] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>