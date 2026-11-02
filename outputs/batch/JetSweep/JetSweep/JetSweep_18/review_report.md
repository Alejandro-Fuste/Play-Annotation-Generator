# Play-Annotation-Generator Annotation Review — JetSweep_18

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `JetSweep_18`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 110
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `2` | `1` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `2` | `1` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `10` | `9` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `2` | `1` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `3` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `1` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 197 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `18` | `17` | 130 | START | 130 | 149 |
| ✅ EXACT | `Action_LeadBlock` | TE | `4` | `3` | 130 | START | 130 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `1` | `0` | 130 | START | 130 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 130 | START | 130 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `11` | 130 | START | 130 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `1` | 130 | START | 130 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `2` | 130 | START | 130 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 138 | END | 138 | 138 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 144 | START | 144 | 149 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `18` | `17` | 150 | START | 150 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `2` | `1` | 164 | START | 164 | 174 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `2` | `1` | 185 | BOUNDARY | 179 | 185 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `10` | `9` | 185 | BOUNDARY | 163 | 185 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `12` | `11` | 185 | BOUNDARY | N/A | 185 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `2` | `1` | 185 | BOUNDARY | 179 | 185 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `3` | `2` | 185 | BOUNDARY | 158 | 185 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 22 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 98 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 137 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 138 | 138 | 1 | inferred_complete_timeline |
| `Action_None` | 139 | 143 | 5 | inferred_complete_timeline |
| `Action_Toss` | 144 | 149 | 6 | inferred_complete_timeline |
| `Action_None` | 150 | 159 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_LeadBlock` | 130 | 165 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 150 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 185 | 28 | inferred_complete_timeline |
| `Action_None` | 186 | 223 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 171 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 163 | 34 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 164 | 174 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 179 | 185 | 7 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 207 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 155 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 157 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 185 | 23 | inferred_complete_timeline |
| `Action_None` | 186 | 188 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 269 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 237 | 183 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 257 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 269 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 169 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 188 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 145 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 178 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 219 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 3–170 | 156 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 5–149 | 125 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 101–214 | 114 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 130–156 | 27 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 135–180 | 44 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 143–212 | 48 | 6 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 159–258 | 90 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 177–196 | 20 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 192–200 | 9 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 195–212 | 18 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 200–203 | 4 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 202–269 | 67 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 210–269 | 52 | 4 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 225–229 | 5 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 226–269 | 44 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 233–258 | 22 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 241–246 | 6 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 247–269 | 23 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `RT` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BallSnap' at frame 124 targets track ID '[?]', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 37: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_ZoneBlock' range [130-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-163] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [164-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-207] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [130-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-169] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-188] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-22] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-98] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [144-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-237] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-23] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-138] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-214] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-163] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-169] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-197] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-171] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-243] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-196] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-234] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-251] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-229] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-250] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-246] for track '30' has 1 frames without a visible bounding box.
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

</details>