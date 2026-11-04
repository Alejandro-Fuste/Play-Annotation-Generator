# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_74

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_74`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `29` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `29` | `23` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `29` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `0` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `1` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `10` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `11` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `12` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `14` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `2` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `6` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `8` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `10` | `10` | 6 | START | 6 | 60 |
| ✅ EXACT | `Action_KickBall` | Kicker | `10` | `10` | 61 | START | 61 | 65 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `29` | `23` | 181 | START | 181 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `29` | `23` | 199 | START | 203 | 253 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `29` | `23` | 538 | START | 538 | 539 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–470
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_KickApproach` | 6 | 60 | 55 | inferred_complete_timeline |
| `Action_KickBall` | 61 | 65 | 5 | inferred_complete_timeline |
| `Action_None` | 66 | 470 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 191 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–402
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 164 | 159 | inferred_complete_timeline |
| `Action_None` | 166 | 189 | 24 | inferred_complete_timeline |
| `Action_None` | 191 | 402 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–404
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 404 | 399 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 539 | 534 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 539 | 534 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 180 | 175 | inferred_complete_timeline |
| `Action_None` | 182 | 203 | 22 | inferred_complete_timeline |
| `Action_None` | 222 | 231 | 10 | inferred_complete_timeline |
| `Action_None` | 233 | 253 | 21 | inferred_complete_timeline |
| `Action_None` | 259 | 263 | 5 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 164 | 159 | inferred_complete_timeline |
| `Action_None` | 166 | 177 | 12 | inferred_complete_timeline |
| `Action_None` | 187 | 192 | 6 | inferred_complete_timeline |
| `Action_None` | 195 | 217 | 23 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 274 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–375
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 165 | 160 | inferred_complete_timeline |
| `Action_None` | 167 | 174 | 8 | inferred_complete_timeline |
| `Action_None` | 176 | 234 | 59 | inferred_complete_timeline |
| `Action_None` | 242 | 274 | 33 | inferred_complete_timeline |
| `Action_None` | 292 | 375 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–522
- **Visible Samples:** 523

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 522 | 517 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 539 | 534 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–446
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 192 | 187 | inferred_complete_timeline |
| `Action_None` | 223 | 446 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 177 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–508
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 508 | 503 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–537
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 204 | 199 | inferred_complete_timeline |
| `Action_None` | 218 | 537 | 320 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–430 | 427 | 3 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–175 | 176 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 54–55 | 2 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 99–237 | 131 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 106–231 | 126 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 108–440 | 332 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 123–240 | 118 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 125–128 | 4 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 146–539 | 388 | 7 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 185–408 | 183 | 9 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 221–445 | 225 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 225–539 | 314 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 247–539 | 293 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 254–401 | 148 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 269–421 | 153 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 286–389 | 102 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 295–297 | 3 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 295–421 | 115 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 319–442 | 109 | 5 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 372–373 | 2 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 395–412 | 16 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 422–442 | 16 | 2 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 439–480 | 37 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `29` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 150: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action 'Action_None' range [6-191] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-203] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-231] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-253] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-189] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-402] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-192] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-446] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-297] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-430] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-404] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-204] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-537] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-539] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-508] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-470] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-164] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-177] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-274] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-539] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-165] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-174] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-234] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-274] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-375] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-522] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-213] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-237] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-231] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-440] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-240] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-253] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [255-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-228] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-291] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-408] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-445] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-299] for track '26' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-539] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-401] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-421] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-298] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-389] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-309] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-421] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-398] for track '33' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-417] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-442] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-399] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-412] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-428] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-442] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-462] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-472] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-480] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>