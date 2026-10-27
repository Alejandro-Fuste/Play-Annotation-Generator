# Play-Annotation-Generator Annotation Review — Counter_218

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_218`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 192 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 191 | START | 191 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `10` | `9` | 193 | START | 193 | 215 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `8` | `7` | 193 | START | 202 | 204 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `9` | `8` | 193 | START | 193 | 242 |
| ✅ EXACT | `Action_PullBlock` | RG | `1` | `0` | 193 | START | 193 | 208 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `2` | `1` | 193 | START | 193 | 219 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 201 | END | 194 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 219 | START | 219 | 263 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 284 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–273
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_SnapReceive` | 194 | 201 | 8 | inferred_complete_timeline |
| `Action_None` | 202 | 218 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 219 | 263 | 45 | inferred_complete_timeline |
| `Action_BallCarry` | 269 | 273 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 229 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–382
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 193 | 219 | 27 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 224 | 284 | 61 | inferred_complete_timeline |
| `Action_None` | 285 | 382 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 242 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 250 | 284 | 35 | inferred_complete_timeline |
| `Action_None` | 285 | 419 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 215 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 221 | 229 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_BallSnap` | 191 | 201 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 208 | 226 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PullBlock` | 193 | 208 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 256 | 66 | inferred_complete_timeline |
| `Action_None` | 280 | 287 | 8 | inferred_complete_timeline |
| `Action_None` | 299 | 306 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 419 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–385
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 58 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 116 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 154 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 178 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 240 | 37 | inferred_complete_timeline |
| `Action_None` | 242 | 257 | 16 | inferred_complete_timeline |
| `Action_None` | 263 | 385 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 35 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 46 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 52 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 59 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 68 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 139 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 154 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 190 | 27 | inferred_complete_timeline |
| `Action_None` | 191 | 202 | 12 | inferred_complete_timeline |
| `Action_None` | 204 | 221 | 18 | inferred_complete_timeline |
| `Action_None` | 224 | 229 | 6 | inferred_complete_timeline |
| `Action_None` | 236 | 240 | 5 | inferred_complete_timeline |
| `Action_None` | 247 | 254 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 216 | 26 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |
| `Action_None` | 317 | 350 | 34 | inferred_complete_timeline |
| `Action_None` | 352 | 419 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 190 | 141 | inferred_complete_timeline |
| `Action_None` | 191 | 206 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 91–307 | 194 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 92–93 | 2 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 101–221 | 117 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 132–419 | 181 | 8 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 212–419 | 130 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 222–419 | 186 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 254–329 | 76 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 257–319 | 17 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 268–404 | 126 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 274–282 | 9 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 282–349 | 68 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 288–419 | 132 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 290–292 | 3 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 300–419 | 116 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 309–419 | 109 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 331–419 | 89 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 341–419 | 79 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 353–419 | 67 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 380–381 | 2 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 386–403 | 15 | 2 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 391–410 | 20 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 392–409 | 18 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 398–419 | 22 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 407–417 | 7 | 3 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 418–419 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [191–201], lower_priority='Action_DownBlock' annotated_start=193, effective_Action_DownBlock_start=202.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (LT) duration 92 frames exceeds threshold 90 frames [start=193, end=284].
- ⚠️ Action 'Action_PullBlock' range [193-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [193-219] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-382] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-190] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-256] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-287] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-306] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [219-263] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [269-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-229] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [202-204] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [208-226] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-242] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-215] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [221-229] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-350] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-35] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-46] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-40] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-59] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-68] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-202] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-221] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-154] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-240] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-257] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-385] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-275] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-307] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-104] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-235] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-419] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-262] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-401] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-263] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-319] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-340] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-369] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-404] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-282] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-349] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-321] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-356] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-398] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-410] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-409] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-419] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-409] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '38' has 1 frames without a visible bounding box.
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

</details>