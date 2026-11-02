# Play-Annotation-Generator Annotation Review — JetSweep_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_28`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 154
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 4
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-F | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `5` | `4` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `13` | `12` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `4` | `3` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `5` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-F | `6` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 94 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 83 | START | 83 | 98 |
| ✅ EXACT | `Action_LeadBlock` | RB | `7` | `6` | 95 | START | 95 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `11` | 95 | START | 95 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `12` | 95 | START | 95 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `3` | 95 | START | 95 | 118 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `5` | `4` | 95 | START | 99 | 121 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 98 | END | 83 | 98 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `16` | `15` | 102 | START | 102 | 110 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 108 | START | 108 | 121 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `16` | `15` | 122 | START | N/A | N/A |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `5` | `4` | 122 | START | 122 | 141 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `12` | `11` | 141 | BOUNDARY | N/A | 141 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `13` | `12` | 141 | BOUNDARY | N/A | 141 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `4` | `3` | 141 | BOUNDARY | 120 | 141 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `5` | `4` | 141 | BOUNDARY | 122 | 141 |

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
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 83 | 98 | 16 | inferred_complete_timeline |
| `Action_None` | 99 | 107 | 9 | inferred_complete_timeline |
| `Action_Toss` | 108 | 121 | 14 | inferred_complete_timeline |
| `Action_None` | 122 | 135 | 14 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_LeadBlock` | 95 | 141 | 47 | inferred_complete_timeline |
| `Action_None` | 142 | 154 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE-F — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 230 | 148 | inferred_complete_timeline |
| `Action_None` | 248 | 261 | 14 | inferred_complete_timeline |
| `Action_None` | 268 | 271 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 109 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 116 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 138 | 18 | inferred_complete_timeline |
| `Action_None` | 162 | 214 | 53 | inferred_complete_timeline |
| `Action_None` | 217 | 329 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 94 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 95 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 118 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_BallSnap` | 83 | 98 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 121 | 23 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 122 | 141 | 20 | inferred_complete_timeline |
| `Action_None` | 142 | 329 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 118 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 141 | 22 | inferred_complete_timeline |
| `Action_None` | 142 | 240 | 99 | inferred_complete_timeline |
| `Action_None` | 243 | 250 | 8 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |
| `Action_None` | 263 | 268 | 6 | inferred_complete_timeline |
| `Action_None` | 271 | 291 | 21 | inferred_complete_timeline |
| `Action_None` | 294 | 329 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 115 | 33 | inferred_complete_timeline |
| `Action_None` | 118 | 262 | 145 | inferred_complete_timeline |
| `Action_None` | 265 | 329 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 194 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 128 | 46 | inferred_complete_timeline |
| `Action_None` | 130 | 198 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 204 | 122 | inferred_complete_timeline |
| `Action_None` | 208 | 211 | 4 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 329 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–141 | 142 | 2 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–329 | 322 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 19–176 | 130 | 9 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 90–329 | 209 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 102–110 | 9 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 102–329 | 216 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 103–329 | 210 | 6 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 112–114 | 3 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 121–168 | 47 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 123–329 | 205 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 124–173 | 40 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 124–329 | 194 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 152–329 | 178 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 174–329 | 149 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 187–329 | 143 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 191–260 | 67 | 4 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 192–241 | 7 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 195–329 | 134 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 210–233 | 24 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 218–271 | 43 | 3 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 224–251 | 9 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 242–329 | 88 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 282–326 | 32 | 5 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 285–329 | 34 | 3 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 287–329 | 30 | 3 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 288–301 | 8 | 3 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 322–324 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `5` (C): Annotated start 95 != Inferred start 99
- ❌ Missing segment for action `Action_BallCarry` on target `16` (Position_Unknown)

### Track Identity Issues

- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 94 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 58: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [83–98], lower_priority='Action_ZoneBlock' annotated_start=95, effective_Action_ZoneBlock_start=99.
- ⚠️ Segment 'Action_BallCarry' for track '15' has invalid range: start=122, end=110. Clamping end to start.
- ⚠️ Action 'Action_None' range [83-115] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-262] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-198] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-240] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-250] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-291] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-230] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-261] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [95-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-90] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-109] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-94] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '12' starts at frame 95, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [95-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-42] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-149] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-212] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-297] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-329] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [102-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-329] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-263] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-307] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-173] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-319] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-204] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-232] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-257] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-278] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-233] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-251] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-261] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-291] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-316] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-312] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>