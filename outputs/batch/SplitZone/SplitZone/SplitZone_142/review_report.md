# Play-Annotation-Generator Annotation Review — SplitZone_142

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_142`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_BlockSecondLevel` | TE1 | offense | `4` | `4` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `12` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 23 | START | 24 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 23 | START | 24 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 23 | START | 24 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 23 | START | 24 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 23 | START | 24 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 23 | START | 24 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 23 | START | 24 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 23 | START | 24 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 23 | START | 24 | 73 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `5` | 71 | START | 71 | 78 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `10` | `10` | 74 | START | 74 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `5` | `5` | 74 | START | 79 | 160 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `6` | 74 | START | 74 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `8` | 74 | START | 74 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `9` | 74 | START | 74 | 93 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 78 | END | 71 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `7` | `7` | 79 | START | 79 | 152 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `17` | 90 | START | 90 | 106 |
| ✅ EXACT | `Action_BlockSecondLevel` | TE1 | `4` | `4` | 94 | START | 94 | 137 |
| ✅ EXACT | `Action_BallCarry` | RB | `12` | `12` | 107 | START | 107 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 229 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 24–245
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 36 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 70 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 71 | 78 | 8 | inferred_complete_timeline |
| `Action_None` | 79 | 89 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 90 | 106 | 17 | inferred_complete_timeline |
| `Action_None` | 107 | 245 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 24–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 106 | 83 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 269 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 24–137
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 93 | 70 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 94 | 137 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 24–161
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 78 | 55 | inferred_complete_timeline |
| `Action_SplitBlock` | 79 | 152 | 74 | inferred_complete_timeline |
| `Action_SplitBlock` | 160 | 161 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 24–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 73 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 229 | 156 | inferred_complete_timeline |
| `Action_None` | 230 | 269 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 24–93
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 73 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 93 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 24–269
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 70 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 71 | 78 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 160 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 229 | 62 | inferred_complete_timeline |
| `Action_None` | 230 | 269 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 24–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 73 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 110 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 229 | 116 | inferred_complete_timeline |
| `Action_None` | 230 | 269 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 24–240
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 73 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 229 | 156 | inferred_complete_timeline |
| `Action_None` | 230 | 240 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 24–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 70 | 47 | inferred_complete_timeline |
| `Action_None` | 71 | 269 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 24–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 70 | 47 | inferred_complete_timeline |
| `Action_None` | 71 | 269 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 24–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 70 | 47 | inferred_complete_timeline |
| `Action_None` | 71 | 269 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 24–269
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 70 | 47 | inferred_complete_timeline |
| `Action_None` | 71 | 143 | 73 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 269 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 24–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 70 | 47 | inferred_complete_timeline |
| `Action_None` | 71 | 269 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 24–117
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 70 | 47 | inferred_complete_timeline |
| `Action_None` | 71 | 117 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 24–123
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 70 | 47 | inferred_complete_timeline |
| `Action_None` | 71 | 123 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 24–220
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 70 | 47 | inferred_complete_timeline |
| `Action_None` | 71 | 202 | 132 | inferred_complete_timeline |
| `Action_None` | 205 | 217 | 13 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 24–249
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 70 | 47 | inferred_complete_timeline |
| `Action_None` | 71 | 220 | 150 | inferred_complete_timeline |
| `Action_None` | 246 | 249 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 66–269 | 180 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 88–114 | 7 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 97–167 | 69 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 105–269 | 146 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 124–136 | 9 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 124–269 | 135 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 136–269 | 134 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 167–269 | 103 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 179–269 | 91 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 202–269 | 68 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 208–269 | 62 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 236–265 | 12 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 252–269 | 18 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (C) duration 156 frames exceeds threshold 90 frames [start=74, end=229].
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [71–78], lower_priority='Action_ZoneBlock' annotated_start=74, effective_Action_ZoneBlock_start=79.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 156 frames exceeds threshold 90 frames [start=74, end=229].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 156 frames exceeds threshold 90 frames [start=74, end=229].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (LT) duration 156 frames exceeds threshold 90 frames [start=74, end=229].
- ⚠️ Action 'Action_None' range [71-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [94-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-229] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-240] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [79-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [160-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-217] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-143] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-36] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-104] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-167] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-230] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-244] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '32' has 1 frames without a visible bounding box.
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

</details>