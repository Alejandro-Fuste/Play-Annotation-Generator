# Play-Annotation-Generator Annotation Review — JetSweep_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_26`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 27
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | offense | `17` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | offense | `1` | `0` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `17` | `15` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `11` | `10` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `13` | `12` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `5` | `4` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `9` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `4` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | `17` | `15` | 14 | START | 141 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `9` | `8` | 140 | START | 140 | 150 |
| ✅ EXACT | `Action_LeadBlock` | RB | `10` | `9` | 140 | START | 140 | 185 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `10` | 147 | START | 147 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `12` | 147 | START | 147 | 150 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `13` | 147 | START | 147 | 159 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `4` | 147 | START | 147 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `8` | 147 | START | 153 | 177 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `0` | 152 | END | 140 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | `1` | `0` | 156 | START | 156 | 157 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `5` | `4` | 167 | START | 167 | 194 |
| ✅ EXACT | `Action_BallCarry` | WR | `17` | `15` | 169 | START | 169 | 177 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `11` | `10` | 194 | BOUNDARY | N/A | 194 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `13` | `12` | 194 | BOUNDARY | 164 | 194 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `14` | `13` | 194 | BOUNDARY | N/A | 194 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `5` | `4` | 194 | BOUNDARY | 167 | 194 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `9` | `8` | 194 | BOUNDARY | N/A | 194 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_SnapReceive` | 140 | 152 | 13 | inferred_complete_timeline |
| `Action_None` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_Toss` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_Toss` | 160 | 168 | 9 | inferred_complete_timeline |
| `Action_None` | 169 | 199 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_LeadBlock` | 140 | 185 | 46 | inferred_complete_timeline |
| `Action_None` | 195 | 214 | 20 | inferred_complete_timeline |
| `Action_None` | 219 | 223 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 174 | 35 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 141–177
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 141 | 152 | 12 | inferred_complete_timeline |
| `Action_JetMotion` | 155 | 168 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 177 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 150 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 194 | 31 | inferred_complete_timeline |
| `Action_None` | 195 | 221 | 27 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 146 | 126 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 166 | 20 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 167 | 194 | 28 | inferred_complete_timeline |
| `Action_None` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_BallSnap` | 140 | 150 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 152 | 152 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 177 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 182 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 190 | 44 | inferred_complete_timeline |
| `Action_None` | 242 | 286 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 146 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 159 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 151 | 242 | 92 | inferred_complete_timeline |
| `Action_None` | 244 | 262 | 19 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_None` | 270 | 272 | 3 | inferred_complete_timeline |
| `Action_None` | 275 | 280 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 162 | 23 | inferred_complete_timeline |
| `Action_None` | 170 | 195 | 26 | inferred_complete_timeline |
| `Action_None` | 231 | 299 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 188 | 49 | inferred_complete_timeline |
| `Action_None` | 191 | 217 | 27 | inferred_complete_timeline |
| `Action_None` | 220 | 228 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 202 | 63 | inferred_complete_timeline |
| `Action_None` | 278 | 296 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 155 | 16 | inferred_complete_timeline |
| `Action_None` | 162 | 299 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 121–180 | 60 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 157–164 | 8 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 160–270 | 96 | 6 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 184–195 | 12 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 191–227 | 37 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 193–254 | 47 | 4 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 197–220 | 24 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 200–299 | 100 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 222–296 | 75 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 227–247 | 21 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 232–299 | 65 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 232–299 | 68 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 272–299 | 28 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 282–299 | 17 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 290–299 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallSnap` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [140–152], lower_priority='Action_ZoneBlock' annotated_start=147, effective_Action_ZoneBlock_start=153.
- ⚠️ Action 'Action_Toss' range [156-157] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-199] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-188] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-217] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [167-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-296] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-242] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-262] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-280] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [140-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [140-185] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-214] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-286] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-195] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-146] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-221] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [141-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-177] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-199] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-233] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-270] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-227] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-231] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-220] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-296] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-247] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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