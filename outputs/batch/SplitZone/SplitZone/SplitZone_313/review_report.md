# Play-Annotation-Generator Annotation Review — SplitZone_313

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_313`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 62
- **Validation Warnings:** 40
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE2 | defense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | LB2 | defense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | SAF1 | defense | `3` | `3` |
| ✅ EXACT | `Action_PressEdge` | DT2 | defense | `10` | `10` |
| ✅ EXACT | `Action_ReadEdgeDefender` | LB2 | defense | `13` | `13` |
| ✅ EXACT | `Action_BlockSecondLevel` | CB3 | defense | `6` | `6` |
| ✅ EXACT | `Action_BallCarry` | DT2 | defense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | LB2 | defense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 115 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 126 |
| ✅ EXACT | `Action_BallSnap` | DE2 | `7` | `7` | 120 | START | 120 | 128 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `15` | `15` | 127 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 127 | START | 194 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `18` | 127 | START | 199 | 199 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `20` | `19` | 127 | START | 204 | 204 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `4` | 127 | START | 127 | 172 |
| ✅ EXACT | `Action_SnapReceive` | LB2 | `13` | `13` | 128 | END | 120 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | SAF1 | `3` | `3` | 133 | START | 133 | 162 |
| ✅ EXACT | `Action_PressEdge` | DT2 | `10` | `10` | 138 | START | 138 | 153 |
| ✅ EXACT | `Action_ReadEdgeDefender` | LB2 | `13` | `13` | 142 | START | 142 | 147 |
| ✅ EXACT | `Action_BlockSecondLevel` | CB3 | `6` | `6` | 151 | START | 151 | 203 |
| ✅ EXACT | `Action_BallCarry` | DT2 | `10` | `10` | 166 | START | 166 | 219 |
| ✅ EXACT | `Action_Handoff` | LB2 | `13` | `13` | 166 | START | 166 | 329 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 188–329
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 188 | 329 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 329 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 329 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 271 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 222 | 103 | inferred_complete_timeline |
| `Action_None` | 230 | 291 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 199–329
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 199 | 199 | 1 | inferred_complete_timeline |
| `Action_None` | 200 | 329 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 115–122
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 115 | 122 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 194–329
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 194 | 194 | 1 | inferred_complete_timeline |
| `Action_None` | 195 | 329 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 204–236
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 204 | 204 | 1 | inferred_complete_timeline |
| `Action_None` | 205 | 236 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 172 | 46 | inferred_complete_timeline |
| `Action_None` | 173 | 208 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 226–230
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 226 | 230 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_BallSnap` | 120 | 128 | 9 | inferred_complete_timeline |
| `Action_None` | 129 | 268 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–307
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 134 | 15 | inferred_complete_timeline |
| `Action_None` | 137 | 143 | 7 | inferred_complete_timeline |
| `Action_None` | 146 | 161 | 16 | inferred_complete_timeline |
| `Action_None` | 167 | 307 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PressEdge` | 138 | 153 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 219 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 252 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_SnapReceive` | 120 | 128 | 9 | inferred_complete_timeline |
| `Action_None` | 129 | 141 | 13 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 142 | 147 | 6 | inferred_complete_timeline |
| `Action_None` | 148 | 165 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 166 | 329 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 143 | 24 | inferred_complete_timeline |
| `Action_None` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_None` | 150 | 161 | 12 | inferred_complete_timeline |
| `Action_None` | 166 | 179 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 329 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 151 | 203 | 53 | inferred_complete_timeline |
| `Action_None` | 204 | 329 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_SplitBlock` | 133 | 162 | 30 | inferred_complete_timeline |
| `Action_SplitBlock` | 165 | 175 | 11 | inferred_complete_timeline |
| `Action_None` | 176 | 329 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 143 | 24 | inferred_complete_timeline |
| `Action_None` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_None` | 165 | 297 | 133 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 247–329 | 80 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 285–329 | 45 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `15` (LG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (RG): Annotated start 127 != Inferred start 204
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 3 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 3 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 6 |
| Missing visible bounding boxes during action | 28 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '15' has invalid range: start=127, end=122. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '17' has invalid range: start=194, end=172. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '18' has invalid range: start=199, end=172. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '19' has invalid range: start=204, end=172. Clamping end to start.
- ⚠️ Action 'Action_None' range [120-271] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [133-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-161] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-252] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [138-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-291] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-143] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-297] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-161] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-307] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-236] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-277] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.

</details>