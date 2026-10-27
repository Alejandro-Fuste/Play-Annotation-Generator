# Play-Annotation-Generator Annotation Review — Counter_199

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_199`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 55
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB3 | defense | `6` | `5` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 9 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 9 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 9 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 9 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 9 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 0 | START | 9 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 9 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 9 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 9 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 9 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 9 | 169 |
| ✅ EXACT | `Action_BallSnap` | LB3 | `6` | `5` | 168 | START | 168 | 181 |
| ✅ EXACT | `Action_DownBlock` | RT | `13` | `12` | 170 | START | 170 | 267 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `16` | `15` | 170 | START | 170 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `9` | `8` | 170 | START | 170 | 184 |
| ✅ EXACT | `Action_PullBlock` | LG | `21` | `20` | 170 | START | 170 | 267 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | `20` | `19` | 170 | START | 170 | 232 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 181 | END | 168 | 181 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 193 | START | 193 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `2` | 212 | START | 212 | 237 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 267 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 9–344
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_SnapReceive` | 168 | 181 | 14 | inferred_complete_timeline |
| `Action_None` | 182 | 192 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 193 | 211 | 19 | inferred_complete_timeline |
| `Action_None` | 212 | 344 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 9–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 199 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 211 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 237 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 239 | 359 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 9–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 359 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 9–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 359 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 9–331
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 169 | 161 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 170 | 232 | 63 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 236 | 267 | 32 | inferred_complete_timeline |
| `Action_None` | 268 | 331 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 359 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 9–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 359 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 9–309
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 70 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 169 | 98 | inferred_complete_timeline |
| `Action_PullBlock` | 170 | 267 | 98 | inferred_complete_timeline |
| `Action_None` | 268 | 309 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 9–359
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 169 | 161 | inferred_complete_timeline |
| `Action_DownBlock` | 170 | 192 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 203 | 233 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 242 | 260 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 263 | 267 | 5 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_None` | 271 | 288 | 18 | inferred_complete_timeline |
| `Action_None` | 293 | 359 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 9–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 169 | 161 | inferred_complete_timeline |
| `Action_DownBlock` | 170 | 184 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 188 | 258 | 71 | inferred_complete_timeline |
| `Action_DownBlock` | 260 | 267 | 8 | inferred_complete_timeline |
| `Action_None` | 268 | 279 | 12 | inferred_complete_timeline |
| `Action_None` | 283 | 330 | 48 | inferred_complete_timeline |
| `Action_None` | 332 | 335 | 4 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_None` | 348 | 359 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 169 | 161 | inferred_complete_timeline |
| `Action_DownBlock` | 170 | 267 | 98 | inferred_complete_timeline |
| `Action_None` | 268 | 359 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 9–204
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 204 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–300
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 300 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 9–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 189 | 22 | inferred_complete_timeline |
| `Action_None` | 208 | 359 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–296
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 242 | 75 | inferred_complete_timeline |
| `Action_None` | 258 | 278 | 21 | inferred_complete_timeline |
| `Action_None` | 294 | 296 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 9–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 260 | 93 | inferred_complete_timeline |
| `Action_None` | 262 | 359 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 9–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 271 | 104 | inferred_complete_timeline |
| `Action_None` | 276 | 359 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_BallSnap` | 168 | 181 | 14 | inferred_complete_timeline |
| `Action_None` | 182 | 257 | 76 | inferred_complete_timeline |
| `Action_None` | 264 | 359 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 9–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 359 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 9–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 359 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 9–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 359 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 9–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_None` | 168 | 325 | 158 | inferred_complete_timeline |
| `Action_None` | 327 | 341 | 15 | inferred_complete_timeline |
| `Action_None` | 346 | 359 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 212–215 | 4 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 236–359 | 124 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 276–352 | 77 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 311–314 | 4 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 325–329 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (RG) duration 98 frames exceeds threshold 90 frames [start=170, end=267].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (RT) duration 98 frames exceeds threshold 90 frames [start=170, end=267].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (C) duration 98 frames exceeds threshold 90 frames [start=170, end=267].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '20' (LG) duration 98 frames exceeds threshold 90 frames [start=170, end=267].
- ⚠️ Action 'Action_None' range [168-325] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-341] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [239-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-271] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-300] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-257] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [170-184] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [188-258] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-279] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-330] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-242] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-278] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-344] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [170-192] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [203-233] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [242-260] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-288] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [170-232] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-331] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [170-267] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-309] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-352] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '26' has 2 frames without a visible bounding box.
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

</details>