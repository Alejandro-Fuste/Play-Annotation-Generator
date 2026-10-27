# Play-Annotation-Generator Annotation Review — Counter_372

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_372`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 66
- **Ball Tracks:** 1
- **Action Segments:** 148
- **Validation Warnings:** 229
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 129
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `12` | `11` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_PullBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 2 | START | 2 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 2 | START | 2 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 2 | START | 2 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 2 | START | 2 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 2 | START | 2 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 2 | START | 2 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 2 | START | 2 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 2 | START | 2 | 40 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 116 | START | 116 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `12` | `11` | 119 | START | 119 | 156 |
| ✅ EXACT | `Action_DownBlock` | LT | `13` | `12` | 119 | START | 119 | 156 |
| ⚠️ START CHANGED | `Action_PullBlock` | C | `11` | `10` | 119 | START | 130 | 143 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `4` | `3` | 119 | START | 119 | 156 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 129 | END | 116 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `14` | `13` | 138 | START | 138 | 149 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 156 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 2–265
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 115 | 114 | inferred_complete_timeline |
| `Action_SnapReceive` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_None` | 130 | 137 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 149 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 152 | 194 | 43 | inferred_complete_timeline |
| `Action_BallCarry` | 201 | 265 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 2–207
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 40 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 115 | 72 | inferred_complete_timeline |
| `Action_None` | 116 | 207 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 2–208
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 115 | 114 | inferred_complete_timeline |
| `Action_None` | 116 | 208 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 2–199
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 118 | 117 | inferred_complete_timeline |
| `Action_DownBlock` | 119 | 156 | 38 | inferred_complete_timeline |
| `Action_None` | 157 | 199 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 2–167
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 118 | 117 | inferred_complete_timeline |
| `Action_DownBlock` | 119 | 156 | 38 | inferred_complete_timeline |
| `Action_None` | 157 | 157 | 1 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_None` | 165 | 167 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–143
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 115 | 114 | inferred_complete_timeline |
| `Action_BallSnap` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 130 | 143 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 2–209
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 115 | 114 | inferred_complete_timeline |
| `Action_None` | 116 | 201 | 86 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 2–445
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 118 | 117 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 119 | 156 | 38 | inferred_complete_timeline |
| `Action_None` | 158 | 190 | 33 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 434 | 231 | inferred_complete_timeline |
| `Action_None` | 440 | 442 | 3 | inferred_complete_timeline |
| `Action_None` | 444 | 445 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 2–187
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 115 | 114 | inferred_complete_timeline |
| `Action_None` | 116 | 164 | 49 | inferred_complete_timeline |
| `Action_None` | 168 | 187 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 2–255
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 115 | 114 | inferred_complete_timeline |
| `Action_None` | 116 | 255 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 2–253
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 115 | 114 | inferred_complete_timeline |
| `Action_None` | 116 | 217 | 102 | inferred_complete_timeline |
| `Action_None` | 228 | 253 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 2–250
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 115 | 114 | inferred_complete_timeline |
| `Action_None` | 116 | 184 | 69 | inferred_complete_timeline |
| `Action_None` | 187 | 192 | 6 | inferred_complete_timeline |
| `Action_None` | 195 | 203 | 9 | inferred_complete_timeline |
| `Action_None` | 205 | 250 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 2–262
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 115 | 114 | inferred_complete_timeline |
| `Action_None` | 116 | 262 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 2–240
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 115 | 114 | inferred_complete_timeline |
| `Action_None` | 116 | 240 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–154
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 115 | 114 | inferred_complete_timeline |
| `Action_None` | 116 | 154 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `10` | Position_Unknown | Team_Unknown | 2–227 | 226 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 120–280 | 81 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 138–182 | 45 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 186–277 | 82 | 4 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 187–209 | 23 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 202–205 | 4 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 211–246 | 36 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 211–297 | 87 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 211–318 | 108 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 212–270 | 59 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 213–449 | 185 | 10 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 213–214 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 229–449 | 221 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 229–242 | 14 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 230–236 | 7 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 287–292 | 5 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 289–295 | 7 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 298–308 | 8 | 3 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 303–308 | 6 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 303–307 | 5 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 308–351 | 21 | 6 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 312–353 | 42 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 320–376 | 27 | 5 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 322–362 | 17 | 4 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 325–338 | 13 | 2 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 329–375 | 30 | 5 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 334–335 | 2 | 1 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 337–449 | 113 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 337–345 | 9 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 345–399 | 32 | 4 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 345–346 | 2 | 1 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 350–378 | 28 | 2 | Undefined position; Undefined team |
| `50` | `71` | Position_Unknown | Team_Unknown | 350–361 | 10 | 3 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 352–358 | 6 | 2 | Undefined position; Undefined team |
| `52` | `74` | Position_Unknown | Team_Unknown | 355–392 | 27 | 4 | Undefined position; Undefined team |
| `53` | `76` | Position_Unknown | Team_Unknown | 362–449 | 88 | 1 | Undefined position; Undefined team |
| `54` | `77` | Position_Unknown | Team_Unknown | 367–381 | 15 | 1 | Undefined position; Undefined team |
| `55` | `83` | Position_Unknown | Team_Unknown | 380–449 | 70 | 1 | Undefined position; Undefined team |
| `56` | `84` | Position_Unknown | Team_Unknown | 382–386 | 5 | 1 | Undefined position; Undefined team |
| `57` | `89` | Position_Unknown | Team_Unknown | 411–415 | 5 | 1 | Undefined position; Undefined team |
| `58` | `90` | Position_Unknown | Team_Unknown | 414–422 | 4 | 2 | Undefined position; Undefined team |
| `59` | `92` | Position_Unknown | Team_Unknown | 417–419 | 3 | 1 | Undefined position; Undefined team |
| `60` | `93` | Position_Unknown | Team_Unknown | 419–426 | 8 | 1 | Undefined position; Undefined team |
| `61` | `96` | Position_Unknown | Team_Unknown | 421–426 | 6 | 1 | Undefined position; Undefined team |
| `62` | `97` | Position_Unknown | Team_Unknown | 423–427 | 5 | 1 | Undefined position; Undefined team |
| `63` | `98` | Position_Unknown | Team_Unknown | 424–447 | 4 | 2 | Undefined position; Undefined team |
| `64` | `101` | Position_Unknown | Team_Unknown | 428–430 | 3 | 1 | Undefined position; Undefined team |
| `65` | `103` | Position_Unknown | Team_Unknown | 433–435 | 3 | 1 | Undefined position; Undefined team |
| `66` | `104` | Position_Unknown | Team_Unknown | 442–448 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | 2 | 112 | 106 | 95.5% | 37, 70–73 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `11` (C): Annotated start 119 != Inferred start 130
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 51 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 51 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 102 |
| Missing visible bounding boxes during action | 125 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [116–129], lower_priority='Action_PullBlock' annotated_start=119, effective_Action_PullBlock_start=130.
- ⚠️ Action 'Action_None' range [116-240] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-255] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [119-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-190] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-434] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-442] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-40] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-227] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [130-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [119-156] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 157, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [157-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [152-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [201-265] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-201] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-280] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-182] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-277] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-209] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-246] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-297] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-318] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-270] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-346] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-353] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-364] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-382] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-417] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-429] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-437] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-449] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-242] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-236] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-295] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-305] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-308] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-353] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-329] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-373] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-332] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-358] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-334] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-337] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-367] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-375] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-345] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-347] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-371] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-399] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-365] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-378] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-357] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-373] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-392] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-381] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-386] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-419] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-426] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-426] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-427] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-430] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-435] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-448] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.

</details>