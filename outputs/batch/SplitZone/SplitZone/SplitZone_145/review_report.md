# Play-Annotation-Generator Annotation Review — SplitZone_145

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_145`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `8` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 17 | START | 12 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 17 | START | 12 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 17 | START | 12 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 17 | START | 12 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 17 | START | 12 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `17` | `Group` | 17 | START | 12 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 17 | START | 12 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 17 | START | 12 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 17 | START | 12 | 118 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 118 | START | 118 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `4` | `4` | 119 | START | 119 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `10` | 121 | START | 121 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `15` | 121 | START | 121 | 140 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `16` | `16` | 121 | START | 121 | 152 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `21` | `21` | 121 | START | 128 | 144 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 127 | END | 118 | 127 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `13` | 134 | START | 134 | 147 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `21` | `21` | 145 | START | 145 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `8` | `8` | 148 | START | 148 | 174 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 209 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 12–289
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_SnapReceive` | 118 | 127 | 10 | inferred_complete_timeline |
| `Action_None` | 128 | 133 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 134 | 147 | 14 | inferred_complete_timeline |
| `Action_None` | 148 | 289 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 12–301
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 301 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 12–308
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 308 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–318
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 118 | 107 | inferred_complete_timeline |
| `Action_SplitBlock` | 119 | 165 | 47 | inferred_complete_timeline |
| `Action_SplitBlock` | 170 | 174 | 5 | inferred_complete_timeline |
| `Action_SplitBlock` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 206 | 209 | 4 | inferred_complete_timeline |
| `Action_None` | 210 | 318 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 12–292
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 222 | 105 | inferred_complete_timeline |
| `Action_None` | 224 | 292 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 12–296
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 120 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 173 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 209 | 34 | inferred_complete_timeline |
| `Action_None` | 210 | 296 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 12–151
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_BallSnap` | 118 | 127 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 144 | 17 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 145 | 151 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 12–152
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 120 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 152 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 12–223
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 120 | 109 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 140 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 198 | 43 | inferred_complete_timeline |
| `Action_None` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_None` | 219 | 223 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–303
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 139 | 22 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 303 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 12–168
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 161 | 44 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 12–301
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 143 | 26 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 301 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 12–298
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 136 | 19 | inferred_complete_timeline |
| `Action_None` | 139 | 208 | 70 | inferred_complete_timeline |
| `Action_None` | 210 | 298 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–207
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 207 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–181
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 154 | 37 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–303
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 303 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–285
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 285 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 12–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 329 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–313
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 304 | 187 | inferred_complete_timeline |
| `Action_None` | 308 | 313 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 12–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 321 | 204 | inferred_complete_timeline |
| `Action_None` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 12–315 | 301 | 3 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 12–329 | 316 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 162–329 | 168 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 170–305 | 134 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 171–289 | 118 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 188–295 | 107 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 221–223 | 3 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 226–294 | 48 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 227–288 | 62 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 233–290 | 58 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 244–246 | 3 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 276–285 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `21` (C): Annotated start 121 != Inferred start 128
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 292: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ Row 292: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [118–127], lower_priority='Action_ZoneBlock' annotated_start=121, effective_Action_ZoneBlock_start=128.
- ⚠️ Action 'Action_None' range [118-308] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-315] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-304] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-313] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [119-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [170-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [199-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-318] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-303] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [148-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [176-288] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-301] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-173] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-296] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-285] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-303] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-289] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-301] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-136] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-321] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-222] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-292] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [118-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [145-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-305] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-289] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-285] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-295] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-258] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-294] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-288] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-285] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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