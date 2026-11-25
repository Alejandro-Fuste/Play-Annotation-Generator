# Play-Annotation-Generator Annotation Review — InsideZoneRead_178

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_178`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | CB5 | defense | `5` | `4` |
| ✅ EXACT | `Action_ReadDefender` | CB5 | defense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | CB5 | defense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | DT1 | defense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 11 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 11 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 11 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `18` | `Group` | 0 | START | 11 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 11 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 11 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 11 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 11 | 147 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 146 | START | 146 | 157 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `9` | 148 | START | 148 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 148 | START | 158 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 148 | START | 148 | 231 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `19` | 148 | START | 148 | 231 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 148 | START | 148 | 231 |
| ✅ EXACT | `Action_SnapReceive` | CB5 | `5` | `4` | 157 | END | 146 | 157 |
| ✅ EXACT | `Action_ReadDefender` | CB5 | `5` | `4` | 160 | START | 160 | 174 |
| ✅ EXACT | `Action_Handoff` | CB5 | `5` | `4` | 175 | START | 175 | 185 |
| ✅ EXACT | `Action_BallCarry` | DT1 | `9` | `8` | 186 | START | 186 | 389 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 231 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 11–313
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 146 | 313 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 11–331
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 146 | 331 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 11–294
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 146 | 219 | 74 | inferred_complete_timeline |
| `Action_None` | 222 | 294 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 11–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 147 | 137 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 231 | 84 | inferred_complete_timeline |
| `Action_None` | 232 | 389 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 11–303
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 147 | 137 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 231 | 84 | inferred_complete_timeline |
| `Action_None` | 232 | 303 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 11–389
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_BallSnap` | 146 | 157 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 203 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 231 | 22 | inferred_complete_timeline |
| `Action_None` | 232 | 251 | 20 | inferred_complete_timeline |
| `Action_None` | 253 | 256 | 4 | inferred_complete_timeline |
| `Action_None` | 268 | 389 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 11–211
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 147 | 137 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 211 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 11–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 147 | 137 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 231 | 84 | inferred_complete_timeline |
| `Action_None` | 232 | 343 | 112 | inferred_complete_timeline |
| `Action_None` | 348 | 389 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 11–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 146 | 200 | 55 | inferred_complete_timeline |
| `Action_None` | 202 | 262 | 61 | inferred_complete_timeline |
| `Action_None` | 264 | 348 | 85 | inferred_complete_timeline |
| `Action_None` | 350 | 389 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 146 | 389 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 11–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 185 | 175 | inferred_complete_timeline |
| `Action_BallCarry` | 186 | 389 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 11–377
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 146 | 211 | 66 | inferred_complete_timeline |
| `Action_None` | 213 | 361 | 149 | inferred_complete_timeline |
| `Action_None` | 376 | 377 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 11–312
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 146 | 312 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 11–209
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 146 | 209 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 11–253
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 146 | 253 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 11–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 146 | 389 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 11–288
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 146 | 231 | 86 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 241 | 245 | 5 | inferred_complete_timeline |
| `Action_None` | 250 | 278 | 29 | inferred_complete_timeline |
| `Action_None` | 283 | 288 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 11–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_None` | 146 | 317 | 172 | inferred_complete_timeline |
| `Action_None` | 319 | 389 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 11–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 145 | 135 | inferred_complete_timeline |
| `Action_SnapReceive` | 146 | 157 | 12 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 160 | 174 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 175 | 185 | 11 | inferred_complete_timeline |
| `Action_None` | 186 | 389 | 204 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 11–297 | 287 | 2 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 11–387 | 376 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 11–389 | 379 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 72–73 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 221–321 | 101 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 222–298 | 66 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 278–279 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 293–389 | 88 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 321–389 | 69 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 378–389 | 12 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 381–389 | 9 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 387–389 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 356: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ Row 356: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [146–157], lower_priority='Action_ZoneBlock' annotated_start=148, effective_Action_ZoneBlock_start=158.
- ⚠️ Action 'Action_None' range [146-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-297] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-331] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-317] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [186-389] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-211] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-381] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-387] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-312] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-278] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-288] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-313] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-262] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-348] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-389] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-219] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-294] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-303] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-343] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-361] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-321] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-270] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-298] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-311] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-389] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_178'; source metadata written as null.

</details>