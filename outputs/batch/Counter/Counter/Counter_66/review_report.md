# Play-Annotation-Generator Annotation Review — Counter_66

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_66`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 44
- **Ball Tracks:** 3
- **Action Segments:** 117
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT | defense | `5` | `4` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | DT | defense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT | defense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 169 |
| ✅ EXACT | `Action_BallSnap` | DT | `5` | `4` | 168 | START | 168 | 169 |
| ✅ EXACT | `Action_DownBlock` | LG | `14` | `13` | 170 | START | 170 | 268 |
| ✅ EXACT | `Action_DownBlock` | DT | `5` | `4` | 170 | START | 170 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `4` | `3` | 170 | START | 170 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | `11` | `10` | 170 | START | 170 | 182 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 183 | END | 168 | 183 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 201 | START | 201 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT | `5` | `4` | 204 | START | 223 | 226 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 268 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 167 | 82 | inferred_complete_timeline |
| `Action_SnapReceive` | 168 | 183 | 16 | inferred_complete_timeline |
| `Action_None` | 184 | 200 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 284 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 167 | 78 | inferred_complete_timeline |
| `Action_None` | 168 | 186 | 19 | inferred_complete_timeline |
| `Action_None` | 190 | 479 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 170 | 182 | 13 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 184 | 199 | 16 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 231 | 246 | 16 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 251 | 268 | 18 | inferred_complete_timeline |
| `Action_None` | 269 | 325 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–315
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 243 | 76 | inferred_complete_timeline |
| `Action_None` | 248 | 267 | 20 | inferred_complete_timeline |
| `Action_None` | 269 | 315 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 226 | 59 | inferred_complete_timeline |
| `Action_None` | 254 | 258 | 5 | inferred_complete_timeline |
| `Action_None` | 262 | 268 | 7 | inferred_complete_timeline |
| `Action_None` | 274 | 277 | 4 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_DownBlock` | 170 | 268 | 99 | inferred_complete_timeline |
| `Action_None` | 269 | 275 | 7 | inferred_complete_timeline |
| `Action_None` | 280 | 328 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–334
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 167 | 87 | inferred_complete_timeline |
| `Action_None` | 168 | 334 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_PullBlock` | 170 | 195 | 26 | inferred_complete_timeline |
| `Action_PullBlock` | 205 | 206 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 10 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 33 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 167 | 133 | inferred_complete_timeline |
| `Action_None` | 168 | 236 | 69 | inferred_complete_timeline |
| `Action_None` | 238 | 307 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 198 | 31 | inferred_complete_timeline |
| `Action_None` | 201 | 435 | 235 | inferred_complete_timeline |
| `Action_None` | 437 | 479 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 167 | 86 | inferred_complete_timeline |
| `Action_None` | 168 | 209 | 42 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 75 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 167 | 81 | inferred_complete_timeline |
| `Action_BallSnap` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 170 | 180 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 226 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 228 | 299 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 479 | 312 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 167 | 96 | inferred_complete_timeline |
| `Action_None` | 168 | 254 | 87 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 7–479
- **Visible Samples:** 473

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 167 | 161 | inferred_complete_timeline |
| `Action_None` | 168 | 479 | 312 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 167 | 132 | inferred_complete_timeline |
| `Action_None` | 168 | 269 | 102 | inferred_complete_timeline |
| `Action_None` | 276 | 479 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–437
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 437 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 180 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `26` | Position_Unknown | Team_Unknown | 202–479 | 270 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 206–297 | 87 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 225–311 | 87 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 232–309 | 77 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 237–240 | 4 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 261–479 | 217 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 265–479 | 215 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 277–280 | 4 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 285–479 | 193 | 3 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 289–372 | 80 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 308–319 | 12 | 1 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 381–387 | 7 | 1 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 389–479 | 91 | 1 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 402–432 | 31 | 1 | Undefined position; Undefined team |
| `35` | `61` | Position_Unknown | Team_Unknown | 433–474 | 10 | 3 | Undefined position; Undefined team |
| `36` | `62` | Position_Unknown | Team_Unknown | 433–479 | 21 | 3 | Undefined position; Undefined team |
| `37` | `63` | Position_Unknown | Team_Unknown | 436–447 | 10 | 2 | Undefined position; Undefined team |
| `38` | `64` | Position_Unknown | Team_Unknown | 440–441 | 2 | 1 | Undefined position; Undefined team |
| `39` | `65` | Position_Unknown | Team_Unknown | 445–479 | 18 | 4 | Undefined position; Undefined team |
| `40` | `66` | Position_Unknown | Team_Unknown | 447–479 | 33 | 1 | Undefined position; Undefined team |
| `41` | `67` | Position_Unknown | Team_Unknown | 450–451 | 2 | 1 | Undefined position; Undefined team |
| `42` | `72` | Position_Unknown | Team_Unknown | 464–479 | 16 | 1 | Undefined position; Undefined team |
| `43` | `76` | Position_Unknown | Team_Unknown | 469–479 | 11 | 1 | Undefined position; Undefined team |
| `44` | `77` | Position_Unknown | Team_Unknown | 469–479 | 11 | 1 | Undefined position; Undefined team |
| `45` | `78` | Position_Unknown | Team_Unknown | 471–472 | 2 | 1 | Undefined position; Undefined team |
| `46` | `79` | Position_Unknown | Team_Unknown | 474–475 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `20` | 50 | 60 | 6 | 54.5% | 54–58 |
| `19` | `21` | 105 | 105 | 1 | 100.0% | None |
| `30` | `44` | 302 | 302 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (LG) duration 99 frames exceeds threshold 90 frames [start=170, end=268].
- ⚠️ Action 'Action_None' range [168-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-198] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-435] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-269] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [170-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [205-206] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [170-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-226] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-437] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-254] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-226] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [170-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [184-199] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [231-246] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-325] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-167] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-284] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-334] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-328] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-479] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-267] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-315] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-33] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-236] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-307] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-479] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-311] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-309] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-306] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-473] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-479] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-329] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-372] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-319] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-387] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-432] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-474] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-466] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-438] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-447] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-447] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-453] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-470] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-479] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '46' has 1 frames without a visible bounding box.
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

</details>