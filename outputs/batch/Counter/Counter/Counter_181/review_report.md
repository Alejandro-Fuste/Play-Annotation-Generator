# Play-Annotation-Generator Annotation Review — Counter_181

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_181`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT2 | defense | `13` | `12` |
| ✅ EXACT | `Action_PlaySideFakeStep` | DT1 | defense | `12` | `11` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT1 | defense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 6 | START | 6 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 6 | START | 6 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 6 | START | 6 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 6 | START | 6 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 6 | START | 6 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 6 | START | 6 | 182 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `16` | `15` | 183 | START | 183 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `16` | `15` | 186 | START | 186 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `20` | `19` | 186 | START | 186 | 202 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `21` | `20` | 186 | START | 186 | 277 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `22` | `21` | 186 | START | 186 | 277 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT2 | `13` | `12` | 186 | START | 186 | 251 |
| ✅ EXACT | `Action_PlaySideFakeStep` | DT1 | `12` | `11` | 194 | START | 194 | 203 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `18` | `17` | 194 | END | 183 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT1 | `12` | `11` | 204 | START | 204 | 359 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `18` | `17` | 204 | START | 204 | 389 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 277 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 6–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 182 | 177 | inferred_complete_timeline |
| `Action_None` | 183 | 207 | 25 | inferred_complete_timeline |
| `Action_None` | 209 | 338 | 130 | inferred_complete_timeline |
| `Action_None` | 347 | 389 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 6–369
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 182 | 177 | inferred_complete_timeline |
| `Action_None` | 183 | 359 | 177 | inferred_complete_timeline |
| `Action_None` | 362 | 363 | 2 | inferred_complete_timeline |
| `Action_None` | 365 | 369 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 182 | 177 | inferred_complete_timeline |
| `Action_None` | 183 | 307 | 125 | inferred_complete_timeline |
| `Action_None` | 310 | 327 | 18 | inferred_complete_timeline |
| `Action_None` | 330 | 376 | 47 | inferred_complete_timeline |
| `Action_None` | 378 | 383 | 6 | inferred_complete_timeline |
| `Action_None` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 6–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 182 | 177 | inferred_complete_timeline |
| `Action_None` | 183 | 389 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 6–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 182 | 177 | inferred_complete_timeline |
| `Action_None` | 183 | 389 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 6–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 182 | 177 | inferred_complete_timeline |
| `Action_None` | 183 | 280 | 98 | inferred_complete_timeline |
| `Action_None` | 282 | 291 | 10 | inferred_complete_timeline |
| `Action_None` | 310 | 389 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 6–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 182 | 177 | inferred_complete_timeline |
| `Action_None` | 183 | 257 | 75 | inferred_complete_timeline |
| `Action_None` | 261 | 264 | 4 | inferred_complete_timeline |
| `Action_None` | 266 | 389 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–389
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 193 | 188 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 194 | 203 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 204 | 359 | 156 | inferred_complete_timeline |
| `Action_BallCarry` | 374 | 389 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–278
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 185 | 180 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 186 | 251 | 66 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 273 | 277 | 5 | inferred_complete_timeline |
| `Action_None` | 278 | 278 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 6–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 182 | 177 | inferred_complete_timeline |
| `Action_None` | 183 | 389 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 182 | 177 | inferred_complete_timeline |
| `Action_None` | 183 | 389 | 207 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 6–306 | 299 | 3 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 6–385 | 380 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 6–389 | 384 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 6–332 | 325 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 6–243 | 203 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 6–222 | 217 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 6–389 | 384 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 6–361 | 356 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 6–389 | 338 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 6–389 | 384 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 6–389 | 384 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 221–232 | 5 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 227–389 | 163 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 248–389 | 142 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 300–329 | 19 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 322–386 | 65 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 324–325 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 331–389 | 44 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 350–351 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 353–389 | 35 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 360–389 | 30 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 382–386 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 364: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 364: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (Unknown) duration 92 frames exceeds threshold 90 frames [start=186, end=277].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (Unknown) duration 92 frames exceeds threshold 90 frames [start=186, end=277].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (Unknown) duration 92 frames exceeds threshold 90 frames [start=186, end=277].
- ⚠️ Action 'Action_None' range [183-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-289] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-306] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-385] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-369] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-307] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-327] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-376] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-383] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-280] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-291] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-338] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [204-359] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [186-251] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [255-256] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [263-264] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 278, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [278-278] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-326] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-197] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [209-211] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [233-238] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [242-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-222] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [204-389] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-361] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-307] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-329] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-386] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-343] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>