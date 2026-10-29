# Play-Annotation-Generator Annotation Review — Duo_128

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_128`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 328
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `16` | `15` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `34` | `25` |
| ✅ EXACT | `Action_ComboBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 23 | START | 0 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 23 | START | 0 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 23 | START | 23 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 23 | START | 23 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 23 | START | 23 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `17` | `Group` | 23 | START | 23 | 283 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 23 | START | 23 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 23 | START | 23 | 328 |
| ✅ EXACT | `Action_ComboBlock` | RG | `12` | `11` | 209 | START | 209 | 233 |
| ✅ EXACT | `Action_ComboBlock` | LG | `16` | `15` | 209 | START | 209 | 259 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `34` | `25` | 209 | START | 209 | 259 |
| ✅ EXACT | `Action_ComboBlock` | RT | `8` | `7` | 209 | START | 209 | 259 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `12` | `11` | 234 | START | 234 | 259 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 259 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 23–287
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 287 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 23–328
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 283 | 261 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 328 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 23–328
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 328 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 23–328
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 137 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 208 | 70 | inferred_complete_timeline |
| `Action_ComboBlock` | 209 | 259 | 51 | inferred_complete_timeline |
| `Action_None` | 260 | 304 | 45 | inferred_complete_timeline |
| `Action_None` | 316 | 319 | 4 | inferred_complete_timeline |
| `Action_None` | 323 | 328 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 23–323
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 208 | 186 | inferred_complete_timeline |
| `Action_ComboBlock` | 209 | 233 | 25 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 234 | 259 | 26 | inferred_complete_timeline |
| `Action_None` | 260 | 263 | 4 | inferred_complete_timeline |
| `Action_None` | 265 | 304 | 40 | inferred_complete_timeline |
| `Action_None` | 314 | 323 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 23–328
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 208 | 186 | inferred_complete_timeline |
| `Action_ComboBlock` | 209 | 259 | 51 | inferred_complete_timeline |
| `Action_None` | 260 | 328 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 23–328
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 177 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 328 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 23–211
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 211 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 23–244
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 196 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 202 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 244 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 23–328
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 202 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 328 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 23–313
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 304 | 282 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 313 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 23–252
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 246 | 224 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 252 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 23–328
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 328 | 306 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 23–283
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 283 | 261 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–22 | 23 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–21 | 22 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–22 | 23 | 1 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 10–20 | 11 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 52–56 | 5 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 72–110 | 37 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 112–328 | 217 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 122–328 | 200 | 4 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 193–292 | 98 | 4 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 221–317 | 59 | 4 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 258–328 | 71 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 264–328 | 65 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 264–280 | 15 | 2 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 265–327 | 61 | 2 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 276–328 | 53 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 276–328 | 31 | 2 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 277–328 | 36 | 2 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 321–322 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 52 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-20] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-283] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [209-259] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-328] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-287] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-304] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-323] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-211] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-304] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-313] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [209-259] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-304] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-283] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-244] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-110] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-328] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-300] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-317] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-208] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [209-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-280] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-292] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-294] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-317] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-276] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-268] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-327] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-280] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-322] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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