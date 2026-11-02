# Play-Annotation-Generator Annotation Review — JetSweep_30

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_30`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 27
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `15` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `10` | `9` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `11` | `10` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `16` | `15` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `18` | `17` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `5` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 102 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `20` | `19` | 102 | START | 106 | 131 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 103 | START | 103 | 116 |
| ✅ EXACT | `Action_LeadBlock` | RB | `8` | `7` | 108 | START | 108 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 108 | START | 108 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 108 | START | 108 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `15` | 108 | START | 108 | 136 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `18` | `17` | 108 | START | 117 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `4` | 108 | START | 108 | 128 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 116 | END | 103 | 116 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 122 | START | 122 | 132 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `18` | `17` | 124 | START | 124 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `20` | `19` | 133 | START | 135 | 246 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `10` | `9` | 177 | BOUNDARY | 108 | 177 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `11` | `10` | 177 | BOUNDARY | 166 | 177 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `16` | `15` | 177 | BOUNDARY | N/A | 177 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `18` | `17` | 177 | BOUNDARY | 124 | 177 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `5` | `4` | 177 | BOUNDARY | N/A | 177 |

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
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_SnapReceive` | 103 | 116 | 14 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_Toss` | 122 | 132 | 11 | inferred_complete_timeline |
| `Action_None` | 133 | 158 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_LeadBlock` | 108 | 177 | 70 | inferred_complete_timeline |
| `Action_None` | 178 | 200 | 23 | inferred_complete_timeline |
| `Action_None` | 206 | 269 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 139 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 212 | 110 | inferred_complete_timeline |
| `Action_None` | 215 | 227 | 13 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 269 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 128 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 171 | 42 | inferred_complete_timeline |
| `Action_None` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_None` | 216 | 253 | 38 | inferred_complete_timeline |
| `Action_None` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 136 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 169 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_BallSnap` | 103 | 116 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 123 | 7 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 124 | 177 | 54 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 162 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 177 | 12 | inferred_complete_timeline |
| `Action_None` | 178 | 269 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 177 | 70 | inferred_complete_timeline |
| `Action_None` | 178 | 184 | 7 | inferred_complete_timeline |
| `Action_None` | 188 | 269 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 132 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 112 | 10 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 116 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 102 | 57 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 174 | 72 | inferred_complete_timeline |
| `Action_None` | 180 | 185 | 6 | inferred_complete_timeline |
| `Action_None` | 211 | 260 | 50 | inferred_complete_timeline |
| `Action_None` | 262 | 264 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 102 | 80 | inferred_complete_timeline |
| `Action_None` | 103 | 222 | 120 | inferred_complete_timeline |
| `Action_None` | 236 | 269 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 187 | 85 | inferred_complete_timeline |
| `Action_None` | 192 | 217 | 26 | inferred_complete_timeline |
| `Action_None` | 219 | 269 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 127 | 144 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 80–112 | 33 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 106–251 | 142 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 111–177 | 46 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 117–162 | 46 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 118–167 | 50 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 133–269 | 113 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 156–172 | 16 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 159–173 | 15 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 167–269 | 79 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 172–269 | 98 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 182–239 | 58 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 216–229 | 14 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 218–269 | 46 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 228–269 | 42 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 235–237 | 3 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 243–269 | 27 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `20` (Position_Unknown): Annotated start 102 != Inferred start 106
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (C): Annotated start 108 != Inferred start 117
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [103–116], lower_priority='Action_ZoneBlock' annotated_start=108, effective_Action_ZoneBlock_start=117.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-144] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-132] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-217] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-253] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-158] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-162] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-260] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-116] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 103, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [103-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-169] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-222] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [106-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [135-246] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-251] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-177] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-167] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-220] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-223] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-269] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>