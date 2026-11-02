# Play-Annotation-Generator Annotation Review — JetSweep_32

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_32`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 9
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `3` | `2` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | DE | defense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `10` | `9` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `2` | `1` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `4` | `3` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `6` | `5` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `8` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `1` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 125 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 122 | START | 122 | 135 |
| ✅ EXACT | `Action_LeadBlock` | RB | `3` | `2` | 126 | START | 126 | 168 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `9` | 126 | START | 136 | 174 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 126 | START | 126 | 174 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `3` | 126 | START | 126 | 174 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 126 | START | 126 | 174 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `7` | 126 | START | 126 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `18` | `16` | 128 | START | 128 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 135 | END | 122 | 135 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 142 | START | 142 | 150 |
| ✅ EXACT | `Action_BallCarry` | DE | `14` | `13` | 151 | START | 151 | 329 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `10` | `9` | 174 | BOUNDARY | 136 | 174 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `2` | `1` | 174 | BOUNDARY | 126 | 174 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `4` | `3` | 174 | BOUNDARY | 126 | 174 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `6` | `5` | 174 | BOUNDARY | 126 | 174 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `8` | `7` | 174 | BOUNDARY | 126 | 174 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_SnapReceive` | 122 | 135 | 14 | inferred_complete_timeline |
| `Action_None` | 136 | 141 | 6 | inferred_complete_timeline |
| `Action_Toss` | 142 | 150 | 9 | inferred_complete_timeline |
| `Action_None` | 151 | 191 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_LeadBlock` | 126 | 168 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 148 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 174 | 49 | inferred_complete_timeline |
| `Action_None` | 175 | 183 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 174 | 49 | inferred_complete_timeline |
| `Action_None` | 175 | 186 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_BallSnap` | 122 | 135 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 174 | 39 | inferred_complete_timeline |
| `Action_None` | 175 | 188 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 174 | 49 | inferred_complete_timeline |
| `Action_None` | 175 | 191 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 174 | 49 | inferred_complete_timeline |
| `Action_None` | 175 | 192 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 128 | 7 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_None` | 147 | 181 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 150 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 151 | 329 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 125 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 137 | 16 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 80 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 121 | 17 | inferred_complete_timeline |
| `Action_None` | 122 | 152 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 161 | 40 | inferred_complete_timeline |
| `Action_None` | 169 | 187 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 121 | 15 | inferred_complete_timeline |
| `Action_None` | 122 | 133 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 36–40 | 5 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 128–329 | 186 | 6 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 150–184 | 35 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 163–329 | 166 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 166–170 | 5 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 169–184 | 12 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 179–329 | 149 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 187–329 | 137 | 5 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 191–329 | 136 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 193–236 | 44 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 196–207 | 12 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 200–248 | 49 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 223–325 | 83 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 245–329 | 85 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 246–329 | 84 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 256–329 | 74 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 263–319 | 57 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 287–306 | 20 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 298–329 | 32 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 309–329 | 18 | 2 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 310–327 | 17 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 311–329 | 19 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 126 != Inferred start 136
- ⚠️ Ambiguous match for action `Action_JetMotion` and target `18` (6 segments found)

### Track Identity Issues

- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [122–135], lower_priority='Action_ZoneBlock' annotated_start=126, effective_Action_ZoneBlock_start=136.
- ⚠️ Action 'Action_None' range [122-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-183] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [126-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-187] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-191] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-181] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-80] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-142] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-133] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [128-150] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [153-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [186-299] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [306-307] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [310-315] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-191] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-273] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-329] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-232] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-267] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-236] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-207] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-255] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-314] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-329] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-319] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-306] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-313] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-327] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-329] for track '38' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>