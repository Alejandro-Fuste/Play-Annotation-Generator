# Play-Annotation-Generator Annotation Review — Counter_358

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_358`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `3` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | LT | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 186 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `3` | 184 | START | 184 | 199 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | LT | `15` | `14` | 187 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `4` | `3` | 187 | START | 207 | 223 |
| ✅ EXACT | `Action_PullBlock` | RG | `2` | `1` | 187 | START | 187 | 292 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `6` | `5` | 187 | START | 187 | 262 |
| ✅ EXACT | `Action_SnapReceive` | LT | `15` | `14` | 203 | END | 184 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 225 | START | 225 | 280 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 292 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–445
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_BallCarry` | 225 | 280 | 56 | inferred_complete_timeline |
| `Action_BallCarry` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 299 | 445 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 214 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–348
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 348 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_SnapReceive` | 184 | 203 | 20 | inferred_complete_timeline |
| `Action_None` | 204 | 240 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 230 | 47 | inferred_complete_timeline |
| `Action_None` | 238 | 260 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_BallSnap` | 184 | 199 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 207 | 223 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_PullBlock` | 187 | 292 | 106 | inferred_complete_timeline |
| `Action_None` | 293 | 350 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 187 | 262 | 76 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 265 | 267 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–366
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 263 | 80 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 366 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 228 | 45 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_None` | 241 | 249 | 9 | inferred_complete_timeline |
| `Action_None` | 253 | 258 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 195 | 12 | inferred_complete_timeline |
| `Action_None` | 229 | 249 | 21 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 194 | 11 | inferred_complete_timeline |
| `Action_None` | 198 | 479 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 225 | 42 | inferred_complete_timeline |
| `Action_None` | 253 | 280 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–379
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 229 | 46 | inferred_complete_timeline |
| `Action_None` | 231 | 238 | 8 | inferred_complete_timeline |
| `Action_None` | 241 | 263 | 23 | inferred_complete_timeline |
| `Action_None` | 265 | 297 | 33 | inferred_complete_timeline |
| `Action_None` | 299 | 379 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–288
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 288 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_None` | 184 | 267 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 219–278 | 54 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 227–393 | 167 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 229–391 | 106 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 246–409 | 159 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 275–395 | 118 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 292–479 | 181 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 294–390 | 97 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 296–354 | 59 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 307–419 | 107 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 311–399 | 89 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 336–383 | 48 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 422–479 | 51 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 431–479 | 49 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 440–479 | 40 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 464–479 | 16 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 465–479 | 15 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 473–479 | 7 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 479–479 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `15` (LT)
- ⚠️ `Action_DownBlock` for actor_track_id `4` (C): Annotated start 187 != Inferred start 207
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '1' (RG) duration 106 frames exceeds threshold 90 frames [start=187, end=292].
- ⚠️ Resolved action overlap for track '3' (C): higher_priority='Action_BallSnap' [184–203], lower_priority='Action_DownBlock' annotated_start=187, effective_Action_DownBlock_start=204.
- ⚠️ Segment 'Action_DownBlock' for track '14' has invalid range: start=187, end=183. Clamping end to start.
- ⚠️ Action 'Action_None' range [184-348] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-350] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-225] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-280] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [184-199] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [207-223] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [225-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-283] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [299-445] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [187-262] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [265-267] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-228] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-249] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-238] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-263] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-297] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-379] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-288] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-230] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-260] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-366] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-267] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-240] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-278] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-393] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-238] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-293] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-347] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-391] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-280] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-409] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-293] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-395] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-347] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-455] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-390] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-354] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-341] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-419] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-399] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-383] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-449] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-458] for track '28' has 1 frames without a visible bounding box.
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

</details>