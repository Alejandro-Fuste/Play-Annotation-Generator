# Play-Annotation-Generator Annotation Review — SplitZone_54

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_54`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 1
- **Action Segments:** 98
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | TE2 | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 0 | START | 0 | 95 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 71 | START | 71 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 74 | START | 74 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `12` | 74 | START | 86 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `15` | 74 | START | 74 | 103 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `4` | 74 | START | 74 | 159 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 74 | START | 74 | 118 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `2` | `2` | 80 | START | 80 | 159 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 85 | END | 71 | 85 |
| ✅ EXACT | `Action_BlockSecondLevel` | TE2 | `9` | `9` | 96 | START | 96 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `7` | `7` | 111 | START | 111 | 120 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 159 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_SnapReceive` | 71 | 85 | 15 | inferred_complete_timeline |
| `Action_None` | 86 | 110 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 111 | 120 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 123 | 269 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 118 | 48 | inferred_complete_timeline |
| `Action_None` | 120 | 129 | 10 | inferred_complete_timeline |
| `Action_None` | 135 | 269 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_SplitBlock` | 80 | 159 | 80 | inferred_complete_timeline |
| `Action_None` | 160 | 177 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 96 | 159 | 64 | inferred_complete_timeline |
| `Action_None` | 160 | 160 | 1 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 269 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 103 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 123 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 145 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 176 | 17 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 246 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 118 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_BallSnap` | 71 | 85 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 102 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 108 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 159 | 86 | inferred_complete_timeline |
| `Action_None` | 160 | 188 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 159 | 86 | inferred_complete_timeline |
| `Action_None` | 160 | 188 | 29 | inferred_complete_timeline |
| `Action_None` | 191 | 242 | 52 | inferred_complete_timeline |
| `Action_None` | 247 | 269 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 218 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 153 | 83 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 117 | 47 | inferred_complete_timeline |
| `Action_None` | 124 | 129 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 139 | 9 | inferred_complete_timeline |
| `Action_None` | 143 | 227 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 269 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 169 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 70 | 67 | inferred_complete_timeline |
| `Action_None` | 71 | 177 | 107 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_None` | 192 | 244 | 53 | inferred_complete_timeline |
| `Action_None` | 247 | 269 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 269 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 152 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 269 | 199 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 70–154 | 83 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 105–175 | 71 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 110–269 | 156 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 125–211 | 85 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 150–152 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 159–239 | 81 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 184–269 | 86 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 184–269 | 86 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 198–238 | 13 | 6 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 203–266 | 57 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 211–214 | 4 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 250–269 | 20 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 250–260 | 11 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 253–267 | 13 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 259–266 | 8 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | 95 | 95 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [71–85], lower_priority='Action_ZoneBlock' annotated_start=74, effective_Action_ZoneBlock_start=86.
- ⚠️ Action 'Action_None' range [71-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-153] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-159] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-188] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-118] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-110] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [111-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 160, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [160-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-188] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-242] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-118] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-227] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-103] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-123] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-145] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-176] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-246] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-244] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-102] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-175] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-250] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-263] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-211] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-239] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-266] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-260] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-267] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-266] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>