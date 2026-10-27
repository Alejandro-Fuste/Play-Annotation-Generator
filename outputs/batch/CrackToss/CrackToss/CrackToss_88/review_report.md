# Play-Annotation-Generator Annotation Review — CrackToss_88

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_88`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 172
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `33` | `26` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `37` | `29` |
| ✅ EXACT | `Action_BallCarry` | CB1 | defense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `17` | `Group` | 0 | START | 0 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `3` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 207 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `33` | `26` | 208 | START | 214 | 214 |
| ✅ EXACT | `Action_PullBlock` | RT | `1` | `0` | 211 | START | 211 | 254 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 212 | END | 208 | 212 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 221 | START | 221 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `37` | `29` | 226 | START | 226 | 235 |
| ✅ EXACT | `Action_BallCarry` | CB1 | `4` | `3` | 239 | START | 239 | 449 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 293 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–411
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_SnapReceive` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_None` | 213 | 220 | 8 | inferred_complete_timeline |
| `Action_Toss` | 221 | 238 | 18 | inferred_complete_timeline |
| `Action_None` | 239 | 411 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 207 | 130 | inferred_complete_timeline |
| `Action_None` | 208 | 333 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_None` | 208 | 241 | 34 | inferred_complete_timeline |
| `Action_None` | 243 | 283 | 41 | inferred_complete_timeline |
| `Action_None` | 291 | 355 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–360
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_None` | 208 | 255 | 48 | inferred_complete_timeline |
| `Action_None` | 258 | 337 | 80 | inferred_complete_timeline |
| `Action_None` | 341 | 342 | 2 | inferred_complete_timeline |
| `Action_None` | 358 | 360 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–344
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 207 | 120 | inferred_complete_timeline |
| `Action_None` | 208 | 344 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_PullBlock` | 211 | 254 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 90 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 207 | 114 | inferred_complete_timeline |
| `Action_None` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 259 | 267 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_None` | 214 | 236 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–13
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_None` | 208 | 217 | 10 | inferred_complete_timeline |
| `Action_None` | 240 | 243 | 4 | inferred_complete_timeline |
| `Action_None` | 252 | 254 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–342
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_None` | 208 | 342 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–345
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_None` | 208 | 345 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 238 | 239 | inferred_complete_timeline |
| `Action_BallCarry` | 239 | 449 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–410
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_None` | 208 | 410 | 203 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–400 | 398 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–242 | 236 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 3–37 | 26 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 25–215 | 159 | 8 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 61–140 | 36 | 4 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 106–258 | 73 | 7 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 110–115 | 6 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 190–194 | 5 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 193–241 | 49 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 209–225 | 17 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 214–348 | 135 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 223–258 | 36 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 225–256 | 28 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 226–339 | 102 | 4 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 230–245 | 16 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 238–240 | 3 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 244–248 | 5 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 255–310 | 56 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 259–262 | 4 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 262–294 | 31 | 2 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 262–296 | 35 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 265–337 | 72 | 2 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 287–290 | 4 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 294–449 | 154 | 2 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 296–446 | 151 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 296–395 | 57 | 3 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 311–449 | 131 | 2 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 331–396 | 66 | 1 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 333–449 | 117 | 1 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 341–344 | 4 | 1 | Undefined position; Undefined team |
| `47` | `71` | Position_Unknown | Team_Unknown | 343–449 | 107 | 1 | Undefined position; Undefined team |
| `48` | `73` | Position_Unknown | Team_Unknown | 346–449 | 104 | 1 | Undefined position; Undefined team |
| `49` | `76` | Position_Unknown | Team_Unknown | 421–445 | 25 | 1 | Undefined position; Undefined team |
| `50` | `77` | Position_Unknown | Team_Unknown | 434–443 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `33` (Position_Unknown): Annotated start 208 != Inferred start 214
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `37` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 35 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 35 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 70 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 178: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '26' has invalid range: start=214, end=212. Clamping end to start.
- ⚠️ Action 'Action_PullBlock' range [211-254] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-333] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [239-449] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-344] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-207] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-267] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-255] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-337] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-360] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-410] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-231] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-400] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-342] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-192] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-207] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-242] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-411] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-241] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-283] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-355] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-345] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-23] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-28] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-37] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-77] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-95] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-215] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-66] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-85] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-115] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-176] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-115] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-241] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-348] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-258] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-231] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-250] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [226-235] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-306] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-339] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-245] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-248] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-310] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-290] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-296] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-277] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-337] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-335] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-449] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-446] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-335] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-351] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-395] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-318] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-449] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-396] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-344] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-449] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-445] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-443] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.

</details>